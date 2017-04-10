import mistune, datetime, yaml

def tilde(line):
    try: command = line[line.index("~")+1:line.index(":")] # get the command
    except ValueError:
        print("Malformed command: \"" + line + "\"")
        sys.exit()

    args = line[line.index(":")+1:].split() # get the rest of the args in a list

    if command == "import":
        with open("templates/" + args[0] + ".html", "r") as tempFile:
            data = tempFile.read() # open the template

        parsedTemp = []
        for line in data.splitlines():
            parsedTemp.append(parseTemplateLine(line, "templates/" + args[0] + ".html"))
        data = "\n".join(parsedTemp)

        if len(args) > 1:
            for arg in args[1:]: # skip first arg (command)
                key = arg[:arg.index("=")] # before the =
                value = arg[arg.index("=")+1:] # after the =
                data = data.replace("{{ " + key + " }}", value) # replace
        return data # return the template

def dot(line):
    if line.startswith(".."):
        if line == "..":
            return "</span>"
        else:
            return "<span class=\"" + line[2:] + "\">"
    if line == ".":
        return "</div>"
    else:
        return "<div class=\"" + line[1:] + "\">"

def parseTemplateLine(line, path): # We need path for some static functions
    config = yaml.load(open("config/painless.yml", "r").read())

    line = line.replace("[[ time ]]", datetime.datetime.now().strftime(config["options"]["timeFormat"]))
    line = line.replace("[[ branding ]]", "<p><i>Built <a href='http://github.com/gusg21/painless'>painlessly</a>.</i></p>")

    return line

def default(line):
    line = mistune.markdown(line)
    return line
