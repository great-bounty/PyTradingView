#!/bin/bash

# PyTradingView Wiki Upload Script
# This script uploads wiki content to GitHub Wiki
#
# Usage:
#   GITHUB_TOKEN=your_token ./upload-wiki.sh
#   or configure git credential helper to store credentials

echo "Preparing to upload PyTradingView Wiki content..."

# Wiki repository URL (without embedded credentials)
WIKI_URL="https://github.com/great-bounty/PyTradingView.wiki.git"

# Create temporary directory for wiki
TEMP_WIKI_DIR="/tmp/pytradingview-wiki"
rm -rf "$TEMP_WIKI_DIR"
mkdir -p "$TEMP_WIKI_DIR"

echo "Cloning wiki repository..."
git clone "$WIKI_URL" "$TEMP_WIKI_DIR"

# If clone fails, the wiki needs to be initialized first
if [ $? -ne 0 ]; then
    echo "Wiki repository not found. Please initialize the wiki on GitHub first:"
    echo "1. Go to https://github.com/great-bounty/PyTradingView/wiki"
    echo "2. Click 'Create the first page'"
    echo "3. Add a simple title and content, then save"
    echo "4. Run this script again"
    exit 1
fi

echo "Copying wiki content..."
cd "$TEMP_WIKI_DIR"

# Copy all generated wiki content
cp -r /Users/main/Documents/Code/github/PyTradingView/.qoder/repowiki/en/content/* .

# Add all files
git add .

# Check if there are changes to commit
if ! git diff-index --quiet HEAD --; then
    echo "Committing changes..."
    git commit -m "Update PyTradingView Wiki documentation"
    
    echo "Pushing to GitHub..."
    git push origin master
    echo "Wiki content uploaded successfully!"
else
    echo "No changes to commit. Wiki is up to date."
fi

# Cleanup
cd ..
rm -rf "$TEMP_WIKI_DIR"
echo "Done!"
