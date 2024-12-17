from file import *

def loopdeloop(simulnbGuichets, files):
    for i in range(1, simulnbGuichets+1):
        f= File()
        files.append(f)
    return files

print(loopdeloop(4, []))