# README
### Description
The primary purpose of this bot is to join voice channel and play requested songs. This discord bot uses `YouTube v3 API` to search and play songs. It also responds to text messages.

### Installation
1. Clone this repository.
2. Run `pip install -r requirements.txt`.
3. Get YouTube v3 API token and download client.json file from [google cloud console](https://console.cloud.google.com/marketplace/product/google/youtube.googleapis.com?project=discord-bot-469723).
4. Get the Discord API token from [discord for developers](https://discord.com/developers/).
5. Create a `.env` file and save your Discord and YouTube token.
6. Run the file `python3 bot.py`.

### Commands
The bot responds to - `$`
- `$hello` - To greet.
- `$join` - Joins voice channel.
- `$leave` - Leaves voice channel.
- `$play <song>` - Plays song in the voice channel.
- `$add <song>` - Add song in queue.
- `$skip` - Skip the current song.
- `$memes` - Generate random funny memes.

### Note
Make sure `ffmpeg` is installed through [brew](https://brew.sh/) and added to your system PATH, otherwise the audio won't play.
