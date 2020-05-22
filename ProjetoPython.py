from time import sleep
from datetime import datetime
from datetime import date

dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']


espetinho = [('ESPETO DE CARNE - R$:8,00', 8.00), ('ESPETO DE CARNE (com creme de alho) - R$:9,50', 9.50),
             ('ESPETO DE PICAHNHA - R$:15,00', 15.00), ('ESPETO DE CUPIM - R$:13,00', 13.00),
             ('ESPETO DE CALABRESA DEFUMADA - R$7,00', 7.00), ('ESPETO DE FRANGO - R$:8,00', 8.00),
             ('ESPETO DE COXINHA DE FRANGO - R$:9,50', 9.50), ('ESPETO DE CORAÇÃO - R$:8,00', 8.00),
             ('ESPETO DE KAFTA - R$:10,00', 10.00), ('ESPETO DE TOSCANA R$:9,00', 9.00),
             ('MEDALHÃO DE CARNE - R$:13,50', 13.50), ('MEDALHÃO DE FRANGO - R$:11,50', 11.50)]

acompanhamento = [('PÃO DE ALHO - R$:6,00', 6.00), ('BATATA FRITA (P) - R$:8,00', 8.00),
                  ('BATATA FRITA (M) - R$:14,00', 14.00), ('BATATA FRITA (G) - R$:24,00', 24.00),
                  ('QUEIJO ASSADO c/MELAÇO OU s/MELAÇO - R$:8,00', 8.00)]

bebidas = [('COCA-COLA 350ml (lata) - R$:5,00', 5.00), ('COCA-COLA (1 litro) - R$:9,00', 9.00),
           ('GUARANÁ 269ml (lata) - R$:3,00', 3.00), ('GUARANÁ 350ml (lata) - R$:3,50', 3.50),
           ('GUARANÁ (1 litro) - R$:9,00', 9.00),('ÁGUA 300ml (sem gás) - R$:3,00', 3.00),
           ('ÁGUA 300ml (com gás) - R$:4,00', 4.00), ('DEVASSA PURO MALTE 350ml (lata) - R$:5,00', 5.00),
           ('HEINEKEN (long neck) - R$:9,00', 9.00)]

combos = [('COMBO 1 - R$:28,00', 28.00), ('COMBO 2 - R$:22,00', 22.00), ('COMBO 3 - R$:35,00', 33.00),
          ('COMBO 4 - R$:22,00', 22.00), ('COMBO 5 - R$:22,00', 22.00), ('COMBO 6 - R$:35,00', 35.00),
          ('COMBO 7 - R$:35,00', 35.00)]

promoção_do_dia = ['COMBO 1 - R$:28,00\n(Batata Frita (P) + 1 Espeto de Picanha + Pão de Alho + 1 Guaraná 269ml (lata)',
'COMBO 2 - R$:17,00\n(1 Espeto de Picanha + Batata Frita (P) + 1 Guaraná 269ml (lata))',
'COMBO 3 - R$:28,00\n(File Acebolado + Batata Frita (M) + 1 Guaraná 269ml (lata))',
'COMBO 4 - R$:17,00\n(1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata)',
'COMBO 5 - R$:17,00\n(1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Guaraná 269ml (lata))',
'COMBO 6 - R$:30,00\n(Carne do Sol Acebolada + Batata Frita (M) + 1 Guaraná 269ml (lata))',
'COMBO 7 - R$:30,00\n(1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata))']


lista_itens_factura = []
lista_precos_factura = []
cont_esp = 0
data = date.today()
indice_da_semana = data.weekday()
dia_da_semana = dias[indice_da_semana]




def car_esp():
    print("""---------------------------------------------------
            ESPETINHOS
---------------------------------------------------""")
    print("""[1]- ESPETO DE CARNE - R$:8,00
[2]- ESPETO DE CARNE (com creme de alho) - R$:9,50
[3]- ESPETO DE PICAHNHA - R$:15,00
[4]- ESPETO DE CUPIM - R$:13,00
[5]- ESPETO DE CALABRESA DEFUMADA - R$:7,00
[6]- ESPETO DE FRANGO - R$:8,00
[7]- ESPETO DE COXINHA DE FRANGO - R$:9,50
[8]- ESPETO DE CORAÇÃO - R$:8,00
[9]- ESPETO DE KAFTA - R$:10,00
[10]- ESPETO DE TOSCANA - R$:9,00
[11]- MEDALHÃO DE CARNE - R$:13,50
[12]- MEDALHÃO DE FRANGO - R$:11,50
---------------------------------------------------""")


