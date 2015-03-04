#!/bin/bash
cd "$1"
git fetch --all
git reset --hard origin/development
git commit --allow-empty -m $(date +%F)
git push
sleep 5
git reset --hard HEAD
git push -f
