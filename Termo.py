#Import de cor, random e escolha das palavras
from colorama import init, Fore
init(autoreset=True)
import random
print(Fore.BLUE + "------------------Terminho sem massagem------------------")
palavras = ["preto", "gatos", "gotas", "barco", "morte", "poder", "sonos", "banda", "magia", "timao", "saber", "beijo",]
palavra_secreta = random.choice(palavras)

#Processo de input ao jogador, e acerto de cada letra respectiva da palavra random, sendo mostrada com as cores
for i in range (6):
    tentativa = input("Escreva uma palavra: ").lower()
    for i in range (5):
        if tentativa[i] == palavra_secreta[i]:
            print(Fore.GREEN + tentativa[i])
        elif tentativa[i] in palavra_secreta:
            print(Fore.YELLOW + tentativa[i])
        else:
            print(Fore.WHITE + tentativa[i])
    #Uma mensagem parebenizando o acerto do jogador
    if tentativa == palavra_secreta:
        print(Fore.GREEN + "Você Acertou, sabe muito!")
        break
    #Agora uma mensagem mostrando que o jogador perdeu, e revelando a palavra secreta
else:
    print(Fore.RED + "Você perdeu! Aí é mal")
    print("\n")
    print(Fore.YELLOW + "A palavra era: " + palavra_secreta) 

print("\n")