# -*- coding: utf-8 -*-
"""Untitled0.ipynb의 사본

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/junan146/d922efe668d0c678fe320ce0da8d8219/untitled0-ipynb.ipynb
"""

import numpy as np
import pandas as pd
import json
import io

from google.colab import files
uploaded = files.upload()

df = pd.read_csv(io.StringIO(uploaded['SWE sample data - Q2 data.csv'].decode('utf-8')),names=["names"])
df2 = pd.DataFrame(columns=("user_id","product_id","quantity"))
index = 0
#print(df)
for i in df["names"]:
  i = eval(i)
  df2.loc[index] = [i.get("user_id"),i.get("product_id"),i.get("quantity")]
  index+=1

# method1
product_counts = df2.drop_duplicates(["user_id","product_id"])
popular = product_counts.groupby(["product_id"]).size().reset_index(name="r")
popular["r"] = popular["r"].rank(ascending=False,method="min")
pop = []
for row in popular[popular["r"]==1.0]["product_id"]:
  pop.append(row)

# method2
quantity = []
sold_counts = df2.groupby("product_id").size().reset_index(name="sum")
sold_counts["sum"] = sold_counts["sum"].rank( ascending=False, method="min")
#print(sold_counts)

for row in sold_counts[sold_counts["sum"]==1.0]["product_id"]:
  quantity.append(row)

print("Most popular product(s) based on the number of purchasers : " , pop)
print("Most popular product(s) based on the quantity of goods sold : " , quantity)

