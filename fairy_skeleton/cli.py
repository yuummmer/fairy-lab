import subprocess, sys
def main():
    # pass-through runner example; replace with something demo-specific later
    sys.exit(subprocess.call(["fairy", *sys.argv[1:]]))
