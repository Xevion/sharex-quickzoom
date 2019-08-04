import os, sys, send2trash

blacklist = [
        'clean.py',
        'main.py',
        'LICENSE',
        'screenshot.png',
        'README.md',
        '.git',
        '.gitignore',
        'resources'
]

def run(recycle=True, print_ignores=False):
    """Main driver function for recycling unneeded files from the folder.
    
    Keyword Arguments:
        recycle {bool} -- True to recycle and send to recycle bin instead of permanently delete a file. (default: {True})
        print_ignores {bool} -- True to print what files have been ignored (default: {False})
    """

    # ternary raise support function, shouldn't ever be raised
    def raiseMe(filePath):
        raise('Invalid file or folder ; \'{}\''.format(filePath))

    # Constants
    basepath = sys.path[0]
    _logFiles = []
    _logFolders = []
    getName = lambda someList : 'folder' if someList is _logFolders else 'file' if someList is _logFiles else '???'

    print('Deletion sequence started')
    for file in os.listdir(basepath):
        filepath = os.path.join(basepath, file)
        # Take action on the offending file
        if file not in blacklist:
            # Send to recycle bin vs straightup permanently delete
            curType = _logFiles if os.path.isfile(filepath) else _logFolders if os.path.isdir(filepath) else raiseMe(filepath)
            # We want to recycle the file
            if recycle:
                send2trash.send2trash(filepath)
                curType.append('Recycled {}: \'{}\''.format(getName(curType), filepath))
            # We want to permanently delete the file
            else:
                os.remove(filepath)
                curType.append('Deleted {}: \'{}\''.format(getName(curType), filepath))
        else:
            if print_ignores:
                curType.append('Ignored {}: \'{}\''.format(getName(curType), filepath))
    
    # Clean up
    ending = '\n' if (_logFiles or _logFolders) else ''
    print('\n'.join(_logFiles), end=ending)
    print('\n'.join(_logFolders), end=ending)    
    print(f'Finished deleting {len(_logFiles)} files and {len(_logFolders)} folders.')

if __name__ == "__main__":
    run()