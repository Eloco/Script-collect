#!/usr/bin/env python
# coding=utf-8
import fire
import os
import hashlib

def init(path="./"):
    os.chdir(path)

fire.Fire(init)


def md5checksum(file_path):
    with open(file_path, "rb") as afile:
        m = hashlib.md5()
        data = afile.read()
        m.update(data)
    return m.hexdigest()

def walk_dir(path="./"):
    final = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            final.append([file_path, md5checksum(file_path), os.path.getmtime(file_path)])
    return(final)

final = list(sorted(walk_dir(), key=lambda x: x[2], reverse=True))

md5=[]
for i in final:
    if i[1] not in md5:
        md5.append(i[1])
    else:
        try:
            os.remove(i[0])
        except:
            pass
