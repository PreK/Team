import dados
from pygame import mixer

def MenuInicial(admin):
    if admin==True:
        while True:
            print("|| Menu Admin\n|| 1. Pesquisar\n|| 2. Editar\n|| 3. Apagar\n|| 0. Sair")
            opt=input("|| Opção:")
            if opt=="1":
                MenuPesquisar()
            elif opt=="2":
                MenuEditar()
            elif opt=="3":
                MenuApagar()
            elif opt=="0":
                print("|| Terminado com sucesso")
                break
            else:
                print("|| O valor introdzido é inválido")
                continue
    else:
        while True:
            print("|| Menu Inicial\n|| 1. Pesquisar\n|| 0. Sair")
            opt=input("|| Opção:")
            if opt=="1":
                MenuPesquisar()
            elif opt=="0":
                print("|| Terminado com sucesso")
                break
            else:
                print("|| O valor introdzido é inválido")
                continue
#Acessivel a admin e utilizador
#Quando for criada a função de leitura e escrita do ficheiro csv retirar Direitos editorais á lista do utilizador
def MenuPesquisar():
    while True:
        print("|| Menu De Pesquisa\n|| 1. Autor\n|| 2. Álbum\n|| 3. Música\n|| 4. Reprodutor\n|| 0. Voltar")
        opt=input("|| Opção:")
        if opt=="1":
            print("|| Pesquisa por Autores")
            artista = input("|| Introduza o Nome Do Autor:")
            dados.pArtista(artista)
        elif opt=="2":
            print("|| Pesquisa por Álbuns")
            album = input("|| Introduza o Nome Do Álbum:")
            dados.pAlbum(album)
        elif opt=="3":
            print("|| Pesquisa por Músicas")            
            musica = input("|| Introduza o Nome Da Música:")
            dados.pMusica(musica)
        elif opt=="4":
            dados.playListMusica()            
            musica = input("|| Introduza o Nome Da Música para ouvir a Demo:")
            dados.playMusica(musica)
        elif opt=="0":
            break
        else:
            print("|| O valor introdzido é inválido")
            continue
#Só acessivel a admin
def MenuEditar():
        while True:
            print("|| Menu Admin\n|| 1. Editar Autores\n|| 2. Editar Álbuns\n|| 3. Editar Músicas\n|| 4. Calcular Direitos editoriais\n|| 5. Listar todos\n|| 0. Voltar")
            opt=input("|| Opção:")
            if opt=="1":
                print("|| Editor de Autores")
                nome = input("|| Introduza o Nome:")
                nacionalidade = input("|| Introduza o Nacionalidade:")
                royalty = input("|| Direitos editoriais:")
                dados.gArtista(nome,nacionalidade,royalty)
            elif opt=="2":
                print("|| Editor de Álbuns")
                artista = input("|| Introduza o Artista:")
                nome = input("|| Introduza o Nome:")
                genero = input("|| Introduza o Género Musical:")
                data = input("|| Introduza o Data de Lançamento:")
                vendas = input("|| Introduza o Unidades Vendidas:")
                preco = input("|| Introduza o Preço:")
                dados.gAlbum(artista,nome,genero,data,vendas,preco)
            elif opt=="3":
                print("|| Editor de Músicas")
                artista = input("|| Introduza o Artista:")
                album = input("|| Introduza o album:")
                adicionar = "sim"
                while adicionar == "sim":
                    musica = input("|| Introduza a musica:")
                    ficheiro = input("|| Tem demo?: (sim/não):")
                    adicionar = input("|| Adicionar outra Música ao album? (sim/não):")
                    dados.gMusica(artista,album,musica,ficheiro)
            elif opt=="4":
                autor = input("|| Introduza o nome do Autor para calcular os Direitos editoriais:")
                print("Cálculo das vendas é de: ", dados.calculo(autor))
            elif opt=="5":
                dados.listAll()
            elif opt=="0":
                break
            else:
                print("|| O valor introdzido é inválido")
                continue
            
def MenuApagar():
        while True:
            print("|| Menu Apagar\n|| 1. Autor\n|| 2. Álbum\n|| 3. Música\n|| 0. Voltar")
            opt=input("|| Opção:")
            if opt=="1":
                print("|| Apagar por Autor! Vai eliminar também os Álbuns")
                nome = input("|| Introduza o Nome:")
                dados.aArtista(nome)
            elif opt=="2":
                print("|| Apagar Álbuns")
                nome = input("|| Introduza o Nome do álbum  :")
                dados.aAlbum(nome)
                
            elif opt=="3":
                print("|| Apagar Música")
                nome = input("|| Introduza o Nome da Musica:")
                dados.aMusica(nome)    
            elif opt=="0":
                break
            else:
                print("|| O valor introdzido é inválido")
                continue

def MenuPlay():
        while True:
            print("|| Menu De Reprodução\n|| 1. Pausar\n|| 2. Resumir\n|| 0. Voltar")
            opt=input("|| Opção:")
            if opt=="1":
                print("|| Reprodução da musica pausada")
                mixer.music.pause()
            elif opt=="2":
                print("|| Reprodução da musica resumida")
                mixer.music.unpause()
            elif opt=="0":
                print("|| Reprodução da musica parada com sucesso")
                mixer.quit()
                break
            else:
                print("|| O valor introdzido é inválido")
                continue
