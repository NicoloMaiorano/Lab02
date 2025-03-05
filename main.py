import translator as tr

t = tr.Translator("dictionary.txt")

txtIn= "aaa"
while(txtIn != "5"):

    t.printMenu()

    txtIn = input("Inserire il numero del menu:")

    # Add input control here!

    match txtIn:
        case "1":
            parolaAliena = input("Ok, quale parola devo aggiungere? ").lower()
            traduzione = input("Qual è la sua traduzione? ").lower()
            mystr = parolaAliena + " " + traduzione
            t.handleAdd(mystr)

        case "2":
            mystr = input("Ok, quale traduzione vuoi cercare? ").lower()
            t.handleTranslate(mystr)

        case "3":
            print("Ok, quale parola devo cercare? ")
        case "4":
            print("Ok, stampo tutto il dizionario: ")
        case "5":
            print("Ok, arrivederci!")
        case _:
            print("ERRORE! INPUT NON VALIDO!!")