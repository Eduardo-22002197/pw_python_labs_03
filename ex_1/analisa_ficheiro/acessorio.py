def pede_nome():
    while(OSError):
        fileName = input("Nome ficheiro .txt: ")

        try:
            f = open(fileName, "r")

            if(f == True):
                f.close()
                return fileName
        
        except(OSError):
            print(f"File {fileName} not found.")

def gera_nome(fileName):
    newName = fileName.split('.')[0] + '.json'
    return newName