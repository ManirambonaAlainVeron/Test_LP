#fuction to correct paranthesis error
def corriger_erreur(input_file, output_file):
    parenthese_ouverte = False
    nombre_de_phrase = 0
    phrase_mal_orthographie = False
    nombre_phrase_mal_orthographie = 0
    caracteres_a_ajouter = 0
    index_parenthese_ouvrante = 0
    long_error = 7
    try:
        with open(input_file, 'r') as file : #open file in read mode
            text_a_corriger = file.read()
        for index, caractere in enumerate(text_a_corriger): #browse the file character by character, index by index
            if(caractere == "("):
                if(parenthese_ouverte == False):
                    parenthese_ouverte = True
                    index_parenthese_ouvrante = index+caracteres_a_ajouter
                else:
                    text_a_corriger = (text_a_corriger[:index+caracteres_a_ajouter]+
                    " !Error "+text_a_corriger[index+caracteres_a_ajouter+1:]
                    ) #replace error with !Error
                    caracteres_a_ajouter += long_error
                    phrase_mal_orthographie = True
            if(caractere == ")"):
                if(parenthese_ouverte == True):
                    parenthese_ouverte = False
                else:
                    text_a_corriger = (text_a_corriger[:index+caracteres_a_ajouter]+
                    " !Error "+text_a_corriger[index+caracteres_a_ajouter+1:]
                    ) #replace error with !Error
                    caracteres_a_ajouter += long_error
                    phrase_mal_orthographie = True
            if (caractere == "."):
                nombre_de_phrase += 1
                if(parenthese_ouverte == True):
                    text_a_corriger = (text_a_corriger[:index_parenthese_ouvrante]+
                    " !Error "+text_a_corriger[index_parenthese_ouvrante+1:]
                    ) #replace error with !Error
                    caracteres_a_ajouter += long_error
                    phrase_mal_orthographie = True
                    parenthese_ouverte = False
                if phrase_mal_orthographie == True:
                    nombre_phrase_mal_orthographie += 1
                phrase_mal_orthographie = False

        
        with open(output_file, 'w') as file: #open file in write mode
            # write in the file
            file.write("Nombre de phrases = "+str(nombre_de_phrase))
            file.write(" ")
            file.write("\nNombre de phrase mal orthographie = "+str(nombre_phrase_mal_orthographie))
            file.write(" ")
            file.write("\n"+text_a_corriger)
    except FileNotFoundError:
        print("Le fichier à corriger est introuvable")


