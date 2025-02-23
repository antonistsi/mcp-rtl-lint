# mcp-rtl-lint

Verilog RTL linter MCP tool: provides an LLM a linting tool for verilog files.

Uses verilator for linting.

## Install mcp tool (Linux/macos)

Install `uv`: [UV installation](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)

```bash
git clone https://github.com/antonistsi/mcp-rtl-lint.git
cd mcp-rtl-lint
uv venv
source .venv/bin/activate
uv pip install .
```

## Use the mcp-rtl-lint tool in your chat

### Goose

[Using Extensions in Goose](https://www.getgoose.ai/docs/latest/getting-started/using-extensions)

### Continue

[Customizing Tools in Continue](https://continue.dev/docs/customization/tools)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
