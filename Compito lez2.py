#Compito 1
#Dichiarare due liste di numeri con cinque elementi ciascuna e creare una lista concatenata che le includa entrambe.

#BONUS: prendere gli elementi delle due liste dall'utente chiedendoli uno per uno

lista1 = []
lista2 = []

for i in range(5):
    n = int(input("Scrivi un numero della lista 1: "))
    lista1.append(n)

for i in range(5):
    n = int(input("Scrivi un numero della lista 2: "))
    lista2.append(n)

print(lista1)
print(lista2)

for i in lista2:
    lista1.append(i)

print(lista1)

#Compito 2
#Immaginiamo di dover creare un registro di utenti per un casinò.
# Creare uno script che chieda da terminale i dati di N utenti (N è una variabile)
# e salvare ogni utente in un dizionario.
# I dizionari relativi ad ogni utente devono essere contenuti in una lista.
# Il programma deve rifiutare una inserizione (e terminare) se il nickname di uno
# degli utenti è già presente nel sistema. Non terminare il programma usando
# la funzione exit() ma assicurarsi che sia il flow del programma a gestire
# questo caso.

#I dati dell'utente sono:

#Nickname
#Eta
#Gender (per semplicità solo M o F)
#Si dia per scontato che l'utente inserisca sempre dati coerenti
#(non sono da implementare i controlli di validità dei dati inseriti).

#Si cerchi di rendere l'interfaccia testuale il più comprensibile possibile,
# ad esempio, anziché chiedere semplicemente Inserire nickname si chieda
# Inserire nickname per account i-esimo dove i sarà naturalmente compreso fra 1 ed N.
# Aggiungere anche stampe quali Utente i-esimo inserito! e poi procedere con il prossimo.

#Terminato l'inserimento degli N utenti si stampi un resoconto.
# Alcuni esempi possono essere: la quantità di utenti maschi e femmine,
# il massimo, minimo e media di età, e la lunghezza media dei nickname.
# In python esistono funzioni built-in per fare queste cose:
# evitare di usarle e re-implementare il codice per trovare massimo, minimo e media.

#Si suggerisce di utilizzare le strutture di supporto adatte alla risoluzione
# del problema, come ad esempio liste temporanee.

print("Benvenuto nel sistema di registrazione utenti del casinò.")
n_user = int(input("Quanti utenti vuoi registrare? "))
userList = []
nickList = []

for i in range(n_user):
    nickname = input(
        "Inserire nickname per registrare l'account " + str(i+1) + ": ")

    while nickname in nickList:
        print("Nickname giá esistente!")
        nickname = input(
            "Inserire nickname per registrare l'account " + str(i+1) + ": ")

    nickList.append(nickname)

    age = int(input("Inserire età dell'account " + str(i+1) + ": "))
    gender = input("Inserire genere dell'account " +
                   str(i+1) + ": ").capitalize()

    user = {"nickname": nickname, "age": age, "gender": gender}
    userList.append(user)
    print(user)
    print("Utente " + str(i+1) + " inserito!")

print("Inserimento completato!")
print("Hai inserito " + str(len(userList)) + "account.")

tot = 0
max = 0
min = 1000
nMale = 0
nFemale = 0
totalNickLenght = 0
for user in userList:
    print(user["age"])
    tot += user['age']
    if user['age'] > max:
        max = user['age']
    if user['age'] < min:
        min = user['age']
    if user['gender'] == 'F':
        nFemale += 1
    if user['gender'] == 'M':
        nMale += 1
    totalNickLenght += len(user['nickname'])

print("Età media : " + str(tot/len(userList)))
print("Età minima: " + str(min))
print("Età massima: " + str(max))
print("Numero utenti donne: " + str(nFemale))
print("Numero utenti uomini: " + str(nMale))
print("Media lunghezza nickname: " + str(totalNickLenght/len(userList)))
