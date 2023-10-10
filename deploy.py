#!/usr/bin/env python

import os
import subprocess

# Set environment variables (replace with your own values)
os.environ["BOT_TOKEN"] = "6294506492:AAHWWWbk1TmdFCvLDGcHRgPJrpyoHEDwoYU"
os.environ["API_ID"] = "24736263"
os.environ["API_HASH"] = "4d53732917b73a6bb89c3b2f2f7b0902"

# Install any necessary dependencies
try:
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Failed to install dependencies: {e}")
    exit(1)

# Start your bot
try:
    subprocess.run(["python", "bot.py"])
except KeyboardInterrupt:
    # Handle graceful shutdown if needed
    pass
  
