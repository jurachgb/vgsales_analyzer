import csv

def check_value():
    while True:
        qtd=input("Selecione a quantidade de jogos dessa categoria que deseja ver: ")
        try:
            qtd=int(qtd)
            if qtd<=0:
                print("Apenas numeros inteiros maiores que zero serão aceitos")
            else:
                return qtd
        except ValueError:
            print("Apenas numeros inteiros e maiores que zero serão aceitos ")

def global_sales():
    with open("vgsales.csv", "r")as sales:
        vgsales=csv.DictReader(sales)
        ordem=sorted(vgsales, key=lambda vg: int(vg["Rank"]))
        gg=1
        for i in ordem[:check_value()]:
            print(gg,end="  ")
            print(i["Name"]+" " +i["Global_Sales"])
            gg+=1

def sales_year():
    while True:
        ano_escolhido=input("Sobre qual ano vc gostaria? ")
        try:
            ano_escolhido=int(ano_escolhido)
            if ano_escolhido>0:
                break
            else:
                print("Apenas numeros inteiros e positivos")
        except ValueError:
            print("Apenas numeros inteiros e positivos")
    with open("vgsales.csv","r")as sales:
        year_sales=csv.DictReader(sales)
        filtro=[]
        for ano in year_sales:
            try:
                if int(ano["Year"]) == ano_escolhido:
                    filtro.append(ano)
            except ValueError:
                continue
        if not filtro:
            print("Não temos dados desse ano")
            return
        ordem=sorted(filtro, key=lambda vg: int(vg["Rank"]))
        gg=1
        for jogo in ordem[:check_value()]:
            print(gg, end="  ")
            print(jogo["Name"],jogo["Global_Sales"])
            gg+=1

def sales_genre():
    escolhido=input("Selecione um genero: ")
    genero_escolhido=escolhido.lower()
    with open("vgsales.csv","r") as genero:
        vendas_por_genero=csv.DictReader(genero)
        filtro=[]
        for genre in vendas_por_genero:
            if genre["Genre"].lower()==genero_escolhido:
                filtro.append(genre)
        if not filtro:
            print("Não encontramos esse genero")
            return
        ordem=sorted(filtro, key=lambda vg: int(vg["Rank"]))
        gg=1
        for jogo in ordem[:check_value()]:
            print(gg,end="  ")
            print(jogo["Name"], jogo["Global_Sales"])
            gg+=1

def sales_name():
    name_escolhido=input("Qual o nome do jogo? ")
    name=name_escolhido.lower()
    with open("vgsales.csv","r")as sales:
        vgsales=csv.DictReader(sales)
        for jogo in vgsales:
            if jogo["Name"].lower() == name:
                print(jogo["Name"],jogo["Platform"],jogo["Year"],jogo["Genre"],jogo["Global_Sales"])

print("1-Ver os jogos mais vendidos")
print("2-Ver os jogos mais vendidos por ano")
print("3-Ver os jogos mais vendidos por genero")
print("4-Ver informações por nome do jogo")
print("5-Sair")

while True:
    print("\n")
    input_user=input("Selecione uma opção para continuar: ")
    if not input_user:
        print("Insira uma opção para continuar: ")
        continue
    elif input_user=="1":
        global_sales()
    elif input_user=="2":
        sales_year()
    elif input_user=="3":
        sales_genre()
    elif input_user=="4":
        sales_name()
    elif input_user=="5":
        print("Até mais")
        break
    else:
        print("Apenas são aceitos os digitos conforme a tabela abaixo:")
        print("1-Ver os jogos mais vendidos")
        print("2-Ver os jogos mais vendidos por ano")
        print("3-Ver os jogos mais vendidos por genero")
        print("4-Ver informações por nome do jogo")
        print("5-Sair")
        continue