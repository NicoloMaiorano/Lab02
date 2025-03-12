from parola import Parola

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

        parole = []
        diz = open("dictionary.txt", "r")

        #riempo il dizionario scorrendo tutto il file di testo
        for l in diz:
            l.strip("\n")
            l = l.split(" ")
            p = Parola(l[0])

            for i in range(1, len(l)):
                p.aggiungiTraduzione(l[i])

            parole.append(p)

        #divido la frase in input
        x = entry.split(" ")

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
            for l in parole:
                #se trovo la parola aliena già inserita
                if l.parola == x[0]:
                    #scorro le traduzioni già presenti per vedere che non ci sia già la traduzione che voglio inserire
                    for traduz in l.traduzioni:
                        for y in x:
                            if traduz == y:
                                print("LA TRADUZIONE ESISTE GIA")
                                trovato = 1
                                break

                    if trovato == 0:
                        for y in range(1, len(x)):
                            l.aggiungiTraduzione(x[y])
                        print("Traduzione aggiornata correttamente")
                        trovato = 1

            if trovato == 0:
                p = Parola("\n" + x[0])
                for i in range(1, len(x)):
                    p.aggiungiTraduzione(x[i])
                parole.append(p)
                print("Traduzione aggiunta correttamente!")

            diz.close()
            riscrivi = open("dictionary.txt", "w")
            for l in parole:
                mystr = l.parola
                for n in l.traduzioni:
                    mystr = mystr + " " + n
                mystr = mystr
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

        query.strip("\n")
        entry = list(query)

        c = 0

        for l in entry:
            if l == "?":
                c = c+1

        if c==0:
            self.handleTranslate(query)
        elif c==1:
            diz = open("dictionary.txt", "r")
            dict={}
            for p in diz:
                if p != "":
                    p.strip("\n")
                    p = p.split(" ")
                    p[0] = list(p[0])

                    i =0
                    for d in range (len(p[0])):
                        if len(p[0]) == len(entry):
                            if p[0][d] == entry[d]:
                                i=i+1
                    if i == (len(entry)-1):
                        dict[str(p[0])] = []
                        for n in range(len(p)):
                            if n > 0:
                                dict[str(p[0])].append(p[n].strip("\n"))


            if len(dict) == 0:
                print("Impossibile trovare una traduzione per questo input!")
            elif len(dict) == 1:
                print("E' stata trovata una sola corrispondenza: ")
                for l in dict:
                    print(dict[l])
            else:
                print("Sono state trovate le seguenti corrispondenze: ")
                for l in dict:
                    print(l)
        else:
            print("ERRORE, CI PUO' ESSERE SOLO UN ? NELLA PAROLA!")

    def printDizionario(self):

        diz = open("dictionary.txt", "r")

        for l in diz:
            print(l)