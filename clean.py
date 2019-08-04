import os, sys

basepath = sys.path[0]
blacklist = [
    'clean.py',
    'main.py',
    'LICENSE',
    'output.jpg',
    'screenshot.png',
    'README.md',
    '.git',
    '.gitignore',
]

_log = []
print('DELETED SEQUENCE STARTED')
for file in os.listdir(basepath):
    filepath = os.path.join(basepath, file)
    if file not in blacklist:
        _log.append('DELETED: \'{}\''.format(filepath))
        os.remove(filepath)
    else:
        pass
        # print('IGNORED: \'{}\''.format(filepath))
print('\n'.join(_log))
print(f'FINISHED DELETED {len(_log)} FILES')