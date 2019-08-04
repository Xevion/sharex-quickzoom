import os, sys, argparse, subprocess

# Simple tester for testing whether a file exists.
# StackOverflow https://stackoverflow.com/a/51212150/6912830
def file_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise NotADirectoryError(string)

# Argparser
# parser = argparse.ArgumentParser()
# parser.add_argument('path', metavar='PATH', type=file_path, help='the full path to the file in question')
# args = parser.parse_args()

# print(args.path)

# Image Processing
command_args = "5x0+90+450"

base_path = sys.path[0]
blur_map = os.path.join(base_path, 'blur_map_polar.jpg')
input_path = os.path.join(base_path, 'blur_radial.jpg')
output_path = os.path.join(base_path, 'output.jpg')

for path in [base_path, blur_map, input_path, output_path]:
    if not os.path.exists(path):
        raise Exception('Invalid File Name')


# command = ['magick convert', input_path, blur_map, '-compose blur', '-define', 'compose:args=' + command_args, '-composite ', output_path]
command = 'magick convert {} {} -compose blur -define compose:args={} -composite {}'.format(input_path, blur_map, command_args, output_path)
print(command)
subprocess.run(command.split(' '))