# LISTA DE HORÁRIOS DO BARBEIRO
horarios_disponiveis = ["9h", "10h", "14h", "15h", "16h"]

# FUNÇÃO 1: Responder Oi
def responder_oi():
    print("Bot: Ola qual corte vai querer?")

# FUNÇÃO 2: Mostrar horários com FOR - COMPLETA AQUI
def mostrar_horarios():
    print("Bot: Horários disponíveis:")
    for horario in horarios_disponiveis:
        print(horario)

def agendar_corte():
    print("Horários Disponiveis pra agendamento: ")
    for hora in horarios_disponiveis:
        print(hora)
    esolha = input("Cliente: Qual horário quer agendar? ")
    if esolha in horarios_disponiveis:
        horarios_disponiveis.remove(esolha)
        print("Bot: Confirmado: Te Vejo Lá!")
    else:
        print("Bot: Esse horario nao existe ou já foi agendado!!!")

# CÓDIGO PRINCIPAL
print("Autoatendimento ON Barbeiro Online!")

while True:
    mensagem = input("Cliente: ").lower()
    
    if mensagem == "sair":
        print("Falou Volta Sempre!!")
        break
    
    if "oi" in mensagem or "ola" in mensagem:
        responder_oi()  # OLHA A FUNÇÃO SENDO CHAMADA
    elif "valor" in mensagem or "preço" in mensagem:
        print("Valores: Corte R$15, barba R$30, combo R$45 ")
    elif "agendar" in mensagem:
        agendar_corte()
    elif "horario" in mensagem or "hora" in mensagem:
        mostrar_horarios()  
    else:
        print("Bot: Nao entendi rsrs Digite: oi, horario, preço!")
  
