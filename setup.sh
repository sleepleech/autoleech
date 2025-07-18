#!/bin/bash

clear
echo "🧠 Sleepy Auto LeechBot Setup 🧠"
echo "Updating system..."

sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip git unzip curl

echo "📥 Cloning repository..."
git clone https://github.com/sleepleech/autoleech.git mirror_leech_autobot
cd mirror_leech_autobot || exit

echo "📦 Installing Python requirements..."
pip3 install -r requirements.txt

echo "✅ Setup selesai!"
echo ""
echo "🔧 Untuk menjalankan bot, gunakan:"
echo "  python3 -m bot"
