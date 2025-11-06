# fairy_skeleton/cli.py
import argparse, subprocess, sys, shutil
from pathlib import Path

DEMO_DIR = Path(__file__).resolve().parent.parent / "demos"

def _find_configs():
    return sorted(p for p in DEMO_DIR.glob("*/config.yaml") if p.is_file())

def cmd_demos():
    for cfg in _find_configs():
        print(cfg.parent.name)

def cmd_run(name: str):
    matches = [c for c in _find_configs() if c.parent.name == name]
    if not matches:
        print(f"No demo named '{name}'. Try: 'fairy-skel demos'", file=sys.stderr)
        sys.exit(2)
    cfg = matches[0]
    runner = ["fairy"] if (shutil.which("fairy")) else [sys.executable, "-m", "fairy.cli.run"]
    subprocess.check_call(["bash", str(DEMO_DIR.parent / "scripts" / "run_demo.sh"), str(cfg)])

def main():
    ap = argparse.ArgumentParser(prog="fairy-skel", description="FAIRy-skeleton demo runner")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("demos", help="List available demos")
    runp = sub.add_parser("run", help="Run a demo by name"); runp.add_argument("name")
    args = ap.parse_args()
    if args.cmd == "demos": cmd_demos()
    elif args.cmd == "run": cmd_run(args.name)
    else: ap.print_help()

if __name__ == "__main__":
    main()
