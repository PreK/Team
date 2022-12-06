while True:
    print("|| Menu Inicial\n|| 1. Pesquisar\n|| 2. Editar\n|| 3. Admin\n|| 0. Sair")
    opt=int(input("|| Opção:"))
    if opt==1:
        while True:
            print("|| Menu Pesquisar\n|| 1. Autor\n|| 2. Álbum\n|| 3. Música\n|| 0. Voltar")
            opt1=int(input("|| Opção:"))
            if opt1==1:
                print("|| Pesquisa por Autores")
                input("|| Introduza o Nome Do Autor:")
            elif opt1==2:
                print("|| Pesquisa por Álbuns")
                input("|| Introduza o Nome Do Álbum:")
            elif opt1==2:
                print("|| Pesquisa por Músicas")            
                input("|| Introduza o Nome Da Música:")
            elif opt1==0:
                break
            else:
                print("O valor introdzido é inválido")
                continue
    elif opt==2:
        while True:
            print("|| Menu Editar\n|| 1. Autores\n|| 2. Álbuns\n|| 0. Voltar")
            opt1=int(input("|| Opção:"))
            if opt1==1:
                print("|| Editor de Autores")
                input("|| Introduza o Nome:")
                input("|| Introduza o Nacionalidade:")
                input("|| Introduza o Álbuns:")
            elif opt1==2:
                print("|| Editor de Álbuns")
                input("|| Introduza o Nome:")
                input("|| Introduza o Género Musical:")
                input("|| Introduza o Data de Lançamento:")
                input("|| Introduza o Unidades Vendidas:")
                input("|| Introduza o Preço:")
            elif opt1==0:
                break
            else:
                print("|| O valor introdzido é inválido")
                continue
    elif opt==3:
        if input("|| Introduza a senha:")=="admin":
            print("|| Menu Admin\n|| 1. Pesquisar\n|| 2. Editar\n|| 0. Sair")
                #Menus anteriores mas com direitos editorais para edição e acesso.
    elif opt==0:
        print("|| Terminado com sucesso")
        break
    else:
        print("|| O valor introdzido é inválido")
        continue