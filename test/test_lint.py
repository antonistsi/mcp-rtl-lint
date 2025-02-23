import pytest
import asyncio
from pathlib import Path
from src.mcp_rtl_lint.server import run_verilator_lint


def test_latch_detection():
    # Get path to test file relative to this test file
    test_dir = Path(__file__).parent
    test_file = test_dir / "latch_example.sv"

    from mcp.server.fastmcp import FastMCP, Context
    mcp = FastMCP("TestApp")
    # Get a context for testing
    mcp_ctx = mcp.get_context()

    # Run linter
    results = asyncio.run(run_verilator_lint(mcp_ctx, str(test_file)))

    expected_substring = "Latch inferred for signal 'q' (not all control paths of combinational always assign a value)"
    
    # Verify we get the expected substring in the results
    assert expected_substring in results, f"Expected '{expected_substring}' to be in the lint results"