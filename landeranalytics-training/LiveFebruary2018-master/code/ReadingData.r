library(readr)
tomato <- read_csv("data/TomatoFirst.csv")

tomato
# tibble or more generic it is a data frame. 
class(tomato)
library(readxl)
excel_sheets("data/ExcelExample.xlsx")
tomatoXL = read_excel("data/ExcelExample.xlsx", sheet="Tomato")
tomatoXL
wineXL = read_excel("data/ExcelExample.xlsx", sheet = 2)
wineXL

file.info("data/ExcelExample.xlsx")
