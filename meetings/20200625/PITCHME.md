# **WS Chat**
## 第1回ミーティング（2020/06/25）

---

@snap[north-west ]
### 発端
- WebSocket使ってみたい→チャットアプリ作れそう
  - なおチャットアプリが一般的にどういう技術で作られているかは知らない
  - 世の中に溢れているので車輪の再発明にはなる
@snapend

---

@snap[north-west ]
### 目的
- チーム開発の経験を積みたい
- アジャイル開発の練習（？）
- 技術習得
@snapend

---

@snap[north-west ]
### 現状
- GCE上にHTTPサーバ，WSサーバ両方を構築
- 今後は違うサービスを使う可能性あり
  - Firebase Hosting
  - AWS
  - Heroku
@snapend

---?image=assets/img/current_server.png&position=left&size=50% 100%
@title[Slide Decks for Developers]

@snap[east span-50 text-center]
## GitPitch
#### Slide Decks
#### for
### Developers
@snapend

---

![IMAGE](assets/img/current_server.png)

---

@snap[north-west ]
### 開発言語・環境
- GitHubでソースコード管理
- クライアント側
  - JavaScriptのフレームワークを使ってみる
  -  とりあえずVue.js
- サーバ側
  - Python
@snapend

---

@snap[north-west ]
### 開発の流れ（1回目のみ）
1. GitHubのcollaboratorになる
2. クローン→ブランチを切る
3. 編集
4. プッシュ→プルリク
5. 管理者がマージ
@snapend

---

```bash
git clone https://github.com/yousukeayada/WSChat.git
git branch feature/test
git checkout feature/test
（編集）
git add .
git commit -m “message”
git push origin feature/test
```

---

@snap[north-west ]
### 開発の流れ（2回目以降）
1. masterブランチに戻る
2. プル→ブランチを切る
3. 編集
4. プッシュ→プルリク
5. 管理者がマージ
@snapend

---

```bash
git checkout master
git pull origin master
git checkout -b feature/ayada
（編集）
git add .
git commit -m “message”
git push origin feature/ayada
```

---

@snap[north-west ]
### 今後欲しい機能（暫定）
- 認証（OAuth）
- いいね
- 履歴保存（DB）
- チャンネル
@snapend

---
