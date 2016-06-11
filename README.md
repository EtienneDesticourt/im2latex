# im2latex

Trying to complete this challenge: https://openai.com/requests-for-research/#im2latex

##Utilities

####Unzipper

Unzips all archives from a directory into another. <br>
Usage: python unzipper.py -s source dir -d destination dir

####Equation Extractor

Extracts all latex equations for every file in a directory and saves them to a file. <br>
Usage: python equationExtractor.py -s source dir -d dest file -p equation regex -e file encoding <br>
Default regex is (\$.*?\$) (for single line equations)

####Equation Renderer

Saves all equations in a file to 200x200 image files. <br>
Usage: python equationRenderer.py -s source file -d destination dir <br>
Source file must have equations separated by line break

##Algorithm

Working on it.
