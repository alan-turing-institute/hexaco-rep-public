#!/usr/local/bin/Rscript --vanilla

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 3) {
  stop("Usage: PCA.R <input_file> <n_factors> <rotation_method>")
}

# capture arguments
input_file <- args[1]
n_factors <- as.numeric(args[2])
rotation_method <- args[3]
cat("Args: input_file=", input_file, ", n_factors=", n_factors, ", rotation_method", rotation_method, "\n")

# load required packages
library(readr)
library(psych)

# read in data from arg-file
df <- read_csv(input_file)

# remove the names column.
df$`...1` <- NULL 

# remove the 'niggardly' adjective/column.
df$niggardly <- NULL

# remove any columns where sd == 0.
df <- df[,apply(df, 2, function(x) sd(x) != 0)]

# call pca
p <- pca(df, nfactors=n_factors, rotate=rotation_method, cor="cov") 

# save results.
write.csv(p$loadings, 'loadings.csv')
