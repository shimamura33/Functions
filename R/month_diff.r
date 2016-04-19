monnb <- function(d) { lt <- as.POSIXlt(as.Date(d, origin="1900-01-01")); 
                       lt$year*12 + lt$mon } 
mondf <- function(d1, d2) { monnb(d2) - monnb(d1) }

### Use Case ###
mondf(as.Date("2008-01-01"), Sys.Date()) # output 24
