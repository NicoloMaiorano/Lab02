class Translator:
    def __init__(self, dict):
        pass

    def printMenu(self):
        print("------------------------------")
        print("Transalator Alien-Italian")
        print("------------------------------")
        print("1- Aggiungi nuova parola")
        print("2- Cerca una traduzione")
        print("3- Cerca con wildcard")
        print("4- Stampa tutto il Dizionario")
        print("5- Exit")
        print("------------------------------")
        pass


    def handleAdd(self, entry):
        #dichiaro il mio dizionario vuoto che andrò a riempire con ciò che c'è scritto nel file di testo
        thisdict = {}
        diz = open("dictionary.txt", "r")
        #riempo il dizionario scorrendo tutto il file di testo
        for l in diz:
            l.strip("\n")
            l = l.split(" ")
            thisdict[l[0]] = []
            for i in range(len(l)):
                if i>0:
                    thisdict[l[0]].append(l[i].strip("\n"))

        #divido la frase in input
        x = entry.split(" ")
        print("STAMPO TUTTO IL DIZIONARIO")
        print(thisdict)
        #variabile bool per controllare se tutte le parole inserite hanno all'interno solo lettere
        controlloLettere = True

        #ciclo che scorre tutte le parole inserite per controllare se contengono solo lettere
        for p in x:
            if p.isalpha():
                pass
            else:
                controlloLettere = False

        #se il controllo ortografico è andato a buon fine allora posso svolgere il mio lavoro, altrimenti passo nell'else
        #e segnalo l'errore di input

        if controlloLettere == True:
            #variabille per sapere se la parola è già presente all'interno del dizionario o se devo aggiungerla al fondo
            trovato = 0

            #scorro il dizionario per cercare la parola aliena che mi interessa
            for l in thisdict:
                #se trovo la parola aliena già inserita
                if l == x[0]:
                    #scorro le traduzioni già presenti per vedere che non ci sia già la traduzione che voglio inserire
                    for traduz in thisdict[l]:
                        for y in x:
                            if traduz == y:
                                print("LA TRADUZIONE ESISTE GIA")
                                trovato = 1
                                break

                    if trovato == 0:
                        for y in range(len(x)):
                            if y >0:
                                thisdict[l].append(x[y])
                        print("Traduzione aggiornata correttamente")
                        trovato = 1

            if trovato == 0:
                thisdict[x[0]] = []
                for i in range(len(x)):
                    if i >0:
                        thisdict[x[0]].append(x[i])
                print("Traduzione aggiunta correttamente!")

            diz.close()
            riscrivi = open("dictionary.txt", "w")
            for l in thisdict:
                mystr = l
                for n in thisdict[l]:
                    mystr = mystr + " " + n
                mystr = mystr + "\n"
                riscrivi.write(mystr)
            riscrivi.close()
        else:
            print("LE PAROLE POSSONO SOLO CONTENERE LETTERE")

    def handleTranslate(self, query):
        trovato = 0
        diz = open("dictionary.txt", "r")
        if query.isalpha():
            print("La parola soddisfa i criteri")
            for l in diz:
                l.strip("\n")
                l = l.split(" ")
                if str(l[0]) == str(query):
                    mystr = "La parola che hai inserito significa:"
                    for i in range(len(l)):
                        if i >0:
                            mystr = mystr +" "+ str(l[i])
                    print(mystr)
                    trovato = 1
                    break

            if trovato == 0:
                print("LA PAROLA NON E' PRESENTE NEL DIZIONARIO!")
        else:
            print("LA PAROLA PUO SOLO CONTENERE LETTERE")
    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass

    def printDizionario(self):

        diz = open("dictionary.txt", "r")

        for l in diz:
            print(l)