def car_acom():
    print("""------------------------------------------------
          ACOMPANHAMENTOS
------------------------------------------------""")
    print("""[1]- PÃO DE ALHO - R$:6,00
[2]- BATATA FRITA (P) - R$:8,00
[3]- BATATA FRITA (M) - R$:14,00
[4]- BATATA FRITA (G) - R$:24,00
[5]- QUEIJO ASSADO c/MELAÇO OU s/MELAÇO R$:8,00
------------------------------------------------""")


def car_bebida():
    print("""-----------------------------------------------
              BEBIDAS
-----------------------------------------------""")
    print("""[1]- COCA-COLA 350ml (lata) - R$:5,00
[2]- COCA-COLA (1 litro) - R$:9,00
[3]- GUARANÁ 269ml (lata) - R$:3,00
[4]- GUARANÁ 350ml (lata) - R$:3,50
[5]- GUARANÁ (1 litro) - R$:9,00
[6]- ÁGUA 300ml (sem gás) - R$:3,00
[7]- ÁGUA 300ml (com gás) - R$:4,00
[8]- DEVASSA PURO MALTE 350ml (lata) - R$:5,00
[9]- HEINEKEN (long neck) - R$:9,00
-----------------------------------------------""")


def car_combo():
    print("""--------------------------------------
               COMBOS             
--------------------------------------""")
    print(f"""O COMBO {promoção_do_dia [indice_da_semana].split()[1]} ESTÁ EM PROMOÇÃO!!
Está custando {promoção_do_dia [indice_da_semana].split()[3]}""")
    print('--------------------------------------')
    print("""[1]- COMBO 1 - R$:28,00
(Batata Frita (P) + 1 Espeto de Picanha + Pão de Alho + 1 Guaraná 269ml (lata))
[2]- COMBO 2 - R$:22,00
(1 Espeto de Picanha + Batata Frita (P) + 1 Guaraná 269ml (lata))
[3]- COMBO 3 - R$:33,00
(File Acebolado + Batata Frita (M) + 1 Guaraná 269ml (lata))
[4]- COMBO 4 - R$:22,00
(1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata))
[5]- COMBO 5 - R$:22,00
(1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Guaraná 269ml (lata))
[6]- COMBO 6 - R$:35,00
(Carne do Sol Acebolada + Batata Frita (M) + 1 Guaraná 269ml (lata))
[7]- COMBO 7 - R$:35,00
(1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata))
-------------------------------------------------------------------------------------------------------------------""")


def conta():
    global lista_itens_factura
    global lista_precos_factura

    print("""|--------------------------------------|
|              SUA CONTA               |
|--------------------------------------|""")
    preco_final = 0

    for i in range(0, len(lista_itens_factura)):
        print(f'{lista_itens_factura[i]}')
        preco_final += lista_precos_factura[i]
    print('|--------------------------------------|')
    print()
    print('|--------------------------------------|')
    print(f'|Total a pagar: R$ {preco_final:.2f}|')
    print('|--------------------------------------|')
    print()
    print('Digite o endereço para a entrega.')


def verificar_tipo_pedido(valor='0', limite=1):
    while not valor.isdigit():
        print('Digite um número inteiro por-favor')
        valor = input(': ')
    valor = int(valor)

    if valor > limite or valor <= 0:
        print('A opção que você digitou não é válida! Por-favor tente novamente')
        return verificar_tipo_pedido(input(': '), limite)
    return valor


def verificar_quant_pedida(valor='0'):
    while not valor.isdigit():
        print('Digite um número inteiro por-favor')
        valor = input(': ')
    valor = int(valor)

    if valor <= 0:
        print('A opção que você digitou não é válida! Por-favor tente novamente')
        return verificar_tipo_pedido(input(': '))
    return valor


