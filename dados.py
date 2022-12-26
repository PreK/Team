import csv

#função para verificar se o artista existe no ficheiro artista.csv
def checkArtista(artista):
    with open('artista.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        pArtista = 0
        for row in csv_reader:
            if row[0] == artista:
                pArtista = 1
         
        if pArtista == 0:
            print("|| Artista não existente, por favor criar")
            return 0
        else:
            return 1
        
#Módulo de procurar por Artista
def pArtista(artista):
    with open('albuns.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        if checkArtista(artista):
            print ("{:<25} {:<35} {:<10} {:<10}".format("Artista", "Album", "Género", "Data"))
            for row in csv_reader:
                if row[0] == artista:
                    print ("{:<25} {:<35} {:<10} {:<10}".format(row[0], row[1], row[2], row[3]))

def pAlbum(album):
    with open('albuns.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        pAlbum = 0
        for item in csv_reader:
            if item[1] == album:
                pAlbum = 1
        if pAlbum:
            print ("{:<25} {:<35} {:<10} {:<10}".format("Artista", "Album", "Género", "Data"))
            for row in csv_reader:
                if row[1] == album:
                    print ("{:<25} {:<35} {:<10} {:<10}".format(row[0], row[1], row[2], row[3]))
def pMusica():
    pass
pAlbum("Pimba")

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
       with open('albuns.csv', mode='a', newline='') as csv_file:
        chaves = ['Artista','Nome','Genero', 'Data', 'Vendas','Preco']
        writer = csv.DictWriter(csv_file, fieldnames=chaves)

        writer.writerow({'Artista': artista,'Album': nome,'Genero': genero, 'Data': data, 'Vendas': vendas,'Preco': preco})
        csv_file.close()
    