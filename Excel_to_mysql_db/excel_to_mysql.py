# Upload data in mysql db.

import pandas as pd
import openpyxl
import sqlalchemy
from sqlalchemy import create_engine
import pymysql

# creating connection to db, using sqlalchemy dialect.
engine = create_engine ('mysql+pymysql://root:root@localhost:3306/reportapp?charset=utf8mb4')
#conn=engine.connet()

# reading excel file and copy it to dataframe
svr_data = pd.ExcelFile(r'D:\site_report.xlsx')

svr_dataframe = svr_data.parse(sheet_name=0)

# I needed to change column name, columns had space in between words, which will be replaced by "_". this will I can query data in mysql using name. 
svr_dataframe.columns = svr_dataframe.columns.str.replace(' ','_')

# importing data to Mysql table named svr, index false because df has its own index which is not required in mysql db, if sql table does'nt exist then it will be created if exist data will be appended.
svr_dataframe.to_sql(name ='svr', con=engine, index=False, if_exists = "append")