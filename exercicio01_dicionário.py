cores = {'preto': 'black', 'verde': 'green', 'amarelo': 'yellow', 'vermelho': 'red'}
cor = input('Digite uma cor em portugues: ').lower()
print(cores.get(cor, 'NÃO TEM ESSA COR NO CADASTRO!'))
