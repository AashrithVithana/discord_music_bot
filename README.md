# README
### Description
The primary purpose of this bot is to join voice channel and play requested songs. This discord bot uses `YouTube v3 API` to search and play songs. It also responds to text messages.


### Installation
1. Clone this repository.
2. Run `pip install -r requirements.txt`.
3. Create a `.env` file and save your Discord and YouTube token.
4. Run the file `python3 bot.py`.

### Commands
The bot responds to - `$`
- `$hello` - To greet.
- `$join` - Joins voice channel.
- `$leave` - Leaves voice channel.
- `$play <song>` - Plays song in the voice channel.
- `$memes` - Generate random funny memes.

### Note
When using the command `$play` the discord bot searches the song and first downloads the `.mp3` audio file of the song locally and then plays the audio in the voice channel.