def efetuar_pedidos():
    global lista_itens_factura
    global lista_precos_factura
    print("""---------------------------
      SUAS OPÇÕES:
---------------------------
[1]- ESPETINHOS
[2]- ACOMPANHAMENTO
[3]- BEBIDAS
[4]- COMBOS
[5]- CANCERLAR PEDIDO
[6]- EFETUAR PEDIDO
---------------------------""")

    op_pedido = input('Digite a opção: ').strip()[0]

    if op_pedido == '1':
        quant_esp = verificar_quant_pedida(input('Quantos você deseja? '))
        while quant_esp > 0:
            car_esp()
            sabor = verificar_tipo_pedido(input(f'Dígite o sabor do Espetinho: '), 12)
            quant = verificar_quant_pedida(input(f'Quantos {espetinho[sabor - 1][0]} você deseja: '))
            while quant > quant_esp:
                print(f'Infelizmente você pediu uma quantidade inferior a essa!'
                      f'\nDigite uma quantidade que vai de 1 até {quant_esp}')
                quant = verificar_quant_pedida(input(f'Quantos {espetinho[sabor - 1][0]} você deseja: '))
            quant_esp -= quant
            lista_itens_factura.append(espetinho[sabor - 1][0])
            lista_precos_factura.append(espetinho[sabor - 1][1] * quant)
    elif op_pedido == '2':
        quant_acom = verificar_quant_pedida(input('Quantos você deseja? '))
        while quant_acom > 0:
            car_acom()
            op_acom = verificar_tipo_pedido(input(f'Dígite o Acompanhamento: '), 5)
            quant = verificar_quant_pedida(input(f'Quantos {acompanhamento[op_acom - 1][0]} você deseja: '))
            while quant > quant_acom:
                print(f'Infelizmente você pediu uma quantidade inferior a essa!'
                      f'\nDigite uma quantidade que vai de 1 até {quant_acom}')
                quant = verificar_quant_pedida(input(f'Quantos {acompanhamento[op_acom - 1][0]} você deseja: '))
            quant_acom -= quant
            lista_itens_factura.append(acompanhamento[op_acom - 1][0])
            lista_precos_factura.append(acompanhamento[op_acom - 1][1] * quant)
    elif op_pedido == '3':
        quant_bebi = int(input('Quantos você deseja? '))
        while quant_bebi > 0:
            car_bebida()
            op_bebi = verificar_tipo_pedido(input(f'Dígite a Bebida: '), 9)
            quant = verificar_quant_pedida(input(f'Quantos {bebidas[op_bebi - 1][0]} você deseja: '))
            while quant > quant_bebi:
                print(f'Infelizmente você pediu uma quantidade inferior a essa!'
                      f'\nDigite uma quantidade que vai de 1 até {quant_bebi}')
                quant = verificar_quant_pedida(input(f'Quantas {bebidas[op_bebi - 1][0]} você deseja: '))
            quant_bebi -= quant
            lista_itens_factura.append(bebidas[op_bebi - 1][0])
            lista_precos_factura.append(bebidas[op_bebi - 1][1] * quant)
    elif op_pedido == '4':
        quant_combo = verificar_quant_pedida(input('Quantos você deseja? '))
        while quant_combo > 0:
            car_combo()
            op_combo = verificar_tipo_pedido(input(f'Dígite o Combo: '), 7)
            quant = verificar_quant_pedida(input(f'Quantos {combos[op_combo - 1][0]} você deseja: '))
            while quant > quant_combo:
                print(f'Infelizmente você pediu uma quantidade inferior a essa!'
                      f'\nDigite uma quantidade que vai de 1 até {quant_combo}')
                quant = verificar_quant_pedida(input(f'Quantas {combos[op_combo - 1][0]} você deseja: '))
            quant_combo -= quant
            lista_itens_factura.append(combos[op_combo - 1][0])

            if indice_da_semana == op_combo - 1:
                print(f'O combo {op_combo}: {combos[op_combo - 1][0]} está custando R$ {combos[op_combo - 1][1] - 5}\nPorque está em promoção')
                lista_precos_factura.append((combos[op_combo - 1][1] - 5) * quant)
            else:
                lista_precos_factura.append(combos[op_combo - 1][1] * quant)
    elif op_pedido == '5':
        lista_itens_factura.clear()
        lista_precos_factura.clear()
    elif op_pedido == '6':
        return False
    return True


def op_pedi():
    flag = efetuar_pedidos()
    while True:
        flag = efetuar_pedidos()

        if flag == False:
            print("""-------------------------------------------
        Seu pedido foi realizado com sucesso!
   -------------------------------------------""")
            conta()
            break
    exit()


