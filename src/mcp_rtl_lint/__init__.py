import argparse
from .server import mcp

def main():
    """MCP RTL Lint - SystemVerilog linting tool using Verilator"""
    parser = argparse.ArgumentParser(
        description="Gives you the ability to run a systemverilog linter on a file given its path, returning a list of lint errors and warnings."
    )
    parser.parse_args()
    mcp.run()

if __name__ == "__main__":
    main()
