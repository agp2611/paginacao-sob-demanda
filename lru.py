def executarLru(quadros : int, referencia : list):
    memoria = []
    faltas = 0
    
    with open("logLRU.txt", "w") as f:
        for paginaRef in referencia:
            if (paginaRef in memoria):
                f.write(f"JA ESTA NA MEMORIA")
                memoria.remove(paginaRef)
                memoria.append(paginaRef)
            
            else:
                f.write("NAO ESTA NA MEMORIA")
                faltas += 1
                
                if (len(memoria) == quadros):
                    memoria.pop(0)
                memoria.append(paginaRef)
                
            f.write(f"pagina: {paginaRef}\n")
            f.write(f"{str(memoria)}\n")
            f.write(f"Faltas atuais: {faltas}\n")
            f.write("--------------------------------\n")

    return faltas