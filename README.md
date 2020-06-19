# WSChat
- websocketを使ったチャットアプリ
```bash
git clone https://github.com/yousukeayada/WSChat.git

mkdir log
touch myvar.py #中身は下記
touch myvar.js #中身は下記
python server.py
```

## サーバ
- Pythonで作成（`server.py`）
- `log`という名前のディレクトリが必要
- `myvar.py`からIPアドレス，ポート番号を読み込む
```python
HOST = '127.0.0.1'
PORT = 12345
```

## クライアント
- JavaScriptで作成（`index.html`）
- `myvar.js`からIPアドレス，ポート番号を読み込む
```js
export const HOST = '127.0.0.1'
export const PORT = 12345
```

## 参考
- https://qiita.com/init/items/91e5841ed53d55a7895e
- https://make-muda.net/2017/10/5645/
- https://clean-copy-of-onenote.hatenablog.com/entry/inrto_websocket#WebSocket%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC
