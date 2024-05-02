from os import walk

def listage():
    listeFichiers = ['IMGP9561.jpg']
    for (repertoire, sousRepertoires, fichiers) in walk(r"D:\babagraphie\image"):
        listeFichiers.extend(fichiers)
    for i in range(len(listeFichiers)-1):
        listeFichiers[i] = str('image/'+listeFichiers[i])
    print (listeFichiers)

listage()