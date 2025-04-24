# Via https://stackoverflow.com/a/46416222/199475
pvalue.extreme.z <- function(z) {
   log.pvalue <- log(2) + pnorm(abs(z), lower.tail = FALSE, log.p = TRUE)
   log10.pvalue <- log.pvalue/log(10) ## from natural log to log10
   mantissa <- 10^(log10.pvalue %% 1)
   exponent <- log10.pvalue %/% 1
   return(list(mantissa=mantissa,exponent=exponent))
}

# Modified to the t-score approach from the Z-score based approach on https://stackoverflow.com/a/46416222/199475
pvalue.extreme.t <- function(t, df) {
   log.pvalue <- log(2) + pt(abs(t), df=df, lower.tail = FALSE, log.p = TRUE)
   log10.pvalue <- log.pvalue/log(10) ## from natural log to log10
   mantissa <- 10^(log10.pvalue %% 1)
   exponent <- log10.pvalue %/% 1
   return(list(mantissa=mantissa,exponent=exponent))
}

# Modified from the Z-score based approach on https://stackoverflow.com/a/46416222/199475
pvalue.extreme.f <- function(f, df1, df2) {
   log.pvalue <- log(2) + pf(abs(f), df1, df2, lower.tail = FALSE, log.p = TRUE)
   log10.pvalue <- log.pvalue/log(10) ## from natural log to log10
   mantissa <- 10^(log10.pvalue %% 1)
   exponent <- log10.pvalue %/% 1
   return(list(mantissa=mantissa,exponent=exponent))
}

# Modified to the chi-square score approach from the Z-score based approach on https://stackoverflow.com/a/46416222/199475
pvalue.extreme.chisq <- function(chisq, df) {
   log.pvalue <- pchisq(chisq, df = df, lower.tail = FALSE, log.p = TRUE)
   log10.pvalue <- log.pvalue / log(10)
   mantissa <- 10^(log10.pvalue %% 1)
   exponent <- log10.pvalue %/% 1
   return(list(mantissa=mantissa,exponent=exponent))
}

# Modified to the chisq approach based on SAIGE: https://rdrr.io/github/weizhouUMICH/SAIGE/src/R/SAIGE_SPATest.R
pvalue.extreme.saiget <- function(t, varT, df) {
   return(pvalue.extreme.chisq(t^2/varT, df))
}
