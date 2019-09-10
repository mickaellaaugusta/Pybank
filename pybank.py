def caixa_eletronico():
    print('===== Bem Vindo ao Caixa Eletrônico =====')
    valor = int(input('Valor a ser sacado: R$'))
    if valor > 0:
        total = valor
        cédulas = 50
        total_de_cédulas = 0

        while True:
            if total >= cédulas:
                total -= cédulas
                total_de_cédulas += 1
            else:
                if total_de_cédulas > 0:
                    print('Total de {} cédulas, de R${}'.format(total_de_cédulas, cédulas))
                if cédulas == 50:
                   cédulas = 20
                elif cédulas == 20:
                    cédulas = 10
                elif cédulas == 10:
                    cédulas = 1
                total_de_cédulas = 0
                if total == 0:
                    break
    else: 
        print('Digite um valor positivo!')
        print('')
        caixa_eletronico()

caixa_eletronico()
