import pandas as pd
import os

df=pd.read_csv('lunarena1.csv',delimiter='\t',encoding='utf-16')

data2 = df.rename({'first_name':'Nombre', 'last_name':'Apellido', 'phone_number':'Numero', 'email':'Correo', 'adset_name':'Campaña', "created_time" : "Hora" }, axis='columns')

data3 = data2[['Nombre','Apellido','Numero',"Correo", "Campaña","Hora"]] 

print(data3)

gdrivepath = "gdrive/lunarena1.xlsx"

data3.to_excel("df/test.xls")