def executarFifo(quadros : int, referencia : list):
    memoria = []
    faltas = 0
    
    with open("logFIFO.txt", "w") as f:
        for pagina in referencia:
            if (pagina in memoria):
                f.write("JA ESTA NA MEMORIA")
            else:
                f.write("NAO ESTA NA MEMORIA")
                faltas += 1
                
                if(len(memoria) == quadros):
                    memoria.pop(0)
                memoria.append(pagina)
                    
            f.write(f"pagina: {pagina}\n")
            f.write(f"{str(memoria)}\n")
            f.write(f"Faltas atuais: {faltas}\n")
            f.write("--------------------------------\n")
            
    return faltas