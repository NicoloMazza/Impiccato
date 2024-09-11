import os
import re

def formatta_parola(testo):
    testo_con_underscore = re.sub(r'[a-zA-Z]', '_', testo)
    testo_finale = re.sub(r' ', ' ', testo_con_underscore)
    return testo_finale

def aggiorna_impiccato(vite):
    switch = {
        6: "\n Vite rimaste: 6 \n |----------\n |         |\n |\n |\n |\n |\n |\n |\n -",
        5: "\n Vite rimaste: 5 \n |----------\n |         |\n |         O\n |\n |\n |\n |\n |\n -",
        4: "\n Vite rimaste: 4 \n |----------\n |         |\n |         O\n |         |\n |\n |\n |\n |\n -",
        3: "\n Vite rimaste: 3 \n |----------\n |         |\n |         O\n |        /|\n |\n |\n |\n |\n -",
        2: "\n Vite rimaste: 2 \n |----------\n |         |\n |         O\n |        /|\ \n |\n |\n |\n |\n -",
        1: "\n Vite rimaste: 1 \n |----------\n |         |\n |         O\n |        /|\ \n |        /\n |\n |\n |\n -",
        0: "\n Vite rimaste: 0 \n |----------\n |         |\n |         O\n |        /|\ \n |        /-\ \n |\n |\n |\n -",
    }
    return switch.get(vite)

def set_up_iniziale():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Benvenuti al gioco dell impiccato!")
    parola_nascosta = input("Giocatore 1, inserisci la parola che Giocatore 2 dovrà indovinare: ")
    return parola_nascosta

def verifica_lettera(lettera, parola_nascosta):
    indici = []
    cont = 0

    while(cont<len(parola_nascosta)):
        if(parola_nascosta[cont].capitalize() == lettera.capitalize()):
            indici.append(cont)
            cont = cont + 1
        else:
            cont = cont + 1
            continue
    return indici


if __name__ == "__main__":
    vite = 6
    parola_nascosta = set_up_iniziale()
    parola_indovinata = formatta_parola(parola_nascosta)        #sostituisce tutte le lettere non indovinate con degli underscore, come nel gioco cartaceo

    while(vite>=0):
        if(parola_indovinata.find("_") != -1):                  #se ci sono altre lettere non trovate, continua il gioco
            print(aggiorna_impiccato(vite))
            if(vite==0):                                        #se non si hanno più vite, il gioco termina
                print("Sei morto! La parola da indovinare era: "+parola_nascosta)
                break
            print(parola_indovinata)
            lettera = input("\n\nInserisci una lettera: ")
            trovate = verifica_lettera(lettera, parola_nascosta)
            if(len(trovate)==0):
                vite = vite -1
            else:
                for i in trovate:
                    parola_indovinata = parola_indovinata[:i]+lettera.capitalize()+parola_indovinata[i+1:]
        else:
            print(parola_indovinata)
            print("complimenti hai vinto!")
            print("  _   _\n / \ / \ \n \  V  /\n  \   /\n   \_/")
            break
