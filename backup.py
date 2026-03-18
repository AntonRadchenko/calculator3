import shutil

def backup(source, destination):
    shutil.copytree(source, destination)
    print("Backup complete!")