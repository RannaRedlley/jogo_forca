import random

palavras = ["abelha", "macaco", "cobra"]

palavra = random.choice(palavras)

letras_certas = []
letras_erradas = []
tentativas = 6

boneco = ["  O", " /|\\", " / \\", " |", " /", " |", " \\"]

print("Bem-vindos ao joguinho da forca!")

while True:
    palavra_secreta = ""
    for letra in palavra:
        if letra in letras_certas:
            palavra_secreta += letra
        else:
            palavra_secreta += "_"

    print("\nPalavra: " + palavra_secreta)
    print("Tentativas restantes: " + str(tentativas))

    for i in range(tentativas, 7):
        if i > 0:
            print(boneco[i - 1])

    if palavra_secreta == palavra:
        print(f"ARRASOU, VOCÊ VENCEU! A palavra era: {palavra}")
        break

    if tentativas == 0:
        print("POXA, SINTO MUITO! VOCÊ PERDEU! A palavra era: " + palavra)
        break

    letra = input("Digite uma letra: ").lower()

    if letra in letras_certas or letra in letras_erradas:
        print("VOCÊ JÁ USOU ESSA LETRA. Tente novamente.")
        continue

    if letra in palavra:
        letras_certas.append(letra)
    else:
        letras_erradas.append(letra)
        tentativas -= 1


