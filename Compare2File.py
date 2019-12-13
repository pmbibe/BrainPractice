import os
import hashlib

path_remote = '/root/remote_machine'
path_local = '/root/compare'

def path_file(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.php' in file:
                files.append(os.path.join(r, file))
    return files

def hash_file(file):
    BUF_SIZE = 65536
    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

def main():
    files_remote = path_file(path_remote)
    files_local = path_file(path_local)
    for file1 in files_local:
        for file2 in files_remote:
            if (file1.split("/")[-1] == file2.split("/")[-1]) and (hash_file(file1) != hash_file(file2)):
                print(file2)
main()
