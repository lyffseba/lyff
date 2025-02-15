import discord
import json
import os
import re
from discord.ext import commands, tasks
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Get values from environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
MUSIC_CHANNEL_ID = os.getenv('MUSIC_CHANNEL_ID')

# Set up intents
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Cache for music messages
cached_messages = []
last_fetch_time = None

@tasks.loop(seconds=30)  # Refresh cache every 30 seconds
async def update_message_cache():
    global cached_messages
    channel = bot.get_channel(int(MUSIC_CHANNEL_ID))
    if channel:
        try:
            messages = []
            async for message in channel.history(limit=100):
                messages.append(message)
            cached_messages = messages
            print(f"Cache updated with {len(messages)} messages")
        except Exception as e:
            print(f"Error updating cache: {e}")

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
async def get_music_links():
    print("Getting music links...")
    if not cached_messages:
        print("No cached messages available")
        return jsonify([{
            'url': 'https://www.youtube.com/watch?v=qEsWePrJZsY&t=467',
            'song': 'LYFF Radio',
            'artist': 'Essential',
            'timestamp': '2022-01-01T00:00:00',
            'platform': 'youtube'
        }])
    
    music_links = []
    seen_urls = set()
    
    print(f"Processing {len(cached_messages)} messages for links...")
    
    for message in cached_messages:
        content = message.content
        # Match both YouTube and Tidal URLs
        youtube_urls = re.findall(r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[^\s]+)', content)
        tidal_urls = re.findall(r'(https?://(?:www\.)?tidal\.com/(?:browse/)?(?:track|album)/[^\s]+)', content)
        
        if youtube_urls:
            print(f"Found YouTube URLs: {youtube_urls}")
        if tidal_urls:
            print(f"Found Tidal URLs: {tidal_urls}")
        
        # Process YouTube links
        for url in youtube_urls:
            clean_url = url.split('&')[0]  # Remove extra parameters
            if clean_url not in seen_urls:
                seen_urls.add(clean_url)
                music_info = parse_music_info(content, clean_url)
                music_links.append({
                    'url': clean_url,
                    'song': music_info['song'],
                    'artist': music_info['artist'],
                    'timestamp': message.created_at.isoformat(),
                    'platform': 'youtube'
                })
                print(f"Added YouTube link: {clean_url}")
        
        # Process Tidal links
        for url in tidal_urls:
            if url not in seen_urls:
                clean_url = url.split('/u')[0]  # Remove /u and anything after
                if clean_url not in seen_urls:
                    seen_urls.add(clean_url)
                    music_info = parse_music_info(content, clean_url)
                    music_links.append({
                        'url': clean_url,
                        'song': music_info['song'],
                        'artist': music_info['artist'],
                        'timestamp': message.created_at.isoformat(),
                        'platform': 'tidal'
                    })
                    print(f"Added Tidal link: {clean_url}")
    
    print(f"Total music links found: {len(music_links)}")
    
    if not music_links:
        print("No music links found, returning default video")
        return jsonify([{
            'url': 'https://www.youtube.com/watch?v=qEsWePrJZsY&t=467',
            'song': 'LYFF Radio',
            'artist': 'Essential',
            'timestamp': '2022-01-01T00:00:00',
            'platform': 'youtube'
        }])
    
    # Sort by timestamp and select random songs
    music_links.sort(key=lambda x: x['timestamp'], reverse=True)
    recent_links = music_links[:50]  # Get 50 most recent songs
    import random
    selected_links = random.sample(recent_links, min(5, len(recent_links)))
    print(f"Selected {len(selected_links)} random links")
    return jsonify(selected_links)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

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
    update_message_cache.start()  # Start the cache update loop

if __name__ == '__main__':
    # Run the bot in a separate thread
    import threading
    bot_thread = threading.Thread(target=bot.run, args=(DISCORD_TOKEN,))
    bot_thread.start()
    
    # Run Flask on the same port as the bot
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5001), debug=True)
