## import des librairies
import interaction_database

## iniatialisation des variables
tab_ticket_distrubuer = [10000]


def main(ID_RFID,nbr_ticket) :
    ticket_genere = []
    for i in range (int(nbr_ticket)) :
        num_ticker_position = len(tab_ticket_distrubuer)
        num_ticket = tab_ticket_distrubuer[num_ticker_position - 1]
        tab_ticket_distrubuer.append(tombola(num_ticket))
        ticket_genere.append(tombola(num_ticket))
    print (tab_ticket_distrubuer)
    print (ticket_genere)
    for ticket in ticket_genere :
        print (ticket)
        envo_ticker_to_datbase(ID_RFID, ticket)
    

def tombola(num_ticket) : 
    num_ticket += 1
    return num_ticket


def envo_ticker_to_datbase(ID_RFID, num_tiket):
    print(ID_RFID, num_tiket)
    interaction_database.ajout_profil_ticket_tombola(ID_RFID, num_tiket)

    ...
