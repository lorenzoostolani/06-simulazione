# Simulazione 1

## Domande scritte

Per ciascuna di esse, rispondere in modo sintetico ma motivato alle domande.

1. **Repository locale:** descrivi working tree, staging area e repository. In quale area si trovano le modifiche dopo `git add` e dopo `git commit`?
2. **Branch e integrazione:** spiega la differenza tra `git merge` e `git fetch`. Quando si usa `git stash`?
3. **GitHub e collaborazione:** descrivi il flusso Issue -> branch -> commit -> push -> Pull Request -> review -> merge.

## Simulazione 1 - Telemetria di un CubeSat

Il team realizza un programma Python da terminale per registrare le letture dei sensori di un CubeSat e segnalare i valori oltre soglia. La soluzione finale deve essere divisa in tre file nella stessa cartella:

- `sensore.py`: definisce la classe `Sensore`;
- `satellite.py`: definisce la classe `Satellite` e gestisce sensori e letture;
- `main.py`: contiene i dati di esempio e avvia la dimostrazione.

### Modelli richiesti

In `sensore.py`, la classe `Sensore` rappresenta un sensore con:

- `codice: str`, identificativo univoco;
- `grandezza: str`, per esempio `"temperatura"` o `"tensione batteria"`;
- `unita: str`, per esempio `"C"`, `"V"` o `"deg/s"`;
- `soglia_massima: float`.

Firma del costruttore: `__init__(self, codice: str, grandezza: str, unita: str, soglia_massima: float) -> None`.

In `satellite.py`, la classe `Satellite` conserva i sensori in un dizionario indicizzato per codice e le letture in una lista. Ogni lettura è un dizionario con le chiavi `sensore`, `grandezza`, `valore`, `unita` e `allarme`; i valori sono rispettivamente codice (`str`), grandezza (`str`), misura numerica (`float`), unità (`str`) e indicatore di allarme (`bool`).

Implementare le seguenti interfacce:

| Metodo | Parametri oltre a `self` | Tipo di ritorno e comportamento |
|---|---|---|
| `aggiungi_sensore` | `sensore: Sensore` | `None`; aggiunge il sensore, solleva `ValueError` se il codice è già presente |
| `registra_lettura` | `codice_sensore: str`, `valore: float` | `None`; salva la misura e calcola `allarme` confrontandola con la soglia; solleva `KeyError` se il codice non è registrato |
| `letture_in_allarme` | nessuno | `list[dict]`; restituisce una nuova lista contenente solo le letture oltre soglia |
| `riepilogo` | nessuno | `None`; stampa il satellite e tutte le letture, marcando ciascuna come `OK` o `ALLARME` |

Il confronto è strettamente `valore > soglia_massima`: una misura uguale alla soglia non è in allarme. `registra_lettura` conserva la lettura e il risultato del confronto; `letture_in_allarme` non deve modificare la lista originale.

In `main.py`, creare il satellite `CubeSat Aurora`, almeno tre sensori e più letture per sensori diversi. Includere almeno una lettura sotto soglia, una uguale alla soglia e una sopra soglia; stampare il riepilogo e la lista degli allarmi. Provare inoltre il caso di codice sensore inesistente e mostrare un messaggio comprensibile senza interrompere il programma.

### Branch, feature e responsabilità

Usare `main` come branch principale. Aprire una Issue per ciascuna feature, assegnarla allo studente responsabile e inserire nella Pull Request il riferimento alla Issue (per esempio `Closes #1`). Ogni branch parte da `main` aggiornato e viene integrato tramite Pull Request dopo review.

| Ordine | Branch | Responsabile | Feature/file | Criteri di completamento |
|---|---|---|---|---|
| 1 | `features/modello-sensore` | Studente A | `sensore.py` | Costruttore tipizzato e memorizzazione dei quattro dati del sensore; provarlo creando due sensori con unità diverse |
| 2 | `features/gestione-satellite` | Studente B | `satellite.py` | Dizionario di sensori e lista di letture; aggiunta senza duplicati; registrazione di letture e gestione del codice inesistente |
| 3 | `features/allarme-telemetria` | Studente B o C | `satellite.py` | Calcolo del flag allarme, filtro `letture_in_allarme()` e riepilogo stampato; provare valori sotto, uguali e sopra soglia |
| 4 | `features/main-telemetria` | Studente C | `main.py` | Istanziazione e collegamento delle classi, dati di esempio, output leggibile e prova dell'errore per codice sconosciuto |

