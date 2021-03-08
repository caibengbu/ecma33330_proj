library(haven)
library(dplyr)
library(x12)
df <- as.data.frame(read_dta("short_ts.dta")) %>%
  filter(!is.na(short))
df <- df[order(df$date),]
short_ts <- ts(df$short, start=c(1994, 1), end=c(2020, 4), frequency=12)
s <- new("x12Single", ts = short_ts)
s <- x12(s)
df$shortadj <- s@x12Output@d11
