'''
Crie um "jogo dos estados". Neste jogo, o jogador precisa responder 
o nome da capital de cada Estado do Brasil. O jogo deve perguntar ao usuário 
"Qual a capital do Estado X?", e checar se o usuário respondeu de forma correta. 
Após cada pergunta, o usuário pode escolher parar o jogo ou continuar para a próxima pergunta.
 Quando o usuário decidir parar, ou quando todas as perguntas forem respondidas, 
 o código mostra o número bruto e porcentagem de acertos.



 Solução:
 * Criar um dicionario com cada estado como chave, e sua capital como valor.
* Criar a estrutura Pergunta,checagem, pontuação, e opção de saida/continuidade.
    * Gerar a pergunta pelo estado de forma aleatoria.
    * Mostrar se a pessoa acertou
    * Mostrar a pontuação da pessoa em tempo Real.
    * Evite repetições de perguntas
    * Coloque um feedback após cada resposta, exemplo: "Você acertou!" ou "Você errou, a capital certa de Goiás é Goiânia.

* Caso a pessoa queira sair, mostrar o sua quantidade de acerto, erro e a porcentagem de aproveitamento.

Dados necessários = um dicionario com cada estado do país e suas respectivas capitais.
'''
#importando as bibliotecas necessárias
import random

#Dicionario com os estados e suas respectivas capitais
estados_capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

#estrutura de Pergunta,checagem, pontuação, e opção de saida/continuidade.
def jogo_capitais():
    acertos = 0
    erros = 0
    estados_restantes = list(estados_capitais.keys())
    random.shuffle(estados_restantes) # Embaralha a lista de estados para perguntas aleatórias
    total_estados = len(estados_restantes)
    print("Bem-vindo ao jogo das capitais do Brasil!")
    print("Você precisa advinhar a capital de cada estado.")
    print("Digite 'sair' a qualquer momento para encerrar o jogo.")
    print("Vamos começar!\n")

    for estado in estados_restantes:
        capital_correta = estados_capitais[estado]
        resposta = input(f"Qual a capital do estado {estado}? ").strip()
        if resposta.lower() == 'sair':
            break
        elif resposta.lower() == capital_correta.lower():
            print("Você acertou!\n")
            acertos += 1
        else:
            print(f"Você errou! A capital do estado {estado} é {capital_correta} \n")
            erros +=1
            # Mostra  a pontuação da pessoa em tempo Real.
            print(f"Você tem {acertos} acertos e {erros} erros.\n")
    # Mostra o resultado final 
    print("Fim do jogo!")
    print(f"Você acertou {acertos} de {total_estados} perguntas.")
    if total_estados > 0:
        porcentagem_acertos = (acertos / total_estados) * 100
        print(f"Sua porcentagem de acertos é {porcentagem_acertos:.2f}%")
    else:
        print("Você não respondeu a nenhuma pergunta.")

# Executa o jogo
if __name__ == "__main__":
    jogo_capitais()

