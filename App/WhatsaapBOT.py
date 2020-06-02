from Models.bot import WhatsaapBot
from time import sleep
from datetime import datetime,date
from Modules.db import get_from_query,insert_from_query,execute_from_query


#===========================================NOVO CODIGO
cadastro = []

def verificar_numero_inteiro():
    numero_sendo_testado = ""

    while not numero_sendo_testado.isdigit():
        numero_sendo_testado = bot.Ultima_Msg()
    return numero_sendo_testado


def totalApagar(produtos):
    total = sum([x[0][3] * x[1] for x in produtos])

    head = f"{'*SUA CONTA*'.center(42)}\n*|{'-'*42}|*\n"
    
    prods = "\n".join([f"{x[1]}x - {f'{x[0][1]} {x[0][2]}'} - (R$: {x[0][3]:.2f})" for x in produtos])

    enfeite1 = f"\n*|{'-'*42}|*"
    
    footer = f"\n*Total a pagar: R$: {total:.2f}*".center(42)

    enfeite2 = f"\n*|{'-'*42}|*"

    menu = "\n*[1]*- CONTINUAR\n*[2]*- CANCELAR PEDIDO"

    msg = head + prods + enfeite1 + footer +enfeite2 + menu

    return aguardaNumero(2,msg) == 1


def aguardaNumero(qtdOpçoes,msg,allowed=[]):
    bot.Envia_Msg(msg)
    num = " "
    while (not num.isdigit()) or int(num) > qtdOpçoes or int(num) <=0 :
        if num[0].upper() in allowed: return num[0].upper()
        num = bot.Ultima_Msg()
    return int(num)



def adcionaPedidoBanco(produtos,client,pagamento,trocoP):

    n_pedido = get_from_query(f"SELECT IFNULL(max(n_pedido),0)+1 from pedidos where ID_CLIENTE={client[0]}")[0][0]

    query = "INSERT INTO PEDIDOS (ID_CLIENTE,ID_PRODUTO,QUANTIDADE,PAGAMENTO,TROCOP,N_PEDIDO) VALUES(%s,%s,%s,%s,%s,%s)"
    lista = [(client[0],x[0][0],x[1],pagamento,trocoP,n_pedido) for x in produtos]
    insert_from_query(query,lista)


def metodoDePagamento():
    opcao = aguardaNumero(2,f"Como deseja efetuar o pagamento?\n*|{'-'*42}|*\n*[1]*- CARTÃO\n*[2]*- DINHEIRO")
    if opcao == 1:
        return "CARTAO",0
    else:
        if aguardaNumero(2,f"Deseja troco?\n*|{'-'*42}|*\n*[1]*- SIM\n*[2]*- NÃO") == 1:
            valor = aguardaNumero(999,"*Deseja troco para quanto?*")
            return "DINHEIRO",valor
        else:
            return "DINHEIRO",0

def selecionaEndereço(cliente):
    opc = aguardaNumero(2,f"*Deseja continuar com o endereço abaixo?*\n*|{'-'*42}|*\n\n{cliente[3]}\n*|{'-'*42}|*\n*[1]*- SIM\n*[2]*- NÃO")
    if opc == 2:
        end = aguardaResposta("*Digite o novo endereço de entrega!*")
        execute_from_query(f"UPDATE CLIENTES SET ENDERECO='{end}' WHERE id={cliente[0]}")
        cliente = get_from_query(f"SELECT * FROM CLIENTES WHERE ID={cliente[0]}")[0]
        selecionaEndereço(cliente)


