def mergeSort(sequencia):
	if len(sequencia) > 1:

		#Achar o termo do meio da sequencia
		termo_meio = len(sequencia)//2

		# Divide a sequencia pela metade
		esquerda = sequencia[:termo_meio]

		direita = sequencia[termo_meio:]

		# Executa o mergesort no lado esquerdo
		mergeSort(esquerda)

		# Executa o mergesort no lado direito
		mergeSort(direita)

		i = j = k = 0

		# Une os dois lados em uma só sequencia
		while i < len(esquerda) and j < len(direita):
			if esquerda[i] < direita[j]:
				sequencia[k] = esquerda[i]
				i += 1
			else:
				sequencia[k] = direita[j]
				j += 1
			k += 1

		# Verifica se existe algum elemento restante
		while i < len(esquerda):
			sequencia[k] = esquerda[i]
			i += 1
			k += 1

		while j < len(direita):
			sequencia[k] = direita[j]
			j += 1
			k += 1

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()

sequencia = input("Insira os termos da sequência consecutivamente:\nexemplo: 2 4 6 8 10 \n->")
sequencia = sequencia.split()
sequencia = list(map(int,sequencia))

print("Sequencia original:", end="\n")
printList(sequencia)
mergeSort(sequencia)
print("Sequencia apos o merge sort: ", end="\n")
printList(sequencia)

