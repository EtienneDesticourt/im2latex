import tarfile, os

def unpackAll(sourceDir, destDir):
    "Extracts all files from all archives of the source directory to the destination directory"
    for archiveName in os.listdir(sourceDir):
        filePath = os.path.join(sourceDir, archiveName)
        with tarfile.open(filePath, "r:gz") as f:
            
            import os
            
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(f, destDir)

if __name__ == "__main__":  
    import argparse, sys

    DEFAULT_EXTRACT_DIR = "data\\papers"

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", dest = "source", help = "source directory containing the archives", required = True)
    parser.add_argument("-d", dest = "destination", default = DEFAULT_EXTRACT_DIR, required = False, help = "destination directory")

    args = parser.parse_args(sys.argv[1:])
    unpackAll(args.source, args.destination)
