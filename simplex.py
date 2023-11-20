#tabelaSimplex = [[-5, -2, 0, 0,0,0],
#                 [1, 0, 1, 0, 0,3],
#                 [ 0, 1, 0, 1, 0,4],
#                 [ 1, 2, 0, 0, 1,9]]
tabelaSimplex = []

indiceColunaPivo = 0
indiceLinhaPivo = -1
def verificarMenorNumero():
    global indiceColunaPivo
    aproximar_matriz_global()
    aux = [row[:] for row in tabelaSimplex]

    if(aux[0][len(aux[0]) - 1] < 0):
        aux[0][len(aux[0]) - 1] *= -1

    numero = min(aux[0])
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


def executarOperacaoElementarInicialFaseI():
    global indiceColunaPivo
    global indiceLinhaPivo

    for i in range(len(tabelaSimplex[0])):
        if(tabelaSimplex[0][i] == 1):
            for j in range(1,len(tabelaSimplex)):
                if(tabelaSimplex[j][i]) == 1:
                    indiceColunaPivo = i
                    indiceLinhaPivo = j
                    realizarOperacoesElementares()
    print(tabelaSimplex)


def aproximar_matriz_global():
    global tabelaSimplex

    # Percorrer a matriz global
    for i in range(len(tabelaSimplex)):
        for j in range(len(tabelaSimplex[0])):
            # Aproximar para zero se o valor for menor que 0,001
            if abs(tabelaSimplex[i][j]) < -0.001:
                tabelaSimplex[i][j] = 0
            else:
                tabelaSimplex[i][j] = round(tabelaSimplex[i][j], 3)
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
    with open('problema2.txt', 'r') as arquivo:

        linhas = [linha.strip() for linha in arquivo.readlines()]
        return linhas

def removerColunaVariavelAritificial(indice_coluna):
    global tabelaSimplex

    # Modificar a matriz global removendo a coluna desejada
    for linha in tabelaSimplex:
        del linha[indice_coluna]

def adicionandoFuncaoObjetivo(quantRestricoesMaiorIgual, funcaoObjetivo, quantRestricoesDesigualdade):
    #adicionando inicalmente a função objetivo
        duasFases = False

        quantVariaveisExcesso = quantRestricoesMaiorIgual
        quantVariaveisFolga = quantRestricoesDesigualdade

        listaAux = []

        #adicionando excesso
        for j in range(len(funcaoObjetivo)):
            listaAux.append(int(funcaoObjetivo[j])*-1)

        for j in range((quantVariaveisExcesso + quantVariaveisFolga) +1):
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
        print("maior igual tabela",tabelaSimplex)

def verificarMenorIgual(quantRestricoesDesigualdade, matrizDesigualdade, quantDeVariaveisDeDecisao,quantidadeVariaveisArtificiais):
    #listaAux = matrizDesigualdade

    listaAux = [row[:] for row in matrizDesigualdade]

    for i in range(len(matrizDesigualdade)):
        for j in range(quantDeVariaveisDeDecisao , quantDeVariaveisDeDecisao + quantidadeVariaveisArtificiais + quantRestricoesDesigualdade):
            if(quantDeVariaveisDeDecisao + i) == j:
                listaAux[i].append(-1)
            elif(quantDeVariaveisDeDecisao + quantidadeVariaveisArtificiais + i) == j:
                listaAux[i].append(1)
            else:
                listaAux[i].append(0)
        listaAux[i].append(listaAux[i].pop(quantDeVariaveisDeDecisao))
    
    print("teste 1 ", listaAux)

    
    listaAux = converterElementosMatrizParaInt(listaAux)
   
    for i in range(len(listaAux)):
        tabelaSimplex.append(listaAux[i])
    print(tabelaSimplex)

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
            adicionarFuncaoObjetivoFaseI(quantDeVariaveisDeDecisao,quantRestricoesDesigualdade , quantidadeVariaveisArtificiais )
            if(quantRestricoesMaiorIgual > 0):
                adicionarVariaveisMaiorIgual(quantDeVariaveisDeDecisao,quantRestricoesMaiorIgual, quantidadeVariaveisArtificiais, quantRestricoesDesigualdade, matrizDesigualdade)
            
            executarOperacaoElementarInicialFaseI()
            duasFases = True   
    if(duasFases == False):
        adicionandoFuncaoObjetivo(quantRestricoesMaiorIgual, funcaoObjetivo, quantRestricoesDesigualdade)

def carregarFuncaoObjetivosAposFaseI():    
    dados = lerArquivo()
    funcaoObjetivo = dados[1].split(' ')
    quantDeVariaveisDeDecisao = int(dados[0])
    quantRestricoesMaiorIgual = int(dados[2])
    quantRestricoesIgualdade = int(dados[3 + quantRestricoesMaiorIgual])
    quantRestricoesDesigualdade = int(dados[4 + quantRestricoesMaiorIgual + quantRestricoesIgualdade])

    #for i in range(len(tabelaSimplex[0]) -2,  quantDeVariaveisDeDecisao + quantRestricoesDesigualdade, -1):
        #removerColunaVariavelAritificial(i)    

    i = len( tabelaSimplex[0]) -2
    aux = quantRestricoesDesigualdade
    while(aux != 0):
        removerColunaVariavelAritificial(i)
        i-= 1
        aux -= 1


    adicionandoFuncaoObjetivo(quantRestricoesMaiorIgual , funcaoObjetivo, quantRestricoesDesigualdade + quantRestricoesIgualdade )
    tabelaSimplex.pop(1)
    procurarVariaveisBasicasAposFaseI(quantRestricoesMaiorIgual + quantRestricoesDesigualdade + quantRestricoesIgualdade)
    
    print(tabelaSimplex)

