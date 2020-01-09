from __future__ import unicode_literals
import re
import sys
import youtube_dl

from os import environ, mkdir, path
from pydub import AudioSegment


environ['PATH'] += ':../Frameworks'


def get_id(s):
    """Get youtube id e.g. &v=< id >"""
    return re.search(r'\?v=([\w\d\-_]+)(?:,[0-9.]+)?$', s).group(1)


def get_crossfade(s):
    """ return optional crossfade converted from Seconds to Milliseconds"""
    cf = re.search(r',([0-9.]+)$', s)
    if cf:
        return int(float(cf.group(1)) * 1000)
    return 0


def build(in_file=None, title=None, cover=None):
    if not in_file and len(sys.argv) < 2:
        print('Oop, requires at least one argument.. (a text file to work on)')
        return

    mix_name = path.splitext(in_file)[0] if in_file else path.splitext(sys.argv[1])[0]
    base_dir = path.dirname(sys.argv[1])

    opts = {
        'outtmpl': '{}/%(id)s.%(ext)s'.format(mix_name),
        'format': 'bestaudio/best',
        'ffmpeg_location': '../Frameworks/ffmpeg',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    config = {
        'format': 'mp3',
        'bitrate': '320k',
        'tags': {
            'title': title or (sys.argv[2] if len(sys.argv) > 2 else mix_name),
            'album': title or (sys.argv[2] if len(sys.argv) > 2 else mix_name),
            'artist': 'Various Artists'
        }
    }

    if not path.exists(mix_name):
        mkdir(mix_name)

    with open(in_file or sys.argv[1], 'r') as f:
        songs = f.readlines()

        with youtube_dl.YoutubeDL(opts) as ydl:
            for song in songs:
                if not path.exists(path.join(mix_name, '%s.mp3' % get_id(song))):
                    ydl.download([re.sub(r',\d+$', '', song)])

        mix = None
        cf = 0
        idx = 0

        for song in songs:
            print('processing song {} of {}'.format(idx + 1, len(songs)))
            song_file = AudioSegment.from_file(
                path.join(base_dir, mix_name, '%s.mp3' % get_id(song)))

            if not mix:
                mix = song_file
            else:
                mix = mix.append(song_file, crossfade=cf)

            # set crossfade for mixing with the next song
            cf = get_crossfade(song)
            idx += 1

        print('exporting {}...'.format(config['tags']['title']))
        with open(path.join(base_dir, '%s.mp3' % mix_name), 'wb') as out:
            if cover or len(sys.argv) > 3:
                config['cover'] = cover or sys.argv[3]

            mix.export(out, **config)

        print('done!')


if __name__ == '__main__':
    try:
        build()
    except Exception as e:
        with open(path.join(path.dirname(sys.argv[1]), 'log.txt'), 'w') as log:
            log.write('error: {}'.format(e))
