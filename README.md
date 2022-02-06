# Warning Stripes

A script to generate warning stripes from IPMA's long datasets
 
# Credits 

This app is based on the script created by 
[**Steven Pestana**](https://github.com/spestana/ulmo-warming-stripes/blob/main/warming-stripes.ipynb)

that, in turn, is based on the script developed by 
[**Maximilian Nöthe**](https://matplotlib.org/matplotblog/posts/warming-stripes/)

# Data Source
Temperature data for Lisbon from [**IPMA**](https://www.ipma.pt/pt/oclima/series.longas/list.jsp)
## Period: 1855 to 2018


* * *


![warming-stripes-lisbon](https://user-images.githubusercontent.com/34355337/152680902-7cb67741-ee9e-4fdc-a9c7-40e4f47a6a59.jpg)

* * *

# How to generate warning stripes based on **IPMA**'s datasets 

1. Download the xls from IPMA's website 
2. Create date column by **concatenating** year month day columns
3. Change xls to csv format 
4. Change the CSV path in line **35**
5. Change city name in line **93**
6. Change final file name in line **100**

