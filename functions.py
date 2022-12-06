def MenuInicial(admin):
    if admin==True:
        while True:
            print("|| Menu Admin\n|| 1. Pesquisar\n|| 2. Editar\n|| 0. Sair")
            opt=int(input("|| Opção:"))
            if opt==1:
                MenuPesquisar()
            elif opt==2:
                MenuEditar()
            elif opt==0:
                print("|| Terminado com sucesso")
                break
            else:
                print("|| O valor introdzido é inválido")
                continue
    else:
        while True:
            print("|| Menu Inicial\n|| 1. Pesquisar\n|| 0. Sair")
            opt=int(input("|| Opção:"))
            if opt==1:
                MenuPesquisar()
            elif opt==0:
                print("|| Terminado com sucesso")
                break
            else:
                print("|| O valor introdzido é inválido")
                continue
#Acessivel a admin e utilizador
#Quando for criada a função de leitura e escrita do ficheiro csv retirar Direitos editorais á lista do utilizador
def MenuPesquisar():
    while True:
        print("|| Menu De Pesquisa\n|| 1. Autor\n|| 2. Álbum\n|| 3. Música\n|| 0. Voltar")
        opt=int(input("|| Opção:"))
        if opt==1:
            print("|| Pesquisa por Autores")
            input("|| Introduza o Nome Do Autor:")
        elif opt==2:
            print("|| Pesquisa por Álbuns")
            input("|| Introduza o Nome Do Álbum:")
        elif opt==3:
            print("|| Pesquisa por Músicas")            
            input("|| Introduza o Nome Da Música:")
        elif opt==0:
            break
        else:
            print("|| O valor introdzido é inválido")
            continue
#Só acessivel a admin
def MenuEditar():
        while True:
            print("|| Menu Editar\n|| 1. Autores\n|| 2. Álbuns\n|| 0. Voltar")
            opt=int(input("|| Opção:"))
            if opt==1:
                print("|| Editor de Autores")
                input("|| Introduza o Nome:")
                input("|| Introduza o Nacionalidade:")
                input("|| Introduza o Álbuns:")
                input("|| Direitos editoriais:")
            elif opt==2:
                print("|| Editor de Álbuns")
                input("|| Introduza o Nome:")
                input("|| Introduza o Género Musical:")
                input("|| Introduza o Data de Lançamento:")
                input("|| Introduza o Unidades Vendidas:")
                input("|| Introduza o Preço:")
            elif opt==0:
                break
            else:
                print("|| O valor introdzido é inválido")
                continue