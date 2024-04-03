def uppercase(string):
    upper = 0
    for i in string:
        if i.isupper() == True:
            upper += 1
    return upper

def lowercase(string):
    lower = 0
    for i in string:
        if i.islower() == True:
            lower += 1
    return lower

def blankSpace(string):
    space = 0 
    for i in string:
        if i.isspace() == True:
            space += 1
    return space

string = input('Digite uma frase: ')

print(string)
print('Maiúsculas: {}'.format(uppercase(string)))
print('Minúsculas: {}'.format(lowercase(string)))
print('Espaços: {}'.format(blankSpace(string)))