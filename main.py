import pandas as pd
import mysql.connector
from mysql.connector import Error


raisin = pd.read_excel("Raisin_Dataset.xlsx")
print(raisin)
name_columns=['area','majoraxislength', 'minoraxislength', 'eccentricity','convexArea', 'extent', 'perimeter', 'class']
raisin.columns=name_columns
print(raisin)

# Chargement du dataframe dans MYSQL
try:
    connexion = mysql.connector.connect(host='localhost',
                                       database='db_raisin',
                                       user='root',
                                       password='')
    if connexion.is_connected():
        print('Connexion à MySQL réussie')
except Error as e:
    print(f"Erreur lors de la connexion à MySQL: {e}")

try:
    cursor = connexion.cursor()

    for i,row in raisin.iterrows():
        sql = """INSERT INTO domaine (area,major_axis_length,minor_axis_length, eccentricity,convex_area,extent,perimeter,class) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        #print(sql)
        cursor.execute(sql, tuple(row))

    connexion.commit()
    connexion.close()
    print("DataFrame chargé dans MySQL avec succès!")
except Exception as e:
    print(f"Erreur lors du chargement du DataFrame dans MySQL: {e}")
