from fastmcp import FastMCP
from extreme_p_helper import ExtremePHelper

extreme_p_helper = ExtremePHelper()

# Create an MCP server
mcp = FastMCP("extreme-p")

@mcp.tool(
    name="pvalue_extreme_z",
    description="Calculate the extreme p-value for a z-score"
)
def pvalue_extreme_z(z: float) -> dict:
    """
    Calculate the extreme p-value for a z-score
    Args:
        z: float
    Returns:
        dict: A dictionary containing the mantissa and exponent of the extreme p-value
    """
    return extreme_p_helper.pvalue_extreme_z(z)

@mcp.tool(
    name="pvalue_extreme_t",
    description="Calculate the extreme p-value for a t-score"
)
def pvalue_extreme_t(t: float, df: int) -> dict:
    """
    Calculate the extreme p-value for a t-score
    Args:
        t: float
        df: int
    Returns:
        dict: A dictionary containing the mantissa and exponent of the extreme p-value
    """
    return extreme_p_helper.pvalue_extreme_t(t, df)

@mcp.tool(
    name="pvalue_extreme_f",
    description="Calculate the extreme p-value for an F-score"
)
def pvalue_extreme_f(f: float, df1: int, df2: int) -> dict:
    """
    Calculate the extreme p-value for an F-score
    """
    return extreme_p_helper.pvalue_extreme_f(f, df1, df2)

@mcp.tool(
    name="pvalue_extreme_chisq",
    description="Calculate the extreme p-value for a chi-square score"
)
def pvalue_extreme_chisq(chisq: float, df: int) -> dict:
    """
    Calculate the extreme p-value for a chi-square score
    """
    return extreme_p_helper.pvalue_extreme_chisq(chisq, df)

@mcp.tool(
    name="pvalue_extreme_saiget",
    description="Calculate the extreme p-value for a SAIGE t-score"
)
def pvalue_extreme_saiget(t: float, varT: float, df: int) -> dict:
    """
    Calculate the extreme p-value for a SAIGE t-score
    """
    return extreme_p_helper.pvalue_extreme_saiget(t, varT, df)

@mcp.tool(
    name="pvalue_extreme_wald",
    description="Calculate the extreme p-value from beta and se"
)
def pvalue_extreme_wald(beta: float, se: float) -> dict:
    """
    Calculate the extreme p-value from beta and se
    Args:
        beta: float
        se: float
    Returns:
        dict: A dictionary containing the mantissa and exponent of the extreme p-value
    """
    assert se > 0, "se must be greater than 0"
    chisq = (beta / se) ** 2
    return extreme_p_helper.pvalue_extreme_chisq(chisq, 1)

if __name__ == "__main__":
    mcp.run()