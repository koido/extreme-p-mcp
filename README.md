# Extreme P-value MCP Server

## Overview

This MCP server provides an API interface to extreme p-value calculation functions (z, t, F, chi-square, SAIGE) implemented in the R script `extreme-P.R`, via Python.

- **Strongly depends on the R script `extreme-P.R` (except for Wald).**
- Uses [pyper](https://github.com/nteract/pyper) to call R from Python.
- The API server is built with [FastMCP](https://github.com/jlowin/fastmcp).
- `extreme_p_helper.py` is a 1-to-1 wrapper for the R functions.
- `server.py` provides the API endpoints.

## Status

🚧 **Under Active Development** 🚧

This project is under active development. APIs and features may change without notice.

## Dependencies

- uv
- pyper
- fastmcp
- mcp[cli]

## Directory structure

```
+.
├── server.py              # Main FastMCP server
├── extreme_p_helper.py    # R function wrapper
├── extreme-P.R            # R script for extreme p-value calculation (see acknowledgements)
├── pyproject.toml         # Dependencies
└── README.md              # This document
```

## Setup and Running

### Install dependencies

```bash
uv sync
```

### Start the server

```bash
uv run server.py
```

## API Endpoint Examples

- `/pvalue_extreme_z(z: float)`
- `/pvalue_extreme_t(t: float, df: int)`
- `/pvalue_extreme_f(f: float, df1: int, df2: int)`
- `/pvalue_extreme_chisq(chisq: float, df: int)`
- `/pvalue_extreme_saiget(t: float, varT: float, df: int)`
- `/pvalue_extreme_wald(beta: float, se: float)`

### Example: Using from Python

```python
from extreme_p_helper import ExtremePHelper
helper = ExtremePHelper()
result = helper.pvalue_extreme_z(10)
print(result)  # {'mantissa': ..., 'exponent': ...}
```

## License

This MCP server is released under the Apache License 2.0.

## Acknowledgements

- [skoyamamd](https://gist.github.com/skoyamamd/4f97b43c7171e01a8c50e9aa18b0ebf0) and [carbocation](https://gist.github.com/carbocation/d39a20ed028b25ff3528468b455b2bcc)
- [pyper](https://github.com/nteract/pyper)
- [FastMCP](https://github.com/jlowin/fastmcp)