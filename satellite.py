from sensore import *


class Satellite:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.sensori = {}
        self.letture = []

    def aggiungi_sensore(self, sensore: Sensore) -> None:
        self.sensori[sensore.codice] = sensore

    def aggiungi_lettura(self, codice_sensore: str, valore: float) -> None:
        sensore = self.sensori[codice_sensore]
        self.letture.append({
            "sensore": codice_sensore,
            "grandezza": sensore.grandezza,
            "valore": valore,
            "unita": sensore.unita,
            "allarme": valore > sensore.soglia_massima,
        })

    def letture_in_allarme(self) -> list[dict]:
        inAllarme = []
        for lettura in self.letture:
            if lettura["allarme"]:
                inAllarme.append(lettura)
        return inAllarme

    def riepilogo(self) -> None:
        print(f"Riepilogo letture per il satellite {self.nome}:")
        for lettura in self.letture:
            if lettura["allarme"]:
                allarme = "ALLARME"
            else:
                allarme = "OK"
            print(f"Sensore: {lettura['sensore']}, Grandezza: {lettura['grandezza']}, Valore: {lettura['valore']} {lettura['unita']}, Allarme: {allarme}")

    