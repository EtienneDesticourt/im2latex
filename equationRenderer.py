#Implementing this has been a major pain in the ass.
#I think it'd probably be easier to install Tex-Live
#and generate the image with it and ImageMagick but
#I don't really like having to depend on external programs.
#Tinker with the render function at your own peril.
#Closing figures instead of clearing the plot will
#bring up Tkinter errors so you're limited to the default
#figure since you clearing the plot deletes it.
#The savefig randomly fails because of a variable called
#cached_font which is None sometimes, not sure why, don't 
#really care to look into it.
#A good thing to do would be to remove the ValueError catch
#from __main__ and instead check for bad equations prior
#to calling this util.
#Probably should also add a starting index so we can restart 
#generation at a certain equation in case of an error.
import matplotlib.pyplot as plt

def render(formula, filePath, fontSize=15, figSize = (2, 2)):
    "Saves an image of the rendered formula to given file path"
    #f, axes = plt.subplots(figsize = figSize)
    plt.figure(num = 1, figsize = figSize) #num = 1 : default figure
    plt.text(0, 0, formula)
    plt.axis('off')
    plt.savefig(filePath)
    plt.clf()

if __name__ == "__main__":
    import argparse, sys, os

    DEFAULT_DEST = "data\\images"

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", dest = "source", required = True, help = "source file containing equations to render")
    parser.add_argument("-d", dest = "destination", default = DEFAULT_DEST, required = False, help = "destination directory")

    args = parser.parse_args(sys.argv[1:])

    with open(args.source, "r") as f:
        index = 0
        for equation in f:
            filePath = os.path.join(args.destination, str(index)+".png")
            try:
                render(equation, filePath)
            except (ValueError, AttributeError): #ValueError for parsing error, AttributeError for cached_font = None error
                plt.clf()
            index += 1
            