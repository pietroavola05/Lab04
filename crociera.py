from logging import raiseExceptions
from cabina import Cabina, CabinaDeluxe, CabinaAnimali
from passeggero import Passeggero
#import operator (nella versione precedente ho fatto l'ordinamento con key=operator.attrgetter('prezzo').
# In questa versione è sostituito da un sorted poichè cabina ha il metodo lt
import csv

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nomeCrociera = nome
        self._listaPasseggeri = []
        self._listaCabine = []

    @property
    def nomeCrociera(self):
        return self._nomeCrociera

    @nomeCrociera.setter
    #faccio un controllo perchè l'utente potrebbe inserire un nome di crociera numerico
    def nomeCrociera(self, nome):
        print("Stai modificando il nome della Crociera")
        #faccio un controllo per vedere se l'utente ha inserito dei caratteri o simboli speciali tipo @!#* che nnon vanno bene per il nome della crociera'
        nome_valido = True
        for carattere in nome:
            if not (carattere.isalnum() or carattere.isspace()):
                nome_valido = False
        if nome_valido:
                self._nomeCrociera = nome.strip()  # tolgo eventuali spazi all'inizio/fine
                print(f"\nNuovo nome impostato in: {self._nomeCrociera}")
        else:
            raise Exception("Nome non valido. Usa solo lettere, numeri e spazi.")


    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            file = open(file_path, "r")
            file_content = csv.reader(file)
            for riga in file_content:
                #capisco se la riga letta indica unca cabina o una persona
                prova_codice_univoco = riga[0] #prova_codice_univoco mi prende il primo elemento di una lista che sarà una stringa
                # di questa stringa prendo il primo elemento e mi chiedo se sia C o P
                if prova_codice_univoco[0] == "C": #caso Cabina
                    #mi chiedo se Cabina Standard, Deluxe o Animali
                    try:
                        int(riga[4]) #se riesco a convertire il 5 elemento in un numero intero
                        cabina = CabinaAnimali(riga) #creo una cabina Animali
                        self._listaCabine.append(cabina)  #aggiungo la cabina alla lista delle cabine del sistema
                    except:
                        if len(riga) == 4: #sono sempre nel caso Cabina, ma non ho il quinto elemento: quindi ho una cabina Standard
                            cabina = Cabina(riga) #creo una cabina Standard
                            self._listaCabine.append(cabina) #aggiungo la cabina alla lista delle cabine del sistema
                        else:
                            cabina = CabinaDeluxe(riga) #creo una cabina deluxe
                            self._listaCabine.append(cabina)  #aggiungo la cabina alla lista delle cabine del sistema
                elif prova_codice_univoco[0] == "P": #il codice univoco inizia per P ed è dunque si tratta di un passeggero
                    passeggero = Passeggero(riga)  #creo l'oggetto passeggero
                    self._listaPasseggeri.append(passeggero)  #lo aggiungo alla lista passeggeri
            file.close()
        except:
            raise Exception("Problemi con il file inserito")


    def trova_passeggero(self, codice_passeggero):
        """Cerca un passeggero nella lista tramite il codice"""
        for passeggero in self._listaPasseggeri:
            if passeggero._codicePasseggero == codice_passeggero:
                return passeggero
        # Se arrivo qui, non ho trovato il passeggero
        raise Exception("Passeggero non trovato")


    def trova_cabina(self, codice_cabina):
        """Cerca una cabina nella lista tramite il codice"""
        for cabina in self._listaCabine:
            if cabina.codiceCabina == codice_cabina:
                return cabina
        # Se non trovo la cabina, sollevo eccezione
        raise Exception("Cabina non trovata")


    def controlliPreAssegnazione(self, passeggero, cabina):
        """Esegue i controlli prima di assegnare una cabina a un passeggero"""
        #controllo se il passeggero ha già una cabina
        if passeggero.cabinaAssegnata is not None: #vuol dire che il campo cabina ha un codice cabina
            # se è già assegnato a quella cabina, lo segnalo ma non è un errore
            if passeggero.cabinaAssegnata == cabina.codiceCabina:
                print(f"Il passeggero {passeggero._codicePasseggero} è già assegnato alla cabina {cabina.codiceCabina}")
                return False
            else:
                # altrimenti ha già un’altra cabina, non posso assegnarne un’altra
                raise Exception(f"Il passeggero {passeggero._codicePasseggero} ha già una cabina assegnata ({passeggero.cabinaAssegnata})")

        # controllo se la cabina è disponibile
        if not cabina.disponibile:
            raise Exception(f"La cabina {cabina.codiceCabina} non è disponibile")

        # se arrivo qui, tutti i controlli sono superati
        print("Controlli superati: si può procedere con l'assegnazione.")
        return True

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        #cerco passeggero e cabina. Mi creo due funzione apposite per miglior ordine
        passeggero = self.trova_passeggero(codice_passeggero)
        cabina = self.trova_cabina(codice_cabina)

        #faccio i controlli prima dell’assegnazione in una funzione a parte
        if not self.controlliPreAssegnazione(passeggero, cabina): #controlli pre assegnazione restituisce True o False(raise Exception)
            return  # Non serve procedere (già assegnato)

        #se tutto ok, procedo con l’assegnazione
        passeggero.cabinaAssegnata = cabina.codiceCabina
        cabina.disponibile = False
        print(f"Assegnazione completata: {passeggero._nomePasseggero} {passeggero._cognomePasseggero}| {cabina.codiceCabina}")


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        #lista_cabine_ordinate = sorted(self._listaCabine, key=operator.attrgetter('prezzo'))

        lista_cabine_ordinate = sorted(self._listaCabine) #richiama il metodo __lt__ delle cabine (dichiarata nel padre)
        return lista_cabine_ordinate


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for passeggero in self._listaPasseggeri:
            print(passeggero)

