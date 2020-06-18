# https://qiita.com/__init__/items/91e5841ed53d55a7895e
# https://make-muda.net/2017/10/5645/
# https://clean-copy-of-onenote.hatenablog.com/entry/inrto_websocket#WebSocket%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC
# Standard
import logging
from datetime import datetime
# Third party
from websocket_server import WebsocketServer
# Local
import my_var

# logging.basicConfig(filename='log/logger.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('log/logger.log')
handler.setFormatter(logging.Formatter(' %(module)s - %(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

def new_client(client, server):
    logger.info('New client {}:{} (id:{}) has joined.'.format(client['address'][0], client['address'][1], client['id']))
    server.send_message_to_all(datetime.now().isoformat() + ": New client has joined!")

def client_left(client, server):
    logger.info('Client {}:{} (id:{}) has left.'.format(client['address'][0], client['address'][1], client['id']))
    server.send_message_to_all(datetime.now().isoformat() + ": client has left")

def message_received(client, server, message):
    logger.info('Message "{}" has been received from {}:{} (id:{})'.format(message, client['address'][0], client['address'][1], client['id']))
    server.send_message_to_all(datetime.now().isoformat() + ": " + message)

if __name__ == "__main__":
    HOST = my_var.HOST
    PORT = my_var.PORT
    # インスタンス作成．loglevel=logging.DEBUGも使える
    server = WebsocketServer(port=PORT, host=HOST, loglevel=logging.INFO)
    # 新しいクライアント接続時
    server.set_fn_new_client(new_client)
    # クライアント切断時
    server.set_fn_client_left(client_left)
    # メッセージ受信時
    server.set_fn_message_received(message_received)
    server.run_forever()
