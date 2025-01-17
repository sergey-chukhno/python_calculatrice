import re
import json
import os
import time

def calculate():
    history = []
    calc_continue = False

    def decompose(calcul):  # Parse the calculation
        pat = re.findall(r'\d+|[+\-*/^()]', calcul)
        if calc_continue:
            pat.insert(0, result[0])
        
        return pat

    def ordre(pat):
        def simple_prio(pat):

            while "^" in pat:
                index = pat.index("^")
                left_num = float(pat[index - 1])
                right_num = float(pat[index + 1])
                pat[index - 1] = left_num ** right_num
                del pat[index:index + 2]

            # For multiplication and division
            while "*" in pat or "/" in pat:
                if "*" in pat:
                    index = pat.index("*")
                    left_num = float(pat[index - 1])
                    right_num = float(pat[index + 1])
                    pat[index - 1] = left_num * right_num
                    del pat[index:index + 2]
                elif "/" in pat:
                    try:
                        index = pat.index("/")
                        left_num = float(pat[index - 1])
                        right_num = float(pat[index + 1])
                        pat[index - 1] = left_num / right_num
                        del pat[index:index + 2]
                    except ZeroDivisionError:
                        print("La division par 0 est interdit")
                        return ["Erreur"]

            # For adittion and soustraction
            while "+" in pat or "-" in pat:
                if "+" in pat:
                    index = pat.index("+")
                    left_num = float(pat[index - 1])
                    right_num = float(pat[index + 1])
                    pat[index - 1] = left_num + right_num
                    del pat[index:index + 2]
                elif "-" in pat:
                    index = pat.index("-")
                    left_num = float(pat[index - 1])
                    right_num = float(pat[index + 1])
                    pat[index - 1] = left_num - right_num
                    del pat[index:index + 2]

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
        os.system('cls')
        if calc_continue:
            print(f"Vous reparter de {result[0]} ,n'oublier pas l'opérateur au début")
        enter = input("Entrer votre calcul\n>> ")

        try:
            calcul = decompose(enter)
            result = ordre(calcul)
            history.append({"calcul": enter, "resultat": result[0]})
            print(f"\nLe résultat est: {result[0]}")
            print("H - Historique | S - Supp Historique | C - Continuer depuis le resultat | N - Recommencer de 0 | Q - Quitter ")
        except Exception:
            print(f"Erreur dans le calcul")
            print("H - Historique | S - Supp Historique | C - Continuer depuis le resultat | N - Recommencer de 0 | Q - Quitter ")
            result = [0]

        with open("historique.json", "w") as fichier:
            json.dump(history, fichier, indent=5)

        user_input = input("Choisissez une option: H/S/C/N/Q\n>> ").lower()

        if user_input == "h":
            os.system('cls')
            print("\nHistorique des calculs :")
            for enter in history:
                print(f"{enter['calcul']} = {enter['resultat']}")
            print("\nS - Supp Historique | C - Continuer depuis le resultat | N - Recommencer de 0 | Q - Quitter ")
            hinput = input("\nChoisissez une option: S/C/N/Q\n>> ").lower()
            if hinput == "s":
                history = []
                os.system("cls")
                print("Historique effacer")
                time.sleep(2)
            elif hinput == "c":
                calc_continue = True
            elif hinput == "n":
                calc_continue = False
            elif hinput == "q":
                print("Tchaoe")
                break

        elif user_input == "s":
            os.system('cls')
            print("L'historique vient d'etre effacé")
            history = []
            time.sleep(2)
        elif user_input == "c":
            calc_continue = True
        elif user_input == "n":
            calc_continue = False
        elif user_input == "q":
            print("Merci et Aurevoir")
            break
        else:
            print("Option non reconnue. Essayez de nouveau.")

calculate()
