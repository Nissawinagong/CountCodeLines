from __future__ import print_function

import os, sys

SEPARATOR = "="*60

def countLines(directories, fileType):
    numFiles = 0
    numLines = 0
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for name in files:
                if name.endswith(fileType):
                    if numFiles == 0:
                        print("\n%s\n%s lines of code\nin %s:\n%s"%
                             (SEPARATOR, fileType, str(directories), SEPARATOR))
                    numFiles += 1
                    nameWithDir = os.path.join(root, name)
                    try:
                        fileLines = sum(1 for line in open(nameWithDir))
                        numLines += fileLines
                        print("%6d lines in file %s"%(fileLines, nameWithDir))
                    except:
                        print(" Failed to open file %s"%nameWithDir)
    if not numFiles == 0:
        print("%6d lines in %d files."%(numLines, numFiles))
    return {'lines':numLines, 'files':numFiles}


directories = ()
if len(sys.argv) == 1:
    directories += (".",)
else:
    argErr = False
    for arg in sys.argv[1:]:
        if os.path.isdir(arg):
            directories += (arg,)
        else:
            if not argErr:
                print("")
                argErr = True
            print("\"%s\" is not a directory."%arg)
if len(directories) == 0:
    print("No directories found in argument list.\nExiting.\n")
    exit()
  
count = countLines(directories, (".cpp", ".c", ".hpp", ".h"))
totalLines  = count['lines']
totalFiles  = count['files']

count = countLines(directories, ".cs")
totalLines += count['lines']
totalFiles += count['files']

count = countLines(directories, ".java")
totalLines += count['lines']
totalFiles += count['files']

count = countLines(directories, ".py")
totalLines += count['lines']
totalFiles += count['files']

print("\n%s\nTotal lines of code:\n%s"%(SEPARATOR, SEPARATOR))
print("%6d lines in %d files.\n"%(totalLines, totalFiles))
        
