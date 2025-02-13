# modules influx et datetime
import influxdb_client,time
from influxdb_client import InfluxDBClient, Point, WritePrecision
#  permet de synchroniser les données
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime
from connexion import connexion as influxConnexion
#generation des trames par nombres aléatoires
import random as rand

def generate_trame_data():
    global time_status_updated
    # global status

    # generation des trames par nombres aléatoires
    status = rand.randint(0, 5)
    current_time = None

    good_status = False

    while not good_status:
        if status in [0, 1]:
            print("Good status")
            good_status = True
        else:
            status = rand.randint(0, 5)
            print("Bad status - re-roll engaged")

    current_time = datetime.datetime.now().timestamp()
    time_taken = current_time-time_status_updated
    time_status_updated = current_time

    return status, time_taken

def check_corruption_status(status_to_check):
    if status_to_check > 1:
        print("The status is too high, please re-roll")
    elif status_to_check < 0:
        print("The status is too low, how did you do it?!")
    else:
        return status_to_check

def envoi_donnees_influxdb(Status, value, time_to_update):
    #  on essaye d'enregistrer les données dans la base de données si ça fonctionne codeajout=0 et affichage de Data sent to database :  {datetime.datetime.now()}
    try:
        # initilisation de la base de données
        bucket = "Interrupteur"

        #  schronisation des données
        write_api = client.write_api(write_options=SYNCHRONOUS)

        # Pour la valeur de status on envoie la valeur de status
        for value in range(Status):
            state = (
                Point("Status").field("Value", value)
            )
            counter = (
                Point("Compteur").field("Secondes", time_to_update)
            )
            write_api.write(bucket=bucket, org="IUTdebeziers", record=state)
            write_api.write(bucket=bucket, org="IUTdebeziers", record=counter)

        print(f"Data sent to database :  {datetime.datetime.now()}")
        return 0

    # sinon codeajout=1 et affichage de Error while sending data to database
    except:
        print("Error while sending data to database")
        return 1

### Last time status updated -> Is going to be updated when called
time_status_updated = datetime.datetime.now().timestamp() # As timestamp

# appel des fonctions


###  connexion à la base de données
INFLUXDB_TOKEN = "token"
INFLUXDB_ORG = "org"
INFLUXDB_PORT = "8086"
INFLUXDB_URL = f"http://localhost:{INFLUXDB_PORT}"

client, connexion_status = influxConnexion(INFLUXDB_URL, INFLUXDB_ORG, INFLUXDB_TOKEN)

#### Tests
new_status, time_to_update = generate_trame_data()

try:
    for i in range(0, 20):
        # generate_trame_data()
        check_corruption_status(new_status)
        time_to_update = float(f"{time_to_update:.2f}")
        envoi_donnees_influxdb(new_status, new_status, time_to_update)
        print(f"Status updated to {new_status} in {time_to_update:.2f}s at {datetime.datetime.fromtimestamp(time_status_updated)}")
        time.sleep(3)
except KeyboardInterrupt:
    print("Program has stopped")
    exit(0)
