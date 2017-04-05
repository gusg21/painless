import argparse, sys
import generate, serve

'''
A simple markdown based static site generator written in Python. Meant to make blog creation painless, hence the name.
'''

def main():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument("command", help="Command for painless (gen, serve)")

    args = parser.parse_args(sys.argv[1:])

    if args.command.lower() == "gen":
        generate.generate()
    elif args.command.lower() == "serve":
        serve.serve(PORT=8000, SERVE="serve")
    else:
        print("Unknown command: " + args.command)
        print("Command is one of: gen, serve")

if __name__ == '__main__':
    main()
