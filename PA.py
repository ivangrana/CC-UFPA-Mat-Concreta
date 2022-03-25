A = [8,6,4,2,0,-2]

for k in range(0,(len(A)-2)):
    if((A[k + 1] - A[k]) == (A[k+2] - A[k+1])):
        status = True
    elif ((A[k + 1] - A[k]) != (A[k+2] - A[k+1])):
        print("Não é uma P.A")
        status = False
        break

if(status == True):
    if(A[k + 1] > A[k]):
        print("Crescente")
    elif(A[k + 1] < A[k]):
        print("Decrescente")



