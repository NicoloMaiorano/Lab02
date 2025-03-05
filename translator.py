class Translator:
    def __init__(self, dict):
        self.diz = open(dict, "r+")

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

        trovato = 0
        x = entry.split(" ")

        y = []

        if x[0].isalpha() and x[1].isalpha():
            for l in self.diz:
                l.strip("\n")
                l = l.split(" ")
                if str(l[0]) == str(x[0]):
                    print("ERRORE! LA PAROLA ESISTE GIA!")
                    trovato = 1
                    break

            if trovato == 0:
                entry = "\n" + entry
                self.diz.write(entry)
                print("Parola aggiunta correttamente!")
        else:
            print("LE PAROLE POSSONO SOLO CONTENERE LETTERE")

    def handleTranslate(self, query):
        trovato = 0

        if query.isalpha():
            for l in self.diz:
                l.strip("\n")
                l = l.split(" ")
                if str(l[0]) == str(query):
                    print("La parola che hai inserito significa: " + str(l[1]))
                    trovato = 1
                    break

            if trovato == 0:
                print("LA PAROLA NON E' PRESENTE NEL DIZIONARIO!")
        else:
            print("LA PAROLA PUO SOLO CONTENERE LETTERE")
    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass