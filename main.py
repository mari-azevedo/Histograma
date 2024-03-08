#Para cada valor par lido, seu programa imprime uma linha com um conjunto de asteriscos correspondente ao valor lido. Para cada valor ímpar lido, ele imprime um número de pontos (i.e., o ponto final ) correspondente a esse valor. 

val= [int(i) for i in input().split()]
impar = '.'
par = '*'

for i in val:
  if i%2==0:
    print(par*i)
  elif i%2!=0:
    print(impar*i)
