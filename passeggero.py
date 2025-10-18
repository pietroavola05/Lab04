class Passeggero:
    def __init__(self, riga):
        #definisco gli attributi del passeggero
        self._codicePasseggero = riga[0]
        self._nomePasseggero = riga[1]
        self._cognomePasseggero = riga[2]
        self.cabinaAssegnata = None

    def __str__(self):
        #stampo due casi diversi a seconda che il passeggero ha già una cabina assegnata o no
        if self.cabinaAssegnata is not None:
            return f"ID: {self._codicePasseggero:<6} | Nome: {self._nomePasseggero:<12} | Cognome: {self._cognomePasseggero:<15} | Cabina: {self.cabinaAssegnata}"
        else:
            return f"ID: {self._codicePasseggero:<6} | Nome: {self._nomePasseggero:<12} | Cognome: {self._cognomePasseggero:<15}"

    def __eq__(self, other):
        #questa funzione mi sta dicendo che confrontare due oggetti di tipo Passeggero vuol dire confrontarli per il codice univoco e per il nome
        if isinstance(other, Passeggero):
            return self._codicePasseggero == other._codicePasseggero and self._nomePasseggero == other._nomePasseggero
        else:
            return False

    def __repr__(self):
        return (f"{type(self).__name__}"
                f"CodicePasseggero: {self._codicePasseggero}"
                f"NomePasseggero: {self._nomePasseggero}"
                f"CognomePasseggero: {self._cognomePasseggero}"
                f"CabinaAssegnata: {self.cabinaAssegnata}")
