#tabelaSimplex = [[-5, -2, 0, 0,0,0],
#                 [1, 0, 1, 0, 0,3],
#                 [ 0, 1, 0, 1, 0,4],
#                 [ 1, 2, 0, 0, 1,9]]
tabelaSimplex = []

indiceColunaPivo = 0
indiceLinhaPivo = -1
def verificarMenorNumero():
    global indiceColunaPivo
    numero = min(tabelaSimplex[0])
    indice = tabelaSimplex[0].index(numero)
    if(numero < 0):
         indiceColunaPivo = indice
    else:
        indiceColunaPivo = -1

def verificarQualALinhaPivo():
    global indiceLinhaPivo
    menor = 1000000000000000000
    for i in range(1,len(tabelaSimplex)):
        print("inicio",tabelaSimplex[i][indiceColunaPivo])
        print("final",tabelaSimplex[i][len(tabelaSimplex[i]) - 1])
        if(tabelaSimplex[i][indiceColunaPivo] > 0 ):
            divisao = float(tabelaSimplex[i][len(tabelaSimplex[i]) - 1]) / tabelaSimplex[i][indiceColunaPivo]
            print("divisao", divisao)
            if(menor > divisao and divisao > 0):
                indiceLinhaPivo = i
                menor = divisao

def igualarLinhaPivoA1():
    global indiceColunaPivo
    global indiceLinhaPivo
    valor = tabelaSimplex[indiceLinhaPivo][indiceColunaPivo]
    if(valor != 1):
        for i in range(len(tabelaSimplex[indiceLinhaPivo])):
            tabelaSimplex[indiceLinhaPivo][i] /= float(valor)


def realizarOperacoesElementares():
    for linha in range(len(tabelaSimplex)):
        if tabelaSimplex[linha][indiceColunaPivo] !=0 :
            valorParaSerZero = tabelaSimplex[linha][indiceColunaPivo]
            if(valorParaSerZero < 0):
                valorParaSerZero *= -1
                for coluna in range(len(tabelaSimplex[linha])):
                    if(linha != indiceLinhaPivo):
                        tabelaSimplex[linha][coluna] += tabelaSimplex[indiceLinhaPivo][coluna]*valorParaSerZero
            else:
                for coluna in range(len(tabelaSimplex[linha])):
                    if(linha != indiceLinhaPivo):
                        tabelaSimplex[linha][coluna] -= tabelaSimplex[indiceLinhaPivo][coluna]*valorParaSerZero
    print(tabelaSimplex)


def lerArquivo():
    with open('problema.txt', 'r') as arquivo:

        linhas = [linha.strip() for linha in arquivo.readlines()]
        return linhas

def adicionandoFuncaoObjetivo(quantRestricoesMaiorIgual, funcaoObjetivo, quantRestricoesDesigualdade):
    #adicionando inicalmente a função objetivo
        duasFases = False

        quantVariaveisExcesso = quantRestricoesMaiorIgual
        quantVariaveisFolga = quantRestricoesDesigualdade

        listaAux = []

        #adicionando excesso
        for j in range(len(funcaoObjetivo)):
            listaAux.append(int(funcaoObjetivo[j])*-1)

        for j in range(quantVariaveisExcesso + quantVariaveisFolga +1):
            listaAux.append(0)

        tabelaSimplex.insert(0,listaAux)

        listaAux = []



def verificarMaiorIgual(matrizMaiorIgual, quantDeVariaveisDeDecisao, quantRestricoesMaiorIgual):
    todosBPostivos = True
    for i in range(len(matrizMaiorIgual)):
        if(int(matrizMaiorIgual[i][quantDeVariaveisDeDecisao])) < 0:
            todosBPostivos = False
    if(todosBPostivos):

            #adicionando as restrições e variaveis de excesso
        for i in range(len(matrizMaiorIgual)):
            for j in range(quantDeVariaveisDeDecisao,quantRestricoesMaiorIgual + quantDeVariaveisDeDecisao):
                if((i + quantDeVariaveisDeDecisao) == j):
                    matrizMaiorIgual[i].append(1)
                else:
                    matrizMaiorIgual[i].append(0)
            matrizMaiorIgual[i].append( matrizMaiorIgual[i].pop(quantDeVariaveisDeDecisao))

        listaAux = converterElementosMatrizParaInt(matrizMaiorIgual)

        for i in range(len(listaAux)):
            tabelaSimplex.append(listaAux[i])
        print(tabelaSimplex)

