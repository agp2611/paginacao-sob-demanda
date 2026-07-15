def executarFifo(quadros : int, referencia : list):
    memoria = []
    faltas = 0
    

    for pagina in referencia:
        if (len(memoria) == quadros) :
            if(pagina not in memoria):
                faltas += 1
                memoria.pop(0)
                memoria.append(pagina)
                    
        else:
            faltas +=1
            memoria.append(pagina)
            
    return faltas


def executarLru(quadros : int, referencia : list):
    memoria = []
    faltas = 0
    

    for paginaRef in referencia:
        if (len(memoria) == quadros):
            if (paginaRef in memoria):
                for paginaMem in memoria:
                    if paginaMem == paginaRef:
                        memoria.remove(paginaMem)
                        memoria.append(paginaMem)
                        break
            else:
                faltas += 1
                memoria.pop(0)
                memoria.append(paginaRef)
        else:
            faltas +=1
            memoria.append(paginaRef)

    return faltas


qQuadros = 0
lReferencias = []

with open("entrada.txt", "r") as f:
    for i, linha in enumerate(f):
        if(i == 0):
            qQuadros = int(linha.strip())
        else:
            lReferencias.append(int(linha.strip()))
            
faltasFifo = executarFifo(qQuadros, lReferencias)
faltasLru = executarLru(qQuadros, lReferencias)

print(f"FIFO {faltasFifo}")
print(f"LRU {faltasLru}")