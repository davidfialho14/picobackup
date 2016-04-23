#!/usr/bin/env bash

# change to the script directory
cd "$(dirname "$0")"

# clear the install log if it exists
rm -f install.log

# ensure the basics are installed
echo "Installing python and setuptools..."
sudo apt-get install python python-setuptools >> install.log 2>&1 || { echo "failed installing basics" && exit 1; }
echo "OK"

# install picobackup
echo "Installing picobackup..."
sudo python setup.py install >> install.log 2>&1 || { echo "failed installing picobackup" && exit 1; }
echo "OK"

# clear up
echo "Clearing up..."
sudo rm -rf dist build pico_backup.egg-info pyftpdlib-1.5.0/ >> install.log 2>&1
echo "Cleared up!"

echo "Installed successfully"
