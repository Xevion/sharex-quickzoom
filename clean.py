import os, sys, send2trash

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

def run(recycle=True, print_ignores=False):
    """Main driver function for recycling unneeded files from the folder.
    
    Keyword Arguments:
        recycle {bool} -- True to recycle and send to recycle bin instead of permanently delete a file. (default: {True})
        print_ignores {bool} -- True to print what files have been ignored (default: {False})
    """

    # Constants
    basepath = sys.path[0]
    _log = []

    print('Deletion sequence started')
    for file in os.listdir(basepath):
        filepath = os.path.join(basepath, file)
        if file not in blacklist:
            _log.append('Recycled: \'{}\''.format(filepath))
            # Send to recycle bin vs straightup permanently delete
            if recycle:
                send2trash.send2trash(filepath)
            else:
                os.remove(filepath)
        else:
            if print_ignores:
                _log.append('IGNORED: \'{}\''.format(filepath))
    print('\n'.join(_log), end='\n' if _log else '')
    print(f'Finished deleting {len(_log)} files')

if __name__ == "__main__":
    run()