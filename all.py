def executarFifo(quadros : int, referencia : list):
    memoria = []
    faltas = 0
    
    with open("logFIFO.txt", "w") as f:
        for pagina in referencia:
            if (pagina in memoria):
                f.write("JA ESTA NA MEMORIA\n")
            else:
                f.write("NAO ESTA NA MEMORIA\n")
                faltas += 1
                
                if(len(memoria) == quadros):
                    memoria.pop(0)
                memoria.append(pagina)
                    
            f.write(f"pagina: {pagina}\n")
            f.write(f"{str(memoria)}\n")
            f.write(f"Faltas atuais: {faltas}\n")
            f.write("--------------------------------\n")
            
    return faltas

def executarLru(quadros : int, referencia : list):
    memoria = []
    faltas = 0
    
    with open("logLRU.txt", "w") as f:
        for paginaRef in referencia:
            if (paginaRef in memoria):
                f.write(f"JA ESTA NA MEMORIA\n")
                memoria.remove(paginaRef)
                memoria.append(paginaRef)
            
            else:
                f.write("NAO ESTA NA MEMORIA\n")
                faltas += 1
                
                if (len(memoria) == quadros):
                    memoria.pop(0)
                memoria.append(paginaRef)
                
            f.write(f"pagina: {paginaRef}\n")
            f.write(f"{str(memoria)}\n")
            f.write(f"Faltas atuais: {faltas}\n")
            f.write("--------------------------------\n")

    return faltas

qQuadros = 0 # quantidade de quadros de memória
lReferencias = [] # sequência de páginas de referência

with open("entrada.txt", "r") as f:
    for i, linha in enumerate(f):
        if(i == 0):
            qQuadros = int(linha.strip())
        else:
            lReferencias.append(int(linha.strip()))
            
faltasFifo = executarFifo(qQuadros, lReferencias)
faltasLru = executarLru(qQuadros, lReferencias)
faltasOtm = executarOtm(qQuadros, lReferencias)

print(f"FIFO {faltasFifo}")
print(f"LRU {faltasLru}")
print(f"OTM {faltasOtm}")