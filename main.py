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

def executarOtm(quadros : int, referencia : list):

    faltas_otm = 0 # Variável de controle de faltas
    memoria_otm = [] # Variável de criação de listas

    indice_atual = 0

    for i in referencia:

        if i not in memoria_otm: # Se não estiver
            faltas_otm+=1 # É falta de certeza

            if len(memoria_otm)<quadros: #Tem espaço vazio na lista? só adicionar ao final dela
                memoria_otm.append(i)

            elif len(memoria_otm)==quadros: #Precisa de vítima

                futuro = referencia[indice_atual + 1 : ] #Vai do indíce atual + 1 até o final (estou olhando essa lista agora)

                vitimas = [] #Lista de vítimas
                vitima_final = None #Variável de controle da vítima final

                for x in memoria_otm: # Para cada elemento x da lista de memória que tenho agora

                    if x not in futuro: 

                        vitima_final = memoria_otm.index(x) # Ele vai ser a vítima final
                        break # Quebro o loop, pois já encontrei a vítima final

                    elif x in futuro:

                        vitimas.append(futuro.index(x)) # Procuro o próximo elemento x na lista futuro e adiciono o índice dele na lista de vítimas

                    else:

                        print("Erro") 
                        exit()

                if vitima_final is None: # Se eu não encontrei a vítima perfeita
                    vitima_final = vitimas.index(max(vitimas))

                else: 
                    pass

                memoria_otm[vitima_final] = i # Substituo o elemento da memória que tem o maior índice na lista de vítimas pelo elemento atual

            else: # Se estiver na memória, não é falta, então só continua
                pass
                    
        indice_atual += 1            

    return faltas_otm

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