def vol_car():
    print("""[1]- IR PARA O CARDÁPIO
[2]- FAZER SEU PEDIDO
[3]- VOLTAR AO MENU INICIAL
--------------------------------------""")
    voltar = input('Dígite sua opção: ').strip()[0]
    if voltar != '1' and voltar != '2' and voltar != '3':
        print("""------------------------------
         Não entendi.
    Dígite uma das opções:
------------------------------
[1]- IR PARA O CARDÁPIO
[2]- FAZER SEU PEDIDO
[3]- VOLTAR AO MENU PRINCIPAL
------------------------------""")
        voltar = input('Dígite uma das opção: ').strip()[0]
    if voltar == '1':
        cardapio()
    elif voltar == '2':
        efetuar_pedidos()
    elif voltar == '3':
        main()


def menu_principal():
    print("""--------------------------
Dígite uma das opções:
--------------------------
[1]- PROMOÇÕES DO DIA
[2]- CARDÁPIO
[3]- FAZER SEU PEDIDO
[4]- FINALIZAR ATENDIMENTO
---------------------------""")


def promocao_do_dia():
    print(f"""--------------------------------------
PROMOÇÃO DO DIA ({dia_da_semana})
--------------------------------------
{promoção_do_dia[indice_da_semana]}
--------------------------------------""")
    vol_car()


def cardapio():
    print("""---------------------------
         CARDÁPIO
---------------------------
[1]- ESPETINHOS
[2]- ACOMPANHAMENTO
[3]- BEBIDAS
[4]- COMBOS
[5]- VOLTAR AO MENU INICIAL
---------------------------""")

    car = input('Dígite sua Opção: ')
    print("""----------------------------""")

    while car != '1' and car != '2' and car != '3' and car != '4' and car != '5':
        print("""----------------------------
        Não entendi
   Dígite uma das opções
----------------------------
[1]- ESPETINHOS
[2]- ACOMPANHAMENTO
[3]- BEBIDAS
[4]- COMBOS
[5]- VOLTAR AO MENU INICIAL
----------------------------""")
        car = input('Dígite sua Opção: ').strip()[0]

    if car == '1':
        car_esp()
        vol_car()
    elif car == '2':
        car_acom()
        vol_car()
    elif car == '3':
        car_bebida()
        vol_car()
    elif car == '4':
        car_combo()
        vol_car()
    elif car == '5':
        main()


def pedido():
    print('----------------------------------')
    pronto = input('Pronto para fazer seu pedido [S/N]: ').upper().strip()[0]

    if pronto != 'S' and pronto != 'N':
        print("""Não entendi
Dígite [S] para SIM | [N] para NÃO """)
        pronto = str(input('Pronto para fazer seu pedido [S/N]: ')).upper().strip()[0]
    elif pronto == 'S':
        op_pedi()
        print("""-----------------------------------
    Deseja fazer mais um pedido?
Dígite [S] para SIM e [N] para NÃO
-----------------------------------""")
    else:
        menu_principal()

def main():
    menu_principal()
    op1 = input('Digite a opção: ').strip()[0]
    if op1 != '1' and op1 != '2' and op1 != '3' and op1 != '4':
        print("""--------------------------
Não entendi a opção dígitada.""")
        menu_principal()
        op1 = input('Digite a opção: ').strip()[0]
    if op1 == '1':
        promocao_do_dia()
    elif op1 == '2':
        cardapio()
    elif op1 == '3':
        pedido()
    elif op1 == '4':
        return False
    return True


if __name__ == '__main__':
    hora = datetime.today().hour
    print("""----------------------------  
--  ESTAÇÃO DO ESPETINHO  --           
----------------------------""")
    sleep(0.5)

    if hora < 12:
        print('Olá Bom Dia!')
    elif hora < 18:
        print('Olá Boa Tarde!')
    else:
        print('Olá Boa Noite!')
    print("""Seja Bem-vindo! 
Sou sua atendente virtual!
eu me chamo Ana.
irei passar agora suas opções""")
    sleep(1)
    while True:
        flag = main()

        if flag == False:
            break
    print("""-----------------------------
       Obrigado, volte sempre.
    -----------------------------""")
