from operator import index
from textwrap import indent
import pandas as pd
import os

path = "D:/Data/Mylecture/DATA7901/Outbound_Dataset/OUTBOUND_DATA_1995-2019"
dirs = os.listdir(path)
df_list = []
origin_list = []

for file in dirs:
    # 处理数据
    df = pd.read_excel(path + '/' + file)
    df = df[6:]
    df.columns = ['Destination', 'SERIES', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '% Change 2019-2018']
    #将介绍信息清理后, 发现末尾仍有两行多余信息, 将其清除
    df.dropna(axis=0, subset=['SERIES'], inplace=True)
    df_list.append(df)

    # All origins' names
    origin_name = ((str(file).split(' O'))[0])
    if origin_name.find('of') != -1:
        if origin_name.index('of') == len(origin_name) - 2:
            origin_name = origin_name.split(' of')[0]
    origin_list.append(origin_name)
    print(origin_name)

# Applying preprocessing on each dataframe
# I only need the data from 2018 to 2019, so lets drop other columns
i = 0
for df in df_list:
    df.drop(columns=['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '% Change 2019-2018'], inplace=True)
    df.reset_index(inplace=True, drop=True)
    df['2018'].fillna(value=0, inplace=True)
    df['2019'].fillna(value=0, inplace=True)
    Average = (df['2018'] + df['2019']) / 2
    df['Average'] = Average

    # export the dataframe to csv file
    df.to_csv(path_or_buf="D:/Data/Mylecture/DATA7901/Outbound_Dataset/cleaning_dataset/" + str(origin_list[i]) + ".csv", index=False)
    i = i + 1