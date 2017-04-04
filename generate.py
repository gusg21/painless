import os, mistune

def generate():
    for fn in os.listdir('pages'):
        with open("pages/" + fn, "r") as mdFile:
        	mdData = mdFile.read()

        with open("serve/" + fn[:fn.index(".")] + ".html", "w") as serveFile:
            parsed = []
            for line in mdData.splitlines():
                if line.startswith("~"):
                    with open("templates/" + line[1:] + ".html", "r") as tempFile:
                    	data = tempFile.read()
                    parsed.append(data)
                elif line.startswith("$"):
                    pass # We don't add the line
                else:
                    parsed.append(mistune.markdown(line))

            parsed = "\n".join(parsed)
            serveFile.truncate(0)
            serveFile.write(parsed)
