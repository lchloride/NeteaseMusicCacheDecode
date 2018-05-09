import os
import sys

CODE = 0xA3


def decode(origin_filepath, result_filepath):
    try:
        fin = open(origin_filepath, "rb")
    except IOError as e:
        print(str(e))
        return

    try:
        fout = open(result_filepath, "wb")
    except IOError as e:
        print(str(e))
        return

    music = fin.read()
    print("Source file length: %s" % len(music))
    music_decode = bytearray()
    for i, byte in enumerate(music):
        sys.stdout.write("\rProgress: %d%%" % (round((i + 1) * 100 / len(music))))
        sys.stdout.flush()
        if type(byte) == str: # For Python 2
            music_decode.append(int(byte.encode("hex"), 16) ^ CODE)
        else: # For Python 3
            music_decode.append(byte ^ CODE)

    print()
    # /Users/lichenghong/Desktop/437292573-_-_320-_-_a198a055f5a79a1a30af1d56fbfd7cea.uc!
    fout.write(music_decode)
    fin.close()
    fout.close()


if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage python nemusiccd.py <source> [<destination>]")
        print("If destination is not specified, its name is same as souce.")
    elif len(sys.argv) == 2:
        last_sep = sys.argv[1].rfind(os.path.sep)
        source_path = sys.argv[1][:last_sep + 1]
        dest = sys.argv[1][:last_sep + sys.argv[1][last_sep:].find(".")] + ".mp3"
        print("Source: %s\nDestination: %s" % (sys.argv[1], dest))
        decode(sys.argv[1], dest)
    else:
        print("Source: %s\nDestination: %s" % (sys.argv[1], sys.argv[2]))
        decode(sys.argv[1], sys.argv[2])
