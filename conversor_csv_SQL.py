import csv
import sqlite3

db=sqlite3.connect("jogos.db")

with open("vgsales.csv","r")as games:
    jogo=csv.DictReader(games)
    for i in jogo:
        print(i)
        name=i["Name"]
        rank=i["Rank"]
        plat=i["Platform"]
        year=i["Year"]
        genre=i["Genre"]
        publ=i["Publisher"]
        sales=i["Global_Sales"]
        db.execute("INSERT INTO jogos (name,ranking,platform,year,genre,publisher,global_sales) VALUES(?,?,?,?,?,?,?)",(name,rank,plat,year,genre,publ,sales))

db.commit()
db.close()