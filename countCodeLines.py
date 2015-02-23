from __future__ import print_function

import os, sys

SEPARATOR = "="*60

def countLines(directories, fileType):
    print("\n%s\n%s lines of code\nin %s:\n%s"%
          (SEPARATOR, fileType, str(directories), SEPARATOR))
    numFiles = 0
    numLines = 0
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for name in files:
                if name.endswith(fileType):
                    nameWithDir = os.path.join(root, name)
                    numFiles += 1
                    try:
                        fileLines = sum(1 for line in open(nameWithDir))
                        numLines += fileLines
                        print("%6d lines in file %s"%(fileLines, nameWithDir))
                    except:
                        print("Failed to open file %s"%nameWithDir)
    print("%6d lines in %d files"%(numLines, numFiles))
    return {'lines':numLines, 'files':numFiles}


directories = ()
if len(sys.argv) == 1:
    directories += (".",)
else:
    for arg in sys.argv[1:]:
        if os.path.isdir(arg):
            directories += (arg,)
        else:
            print("\n\"%s\" is not a directory"%arg)
if len(directories) == 0:
    print("No directories found in argument list.\nExiting.\n")
    exit()
  
count = countLines(directories, (".cpp", ".hpp", ".h"))
totalLines  = count['lines']
totalFiles  = count['files']

count = countLines(directories, ".cs")
totalLines += count['lines']
totalFiles += count['files']

count = countLines(directories, ".py")
totalLines += count['lines']
totalFiles += count['files']

print("\n\n%s\nTotal lines of code:\n%s"%(SEPARATOR, SEPARATOR))
print("%6d lines in %d files"%(totalLines, totalFiles))
        
