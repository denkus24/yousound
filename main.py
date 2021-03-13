from pytube import Playlist, YouTube
from ffmpeg import output, input, run
from os import remove

text = '''
Y88b   d88P               .d8888b.                              888 
 Y88b d88P               d88P  Y88b                             888 
  Y88o88P                Y88b.                                  888 
   Y888P  .d88b. 888  888 "Y888b.   .d88b. 888  88888888b.  .d88888 
    888  d88""88b888  888    "Y88b.d88""88b888  888888 "88bd88" 888 
    888  888  888888  888      "888888  888888  888888  888888  888 
    888  Y88..88PY88b 888Y88b  d88PY88..88PY88b 888888  888Y88b 888 
    888   "Y88P"  "Y88888 "Y8888P"  "Y88P"  "Y88888888  888 "Y88888 
                                                by denkus24
'''

print(text)


def name_input():
    name = input('Please enter name without ",/,\\,:,?,<,>,|: ')
    if '"' not in name and '/' not in name and '\\' not in name and ":" not in name and '?' not in name and '>' not in name and '<' not in name and '|' not in name:
        return name
    else:
        print('Name is incorrect!')
        name_input()


def download_and_convert(link):
    video_example = YouTube(link)
    name = video_example.title
    if '"' not in video_example.title and '/' not in video_example.title and '\\' not in video_example.title and ":" not in video_example.title and '?' not in video_example.title and '>' not in video_example.title and '<' not in video_example.title and '|' not in video_example.title:
        pass
    else:
        name = name_input()

    input_name = name + '.mp4'
    output_name = name + '.mp3'

    print(f'Downloading {name}...')

    video_example.streams.filter(only_audio=True).first().download(filename=name)

    stream = input(input_name)
    audio = stream.audio
    stream = output(audio, output_name, loglevel='quiet')
    run(stream)

    remove(input_name)


video_or_playlist = input('Download single video or playlist?(v/p): ')

if video_or_playlist.lower() == 'v':
    video_link = input('Enter link for video: ')
    if 'youtube.com/watch?v=' in video_link:
        print('Starting downloading video...')
        download_and_convert(video_link)
        print('Download finished!')
    else:
        print('Link incorrect!')
        quit()

elif video_or_playlist.lower() == 'p':
    playlist_link = input('Enter link for playlist: ')
    if 'youtube.com/playlist?list=' in playlist_link:
        playlist_example = Playlist(playlist_link)
        print('Start downloading playlist...')
        for link in playlist_example.video_urls[:3]:
            download_and_convert(link)
        print('Downloading finished!')
    else:
        print('Link incorrect!')
        quit()
else:
    quit()