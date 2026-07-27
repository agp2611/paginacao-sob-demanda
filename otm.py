def executarOtm(quadros : int, referencia : list):

    faltas_otm = 0 # Variável de controle de faltas
    memoria_otm = [] # Variável de criação de listas

    #Primeira parte----------------------------------------------------------------------------

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


"""
1 parte:

ta basicamente eu tenho que criar uma lista com o tamanho dos slots

toda vez que eu adiciono um número eu percorro a lista e vejo se tem slots vazios

se tiver incremento falta

se não eu percorro a lista

se o que eu adicionar não tiver é falta 

se ja tiver continua

"""

"""
4 -> 4 quadros
1 2 3 4 1 2 5 1 2 3 4 5 -> sequência

[_,_,_,_] F 
[1,_,_,_] F 
[1,2,_,_] F 
[1,2,3,_] F 
[1,2,3,4] Ok
[1,2,3,4] Lê 1 e ja tem - Ok
[1,2,3,4] Lê 2 e ja tem - Ok
[1,2,3,4] Lê 5 - Faltou - Vejo quem ta mais distante a direita (4)
[1,2,3,5] Lê 1 e ja tem - Ok
[1,2,3,5] Lê 2 e ja tem - Ok
[1,2,3,5] Lê 3 e ja tem - Ok
[1,2,3,5] Lê 4 - Faltou - Vejo quem ta mais distante a direita (1,2,3) (nem tem mais) - escolho qualquer um (3)
[1,2,4,5] Lê 5 e ja tem - Ok

Faltas - 6 

"""