from fifo import executarFifo
from lru import executarLru
from otm import executarOtm

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
print(f"OTM {faltasOtm}")
print(f"LRU {faltasLru}")