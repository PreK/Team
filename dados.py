import csv

#Módulo de procurar por Artista
def pArtista():
    with open('albuns.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
        
def pAlbum():
    pass
def pMusica():
    pass

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

        writer.writerow({'Artista': artista,'Nome': nome,'Genero': genero, 'Data': data, 'Vendas': vendas,'Preco': preco})
        csv_file.close()
    