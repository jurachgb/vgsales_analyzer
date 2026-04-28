import sqlite3

db=sqlite3.connect("jogos.db")

def formatar(texto):
    return texto[0].upper() + texto[1:].lower()


def check_value():
    while True:
        qtd=input("Selecione a quantidade de jogos dessa categoria que deseja ver: ")
        try:
            qtd=int(qtd)
            if qtd<=0:
                print("Apenas numeros inteiros maiores que zero serão aceitos")
            else:
                return qtd
                break
        except ValueError:
            print("Apenas numeros inteiros e maiores que zero serão aceitos ")
           

def global_sales():
    
    names=db.execute("SELECT name,global_sales FROM jogos ORDER BY global_sales DESC LIMIT (?)",(check_value(),)).fetchall()

    for i,jogos in enumerate(names,1):
        print(i,jogos[0],jogos[1])
    


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
        

    ano=db.execute("SELECT name,global_sales FROM jogos WHERE year=? ORDER BY ranking DESC LIMIT ?",(ano_escolhido,check_value(),)).fetchall()
    if not ano:
        print("Não temos dados desse ano",end="\n")
    else:
        for i,jogos in enumerate(ano,1):
            print(i,jogos[0],jogos[1])

        
def sales_genre():
    escolhido=input("Selecione um genero:  ")
    
    normal=formatar(escolhido)

    genero=db.execute("SELECT name,global_sales FROM jogos WHERE genre=? ORDER BY global_sales DESC LIMIT (?)",(normal,check_value(),)).fetchall()
    for i,jogos in enumerate(genero,1):
        print(i,jogos[0],jogos[1])

def sales_name():
    name=formatar(input("Qual o nome do jogo? "))
    
    nome=db.execute("SELECT name,platform,genre,publisher,year FROM jogos WHERE name LIKE ?",(f"%{name}%",)).fetchall()
    if not nome:
        print("Não achamos nada, por favor corrija a digitação")
    else:
        for i,jogos in enumerate(nome,1):
            print(i,jogos[0],jogos[1],jogos[2],jogos[3],jogos[4])
        
def compare_games():
    generos=db.execute("SELECT DISTINCT genre FROM jogos").fetchall()
    for i in generos:
        print(i[0])
    

    n1=formatar(input("Escolha um desses generos disponiveis:   "))
    n2=formatar(input("Escolha mais um para poder compara-los:  "))

    number=check_value()
    genero_n1=db.execute("SELECT name FROM jogos WHERE genre=? ORDER BY global_sales DESC LIMIT ?",(n1,number),).fetchall()
    genero_n2=db.execute("SELECT name FROM jogos WHERE genre=? ORDER BY global_sales DESC LIMIT ?",(n2,number,)).fetchall()
    contagem=1
    for jogo1,jogo2 in zip(genero_n1,genero_n2):
        print(contagem,"--->  ",jogo1[0]," | ",jogo2[0])
        contagem+=1
        


    

        
print("1-Ver os jogos mais vendidos")
print("2-Ver os jogos mais vendidos por ano")
print("3-Ver os jogos mais vendidos por genero")
print("4-Ver informações por nome do jogo")
print("5-comparar generos")
print("6-Sair")

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
        compare_games()
        
    elif input_user=="6":
        print("Até mais")
        break
    else:
        print("Apenas são aceitos os digitos conforme a tabela abaixo:")
        print("1-Ver os jogos mais vendidos")
        print("2-Ver os jogos mais vendidos por ano")
        print("3-Ver os jogos mais vendidos por genero")
        print("4-Ver informações por nome do jogo")
        print("5-comparar generos")
        print("6-Sair")

        continue
    




