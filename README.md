# RedditBotty

A Reddit bot that responds with a robot image whenever someone mentions the keyword "bot" in a specific subreddit.

## Overview

RedditBotty is a Python bot built using **PRAW (Python Reddit API Wrapper)** that scans a subreddit for comments containing a keyword ("bot") and replies with a robot image.  

I created this project to practice **Python scripting, working with APIs**, and building an automated bot that interacts with social media platforms in a safe, controlled environment. It’s also a fun way to explore automation and text processing in Python.


## Features

- Scans the latest comments in a specified subreddit.
- Detects a keyword in comments ("bot").
- Replies with a robot image hyperlink.
- Keeps track of which comments it has already replied to.
- Avoids replying to your own comments.
- Can be run continuously with time delays to prevent spamming.


## Installation

Make sure you have Python 3 installed.

Install the required dependency:
  pip install praw

## Usage

Create a Reddit app on Reddit to get your client_id and client_secret.

Add your credentials to config.py or set them as environment variables:

username = "reddit_username"
password = "reddit_password"
client_id = "client_id"
client_secret = "client_secret"

To Run the bot: 
  python reddit_bot.py

## Configuration

reddit_bot.py: Main bot script.

config.py: Stores Reddit credentials (use environment variables for security).

comments_replied_to.txt: Tracks comment IDs the bot has replied to.

The Bot in Action: 

<img width="950" height="950" alt="k4i5SOR" src="https://github.com/user-attachments/assets/c9851841-113a-43aa-83b7-bedaf4684673" />

*This robot automatically replies to comments containing the keyword "bot".

Credits:
Built by Valerie Salinas – GitHub Profile
Uses PRAW –> Python Reddit API Wrapper
