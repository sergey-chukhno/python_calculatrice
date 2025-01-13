def calculate():
    print("Tapez un calcul (exemple : 12 + 34)")

    while True:
        enter = input(">> ")

        try:
            elements = enter.split()
            if len(elements) != 3:
                print("Erreur : Saisir un calcul sous forme : x + y")
                continue

            nombre1 = float(elements[0])
            operator = elements[1]
            nombre2 = float(elements[2])

            match operator:
                case "+":
                    resultat = nombre1 + nombre2
                case "-":
                    resultat = nombre1 - nombre2
                case "*":
                    resultat = nombre1 * nombre2
                case "/":
                    if nombre2 == 0:
                        print("Erreur : Division par 0 impossible.")
                        continue
                    resultat = nombre1 / nombre2
                case "^":
                    resultat = nombre1 ** nombre2
                case _:
                    print(f"Erreur : Saisir un operateur valide '{operator}'.")
                    continue

            print(f"Résultat : {resultat}")

        except ValueError:
            print("Erreur : Entrer des nombres valides.")
        except Exception as e:
            print(f"Erreur : {e}")

calculate()
