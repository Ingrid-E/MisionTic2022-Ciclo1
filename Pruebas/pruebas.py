from typing import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

dictc = {"country": ["Brazil", "Russia", "India",
"China", "South Africa", "Colombia"],
"capital": ["Brasilia", "Moscow", "New Dehli",
"Beijing", "Pretoria", "Bogot ́a"],
"area": [8.516, 17.10, 3.286, 9.597, 1.221, 1.142],
"population": [200.4, 143.5, 1252, 1357, 52.98, 49.65] }

brics = pd.DataFrame(dictc)
#        country    capital    area  population
#0        Brazil   Brasilia   8.516      200.40
#1        Russia     Moscow  17.100      143.50
#2         India  New Dehli   3.286     1252.00
#3         China    Beijing   9.597     1357.00
#4  South Africa   Pretoria   1.221       52.98
#5      Colombia   Bogot ́a   1.142       49.65

ventasPaises = pd.read_csv("SalesJan2009.csv")
ventasPaises.head(3)
#    Transaction_date   Product  Price  ...      Last_Login   Latitude   Longitude
# 0      1/2/2009 6:17  Product1   1200  ...   1/2/2009 6:08  51.500000   -1.116667
# 1      1/2/2009 4:53  Product1   1200  ...   1/2/2009 7:49  39.195000  -94.681940
# 2     1/2/2009 13:08  Product1   1200  ...  1/3/2009 12:32  46.188060 -123.830000
# 3     1/3/2009 14:44  Product1   1200  ...  1/3/2009 14:22 -36.133333  144.750000
# 4     1/4/2009 12:56  Product2   3600  ...  1/4/2009 12:45  33.520560  -86.802500
# ..               ...       ...    ...  ...             ...        ...         ...
# 992  1/22/2009 14:25  Product1   1200  ...   3/1/2009 3:37  54.583333   -5.933333
# 993   1/28/2009 5:36  Product2   3600  ...   3/1/2009 4:40 -20.360278   57.366111
# 994    1/1/2009 4:24  Product3   7500  ...   3/1/2009 7:21  42.946940  -76.429440
# 995   1/8/2009 11:55  Product1   1200  ...   3/1/2009 7:28  52.083333    0.433333
# 996  1/12/2009 21:30  Product1   1200  ...  3/1/2009 10:14  43.073060  -89.401110
#[997 rows x 12 columns]
cantidadPais = Counter(ventasPaises["Country"])
print(cantidadPais) # diccionario con la cantidad de veces que aparece 
                    # un pais en el archivo
print(cantidadPais.most_common(3)) #[('United States', 462), ('United Kingdom', 100), ('Canada', 76)]

ventasPaises["Transaction_date"] = pd.to_datetime(ventasPaises["Transaction_date"])
A = (ventasPaises['Transaction_date']
        .dt.floor("d")
        .value_counts()
        .rename_axis("date")
        .reset_index(name="num ventas"))

G = A.plot(x="date", y="num ventas", color="green", title="Ventas por fecha")
plt.show()