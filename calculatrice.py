import re

def calculate():
    print("Tapez un calcul")

    def decompose(calcul):#Parse calcul
        pat = re.findall(r'\d+|[+\-*/^]', calcul)
        return pat

    def ordre(pat): #Just left to right for start 
        result = float(pat[0])

        for i in range (1, len(pat), 2):
            operator = pat[i]
            next_num = float(pat[i+1])

            if operator == '+':
                result += next_num
            elif operator == '-':
                result -= next_num
            elif operator == '*':
                result *= next_num
            elif operator == '/':
                if next_num == 0:
                    print("Division par 0 impossible.")
                result /= next_num
            elif operator == '^':
                result **= next_num
            else:
                print(f"Opérateur non valide")

        return result
    



    while True:
        enter = input(">> ")

        try:
           calcul = decompose(enter)
           resultat = ordre(calcul)
           print(f"Résultat : {resultat}")
        except ValueError:
            print(f"Valeur incorrect")

calculate()
