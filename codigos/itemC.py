#Análisis de formato
#Scripts utilizado:


import json
import datetime

try:
    with open('/home/devasc/labs/devnet-src/parsing/myfile.json') as f:
        json_file = json.load(f)

    token = json_file["access_token"]
    expiration_time = datetime.datetime.now() + datetime.timedelta(seconds=json_file["expires_in"])
    time_left = expiration_time - datetime.datetime.now()

    print("Token obtenido con éxito: {}".format(token))
    print("Tiempo restante antes de que expire el token: {}".format(time_left))

except FileNotFoundError:
    print("No se encontró el archivo especificado.")
except json.JSONDecodeError:
    print("Error al decodificar el archivo JSON.")
except KeyError:

