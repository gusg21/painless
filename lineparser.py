def tilde(line):
    try: command = line[line.index("~")+1:line.index(":")] # get the command
    except ValueError:
        print("Malformed command: \"" + line + "\"")
        sys.exit()

    args = line[line.index(":")+1:].split() # get the rest of the args in a list

    if command == "import":
        with open("templates/" + args[0] + ".html", "r") as tempFile:
            data = tempFile.read() # open the template
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
