import re

print("As palavras iniciadas com números, são reservadas pelo sistema.")
entrada = input("Digite uma palavra: ")[:10]

regex = re.compile(
    r'^[^0-9][a-zA-Z0-9(){}[\]!@#$%^~;:.,><+=\-_*|&¨¬§¢£°/?ºª´`"áéíóúàèìòùâêîôûãõçÇÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕ\s]*$')
invalid_chars_regex = re.compile(r'[xyztwXYZTW]')


def verifica_expressao(entrada):
    special_chars = ['+', '-', '*', '/', '[', ']',
                     '{', '}', '(', ')', '!', '@', '#', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    error_count = 0

    for i, char in enumerate(entrada):
        if char.lower() in ['x', 'y', 'z', 't', 'w']:
            if i == 0 or i == len(entrada) - 1:
                error_count += 1
            elif entrada[i-1] in special_chars and entrada[i+1] in special_chars:
                pass
            else:
                error_count += 1

    if error_count != 0:
        print("Compilador não aceitou")
    else:
        print("Expressão numérica")


if regex.match(entrada) and not invalid_chars_regex.search(entrada):
    print("Compilador aceitou.")
    print(", ".join([c for c in entrada]))
elif regex.match(entrada):
    verifica_expressao(entrada)
else:
    print("Números no inicio são reservados para o sistema")