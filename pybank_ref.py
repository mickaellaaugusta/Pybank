"""
Boas práticas para um código limpo:

    1. Variáveis e funções devem ter nomes que deixem claro o que elas fazem.
    2. Funções não devem ter mais que dois parâmentros. [Ex.: def myassert(result, nome)]
    3. Toda função deve ter apenas um ponto de saída. [Ex.: um return apenas]
    4. Código limpo tem que ter teste unitário. [O atendimento às regras anteriores sem 
        teste unitário invalida o código ser limpo.]
    5. Código limpo não possui comentário. O código precisa ser autoexplicativo. 
        [Igone os comentários abaixo, estou aprendendo...]
"""

def caixa_eletronico():
    
    total = valor_saque()
        
    lista_resultado = calcular_cedulas(total)
    resultado(lista_resultado)
        
#============================Interface=====================================
#função de interface - função para obter valor de saque
def valor_saque():

    saque_valido = False
    value = 0

    print('===== Bem Vindo ao Caixa Eletrônico =====\n')
    
    while saque_valido is False:
         value = int(input('Digite o valor a ser sacado: R$'))
         saque_valido = valida_saque(value)

         if saque_valido is False:
            print('Digite um valor positivo!\n')
          
    return value

#imprime resultado de quantidade de cédulas na tela
def resultado(lista_resultado):
    if len(lista_resultado) == 0:
        print('Valor informado igual a R$0. Saque não efetuado.\n')
    
    for item in lista_resultado:
        total_de_cedulas=item[0]
        cedulas=item[1]

        print('Total de {} cédulas, de R${}'.format(total_de_cedulas, cedulas))

#========================Negócio=========================================
#função validando o input da interface
def valida_saque(value):
    result = False
    if value >= 0:
        result = True

    return result

def calcular_cedulas(total):
    cedulas = 50
    total_de_cedulas = 0
    lista_resultado = []

    while True:
        if total >= cedulas:
            total -= cedulas
            total_de_cedulas += 1
        else:
            if total_de_cedulas > 0:
               lista_resultado.append((total_de_cedulas,cedulas)) 

            if cedulas == 50:
               cedulas = 20
            elif cedulas == 20:
                cedulas = 10
            elif cedulas == 10:
                cedulas = 1

            total_de_cedulas = 0

            if total == 0:
                break
    return lista_resultado

if __name__ == "__main__":
    caixa_eletronico()
