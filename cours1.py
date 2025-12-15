def sayHi(name) :
    return f"Hiiii {name} !!"


#fonction pour calculer a + b
def calculate(a,b):
    return a + b


# block d'exécution
if __name__ == "__main__":

    myName = "X"
    print(sayHi(myName))

    result = calculate(10,5)

    print(f"la somee des deux chiffre est : {result}")