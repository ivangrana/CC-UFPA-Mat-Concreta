seq = [4,2,1] #sequência a ser analisada

for k in range(0,(len(seq) - 2)): #checar de 3 em 3
    if((seq[k + 1]*(seq[k + 1])) == (seq[k + 2]*seq[k])):
        seq_is_pg = True   #se for p.g, retorna True
    else:
        seq_is_pg = False #caso não seja, retorna falso
        print("A sequência não é uma P.G")

#Classificação da P.G
if seq_is_pg == True: 
    if(seq[k + 1] > seq[k] and (seq[k+2] != seq[k])): 
        print("Crescente")
    elif(seq[k + 1] < seq[k] and (seq[k+2] != seq[k])):
        print("Decrescente")
    elif(seq[k + 1] == seq[k]):
        print("Constante")
    elif(seq[k + 2] == seq[k]):
        print("Alternada")
    
    
