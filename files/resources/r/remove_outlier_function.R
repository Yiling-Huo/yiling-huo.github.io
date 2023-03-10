remove_outliers <- function(x, na.rm = TRUE, ...) {
  mean = mean(x)
  std = sd(x)
  Tmin = mean-(3*std)
  Tmax = mean+(3*std)
  y <- x
  y[which(x < Tmin)] <- NA
  y[which(x > Tmax)] <- NA
  print(paste('Removed:', sum(is.na(y)), sep=' '))
  y
}
