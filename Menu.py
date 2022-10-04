#Lista que armazena cadastro
cadastro = []


#Tratamento de erros, caso o úsuario não preencha os campos corretamente.
def  leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor digite um número válido. ')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


#Tamanho da linha
def linha(tam=42):
    return '-' * tam


#Cabeçalho armazenando a linha e o texto central
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


#Quando o usuário entra no programa, aparece essa lista que são os menus de opções para o usuário escolher 
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua Opção: ')
    return opc


#Aqui armazena nome, email e número de telefone do usuário, que será usado futuramente.
def add_cadastro():
    name = input('Coloque seu nome: ')
    email = input('Coloque seu email: ')
    telephone = input('Coloque seu número de telefone: ')
    cadastro.append([name, email, telephone])


#Aqui é o campo de pesquisa, lower funciona para transformar o texto em minúsculo. (Previnir erro de digitação)
def pesquisa(name):
    n = name.lower()
    for i, t in enumerate(cadastro):
        if t[0].lower() == n:
            return i
    return None


#Quando quiser escolher uma conta o usuário aperta o número 2, ae o programa identifica a conta que irá ser apaga e exclui ela.
def apaga():
    name = input('Qual conta gostaria de excluir? ')
    i = pesquisa(name)
    if i is not None:
        del cadastro[i]
    else:
        print('Nome não encontrado.')


#Alterar serve para se caso o usuário desejar alterar o seus campos de informações. Ele pode mudar o nome, telefone e email. Automaticamente muda as informações lá no "Banco de dados" do programa.
def altere():
    i = pesquisa(input('Insira o nome que deseja alterar: '))
    if i is not None:
        nome = cadastro[i][0]
        email = cadastro[i][1]
        telefone = cadastro[i][2]
        print('Encontrado: ')
        print(nome,email, telefone)
        nome = input('Coloque seu nome: ')
        email = input('Coloque seu número de telefone: ')
        telefone = input('Coloque seu email: ')
        cadastro[i] = [nome, email, telefone]
    else:
        print('Nome não encontrado.')


#Ordenar o cadastro
def ordena():
    cadastro.sort()


#Aqui é o campo de decisões do usuário, cada opção que ele utilizar, resultará em uma função que o programa irá executar.
while True:
    resposta = menu(['Cadastrar nova Pessoa', 'Vizualizar os cadastros', 'Excluir cadastro','Alterar Cadastro','Ordenar cadastros', 'Sair do sistema'])
    if resposta == 1:
        add_cadastro()
    elif resposta == 2:
        print(cadastro)
    elif resposta == 3:
        apaga()
    elif resposta == 4:
        altere()
    elif resposta == 5:
        ordena()
    elif resposta == 6:
        break
    else:
        print('ERRO! Digite uma opção válida!')