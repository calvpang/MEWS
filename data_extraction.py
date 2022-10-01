from re import L
import pandas as pd
import csv
from datetime import datetime


output_df = pd.DataFrame(
    columns=[
        "Lat",
        "Long",
        "Date",
        "Type",
        "Source",
    ]
)

df = pd.read_csv('Data/gagnepian_2006_catalog.csv')
print (df)
for idx, row in df.iterrows():
    date = datetime.strptime(str(row["Date"]), "%y%m%d%H%M")
    output_df = output_df.append({
        "Lat":row["Lat"],
        "Long":row["Long"],
        "Date":date,
        "Type":row["Type"],
        "Source": "gagnepian_2006_catalog",
    }, ignore_index=True)

df = pd.read_csv('Data/lognonne_2003_catalog.csv')
print (df)
for idx, row in df.iterrows():
    print(row["Date"])
    if row["Date"] == 7704712332:
        # skip incorrect data
        continue
    date = datetime.strptime(str(row["Date"]), "%y%m%d%H%M")
    output_df = output_df.append({
        "Lat":row["Lat"],
        "Long":row["Long"],
        "Date":date,
        "Type":row["Type"],
        "Source": "lognonne_2003_catalog",
    }, ignore_index=True)


df = pd.read_csv('Data/nakamura_1979_sm_locations.csv')
print (df)
for idx, row in df.iterrows():
    date_str = f'{row["Year"]}{row["Day"]:03d}{row["H"]:02d}{row["M"]:02d}{row["S"]:02d}'
    print(date_str)
    date = datetime.strptime(date_str, "%Y%j%H%M%S")
    output_df = output_df.append({
        "Lat":row["Lat"],
        "Long":row["Long"],
        "Date":date,
        "Type":"sm",
        "Source": "nakamura_1979_sm_locations",
    }, ignore_index=True)

df = pd.read_csv('Data/nakamura_1983_ai_locations.csv')
print (df)
for idx, row in df.iterrows():
    date_str = f'{row["Y"]}{row["JD"]:03d}{row["Hour"]:02d}{row["Min"]:02d}{int((str(row["Sec"])[:2])):02d}'
    print(date_str)
    date = datetime.strptime(date_str, "%Y%j%H%M%S")
    output_df = output_df.append({
        "Lat":row["Lat"],
        "Long":row["Long"],
        "Date":date,
        "Type":"ai",
        "Source": "nakamura_1983_ai_locations",
    }, ignore_index=True)


# Create a dictionary of cluster numbers that output their datetime
cluster_num = {}
df = pd.read_csv('Data/levent.1008weber.csv')
for idx, row in df.iterrows():
    datetime_str = f'{row["Y"]}{row["JD"]:03d}{row["S"]}'
    this_datetime = datetime.strptime(datetime_str, "%y%j%H%M")
    cluster_num[row["N2"]] = this_datetime


df = pd.read_csv('Data/nakamura_2005_dm_locations.csv')
print (df)
for idx, row in df.iterrows():
    date = cluster_num[row["A"]]
    output_df = output_df.append({
        "Lat":row["Lat"],
        "Long":row["Long"],
        "Date":date,
        "Type":"dm",
        "Source": "nakamura_2005_dm_locations",
    }, ignore_index=True)

print(output_df)
output_df.to_csv("cleaned_data.csv")