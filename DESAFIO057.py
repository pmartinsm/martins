sexo = input('Informe seu sexo: [F/M] ').lower()
sex = sexo

while sexo != 'm' and sexo != 'f':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').lower()
    if sexo == 'm' or sexo == 'f':
        sex = sexo
print(f'Sexo {sex} registrado com sucesso!')