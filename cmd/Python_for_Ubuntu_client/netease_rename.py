"""
# Download
http://music.163.com/song/media/outer/url?id={Song id}.mp3

# Music detail
http://music.163.com/api/song/detail/?id={Song id}&ids=[{Song id}]

# Function
Rename Netease mp3 files name
From: source path/<song id>-<bite rate>-<random number>.mp3
To: dist path/<artist name> - <song title>.mp3

Default source path: $HOME/.cache/netease-cloud-music/CachedSongs
Default dist path: $HOME/output_music
"""

import requests
import json
import os
import sys
import argparse
import eyed3
import shutil


def detect_netease_music_name(file_path, dist_path, KEEP_SOURCE=True):
    """
    Rename Netease mp3 files name
    From: file_path/<song id>-<bite rate>-<random number>.mp3
    To: dist_path/<artist name> - <song title>.mp3
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
    }
    url_base = "http://music.163.com/api/song/detail/?id={}&ids=[{}]"

    if not os.path.exists(dist_path):
        os.mkdir(dist_path)

    for file_name in os.listdir(file_path):
        if not file_name.endswith(".mp3"):
            continue
        if not len(file_name.split("-")) == 3:
            print(
                ">>>> File %s not in format <song id>-<bite rate>-<random number>.mp3"
                % (file_name)
            )
            continue

        try:
            song_id = file_name.split("-")[0]
            url_target = url_base.format(song_id, song_id)
            resp = requests.get(url_target, headers=headers)
            rr = json.loads(resp.text)

            tt = eyed3.load(os.path.join(file_path, file_name))
            tt.tag.title = rr["songs"][0]["name"].replace("\xa0", " ")
            tt.tag.artist = rr["songs"][0]["artists"][0]["name"]
            tt.tag.album = rr["songs"][0]["album"]["name"]
            tt.tag.album_artist = rr["songs"][0]["album"]["artists"][0]["name"]
            print(
                "song_id = %s, tt.tag title = %s, artist = %s, album = %s, album_artist = %s"
                % (
                    song_id,
                    tt.tag.title,
                    tt.tag.artist,
                    tt.tag.album,
                    tt.tag.album_artist,
                )
            )
            tt.tag.save()
        except UnicodeEncodeError as e:
            print(
                ">>>> UnicodeEncodeError, try again later: file_name = %s, error = %s"
                % (file_name, str(e))
            )
            continue
        except:
            print(">>>> Some other error happens: file_name = %s" % (file_name))
            continue

        dist_name = (
            os.path.join(
                dist_path,
                "%s - %s"
                % (tt.tag.artist.replace("/", " "), tt.tag.title.replace("/", " ")),
            )
            + ".mp3"
        )
        
        if KEEP_SOURCE == True:
            shutil.copyfile(os.path.join(file_path, file_name), dist_name)
        else:
            os.rename(os.path.join(file_path, file_name), dist_name)


def parse_arguments(argv):
    HOME_DIR = os.getenv("HOME")
    default_file_path = os.path.join(HOME_DIR, ".cache/netease-cloud-music/CachedSongs")
    default_dist_path = os.path.join(HOME_DIR, "output_music")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dist_path", type=str, help="Music output path", default=default_dist_path
    )
    parser.add_argument(
        "--source_path", type=str, help="Music source path", default=default_file_path
    )

    return parser.parse_args(argv)


if __name__ == "__main__":
    args = parse_arguments(sys.argv[1:])
    print("source = %s, dist = %s" % (args.source_path, args.dist_path))
    detect_netease_music_name(args.source_path, args.dist_path)
