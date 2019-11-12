## ~ MixIt ~
A very basic tool for composing a mix from youtube videos.

### How to use as CLI:
+ install requirements the first time `pip install -e requirements.txt`
  + also requires [ffmpeg](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#do-i-need-any-other-programs)
+ create a text file with youtube videos on each line, e.g. `subtle-sounds.txt`:

 ```
https://www.youtube.com/watch?v=17yWeynOfOI
https://www.youtube.com/watch?v=s3gge17rub0
https://www.youtube.com/watch?v=sCzJQRVbWtE
```
 + you can also add optional crossfade after a track by adding a comma and the duration in seconds:

 ```
https://www.youtube.com/watch?v=17yWeynOfOI
https://www.youtube.com/watch?v=s3gge17rub0,5
https://www.youtube.com/watch?v=sCzJQRVbWtE
```

+ make it happen `python mixit.py subtle-sounds.txt "~ Subtle Sounds ~" ~/Desktop/cover.jpg`
  + the command is `python mixit.py  <mix file> <id3 title> <cover art>` both title and cover are optional.
  + The script will create a directory matching the input text filename, download the videos as mp3s via [youtube_dl](https://github.com/ytdl-org/youtube-dl/) and then concatenate into one final mix matching the input filename.

+ 🎶 enjoy 🔊


### How to use as a library:
+ Import the build function `from mixit import build`
+ run `build('subtle-sounds.txt', '~ Subtle Sounds ~', '~/Desktop/cover.jpg')`