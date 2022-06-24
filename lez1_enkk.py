#Creare uno script di python che simuli il login ad un sito di casino.

#si chieda all'utente: nome, cognome, ed età
#si verifichi che il nome e il cognome siano più lunghi di un carattere e che l'età sia maggiore o uguale di 18 anni
#se tutto è corretto stampare una string di conferma altrimenti comunicare l'errore all'utente
#si consideri che l'utente fornirà sempre dati di tipo corretto
#BONUS: stampare resoconto dei dati assicurandosi che nome e cognome inizino con la maiuscola

print("Per accedere al sito è necessario verificare i tuoi dati.")
nome = input("Nome: ")
lnome = len(nome)
cognome = input("Cognome: ")
lcognome = len(cognome)
eta = input("Età: ")
inteta = int(eta)

if lnome > 1 and lcognome > 1 and inteta >= 18 :
    print("I dati inseriti sono validi.")
    print(nome.capitalize())
    print(cognome.capitalize())
    print(eta)
    
else :
    print("Attenzione, i dati da te inseriti non sono validi.")





