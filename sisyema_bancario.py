customer = []


from InquirerPy import prompt

def create_account():# Função para que seja crido uma conta.
    print("Função para criar conta chamada.")
    collecting_data_costumer()# Sendo chamada.
#Tesk of 
#[]Criar uma constante que recebe os dados de cada usuário(tupla).
#[x]Criar um validador número ou string.
#[x]Criar um Password.
#[]Valor inicial da conta para cada usuário.
#[]Largura de numeros que CPF/CNPJ pode receber/CPF: 11 Números - CNPJ: 14 Números .
#--------------------------------------------------------------------------------------------------------------------------------
def collecting_data_costumer():# Função para que seja crido uma conta.
    global customer # Permite que a variavel global possa ser modificada.
    name_account = input(f'''>>>Digite o nome da sua conta: ''') # Nome da conta.
    accounts_customers = {name_account: dates_user()} # Variável recebe os dados que foi gerado pela função dates_user().
    customer.append(accounts_customers) # Todos os dados estará sendo colocado na lista global.
    home() # Volta para o menu de entrar ou criar conta.
    print(customer)
#--------------------------------------------------------------------------------------------------------------------------------
def dates_user():

    customer_data = {
    "nome": None,
    "data_nascimento": None,
    "idade": None,
    "cpf_cnpj": None,
    "senha": None,
    "logradouro": None,
    "bairro": None,
    }  # Dicionário para armazenar os dados do cliente.

    questions_manual = [ # Lista de array sobre asperguntas e os dados do usuário.
        {"key": "nome"            ,"message": "Digite seu nome: "}, # Nome , Chave, Menssagem referente a pergunta.
        {"key": "data_nascimento" ,"message": "Digite sua data de nascimento: "}, # Nome , Chave, Menssagem referente a pergunta.
        {"key": "idade"           ,"message": "Digite sua idade: "}, # Nome , Chave, Menssagem referente a pergunta.
        {"key": "cpf_cnpj"        ,"message": "Digite seu CPF ou CNPJ: "}, # Nome , Chave, Menssagem referente a pergunta.
        {"key": "senha"           ,"message": "Digite sua senha: "}, # Nome , Chave, Menssagem referente a pergunta.
        {"key": "logradouro"      ,"message": "Digite seu logradouro: "}, # Nome , Chave, Menssagem referente a pergunta.
        {"key": "bairro"          ,"message": "Digite seu bairro: "}, # Nome , Chave, Menssagem referente a pergunta.
    ]
   # validations(question)
    for question in questions_manual: # Laço que percorre o questions_manual e sua posição atual.

       while True:  # Laço para validar a resposta.
        reply = input(question["message"])  # Mensagem exibida ao usuário.
        
        if reply.strip() == "":  # Verifica se a entrada está vazia ou apenas contém espaços.
            print(f'''
            {"-".center(50, "-")}
            Por favor, escreva seus dados conforme solicita a mensagem!
            {"-".center(50, "-")}
            ''')
            continue
        
        if question["key"] == "idade" and not reply.isdigit(): # Validação específica para idade (deve ser numérica)
            print(f'''
            {"=".center(50, "-")}
            A idade deve conter apenas números!
            {"=".center(50, "-")}
            ''')
            continue

        if question["key"] == "cpf_cnpj" and not reply.isdigit(): # Validação específica para CPF/CNPJ (deve ser numérico)
            print(f'''
            {"=".center(50, "-")}
            O CPF ou CNPJ deve conter apenas números!
            {"=".center(50, "-")}
            ''')
            continue

 #       if question["key"] == "cpf_cnpj" != len(11):
  #          print(f'''
     #       {"=".center(50, "-")}
    #        Não é possível continuar a operação, quantidade de números insuficiente.
  #          {"=".center(50, "-")}
     #       ''')
      #      continue


        customer_data[question["key"]] = reply
        break  # Sai do laço enquanto e segue para a próxima pergunta.

        
    
#--------------------------------------------------------------------------------------------------------------------------------
    state_question = [ # Seleção da sigla do estado usando InquirerPy
        {
            "type": "list",# Tipo lista
            "message": "Digite a sigla referente ao estado onde você vive:", # Menssagem que irá ser mostrada para o usuário
            "choices": ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", 
            "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", 
            "RR", "SC", "SP", "SE", "TO"
            ], # Siglas estados
            "name": "estado", # Mensagem para o estado
        }
    ]

    state_response = prompt(state_question)  # Captura a escolha do estado
    customer_data["estado"] = state_response["estado"]
    

    # Adiciona os dados coletados ao array de clientes
    print(f'''
    {"-".center(50,"-")}
    Cliente cadastrado com sucesso!
    {"-".center(50,"-")}
    ''')

    return customer_data # Retorna todos os dados colocado pelo usuário.
#-------------------------------------------------------------------------------------------
def enter_account():
    print("Função para entrar na conta chamada.")


questions = [
    {
        "type": "list",  # Tipo de pergunta "list" para exibir opções
        "message": "Crie ou entre em uma conta:",
        "choices": ["Entrar", "Criar conta"],  # Lista de escolhas
        "name": "option",  # Nome da variável que armazenará a resposta
    },
]
#-------------------------------------------------------------------------------------------
def home(): # Primeira função que será chamada do sistema
    response = prompt(questions)  # Retorna um dicionário

    # Comparação usando o valor da resposta
    if response["option"] == "Entrar":
        enter_account()
    elif response["option"] == "Criar conta":
        create_account()
home()
