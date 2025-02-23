import subprocess
from pathlib import Path
from typing import List, Dict

from mcp.server.fastmcp import FastMCP, Context
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS

mcp = FastMCP("rtl_lint")


@mcp.tool()
async def run_verilator_lint(ctx: Context, filename: str) -> str:
    """Run verilator lint on a SystemVerilog file and return the results.

    Args:
        ctx: MCP Context object for logging
        filename: Absolute path to the SystemVerilog file to lint

    Returns:
        String of verilator output (stderr)
    """
    # TODO verilator bin param
    try:
        await ctx.info(f"Running verilator lint on file: {filename}")
        
        # Run verilator with lint-only and all warnings enabled
        result = subprocess.run(
            ["/opt/homebrew/bin/verilator", "--lint-only", "-Wall", filename],
            capture_output=True,
            text=True,
            check=False,
        )

        # Log the lint request and results
        await ctx.info(f"Verilator return code: {result.returncode}")
        await ctx.debug(f"Verilator stdout: {result.stdout}")

        # Log an error if the return code is non-zero
        if result.returncode != 0:
            await ctx.error(f"Verilator encountered an error (return code: {result.returncode})")

        return result.stderr

    except subprocess.CalledProcessError as e:
        await ctx.error(f"CalledProcessError: {str(e)}")
        return f"Error: {str(e)}"
    except Exception as e:
        await ctx.error(f"Unexpected error: {str(e)}")
        return f"Error: {str(e)}"

# import ipdb;
# ipdb.set_trace()
