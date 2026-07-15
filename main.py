def executarFifo(quadros : int, referencia : list):
    memoria = []
    faltas = 0
    

    for pagina in referencia:
        if (pagina not in memoria):
            faltas += 1
            
            if(len(memoria) == quadros):
                memoria.pop(0)
            memoria.append(pagina)
            
            
    return faltas


def executarLru(quadros : int, referencia : list):
    memoria = []
    faltas = 0
    

    for paginaRef in referencia:
        if(paginaRef in memoria):
            memoria.remove(paginaRef)
            memoria.append(paginaRef)
            
        else:
            faltas += 1
            
            if(len(memoria) == quadros):
                memoria.pop(0)
                
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