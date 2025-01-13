def calculate():
    print("Bienvenue sur la calculatrice")
    print("Entrer un calcul")

    while True:
        enter = input(">> ")

        try:
            elements = list(enter)
            if len(elements) != 3:
                print("Veuiller saisir un calcul sous forme 1+1")

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
                        print("Division par 0 impossible")
                        continue
                    resultat = nombre1 / nombre2
                    
            print(f"Résultat : {resultat}")
        
        except ValueError:
            print("Erreur : Assurer vous d'entrer un nombre valide")
        except Exception as e:
            print(f"Erreur : {e}")

calculate()