import os, mistune
import lineparser

def generate(outputDirectory):
    for fn in os.listdir('pages'):
        # make sure it's markdown
        if not fn.endswith(".md"):
            continue # skippy

        # read file in mdData
        with open("pages/" + fn, "r") as mdFile:
        	mdData = mdFile.read()

        # open the file we'll write to
        with open(outputDirectory + "/" + fn[:fn.index(".")] + ".html", "w") as serveFile:
            parsed = [] # the final list of lines in HTML
            for line in mdData.splitlines(): # iterate over lines
                if line.startswith("~"): # if it's an import
                    parsed.append(lineparser.tilde(line))
                elif line.startswith("."): # class line
                    parsed.append(lineparser.dot(line))
                elif line.startswith("$"): # it it's a comment
                    pass # We don't add the line
                else:
                    parsed.append(mistune.markdown(line)) # parse as markdown

            parsed = "\n".join(parsed) # turn the lines into a string
            serveFile.truncate(0) # empty file
            serveFile.write(parsed) # write string
