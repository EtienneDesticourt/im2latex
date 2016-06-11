import re, os, sys

def numGroups(pattern):
    "Returns the number of groups in a pattern"
    return re.compile(pattern).groups

def extract(filePath, eqPattern, encoding):
    "Returns all equations matching the given pattern in the file"
    with open(filePath, "r", encoding = encoding) as f: 
        matches = re.findall(eqPattern, f.read())
        #If there is more than one group we get a list of tuples of equations otherwise a list of equations
        if numGroups(eqPattern) > 1: 
            #Unpack each match and get rid of empty equations (1 match = x equations tuple for x pattern groups)
            return [equation for match in matches for equation in match if equation != ""]
        return matches

def extractAll(rootDirPath, eqPattern, encoding):
    "Returns all the equations from all the files in the given root directory and all its subdirectories"
    equations = []
    for dirPath, dirNames, fileNames in os.walk(rootDirPath):
        for fileName in fileNames:
            filePath = os.path.join(dirPath, fileName)
            equations += extract(filePath, eqPattern, encoding)
    return equations
    

if __name__ == "__main__":  
    import argparse, sys

    OLD_EQ_PATTERN = "(\\\\begin\{equation\}.*?\\\\end\{equation\})|(\\\\be.*?\\\\ee)|(\$.*?\$)"
    DEFAULT_EQUATION_PATTERN = "(\$.*?\$)"
    DEFAULT_DEST = "equations.txt"
    DEFAULT_ENCODING = "latin1"

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", dest = "source", required = True, help = "source directory containing the papers")
    parser.add_argument("-d", dest = "destination", default = DEFAULT_DEST,             required = False, help = "destination filepath")
    parser.add_argument("-p", dest = "pattern",     default = DEFAULT_EQUATION_PATTERN, required = False, help = "pattern to match equations")
    parser.add_argument("-e", dest = "encoding",    default = DEFAULT_ENCODING,         required = False, help = "encoding of the source files")

    args = parser.parse_args(sys.argv[1:])
    #Took a couple minutes on my PC for the challenge's dataset
    equations = extractAll(args.source, args.pattern, args.encoding)    
    with open(args.destination, "w", encoding = args.encoding) as f:
        f.write("\n".join(equations))

    