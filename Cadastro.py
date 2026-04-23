
"""
Código incompleto!!!###############################################################################
Mais informacoes no final do codigo
"""

def cadastrar_usuario():
    # Solicita que digite um nome de usuário
    nome_usuario = input("Digite seu nome de usuário: ")

    # Solicita ao usuário que digite seu e-mail
    email = input("Digite seu e-mail: ")

    # Solicita ao usuário que digite uma senha
    senha = input("Digite sua senha: ")

    # Solicita ao usuário que confirme a senha digitada)
    confirmar_senha = input("Confirme sua senha: ")

    # Verifica se a senha e a confirmação são iguais
    if senha != confirmar_senha:
        print("Erro: As senhas não coincidem. Por favor, tente novamente.")
        return None

    # Cria um dicionário com os dados do usuário
    dados_usuario = {

        "usuario": nome_usuario,
        "email": email,
        "senha": senha

    }

    # Mensagem de sucesso
    print("Usuário cadastrado com sucesso!")

    # Retorna o dicionário com os dados do usuário
    return dados_usuario


# Exemplo de uso da função
usuario = cadastrar_usuario()
print(usuario)

"""
falta definir uma rota para a função de cadastro
arrumar o retorno para ir para outra pagina
assim que fizer a rota e testar, apagar o exemplo de uso
testar o confirmador de senha

-Adicionar outros tratamentos para melhor segurança
-Adicionar tratamentos de erro
"""