import translator as tr

t = tr.Translator("dictionary.txt")

txtIn= "aaa"

while(txtIn != "5"):

    t.printMenu()
    txtIn = input("Inserire il numero del menu:")

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
            mystr= input("Ok, quale parola devo cercare? ").lower()
            t.handleWildCard(mystr)
        case "4":
            print("Ok, stampo tutto il dizionario: ")
            t.printDizionario()
        case "5":
            print("Ok, arrivederci!")
        case _:
            print("ERRORE! INPUT NON VALIDO!!")