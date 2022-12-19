import random

print ("Seja muito bem vindo ao Guess Number do Augusto")
choice_number = input ("Digite o número teto do desafio:")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro! Valor informado não é númerico. Favor execute novamente e informe o número!")
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0
while True:
    answer_user = input("Advinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro! Valor informado não é númerico. Favor execute novamente e informe o número!")
        continue

    n_choices = n_choices + 1

    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Chutou alto, o número randomico é menor que isso...")
    else:
        print("Chutou baixo, o número randomico é maior que isso...")

print ("Número de tentativas: " + str(n_choices))