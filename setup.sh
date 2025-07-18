#!/bin/bash

clear
echo "Installing Python requirements..."
pip install -r requirements.txt

echo "Setting up environment file..."
cp .env.example .env

echo "Bot setup complete! Run the bot using:"
echo "python3 -m bot"
