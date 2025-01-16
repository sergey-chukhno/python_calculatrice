import re
import json
import msvcrt
import os
import time 

def calculate():
    history = []
    calc_continue = False

    def decompose(calcul):#Parse calcul
        pat = re.findall(r'\d+|[+\-*/^()]', calcul)
        if calc_continue:
            pat.insert(0, result[0])

        return pat

    def ordre(pat): 
        def simple_prio(pat):
            while "^" in pat:
                index = pat.index("^")
                left_num = float(pat[index -1])
                right_num = float(pat[index +1])
                pat[index-1] = left_num**right_num
                del pat[index:index+2]
                print(pat)

            while "*" in pat:
                index = pat.index("*")
                left_num = float(pat[index-1])
                right_num = float(pat[index+1])
                pat[index-1] = left_num*right_num
                del pat[index:index+2]

            while "/" in pat:
                try:
                    index = pat.index("/")
                    left_num = float(pat[index-1])
                    right_num = float(pat[index+1])
                    pat[index-1] = left_num/right_num
                    del pat[index:index+2]

                except ZeroDivisionError:
                    print("La division par 0 est interdit")
                    break
            
            while "+"in pat:
                index = pat.index("+")
                left_num = float(pat[index-1])
                right_num = float(pat[index+1])
                pat[index-1] = left_num+right_num
                del pat[index:index+2]

            while "-"in pat:
                index = pat.index("-")
                left_num = float(pat[index-1])
                right_num = float(pat[index+1])
                pat[index-1] = left_num-right_num
                del pat[index:index+2]


            return pat

        while "(" in pat:
            open_parenthese = len(pat) - 1 - pat[::-1].index("(")
            try:
                close_parenthese = pat.index(")", open_parenthese)
            except ValueError:
                print("Erreur de parenthese")
                return ["Erreur"]

            prio_calcul = pat[open_parenthese + 1:close_parenthese]
            result = simple_prio(prio_calcul)
            
            if result == ["Erreur"]:
                return ["Erreur"]

            pat[open_parenthese:close_parenthese + 1] = result

        return simple_prio(pat)
    
    try: 
        with open("historique.json", "r") as fichier:
            history = json.load(fichier) 
    except FileNotFoundError:
        history = []


    while True:
        quit = True
        os.system('cls')
        if calc_continue:
            print(f"Vous reparter de {result[0]} ,n'oublier pas l'opérateur au début")
        enter = input("Entrer votre calcul\n>> ")

        try:
           calcul = decompose(enter)
           result = ordre(calcul)
           history.append({"calcul": enter, "resultat": result})
           print(f"\nLe résultat est: {result[0]}")
           print("H - Historique | S - Supp Historique | C - Continuer depuis le resultat | N - Recommencer de 0 | Q - Quitter ")
        except ValueError:
            print(f"Valeur incorrect")

        with open("historique.json", "w") as fichier:
            json.dump(history, fichier, indent=5)

        if msvcrt.kbhit:
            key = msvcrt.getch().decode('utf-8')
            if key == "h":
                os.system('cls')
                print("\nHistorique des calculs :")
                for enter in history: 
                    print(f"{enter['calcul']} = {enter['resultat']}")
                print("Reappuyer H pour sortir")
                while True:
                    if msvcrt.kbhit(): 
                        key2 = msvcrt.getch().decode('utf-8')
                        if key2 == "h":
                            os.system('cls')
                            quit = False
                            break
            if key == "s":
                os.system('cls')
                print("L'historique vient d'etre effacé")
                history = []
                quit = False
                time.sleep(2)
            if key == "p":
                calc_continue = True
                pass
            if key == "n" or key == "c":
                if key == "n":
                    calc_continue = False
                else:
                    calc_continue = True
                pass
            else:
                if quit==True:
                    print("Merci et Aurevoir")
                    break

calculate()
