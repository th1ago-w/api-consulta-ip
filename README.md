# API de Consulta de IP

API simples em Python para consultar informações de um endereço IP.

## Como rodar

`pip install -r requirements.txt`  
`python app.py`

## Como usar

Acesse no navegador:

`http://127.0.0.1:5000/ip/8.8.8.8`

## Exemplo de resposta

```json
{
  "ip": "8.8.8.8",
  "pais": "United States",
  "cidade": "Ashburn",
  "provedor": "Google LLC",
  "latitude": 39.03,
  "longitude": -77.5
}
```

## Tecnologias
- Python
- Flask
- Requests
