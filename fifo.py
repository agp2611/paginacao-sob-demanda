def executarFifo(quadros : int, referencia : list):
    memoria = []
    faltas = 0
    
    with open("logFIFO.txt", "w") as f:
        for paginas in referencia:
            if (len(memoria) == quadros):
                if (paginas in memoria):
                    f.write("JA ESTA NA MEMORIA\n")

                else:
                    f.write("NAO ESTA NA MEMORIA\n")
                    faltas += 1
                    memoria.pop(0)
                    memoria.append(paginas)
            else:
                faltas +=1
                memoria.append(paginas)
                
            f.write(f"pagina: {paginas}\n")
            f.write(f"{str(memoria)}\n")
            f.write(f"Faltas atuais: {faltas}\n")
            f.write("--------------------------------\n")
    f.close
    return faltas