import websocket, ssl

ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
ws.connect("ws://localhost:9001")

for a in range(10):
    ws.send(f'pub{chr(30)}app{chr(30)}{a}')

ws.close()