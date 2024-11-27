from simple_websocket_server import WebSocketServer, WebSocket
import ssl

import logging
logging.basicConfig(level=logging.DEBUG)

clients = []
class ws_handler(WebSocket):
    def handle(self):
        separator = chr(30)
        try:
            data = self.data
            data_split = data.split(separator)
            cmd = data_split[0]
            if cmd == 'sub':
                channels = data_split[1:]
                for channel in channels:
                    if channel not in self._channels:
                        self._channels.append(channel)
                        logging.info(f'{self._client_id}\tSub\t{channel}')
            elif cmd == 'unsub':
                channels = data_split[1:]
                for channel in channels:
                    if channel in self._channels:
                        self._channels.remove(channel)
                        logging.info(f'{self._client_id}\tuSub\t{channel}')
            elif cmd == 'pub':
                channel = data_split[1]
                message = data_split[2]
                total_clients = 0
                for client in clients:
                    if client != self:
                        if channel in client._channels:
                            total_clients += 1
                            client.send_message('{}{}{}'.format(channel,separator,message))
                if total_clients > 0: 
                    logging.info(f'#{total_clients}\tAir\t{channel}/{message}')
        except Exception as e:
            print('Error receive: ' + str(e))
            logging.error(f"Error receive: {e}")

    def connected(self):
        try:
            if self not in clients:
                self._client_id = list(self.address)[1]
                self._client_ip = list(self.address)[0]
                self._channels = []
                logging.info(f'{self._client_id}\tConn\t{self._client_ip}')
                clients.append(self)
        except Exception as e:
            logging.error(f"Connect: {e}")

    def handle_close(self):
        try:
            logging.info(f'{self._client_id}\tClose\t{self._client_ip}')
            clients.remove(self)
        except Exception as e:
            logging.error(f"Close: {e}")


if __name__ == '__main__':
    print('Server running...')
    server = WebSocketServer('0.0.0.0', 9001, ws_handler)

    # Use your own certificates
    #sslopts = dict(certfile='fullchain.pem', keyfile='privkey.pem', ssl_version=ssl.PROTOCOL_TLSv1_2)
    #server = WebSocketServer('0.0.0.0', 9001, ws_handler, **sslopts)

    server.serve_forever()