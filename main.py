from sensore import *
from satellite import *

def main() -> None:
    # Creazione dei sensori
    sensore_temperatura = Sensore("S1", "Temperatura", "°C", 50.0)
    sensore_pressione = Sensore("S2", "Pressione", "Pa", 200000.0)
    sensore_umidita = Sensore("S3", "Umidità", "%", 80.0)

    # Creazione del satellite
    satellite = Satellite("Sat-1")

    # Aggiunta dei sensori al satellite
    satellite.aggiungi_sensore(sensore_temperatura)
    satellite.aggiungi_sensore(sensore_pressione)
    satellite.aggiungi_sensore(sensore_umidita)

    # Aggiunta delle letture
    satellite.aggiungi_lettura("S1", 45.0)  # Temperatura OK
    satellite.aggiungi_lettura("S2", 210000.0)  # Pressione in allarme
    satellite.aggiungi_lettura("S3", 75.0)  # Umidità OK

    # Stampa del riepilogo delle letture
    satellite.riepilogo()

if __name__ == "__main__":
    main()