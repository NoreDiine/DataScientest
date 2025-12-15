def countVoyelles(string):
    
    voyelles= "aeiouyAEIOUY"

    conter = 0

    for caractere in string:
            if caractere in voyelles:
                conter += 1

    return conter

if __name__ == "__main__":
     

    text = "Noureddine"
    print(f" le nombre de voyelles sur {text} est {countVoyelles(text)}")