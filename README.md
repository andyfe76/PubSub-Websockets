# PubSub-Websockets
Websocket Server with Pub/Sub and channels

Simple Websocket server with multiple clients and pub/sub with channel support.

### Server
- configure message line separator in ws_handler() function if needed

        separator = chr(30)


- start the server
    
        python3 server.py



### Receiver

Open in your browser receiver.html from examples/ folder
- this will connect to the Websocket server and subscribe to app channel

### Sender

Start sender.py from examples/ folder

    python3 examples/sender.py

The server app console will print the connections id and messages:

    50530	Conn	127.0.0.1
    50530	Sub	app
    50559	Conn	127.0.0.1
    #1	Air	app/0
    #1	Air	app/1
    #1	Air	app/2
    #1	Air	app/3
    #1	Air	app/4
    #1	Air	app/5
    #1	Air	app/6
    #1	Air	app/7
    #1	Air	app/8
    #1	Air	app/9
    50559: Closed

The browser will print the received messages:

    app: 0
    app: 1
    app: 2
    app: 3
    app: 4
    app: 5
    app: 6
    app: 7
    app: 8
    app: 9