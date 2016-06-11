import tarfile, os

def unpackAll(sourceDir, destDir):
    "Extracts all files from all archives of the source directory to the destination directory"
    for archiveName in os.listdir(sourceDir):
        filePath = os.path.join(sourceDir, archiveName)
        with tarfile.open(filePath, "r:gz") as f:
            f.extractall(destDir)

if __name__ == "__main__":  
    import argparse, sys

    DEFAULT_EXTRACT_DIR = "data\\papers"

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", dest = "source", help = "source directory containing the archives")
    parser.add_argument("-d", dest = "destination", default = DEFAULT_EXTRACT_DIR, required = False, help = "destination directory")

    args = parser.parse_args(sys.argv[1:])
    unpackAll(args.source, args.destination)






