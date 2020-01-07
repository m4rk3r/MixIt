## ~ MixIt ~
A simple tool for composing a mix from youtube videos.


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

> [here's a full example](https://gist.github.com/m4rk3r/48a4fff6ae488bfd4c624bb745627995) with more advanced fading

+ make it happen `python mixit.py subtle-sounds.txt "~ Subtle Sounds ~" ~/Desktop/cover.jpg`
  + the command is `python mixit.py  <mix file> <id3 title> <cover art>` both title and cover are optional.
  + The script will create a directory matching the input text filename, download the videos as mp3s via [youtube_dl](https://github.com/ytdl-org/youtube-dl/) and then concatenate into one final mix matching the input filename.


### How to use as App:
Download the osx app from [the releases tab](https://github.com/m4rk3r/MixIt/releases/latest).

Create the text file mix as you would with the CLI, and then drag and drop on the unzipped app. The mix will be created in the same direcotry that the text file was dragged from.

![Demo gif](http://duskjacket.com/static/demo.gif)


#### 🎶 enjoy 🔊


### How to use as a library:
+ Import the build function `from mixit import build`
+ run `build('subtle-sounds.txt', '~ Subtle Sounds ~', '~/Desktop/cover.jpg')`
