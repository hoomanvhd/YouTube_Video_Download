
import os
import sys
import subprocess

script = sys.argv[0]

lineSet = set()

with open("/home/hoomanvhd/Desktop/data.txt", "r") as dataFile:
    for line in dataFile:
        lineSet.add(line)

counter = 1

cnt = 0
problem = []

for i in lineSet:
    try:
        os.mkdir("/home/hoomanvhd/Desktop/Data/Video" + str(counter))
        print("===============================================")
        print("directory created", counter)
        print("===============================================")
        command = 'youtube-dl --write-info-json ' + '"' + i + '" ' + '-o /home/hoomanvhd/Desktop/Data/Video' + str(counter) + '/Video1'
        subprocess.run(command, shell=True)
        print("================================================")
        print("Video Downloaded", counter)
        print("================================================")
    except:
        print("****************************************************************************")
        print("there was a problem with the file number", counter)
        print("****************************************************************************")
        cnt += 1
        problem.append(counter)

    counter += 1


print(cnt)
for j in problem:
    print(j)


    