def adicionarFuncaoObjetivoFaseIComApenasDesigualdade(quantDeVariaveisDeDecisao,quantidadeVariaveisArtificiais, quantRestricoesDesigualdade):
    for i in range(0 , quantRestricoesDesigualdade  + 1):
        for j in range(len(tabelaSimplex[i])):
            if(j >= quantDeVariaveisDeDecisao and j < quantDeVariaveisDeDecisao + quantRestricoesDesigualdade):
                tabelaSimplex[i].insert(j, 0)

def procurarVariaveisBasicasAposFaseI(numeroTotalRestricoes):
    global indiceColunaPivo
    global indiceLinhaPivo

    
    aux = [row[:] for row in tabelaSimplex]
    for i in range(len(aux[0])):
        contarZero = 0
        contarUm = 0    

        guardarLinha = 0
        for j in range(1, numeroTotalRestricoes + 1):
            if(aux[j][i] == 0):
                contarZero += 1
            if(aux[j][i] == 1):
                contarUm += 1
                guardarLinha = j
            
        if(contarUm == 1 and contarZero == numeroTotalRestricoes - 1):
            print("é base")
            indiceColunaPivo = i
            indiceLinhaPivo = guardarLinha
            realizarOperacoesElementares()
            


def adicionarVariaveisMaiorIgual(quantDeVariaveisDeDecisao,quantRestricoesMaiorIgual, quantidadeVariaveisArtificiais, quantRestricoesDesigualdade,matrizDesigualdade):
    #adicionando na função objetivo
    for i in range(quantRestricoesMaiorIgual):
        tabelaSimplex[0].insert(0, 0)
    
    #adicionando nas restrições de menor igual
    for i in range(1, quantRestricoesMaiorIgual + 1):
        ultimoElemento = tabelaSimplex[i][len(tabelaSimplex[i]) - 1]
        for j in range(len(tabelaSimplex[i]) + quantRestricoesDesigualdade + quantidadeVariaveisArtificiais):
            if(j >= (quantDeVariaveisDeDecisao + quantRestricoesMaiorIgual )  ):
                tabelaSimplex[i].insert(j, 0)
        tabelaSimplex[i].pop()
        tabelaSimplex[i].pop()
        tabelaSimplex[i].append(ultimoElemento)

    #criando linha de restrições de maior igual
    aux = []
    for i in range(quantRestricoesDesigualdade):
        aux2 = []
        for j in range(quantDeVariaveisDeDecisao + quantRestricoesMaiorIgual + quantRestricoesDesigualdade*2 + 1):
            if(j >= 0 and j <= quantDeVariaveisDeDecisao - 1):
                aux2.append(matrizDesigualdade[i][j])
            elif(j >= quantDeVariaveisDeDecisao and j < quantDeVariaveisDeDecisao + quantRestricoesMaiorIgual):
                aux2.append(0)
            elif(j == (quantDeVariaveisDeDecisao + quantRestricoesMaiorIgual)):
                aux2.append(-1)
            elif(j == (quantDeVariaveisDeDecisao + quantRestricoesMaiorIgual + 1)):
                aux2.append(1)
            else:
                aux2.append(0)
        aux2.pop()
        aux2.append(matrizDesigualdade[i][len(matrizDesigualdade[i]) - 1])
        aux.append(aux2)
    
    for i in range(quantRestricoesMaiorIgual +1, len(tabelaSimplex)):
        tabelaSimplex.pop(i)
    for i in range(len(aux)):
        tabelaSimplex.append(aux[i])
    
    converterElementosMatrizParaInt(tabelaSimplex)
    print("teste")


def adicionarFuncaoObjetivoFaseI(quantDeVariaveisDeDecisao, quantVariaveisExcessoEFolga,quantVariaveisArtificiais):
    listaAux = []
    for i in range(quantDeVariaveisDeDecisao+ quantVariaveisExcessoEFolga + quantVariaveisArtificiais + 1):
        if i >= (quantDeVariaveisDeDecisao + quantVariaveisExcessoEFolga):
            listaAux.append(1)
        else:
            listaAux.append(0)
    listaAux.pop()
    listaAux.append(0)
    print("função objetivo", listaAux)
    tabelaSimplex.insert(0, listaAux)
    print("tabela simplex", tabelaSimplex)

def executarFaseDois():
    while(True):
        verificarMenorNumero()
        if(indiceColunaPivo == -1):
            break
        verificarQualALinhaPivo()
        igualarLinhaPivoA1()
        realizarOperacoesElementares()
def executarFaseUm():
    while(True):
        verificarMenorNumero()
        if(indiceColunaPivo == -1):
            print("Fase I concluída")
            carregarFuncaoObjetivosAposFaseI()
            executarFaseDois()
            break
        verificarQualALinhaPivo()
        igualarLinhaPivoA1()
        realizarOperacoesElementares()
        aproximar_matriz_global()

#executarFaseDois()
def main():
    montarTabelaSimplex()
    if(duasFases == False):
        executarFaseDois()
    else:
        executarFaseUm()
main()
#montarTabelaSimplex()