def verificarMenorIgual(quantRestricoesDesigualdade, matrizDesigualdade, quantDeVariaveisDeDecisao,quantidadeVariaveisArtificiais):

    for i in range(len(matrizDesigualdade)):
        for j in range(quantDeVariaveisDeDecisao + 1, quantDeVariaveisDeDecisao + quantidadeVariaveisArtificiais):
            if()

    listaAux = []
    listaAux = converterElementosMatrizParaInt(matrizDesigualdade)
    print("teste",tabelaSimplex)
    for i in range(len(listaAux)):
        tabelaSimplex.append(listaAux[i])
    #print(listaAux)

def converterElementosMatrizParaInt(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(matriz[i][j])
    return matriz
duasFases = False
def montarTabelaSimplex():
    global duasFases
    dados = lerArquivo()
    quantDeVariaveisDeDecisao = int(dados[0])
    funcaoObjetivo = dados[1].split(' ')
    quantRestricoesMaiorIgual = int(dados[2])

    matrizMaiorIgual = []
    for i in range( 3, 3 + quantRestricoesMaiorIgual):
        matrizMaiorIgual.append(dados[i].split(' '))

    quantRestricoesIgualdade = int(dados[3 + quantRestricoesMaiorIgual])
    matrizIgualdade = []
    for i in range(4 + quantRestricoesMaiorIgual, 4 + quantRestricoesMaiorIgual + quantRestricoesIgualdade):
        matrizIgualdade.append(dados[i].split(' '))

    quantRestricoesDesigualdade = int(dados[4 + quantRestricoesMaiorIgual + quantRestricoesIgualdade])
    matrizDesigualdade = []
    for i in range(5 + quantRestricoesMaiorIgual + quantRestricoesIgualdade, 5 +quantRestricoesDesigualdade + quantRestricoesMaiorIgual + quantRestricoesIgualdade):
        matrizDesigualdade.append(dados[i].split(' '))

    print(matrizMaiorIgual)
    print(matrizIgualdade)
    print(matrizDesigualdade)

    adicionandoFuncaoObjetivo(quantRestricoesMaiorIgual, funcaoObjetivo, quantRestricoesDesigualdade)
    print("teste",tabelaSimplex)

    #adiciona restrições de maior igual na função
    if(quantRestricoesMaiorIgual > 0):
        verificarMaiorIgual(matrizMaiorIgual, quantDeVariaveisDeDecisao, quantRestricoesMaiorIgual )

    #verificar menor ou igual
    quantidadeVariaveisArtificiais = 0
    print(quantRestricoesDesigualdade)
    if(quantRestricoesDesigualdade > 0):
        todosBPostivos = True
        for i in range(len(matrizDesigualdade)):
            if(int(matrizDesigualdade[i][quantDeVariaveisDeDecisao])) < 0:
                todosBPostivos = False
            if(todosBPostivos):
                quantidadeVariaveisArtificiais = quantRestricoesDesigualdade
                verificarMenorIgual(quantRestricoesDesigualdade, matrizDesigualdade, quantDeVariaveisDeDecisao, quantidadeVariaveisArtificiais)






def executarFaseDois():
    while(True):
        verificarMenorNumero()
        if(indiceColunaPivo == -1):
            break
        verificarQualALinhaPivo()
        igualarLinhaPivoA1()
        realizarOperacoesElementares()

#executarFaseDois()
def main():
    montarTabelaSimplex()
    if(duasFases == False):
        executarFaseDois()
#main()
montarTabelaSimplex()
