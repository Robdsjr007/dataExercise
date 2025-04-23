import pandas as pd
import mysql.connector 

anoIncidentes = pd.read_csv("C:/Sgsp/ano_incidentes.csv", encoding="latin1", on_bad_lines='skip', sep=";")
plan = pd.read_csv("C:/Sgsp/dataset.csv", encoding="latin1", on_bad_lines='skip', sep=";")

plan.columns = plan.columns.str.strip() #remove os espaços
anoIncidentes.columns = anoIncidentes.columns.str.strip()

plan = plan.dropna() #remove nulos
anoIncidentes = anoIncidentes.dropna()

plan = plan.drop_duplicates()
anoIncidentes = anoIncidentes.drop_duplicates()

print(plan.head()) #mostra a a tabela
print("----------------------------------")
print(anoIncidentes.head())

print("Total de duplicadas encontradas")
print(plan.duplicated().sum()) #verfica quantos nulos tem
print(anoIncidentes.duplicated().sum())



