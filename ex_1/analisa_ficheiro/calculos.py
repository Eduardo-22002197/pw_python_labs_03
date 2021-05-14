def calcula_linhas(fileName):
    line_count = 0

    with open(fileName, 'r') as f:
        for line in f:
            if line != "\n":
                line_count += 1
            
    return line_count