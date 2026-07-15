def executarFifo(quadros : int, referencia : list):
    memoria = []
    faltas = 0
    
    with open("logFIFO.txt", "w") as f:
        for pagina in referencia:
            if (len(memoria) == quadros):
                if (pagina in memoria):
                    f.write("JA ESTA NA MEMORIA\n")

                else:
                    f.write("NAO ESTA NA MEMORIA\n")
                    faltas += 1
                    memoria.pop(0)
                    memoria.append(pagina)
            else:
                faltas +=1
                memoria.append(pagina)
                
            f.write(f"pagina: {pagina}\n")
            f.write(f"{str(memoria)}\n")
            f.write(f"Faltas atuais: {faltas}\n")
            f.write("--------------------------------\n")
    f.close
    return faltas