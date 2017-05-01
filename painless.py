import argparse, sys, yaml
import generate, serve

VERSION = "v0.0"

__doc__ = '''
A simple markdown based static site generator written in Python. Meant to make site creation painless, hence the name.

Version: ''' + VERSION

def main():
    # Argument parser
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument("command", help="Command for painless (gen, serve, version)")

    args = parser.parse_args(sys.argv[1:])

    # Load config
    config = yaml.load(open("config/painless.yml", "r").read())

    if args.command.lower() == "gen":
        generate.generate(config["options"]["outputDirectory"])
    elif args.command.lower() == "serve":
        serve.serve(PORT=config["options"]["port"], SERVE=config["options"]["outputDirectory"])
    elif args.command.lower() == "version":
        print("Version: " + VERSION)
    else:
        print("Unknown command: " + args.command)
        print("Command is one of: gen, serve, version")

if __name__ == '__main__':
    main()
