from fifo import executarFifo
from lru import executarLru

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