def efetuar_pedidos(anterior=[],client=None):
    #lista opçoes
    escolhidos = anterior
    opcoes = get_from_query("select distinct tipo from menu")
    texto_opcoes = "\n".join([f"*[{i+1}]*- {x[0].upper()}" for i,x in enumerate(opcoes)])
    
    msg = f"{'*SUAS OPÇÕES:*'.center(42)}\n*|{'-'*42}|*\n{texto_opcoes}\n*|{'-'*42}|*"
    num = aguardaNumero(len(opcoes),msg)
    
    itens = get_from_query(f"select * from menu where tipo = '{opcoes[num-1][0]}'")

    texto_itens = "\n".join([f"*[{i+1}]*- {x[2].upper()} - R$: {x[3]:.2f}" for i,x in enumerate(itens)])
    
    msg = f"{'*ESCOLHA O ITEM:*'.center(42)}\n*|{'-'*42}|*\n{texto_itens}\n*|{'-'*42}|*"
    num = aguardaNumero(len(itens),msg)

    produto = itens[num-1]

    qtd = aguardaNumero(99,f"*Quantos você deseja?*")
    qtd2 = sum([x[1] for x in escolhidos if x[0][0] == produto[0]])
    while qtd + qtd2 > produto[4]:
        bot.Envia_Msg(f"*Só temos {produto[4]} disponíveis!*")
        qtd = aguardaNumero(99,f"*Quantos você deseja?*\n*[C]*-CANCELAR",["C"])
        if qtd == "C":
            return efetuar_pedidos(escolhidos,client=client)

    num = aguardaNumero(2,f"*Deseja continuar comprando?*\n*|{'-'*42}|*\n*[1]*- SIM\n*[2]*- NÃO")

    produtos = [*escolhidos,*[(produto,qtd)]]
    if num == 1:
        return efetuar_pedidos(produtos,client=client)
    else:
        if totalApagar(produtos): #clicou em Continuar
            pagamento,trocoP = metodoDePagamento()
            selecionaEndereço(client)
            adcionaPedidoBanco(produtos,client,pagamento,trocoP)
            bot.Envia_Msg("*Pedido realizado com sucesso!*\n*Estaremos enviando seu pedido em até 30 minutos!*")
        else: #clicou em Cancelar Pedido
            return #sai do pedido


def aguardaResposta(mensagem):
    bot.Envia_Msg(mensagem)
    sleep(0.5)
    while bot.Ultima_Msg() in mensagem:
        pass
    return bot.Ultima_Msg()

def cadastraCliente():
    telefone    = bot.capturaTelefone()
    cliente = get_from_query(f"SELECT * FROM CLIENTES WHERE TELEFONE = '{telefone}'")

    if not cliente:
        bot.Envia_Msg(f"\n*|{'-'*42}|*\n{'*ESTAÇÃO DO ESPETINHO*'.center(42)}\n*|{'-'*42}|*\n*Olá, Eu me chamo Ana*")
        bot.Envia_Msg(f"*Percebi que você ainda nao tem cadastro conosco, para que possamos continuar com o seu pedido gostariamos que nos informasse alguns dados:*")
        Nome        = aguardaResposta("*Qual seu nome?*")
        end         = aguardaResposta("*Qual seu endereço?*")

        insert_from_query("INSERT INTO CLIENTES (NOME,TELEFONE,ENDERECO) VALUES (%s,%s,%s)",[(Nome,telefone,end)])
    else:
        Nome = cliente[0][1]
    bot.Envia_Msg(f"\n*|{'-'*42}|*\n{'*ESTAÇÃO DO ESPETINHO*'.center(42)}\n*|{'-'*42}|*")
    bot.Envia_Msg(f"*{Saudação}, {Nome}*\n*Seja Bem-vindo!*")
    return cliente[0]


if __name__ == '__main__':
    bot = WhatsaapBot()  # Inicia o objeto WhatsaapBot
    #bot.Abre_Conversa("+55 11 98128-1791")  # Passando o numero ou o nome do contato
    hora = datetime.today().hour
    Saudação = ""
    if hora < 12:
        Saudação = "Bom Dia!"
    elif hora < 18:
        Saudação = "Boa Tarde!"
    else:
        Saudação = "Boa Noite!"
    #bot.Envia_Msg(f"\n*|{'-'*42}|*\n{'*ESTAÇÃO DO ESPETINHO*'.center(42)}\n*|{'-'*42}|*\n*Olá, Eu me chamo Ana*")

    bot.watch()

    client = cadastraCliente()

    efetuar_pedidos(client=client)

    bot.Envia_Msg("*Estação do Espetinho agradece a sua preferência!*")


   
    #efetuar_pedidos()


