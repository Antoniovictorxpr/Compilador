def transform_to_fng(grammar):
    # Adiciona um novo símbolo inicial S' e a produção S' -> S
    grammar['S\''] = ['S']
    
    # Remove produções da forma A -> αB, onde α é uma sequência de símbolos e B é um não-terminal
    new_productions = {}
    for non_terminal in grammar.keys():
        for production in grammar[non_terminal]:
            if len(production) > 1 and production[1] in grammar.keys():
                new_non_terminal = production[1]
                new_production = production[0]
                if len(production) > 2:
                    new_production += production[2:]
                if new_non_terminal not in new_productions:
                    new_productions[new_non_terminal] = []
                new_productions[new_non_terminal].append(new_production)
    
    # Adiciona as novas produções à gramática
    for non_terminal in new_productions.keys():
        if non_terminal in grammar:
            grammar[non_terminal].extend(new_productions[non_terminal])
        else:
            grammar[non_terminal] = new_productions[non_terminal]
    
    # Remove produções da forma A -> λ, adicionando novas produções para substituir cada ocorrência de A nas produções existentes
    epsilon_productions = []
    for non_terminal, productions in grammar.items():
        if 'λ' in productions:
            epsilon_productions.append(non_terminal)
            grammar[non_terminal].remove('λ')
    
    for non_terminal, productions in grammar.items():
        for epsilon_nt in epsilon_productions:
            for production in productions:
                new_productions = []
                for i in range(len(production)):
                    if production[i] == epsilon_nt:
                        new_productions.append(production[:i] + production[i+1:])
                grammar[non_terminal].extend(new_productions)
    
    return grammar

# Exemplo de gramática
grammar = {
    'S': ['aAd', 'A'],
    'A': ['Bc', 'λ'],
    'B': ['Ac', 'a']
}

# Transforma a gramática para FNG
fng_grammar = transform_to_fng(grammar)

# Imprime a gramática transformada
for non_terminal, productions in fng_grammar.items():
    print(f'{non_terminal} -> {" | ".join(productions)}')
