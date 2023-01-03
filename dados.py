import csv
import functions
#Para esperar enquanto o MP3 toca
import time
#Caso python 3.11 usar a versão pre realease "pip install pygame --pre"
from pygame import mixer

#função para verificar se o artista existe no ficheiro artista.csv
def checkArtista(artista):
    with open('artista.csv', "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        pArtista = 0
        for row in csv_reader:
            if row[0] == artista:
                pArtista = 1
         
        if pArtista == 0:
            print("|| Artista não existente!")
            return 0
        else:
            return 1
#função para verificar se o album existe no ficheiro albuns.csv
def checkAlbum(album):
    with open('albuns.csv', "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        pAlbum = 0
        for row in csv_reader:
            if row[1] == album:
                pAlbum = 1
         
        if pAlbum == 0:
            print("|| Album não existente!")
            return 0
        else:
            return 1

#função para verificar se a musica existe no ficheiro musicas.csv
def checkMusica(Musica):
    with open('musicas.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        pMusica = 0
        for row in csv_reader:
            if row[2] == Musica:
                pMusica = 1
         
        if pMusica == 0:
            print("|| Musica não existente!")
            return 0
        else:
            return 1
def checkDemo(Musica):
    with open('musicas.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        pDemo = 0
        for row in csv_reader:
            if row[2] == Musica and row[3] == "sim":
                pDemo = 1
         
        if pDemo == 0:
            print("|| Musica sem demo!")
            return 0
        else:
            return 1
        
#Função de listar musicas e tocar
def playListMusica():
    with open('musicas.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        print ("{:<25} {:<35} {:<10}".format("Artista", "Album", "Música"))
        for row in csv_reader:
            if row[3] == "sim":
                print ("{:<25} {:<35} {:<10}".format(row[0], row[1], row[2]))
                
                
def playMusica(Musica):
    if checkMusica(Musica) and checkDemo(Musica):
        mixer.init()
        mixer.music.load("Musicas/" + Musica + ".mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(1)
                          
#Módulo de procurar por Artista
def pArtista(artista):
    with open('albuns.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        if checkArtista(artista):
            print ("{:<25} {:<35} {:<10} {:<10}".format("Artista", "Album", "Género", "Data"))
            for row in csv_reader:
                if row[0] == artista:
                    print ("{:<25} {:<35} {:<10} {:<10}".format(row[0], row[1], row[2], row[3]))
#Módulo de procurar por Album
def pAlbum(album):
    if checkAlbum(album):
        with open('albuns.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            print ("{:<25} {:<35} {:<10} {:<10} {:<10} {:<10}".format("Artista", "Album", "Género", "Data", "Nº Vendas", "Preço"))
            for row in csv_reader:
                if row[1] == album:
                    print ("{:<25} {:<35} {:<10} {:<10} {:<10} {:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        with open('musicas.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            print("----------------------------------------------------------------------------------------------------")
            print ("{:<10}".format("Músicas:"))
            for row in csv_reader:
                if row[1] == album:
                    print ("--","{:<10}".format(row[2]))
#Módulo de procurar por Música
def pMusica(musica):
    if checkMusica(musica):
        with open('musicas.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            print ("{:<25} {:<35} {:<10}".format("Artista", "Album", "Música"))
            for row in csv_reader:
                if row[2] == musica:
                    print ("{:<25} {:<35} {:<10}".format(row[0], row[1], row[2]))

#Função para adicionar Artista        
def gArtista(nome,nacionalidade,royalty):
    if checkArtista(nome):
        print("|| Artista já existe, não pode haver dois artistas com o mesmo nome!!!")
    else:
        with open('artista.csv', mode='a', newline='') as csv_file:
            chaves = ['Nome', 'Nacionalidade', 'Royalty']
            writer = csv.DictWriter(csv_file, fieldnames=chaves)

            writer.writerow({'Nome': nome, 'Nacionalidade': nacionalidade, 'Royalty': royalty})
            csv_file.close()

#Função para gravar novo album 
def gAlbum(artista,nome,genero,data,vendas,preco):
   if checkArtista(artista):
        if checkAlbum(nome):
            print("|| Album já existe!!")
        else:
            with open('albuns.csv', mode='a', newline='') as csv_file:
                chaves = ['Artista','Album','Genero', 'Data', 'Vendas','Preco']
                writer = csv.DictWriter(csv_file, fieldnames=chaves)

                writer.writerow({'Artista': artista,'Album': nome,'Genero': genero, 'Data': data, 'Vendas': vendas,'Preco': preco})
                csv_file.close()

#Função para gravar nova música
def gMusica(artista,album,musica,ficheiro):
   if checkArtista(artista) and checkAlbum(album):
        with open('musicas.csv', mode='a', newline='') as csv_file:
            chaves = ['Artista','Album','Música', 'Demo']
            writer = csv.DictWriter(csv_file, fieldnames=chaves)

            writer.writerow({'Artista': artista,'Album': album,'Música': musica, 'Demo': ficheiro})
            csv_file.close()
   else:
        functions.MenuEditar()   
        
#Função apagar Musica              
def aMusica(musica):
    if checkMusica(musica):
        lmusica = list()    
        with open('musicas.csv', mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                lmusica.append(row)
                for field in row:
                    if field == Album:
                        lmusica.remove(row)      

#Função apagar Album              
def aAlbum(Album):
    if checkAlbum(Album):
        lalbum = list()    
        with open('albuns.csv', mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                lalbum.append(row)
                for field in row:
                    if field == Album:
                        lalbum.remove(row)

        with open('albuns.csv', mode='w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lalbum)
        
        lmusica = list()    
        with open('musicas.csv', mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                lmusica.append(row)
                for field in row:
                    if field == Album:
                        lmusica.remove(row)

        with open('musicas.csv', mode='w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lmusica)
            


        with open('musicas.csv', mode='w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lmusica)

#Função apagar Artista  
def aArtista(artista):
    if checkArtista(artista):
        lartista = list()

        with open('artista.csv', mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                lartista.append(row)
                for field in row:
                    if field == artista:
                        lartista.remove(row)
        
        with open('artista.csv', mode='w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lartista)

        lalbum = list()    
        with open('albuns.csv', mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                lalbum.append(row)
                for field in row:
                    if field == artista:
                        lalbum.remove(row)

        with open('albuns.csv', mode='w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lalbum)
        
        lmusica = list()    
        with open('musicas.csv', mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                lmusica.append(row)
                for field in row:
                    if field == artista:
                        lmusica.remove(row)

        with open('musicas.csv', mode='w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lmusica)

#Calculo de royalty's
def calculo(Autor):
    if checkArtista(Autor):
        soma = 0
        royalty = 0
        with open('artista.csv', "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == Autor:
                    royalty = int(row[2])
        if royalty == 0:
            return "0 (Royalty free)"
        else:
            with open('albuns.csv') as csv_file:
                        csv_reader = csv.reader(csv_file, delimiter=',')
                        for row in csv_reader:
                            if row[0] == Autor:
                                soma += int(row[4]) * int(row[5]) * (royalty / 100)
                                
                        return soma
    else:
        print("Artista não encontrdo na base de dados")