import discord
import json
import os
import re
from discord.ext import commands
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Get values from environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
MUSIC_CHANNEL_ID = os.getenv('MUSIC_CHANNEL_ID')

# Serve static files
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

# Set up intents
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

def parse_music_info(content, url):
    """Extract song name and artist from message content or YouTube URL"""
    # Remove the URL from the content
    content = content.replace(url, '').strip()
    
    if ' - ' in content:
        parts = content.split(' - ', 1)
        return {'artist': parts[0].strip(), 'song': parts[1].strip()}
    
    # If no artist-song format, use the whole content as song name
    return {'artist': 'From Discord', 'song': content if content else 'Music Share'}

@app.route('/get-music-links')
def get_music_links():
    print("Getting music links...")
    channel = bot.get_channel(int(MUSIC_CHANNEL_ID))
    if not channel:
        print("Channel not found!")
        return jsonify([{
            'url': 'https://www.youtube.com/watch?v=uFiR3nVtYKY&t=1388s',
            'song': 'Recommended Video',
            'artist': 'Click to watch'
        }])
    
    music_links = []
    print(f"Found channel: {channel.name}")
    
    messages = []
    import asyncio
    
    async def fetch_messages():
        print("Fetching messages...")
        try:
            async for message in channel.history(limit=50):  # Increased limit to get more songs
                messages.append(message)
            print(f"Found {len(messages)} messages")
        except Exception as e:
            print(f"Error fetching messages: {e}")
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(fetch_messages())
    
    for message in messages:
        content = message.content
        urls = re.findall(r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[^\s]+)', content)
        if urls:
            url = urls[0]
            music_info = parse_music_info(content, url)
            music_links.append({
                'url': url,
                'song': music_info['song'],
                'artist': music_info['artist'],
                'timestamp': message.created_at.isoformat()
            })
    
    if not music_links:
        return jsonify([{
            'url': 'https://www.youtube.com/watch?v=uFiR3nVtYKY&t=1388s',
            'song': 'Recommended Video',
            'artist': 'Click to watch'
        }])
        
    # Sort by timestamp and select random recent songs
    music_links.sort(key=lambda x: x['timestamp'], reverse=True)
    recent_links = music_links[:20]  # Get 20 most recent songs
    import random
    selected_links = random.sample(recent_links, min(3, len(recent_links)))
    return jsonify(selected_links)

@bot.event
async def on_ready():
    print(f'Bot is ready: {bot.user.name}')
    channel = bot.get_channel(int(MUSIC_CHANNEL_ID))
    if channel:
        print(f'Found channel: {channel.name}')
        print(f'Channel permissions: {channel.permissions_for(channel.guild.me)}')
        # Try to fetch one message to test permissions
        try:
            async for message in channel.history(limit=1):
                print(f'Successfully fetched a message from {message.author}')
                break
        except Exception as e:
            print(f'Error fetching messages: {e}')
    else:
        print(f'ERROR: Could not find channel with ID: {MUSIC_CHANNEL_ID}')
        print(f'Available channels: {[ch.name for ch in bot.get_all_channels()]}')

if __name__ == '__main__':
    # Run the bot in a separate thread
    import threading
    bot_thread = threading.Thread(target=bot.run, args=(DISCORD_TOKEN,))
    bot_thread.start()
    
    # Run Flask on a different port
    app.run(port=5001, debug=True)
