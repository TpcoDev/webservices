import json

from requests import Session

headers = {
    'accept': '*/*',
    'Content-Type': 'application/json',
    'charset': 'utf-8',
}

url_authenticate = 'http://localhost:8069/web/session/authenticate'

# Boddy para autenticar
data = {
	"jsonrpc":"2.0",
	"method":"call",
	"id":1,
	"params": {
		"login":"admin",
		"password":"1",
		"db":"helpdeskcompany2_odoo12_demo"
	}
	
}

url_ticket = 'http://localhost:8069/helpdesk_rest/private/ticket/'

# Parametros para hacer una busqueda en los tickets
params = {'name': 'a'}

# Json para crear un ticket
ticket = {
    "id_usercore": "122222-a",
    "rut": "1223444",
    "nombre": "Antonio Ruban",
    "id_usercore_tecnico": 1222,
    "cargo": "Especialista",
    "correo": "adre@tmail.com",
    "celular": "58544330",
    "id_usercore_tecnico": 2,
    "prioridad": 3,
    "tipoticket": "Pregunta",
    "sucursal": "ANTOFAGASTA",
    "empresa": "PCL",
    "numticket_UserCore": 11112,
    "asunto": "Ticket mejorado",
    "descripcion": "Este ticket esta mejor sin mi"
}

def main():
    s = Session()

    # Autenticarse, la session_id se guardara en las cookies  
    req = s.post(url_authenticate, headers=headers, data=json.dumps(data))
    print(req.status_code)
    print(req.json())
    

    # Listar los tickets, la session_id estara guardada en las cookies de la Session
    req = s.get(url_ticket, headers=headers, params=params)
    print(req.status_code)
    print(req.json())


    # Crear un ticket, la session_id estara guardada en las cookies de la Session
    req = s.post(url_ticket, headers=headers, data=json.dumps(ticket))
    print(req.status_code)
    print(req.json())





if __name__ == "__main__":
    main()