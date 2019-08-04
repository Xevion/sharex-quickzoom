import os, sys, time, argparse

# Simple tester for testing whether a file exists.
# StackOverflow https://stackoverflow.com/a/51212150/6912830
def file_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise NotADirectoryError(string)

# Argparser
parser = argparse.ArgumentParser()
parser.add_argument('path', metavar='PATH', type=file_path, help='the full path to the file in question')
args = parser.parse_args()

print(args.path)