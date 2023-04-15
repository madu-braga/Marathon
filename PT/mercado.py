v= [1, 2, 3, 4, 5]
N = 6

def maior_perda(N, v):
    for x in range (N):
        if v[x] == v[0]:
            maior = v[x]
            perda = 0
        elif v[x] == v[-1] and v[x] > maior:
            perda = perda
        elif v[x] > maior:
            maior = v[x]
            perda = 0
        else:
            perda = v[x] + maior
    print(perda)

def acoes(N, v):
    maior_perda(N, v)

acoes(N, v)
