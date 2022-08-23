rotas = []
saida = str

def tratando_matriz(documento):
    arquivo = open(documento, 'r')
    linhas, colunas = map(int, arquivo.readline().split(' '))
    pontos = {}

    for i in range(linhas):
        linha = arquivo.readline().split(' ')
        if len(linha) == colunas:
            for coluna in range(colunas):
                if '\n' in linha[coluna]:
                    linha[coluna] = linha[coluna][-2]
                if linha[coluna] != '0':
                    pontos[linha[coluna]] = (i,coluna)
        else:
            return "Matriz inválida"
    return pontos

def permutacao(pontos, n=0):
    if n==len(pontos):
        rotas.append('R'+"".join(pontos)+'R')
    for p in range(n, len(pontos)):
        locais = [a for a in pontos]
        locais[n], locais[p] = locais[p], locais[n]
        permutacao(locais, n+1)
    return rotas

def menor_custo(pontos, rotas):
    menor_custo = 99999
    menor_rota = str
    for r in rotas:
        custo = 0
        for q in range(len(r)-1):
            custo += abs(pontos[r[q]][0] - pontos[r[q+1]][0]) + abs(pontos[r[q]][1] - pontos[r[q+1]][1] )
        if custo < menor_custo:
            menor_custo = custo
            menor_rota = r[1:len(r)-1]

    return f'O menor trajeto foi {menor_rota} custando {menor_custo}'
        


locais = tratando_matriz('matriz.txt')
perm = permutacao([p for p in locais if p != 'R'])
min_custo = menor_custo(locais, perm)
print(rotas)
print('---------------------------')
print(locais)
print('---------------------------------')
print(min_custo)