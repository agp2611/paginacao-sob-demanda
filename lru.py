def executarLru(quadros : int, referencia : list):
    memoria = []
    faltas = 0
    
    with open("logLRU.txt", "w") as f:
        for paginaRef in referencia:
            if (len(memoria) == quadros):
                if (paginaRef in memoria):
                    f.write("JA ESTA NA MEMORIA\n")
                    for paginaMem in memoria:
                        if paginaMem == paginaRef:
                            memoria.remove(paginaMem)
                            memoria.append(paginaMem)
                            break
                else:
                    f.write("NAO ESTA NA MEMORIA\n")
                    faltas += 1
                    memoria.pop(0)
                    memoria.append(paginaRef)
            else:
                faltas +=1
                memoria.append(paginaRef)
                
            f.write(f"pagina: {paginaRef}\n")
            f.write(f"{str(memoria)}\n")
            f.write(f"Faltas atuais: {faltas}\n")
            f.write("--------------------------------\n")
    f.close
    return faltas