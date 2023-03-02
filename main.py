import telegram
import datetime
import time

# Aggiungi il tuo token del bot qui
bot = telegram.Bot("INSERISCI IL TUO TOKEN QUI")

# Aggiungi qui l'ID del gruppo in cui vuoi fare le domande
group_id = "INSERISCI L'ID DEL GRUPPO QUI"

# Aggiungi qui le domande che vuoi fare
domande = [
    "Qual è il tuo cibo preferito?",
    "Hai mai viaggiato all'estero? Dove?",
    "Qual è il tuo film preferito?",
    "Qual è la tua canzone preferita?",
    "Hai mai fatto uno sport? Quale?",
]

# Funzione che invia una domanda casuale nel gruppo
def invia_domanda():
    domanda = random.choice(domande)
    bot.send_message(chat_id=group_id, text=domanda)

# Ciclo principale del bot
while True:
    # Controlla se oggi è domenica
    oggi = datetime.datetime.today()
    if oggi.weekday() == 6: # Domenica = 6
        invia_domanda()
    # Attendi un giorno prima di controllare di nuovo
    time.sleep(24*60*60)
