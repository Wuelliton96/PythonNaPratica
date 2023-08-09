import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"Oi|Olá|Hey",
        ["Olá! Bem-vindo à nossa farmácia.", "Oi! Como posso ajudar?"]
    ],
    [
        r"Qual é o seu nome?",
        ["Eu sou o Farmabot, seu assistente virtual."]
    ],
    [
        r"Como você está?",
        ["Como um bot, não tenho sentimentos, mas estou aqui para ajudar."]
    ],
    [
        r"Você pode me ajudar a encontrar um medicamento\?",
        ["Claro! Por favor, me informe o nome do medicamento que você está procurando."]
    ],
    [
        r"Eu procuro por (.*)",
        ["Desculpe, não temos o medicamento {0} disponível no momento."]
    ],
    [
        r"Qual é o preço do (.*)\?",
        ["O preço do {0} é de R$ XX,XX."]
    ],
    [
        r"Obrigado|Agradecido",
        ["Você é bem-vindo! Se precisar de mais ajuda, é só me perguntar."]
    ],
    [
        r"Encerramento",
        ["Foi bom ajudar! Se precisar de mais assistência, estarei aqui. Até logo!"]
    ]
]

def chatbot():
    print("Olá! Sou o Farmabot, seu assistente virtual da farmácia. Como posso ajudar?\n")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
