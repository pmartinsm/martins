import ccpf
cpf = input('Digiteu seu cpf: ')
cpf_true = ccpf.validate(cpf)

if cpf_true:
    print(f"O CPF {cpf} é válido.")
else:
    print(f"O CPF {cpf} é inválido.")
