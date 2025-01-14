#!/bin/bash

current_branch=$(git branch --show-current)
upstream=$(git rev-parse --abbrev-ref $current_branch@{u} 2>/dev/null)

if [ -n "$upstream" ]; then
  merge_base=$(git merge-base "$upstream" origin/main)
  main_head=$(git rev-parse origin/main)

  if [ "$merge_base" == "$main_head" ]; then
    echo "$current_branch is tracking $upstream, which is up-to-date with origin/main"
  elif [ $(git merge-base --is-ancestor "$merge_base" origin/main) == 0 ]; then
    echo "$current_branch is tracking $upstream, which is based on origin/main (at $merge_base)"
  else
    echo "$current_branch is tracking $upstream, but its relationship to origin/main is unclear"
  fi
else
  echo "$current_branch is not tracking an upstream branch"
fi
