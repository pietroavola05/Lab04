class Cabina():
    def __init__(self, riga):
        self.codiceCabina = riga[0]
        self.numeroLetti = int(riga[1])
        self.ponte= int(riga[2])
        self.prezzo = int(riga[3])
        self.disponibile = True #True se è disponibile. False se non è disponibile

    def __str__(self):
        #faccio due casi perchè i print saranno diversi nel caso in cui la cabina è disponibile oppure no
        if self.disponibile == True:
            return f"{self.codiceCabina}: Standard | {self.numeroLetti} letti - {self.ponte} - Prezzo {self.prezzo:.2f}€ - Disponibile"
        else:
            return f"{self.codiceCabina}: Standard | {self.numeroLetti} letti - {self.ponte} - Prezzo {self.prezzo:.2f}€"

    def __repr__(self):
        #considero i due casi anche per il repr
        if self.disponibile:
            return (f"<{type(self).__name__} {self.codiceCabina}: "
                    f"{self.numeroLetti} letti - Ponte {self.ponte} - Prezzo {self.prezzo:.2f}€ - Disponibile>")
        else:
            return (f"<{type(self).__name__} {self.codiceCabina}: "
                    f"{self.numeroLetti} letti - Ponte {self.ponte} - Prezzo {self.prezzo:.2f}€ - Occupata>")

    def __eq__(self, other):
        #questa funzione mi dice che confrontare due oggetti di tipo Cabina vuol dire confrontare i loro codici univoci
        if isinstance(other, Cabina): #se sono uguali ritorna una condzione vera
            return self.codiceCabina == other.codiceCabina
        else: #altrimenti ritorna una condizione falsa
            return False


class CabinaAnimali(Cabina):
    def __init__(self, riga):
        super().__init__(riga)
        self.animaliOspitabili = int(riga[4])
        self.prezzo = int(riga[3])*(1 + 0.10 * self.animaliOspitabili) #override cioè sto modificando un solo attributo della classe padre che ho ereditato perchè il figlio ha un valore diverso diverso dal padre

    def __str__(self):
        #printo considerando il caso in cui è disponibile ed il caso in cui non è disponibile
        if self.disponibile == True:
            return f"{self.codiceCabina}: Animali | {self.numeroLetti} letti - {self.ponte} - Prezzo {self.prezzo:.2f}€ - Max animali: {self.animaliOspitabili} – Disponibile"
        else:
            return f"{self.codiceCabina}: Animali | {self.numeroLetti} letti - {self.ponte} - Prezzo {self.prezzo:.2f}€ - Max animali: {self.animaliOspitabili}"

    def __repr__(self):
        #considero i due casi anche per il repr
        if self.disponibile:
            return (f"<{type(self).__name__} {self.codiceCabina}: "
                    f"{self.numeroLetti} letti - Ponte {self.ponte} - Prezzo {self.prezzo:.2f}€ - Max animali: {self.animaliOspitabili} - Disponibile>")
        else:
            return (f"<{type(self).__name__} {self.codiceCabina}:"
                    f" {self.numeroLetti} letti - Ponte {self.ponte} - Prezzo {self.prezzo:.2f}€ - Max animali: {self.animaliOspitabili} - Occupata>")


class CabinaDeluxe(Cabina):
    def __init__(self, riga):
        super().__init__(riga)
        self.prezzo = int(riga[3]) * 1.20 #override
        self.tipologiaDeluxe = riga[4]

    def __str__(self):
        # printo considerando il caso in cui è disponibile ed il caso in cui non è disponibile
        if self.disponibile == True:
            return f"{self.codiceCabina}: Deluxe {self.tipologiaDeluxe} | {self.numeroLetti} letti - {self.ponte} - Prezzo {self.prezzo:.2f}€ - Disponibile"
        else:
            return f"{self.codiceCabina}: Deluxe {self.tipologiaDeluxe} | {self.numeroLetti} letti - {self.ponte} - Prezzo {self.prezzo:.2f}€"

    def __repr__(self):
        #considero i due casi anche per il repr
        if self.disponibile:
            return (f"<{type(self).__name__} {self.codiceCabina}:"
                    f" {self.tipologiaDeluxe} | {self.numeroLetti} letti - Ponte {self.ponte} - Prezzo {self.prezzo:.2f}€ - Disponibile>")
        else:
            return (f"<{type(self).__name__} {self.codiceCabina}: "
                    f"{self.tipologiaDeluxe} | {self.numeroLetti} letti - Ponte {self.ponte} - Prezzo {self.prezzo:.2f}€ - Occupata>")