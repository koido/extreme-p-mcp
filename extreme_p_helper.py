import os
from pyper import R

class ExtremePHelper:
    def __init__(self, r_script_path: str = "extreme-P.R"):
        self.r = R()
        # Use absolute path to ensure the R script is loaded from anywhere
        abs_r_script_path = os.path.abspath(r_script_path)
        with open(abs_r_script_path, "r") as f:
            r_code = f.read()
        self.r(r_code)

    def pvalue_extreme_z(self, z: float) -> dict:
        """
        Call pvalue.extreme.z(z) in R.
        """
        self.r.assign("z", z)
        self.r("result <- pvalue.extreme.z(z)")
        mantissa = self.r.get("result$mantissa")
        exponent = self.r.get("result$exponent")
        return {"mantissa": mantissa, "exponent": exponent}

    def pvalue_extreme_t(self, t: float, df: int) -> dict:
        """
        Call pvalue.extreme.t(t, df) in R.
        """
        self.r.assign("t", t)
        self.r.assign("df", df)
        self.r("result <- pvalue.extreme.t(t, df)")
        mantissa = self.r.get("result$mantissa")
        exponent = self.r.get("result$exponent")
        return {"mantissa": mantissa, "exponent": exponent}

    def pvalue_extreme_f(self, f_val: float, df1: int, df2: int) -> dict:
        """
        Call pvalue.extreme.f(f, df1, df2) in R.
        """
        self.r.assign("f", f_val)
        self.r.assign("df1", df1)
        self.r.assign("df2", df2)
        self.r("result <- pvalue.extreme.f(f, df1, df2)")
        mantissa = self.r.get("result$mantissa")
        exponent = self.r.get("result$exponent")
        return {"mantissa": mantissa, "exponent": exponent}

    def pvalue_extreme_chisq(self, chisq: float, df: int) -> dict:
        """
        Call pvalue.extreme.chisq(chisq, df) in R.
        """
        self.r.assign("chisq", chisq)
        self.r.assign("df", df)
        self.r("result <- pvalue.extreme.chisq(chisq, df)")
        mantissa = self.r.get("result$mantissa")
        exponent = self.r.get("result$exponent")
        return {"mantissa": mantissa, "exponent": exponent}

    def pvalue_extreme_saiget(self, t: float, varT: float, df: int) -> dict:
        """
        Call pvalue.extreme.saiget(t, varT, df) in R.
        """
        self.r.assign("t", t)
        self.r.assign("varT", varT)
        self.r.assign("df", df)
        self.r("result <- pvalue.extreme.saiget(t, varT, df)")
        mantissa = self.r.get("result$mantissa")
        exponent = self.r.get("result$exponent")
        return {"mantissa": mantissa, "exponent": exponent} 