L'ordine è intenzionale, in quanto la feature del satellite dipende dalla classe `Sensore`; le feature di allarme e del main partono da `main` dopo l'integrazione del branch precedente. Prima di creare ciascun branch, aggiornare `main` con `fetch` e `pull`. Dopo ogni Pull Request integrata, gli altri studenti aggiornano il proprio `main` e creano da quello il branch successivo. Non creare branch indipendenti da una versione vecchia di `main`.

Ogni studente deve fare almeno due commit e descrittivi sul proprio branch. Esempi possibili:

```text
feat: definisce il modello del sensore
feat: registra i sensori del satellite
feat: segnala letture oltre soglia
feat: aggiunge il programma dimostrativo
```

### Procedura Git e GitHub

1. Lo Studente C crea il repository remoto, lo clona e prepara un `README.md` con titolo e istruzioni di avvio. Crea e pubblica il branch principale (si può fare anche in altri modi, non per forza così):

   ```bash
   git checkout main
   git add README.md
   git diff --staged
   git commit -m "prepara il progetto di telemetria"
   git push -u origin main
   ```

2. Lo Studente A crea e pubblica il branch del modello:

   ```bash
   git switch main
   git fetch origin
   git pull origin main
   git switch -c features/modello-sensore
   ```

   Implementa `sensore.py`, prova la creazione di sensori, controlla `git status` e `git diff`, quindi crea almeno due commit. Pubblica il branch, apre una PR verso `main` e chiede la review:

   ```bash
   git push -u origin features/modello-sensore
   ```

3. Dopo il merge della prima PR, lo Studente B aggiorna `main` e crea `features/gestione-satellite`. Implementa e verifica `satellite.py`. Per provare lo stash, seguire l'esempio nella sezione successiva. Dopo aver recuperato il lavoro, completa almeno due commit, pubblica il branch e apre una PR.

4. Dopo il merge della PR del satellite, creare `features/allarme-telemetria` da `main` aggiornato. Completare filtro e riepilogo, verificare i tre casi di soglia e aprire una PR. La feature può essere sviluppata dallo Studente B o C, ma non contemporaneamente a un'altra modifica non integrata dello stesso file.

5. Dopo il merge degli allarmi, lo Studente C crea `features/main-telemetria`, aggiunge `main.py` e prova il programma completo. Pubblica il branch e apre la PR finale. Dopo il merge, ciascuno aggiorna `main` e verifica l'esecuzione dalla copia aggiornata.

Prima di ogni commit osservare le modifiche. Per esempio:

```bash
git status
git diff
git add sensore.py
git diff --staged
git commit -m "feat: definisce il modello del sensore"
git log --graph --oneline --all
```

Sostituire `sensore.py` e il messaggio di commit con il file e la feature effettivi. Non includere file estranei nello staging.

### Esempio pratico di `git stash`

Durante `features/gestione-satellite`, lo Studente B inizia una modifica locale non pronta alle istruzioni di avvio in `README.md`. Prima di passare temporaneamente a `main`, verifica cosa sta salvando e crea lo stash:

```bash
git status
git stash push -m "WIP: istruzioni di avvio"
git stash list
git switch main
git fetch origin
git pull origin main
```

Dopo il controllo su `main`, torna al branch che possiede il lavoro incompleto e recuperalo:

```bash
git switch features/gestione-satellite
git stash list
git stash pop
git status
git diff
```

`git stash pop` riapplica la modifica e rimuove la voce dallo stash se l'applicazione riesce. Per riapplicarla mantenendo la voce usare `git stash apply`. Se compaiono conflitti, risolverli nei file, controllare `git diff` e fare `git add` solo dopo aver verificato il risultato. Lo stash è locale: non è un commit e non viene pubblicato con `git push`.


Consegnare URL del repository.