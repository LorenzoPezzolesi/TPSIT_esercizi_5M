import re
class EsprReg:
    
    def __init__ (self,espressione_regolare:str):
        self.espressione_regolare=espressione_regolare

    def mio_match(self, stringa:str):
        return re.fullmatch(self.espressione_regolare, stringa)

def main():
    espressione = EsprReg(input("Inserisci un'espressione regolare: ")) 
    stringa = input("Inserisci una stringa da testare: ")
    if espressione.mio_match(stringa):
        print("La stringa corrisponde all'espressione regolare.")
    else:
        print("La stringa NON corrisponde all'espressione regolare.")
    
if __name__ == "__main__":
    main()



#import re
#
#class EsprReg:
#    """Semplice validatore regex: compila il pattern e può eseguire fullmatch o match."""
#
#    def __init__(self, espressione_regolare: str = "") -> None:
#        self._pattern_str = ""
#        self._compiled = None
#        if espressione_regolare:
#            self.set_pattern(espressione_regolare)
#
#    def set_pattern(self, pattern: str) -> None:
#        """Compila e memorizza il pattern; solleva ValueError se non valido."""
#        try:
#            self._compiled = re.compile(pattern)
#            self._pattern_str = pattern
#        except re.error as e:
#            raise ValueError(f"Pattern non valido: {e}") from e
#
#    def mio_match(self, stringa: str, full: bool = True) -> bool:
#        """
#        Esegue il test e restituisce True/False.
#        - full=True : usa fullmatch (intera stringa)
#        - full=False: usa match (dall'inizio)
#        """
#        if not self._compiled:
#            raise ValueError("Pattern non impostato. Chiamare set_pattern() prima.")
#        m = self._compiled.fullmatch(stringa) if full else self._compiled.match(stringa)
#        return bool(m)
#
#    def validate_and_print(self, stringa: str, full: bool = True) -> None:
#        """Stampa 'match' o 'mismatch' come richiesto dall'esercizio."""
#        print("match" if self.mio_match(stringa, full=full) else "mismatch")
#
#
#def main():
#    try:
#        pattern = input("Inserisci un'espressione regolare: ")
#        validator = EsprReg(pattern)
#    except ValueError as e:
#        print(e)
#        return
#
#    stringa = input("Inserisci una stringa da testare: ")
#    modo = input("Match completo? (s/N): ").strip().lower() == "s"
#    validator.validate_and_print(stringa, full=modo)
#
#
#if __name__ == "__main__":
#    main()
## ...existing code...