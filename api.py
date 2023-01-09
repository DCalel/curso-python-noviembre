# API - stateless (sin estado)
# request
# URL - dominio - https://google.com - https://189.205.65.69
# URL - path - https://google.com/photos
# método - GET - POST - PUT - DELETE
# POST Y PUT tiene body
# body (JSON) - {
#   "name": "Rafael",
#   "email": "email@ejemplo.com"
# }
# metadata: headers o encabezados (llave-valor)
# headers - Authorization: abc-123 (sesión)
#         - Content-Type: application/jpg
#         - Accept: application/excel
# Path parameters htt.../photos/1
# Filtrar información - Query params /friends?gender=male&adults=yes

# endpoint
# response (Respuesta que recibimos del servidor)
# Body
# Headers
# Códigos HTTP - 100 200 300 400 500
#

import requests

response = requests.get("https://swapi.dev/api/people", params={"page": 1})

#print(response) # <Response [200]>
#print(response.status_code) # 200
#print(response.content)
#print(response.headers)

data = response.json()
print(data["results"][0]["name"])

# Lado del cliente