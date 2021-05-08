# CaveJohnsonBot
A Discord Bot for welcome messages and random heart warming quotes from Cave Johnson

Dependencies:

pip install -U discord.py

pip install -U python-dotenv

## Required Permissions

The following bot permissions on the discord Oauth 2 settings are required:

- View Channels
- Send Messages
- Embeded Links
- Read Message History

## .env File

Make sure to create a .env file and populate the following values:

DISCORD_TOKEN=

FAQ_CHANNEL_ID=

WELCOME_CHANNEL_ID=

GENERAL_CHANNEL_ID=

`DISCORD_TOKEN` is the API token used by your application

The `_CHANNEL_IDs` are unique channel IDs for the FAQ and Welcome Rules respective text channels in your server.

