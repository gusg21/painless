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
            parsedTemp.append(parseLine(line))
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

def parseLine(line): # Function for parsing our HTML templates
    config = yaml.load(open("config/painless.yml", "r").read()) # load config

    for name in config["customValues"]: # iterate
        value = config["customValues"][name] # get name
        line = replaceSpecials(line, name, value)

    # pre-made one
    line = replaceSpecials(line, "time", datetime.datetime.now().strftime(config["options"]["timeFormat"]))
    line = replaceSpecials(line, "branding", "<p><i>Built <a href='http://github.com/gusg21/painless'>painlessly</a>.</i></p>")

    return line

def replaceSpecials(line, name, value, BRACKETS="["):
    bracketPairs = {
        "[" : "]",
        "{" : "}",
        "(" : ")"
    }
    RBRACKETS = bracketPairs[BRACKETS]

    line = line.replace((BRACKETS * 2) + " " + name + " " + (RBRACKETS * 2), value)
    line = line.replace((BRACKETS * 2) + name + (RBRACKETS * 2), value)

    return line

def default(line): # do to all lines in markdown
    line = parseLine(line)
    print(line)
    line = mistune.markdown(line)
    return line
