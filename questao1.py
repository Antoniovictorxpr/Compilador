def fng(gramatica):
    gramatica_auxiliar = gramatica.copy()
    simbolos_removidos = set()

    # Remover produções com símbolos terminais
    for variavel, producoes in gramatica_auxiliar.items():
        novas_producoes = []
        for producao in producoes:
            if len(producao) == 1 and producao.isupper():
                simbolos_removidos.add(producao)
            else:
                novas_producoes.append(producao)
        gramatica_auxiliar[variavel] = novas_producoes
    
    # Remover produções que contêm símbolos removidos
    for variavel, producoes in gramatica_auxiliar.items():
        novas_producoes = []
        for producao in producoes:
            for removido in simbolos_removidos:
                if removido in producao:
                    producao = producao.replace(removido, "")
            if producao:
                novas_producoes.append(producao)
        gramatica_auxiliar[variavel] = novas_producoes
    
    # Expandir a gramática
    gramatica_auxiliar = expandir_gramatica(gramatica_auxiliar, gramatica)
    
    # Substituir símbolos na gramática
    nova_variavel = {}
    contador = 1
    for variavel in gramatica_auxiliar:
        nova_variavel[variavel] = 'A' + str(contador)
        contador += 1
    gramatica_auxiliar = substituir_simbolos(gramatica_auxiliar, nova_variavel)
    
    return gramatica_auxiliar


def expandir_gramatica(gramatica, original):
    nova_gramatica = {}
    for variavel, producoes in gramatica.items():
        novas_producoes = []
        for producao in producoes:
            if producao[0].isupper() and producao[0] in original:
                novas_producoes.extend([subproducao + producao[1:] for subproducao in original[producao[0]]])
            else:
                novas_producoes.append(producao)
        nova_gramatica[variavel] = novas_producoes
    return nova_gramatica

def substituir_simbolos(gramatica, simbolos):
    nova_gramatica = {}
    for variavel, producoes in gramatica.items():
        novas_producoes = []
        for producao in producoes:
            nova_producao = ""
            for simbolo in producao:
                if simbolo.isupper() and simbolo in simbolos:
                    nova_producao += simbolos[simbolo]
                else:
                    nova_producao += simbolo
            novas_producoes.append(nova_producao)
        nova_gramatica[simbolos[variavel]] = novas_producoes
    return nova_gramatica

# Definição da gramática
gramatica = {
    "S": ["AB", "CSB"],
    "A": ["aB", "C"],
    "B": ["bbB", "b"]
}

print(fng(gramatica))
