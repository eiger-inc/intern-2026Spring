# 2027年度エンジニアインターンシップ：事前学習課題

本資料は、開発未経験（または経験が浅い）学生が、インターンシップ当日のチーム開発にスムーズに合流できるよう、最低限必要な知識とスキルを習得するためのガイドです。

各DAYの課題は、最低限自分で一度は取り組んだことがあるレベルを想定しています。開発未経験の方は必ず一通り目を通し、手を動かしてみてください。

**目標学習時間：約24時間（8時間×3日間）**

> **本資料について**: 初学者にもわかりやすいよう、技術用語はできるだけ噛み砕いた表現を使っています。そのため、厳密な定義とは異なる場合があります。より正確な情報は、末尾の「参考リンク集」にある各公式ドキュメントをご参照ください。

> **AI活用について**: 本課題ではAIツール（ChatGPT、GitHub Copilot等）の利用をOKとしています。ただし「コピペして終わり」ではなく、**生成されたコードの意味を理解する**ことを心がけてください。
---

## 事前準備：必要なツールのインストール

以下のツールを事前にインストールしてください。すべて無料で利用できます。

| ツール | 用途 | 
|--------|------|
| **Cursor or Visual Studio Code (VS Code)** | コードエディタ |
| **Git** | バージョン管理 |
| **Docker Desktop** | コンテナ環境 |
| **Node.js (v20以上)** | JavaScriptの実行環境 |
| **GitHub アカウント** | コード共有 |

> **Windowsの方へ**: Gitインストール時に「Git Bash」も一緒にインストールされます。ターミナル操作はGit Bashを使うのがおすすめです。

> **Macの方へ**: ターミナル.appが最初から使えます。Gitは `xcode-select --install` コマンドでもインストール可能です。

---

## 📅 DAY 1：開発の土台を作る（Git / GitHub / VS Code）

**目標：コードを保存し、インターネットを通じて共有・公開できる。**

### そもそも Git / GitHub とは？

| 用語 | 説明 |
|------|------|
| **Git** | ファイルの変更履歴を記録・管理するツール。「いつ」「誰が」「何を」変えたかを追跡できる |
| **GitHub** | Gitの変更履歴をインターネット上に保存・共有するサービス。チーム開発の基盤 |
| **リポジトリ** | プロジェクトのファイルと変更履歴をまとめた「箱」。略して「リポ」 |
| **コミット** | 変更内容を記録すること。ゲームの「セーブ」のようなもの |
| **ブランチ** | メインの開発ラインから分岐して作業するための仕組み |
| **プルリクエスト (PR)** | 変更内容をレビューしてもらい、メインブランチに取り込む依頼 |

### 1-1. 環境構築

1. **Visual Studio Code (VS Code)** をインストールする。
2. **Git** をインストールする。
3. **GitHub** アカウントを作成する。
4. ターミナル（コマンドライン）を開き、以下のコマンドでGitの初期設定をする。

```bash
# 自分の名前とメールアドレスを登録（GitHubと同じものを推奨）
git config --global user.name "あなたの名前"
git config --global user.email "あなたのメールアドレス"
```

> **ターミナルとは？** コンピュータに文字で命令を送るための画面です。VS Codeでは上部メニューの「ターミナル」→「新しいターミナル」で開けます。

### 1-2. 課題：GitHubリポジトリの作成とプッシュ

1. GitHub上に `eiger-internship-pre-study` という名前のリポジトリを作成する（Public設定）。
2. ローカル（自分のPC）でフォルダを作成し、Gitで初期化する。

```bash
mkdir eiger-internship-pre-study
cd eiger-internship-pre-study
git init
```

3. `README.md` を作成し、「インターンへの意気込み」を記載してコミットする。

```bash
# README.mdをVS Codeで作成・編集してもOK
echo "# インターンシップ事前学習" > README.md

# 変更をステージング（次のコミットに含める準備）
git add README.md

# コミット（変更を記録）
git commit -m "初回コミット：READMEを追加"
```

4. GitHubへプッシュし、ブラウザで自分の意気込みが表示されていることを確認する。

```bash
# GitHubのリポジトリと紐づけ（URLはGitHub上の自分のリポジトリからコピー）
git remote add origin https://github.com/あなたのユーザー名/eiger-internship-pre-study.git

# メインブランチとして設定し、プッシュ
git branch -M main
git push -u origin main
```

### 1-3. 課題：ブランチとプルリクエストの体験

1. `feature/add-profile` という新しいブランチを作成し、切り替える。

```bash
git checkout -b feature/add-profile
```

2. `profile.md` を追加し、氏名や好きな技術（または興味のあること）を記載してコミットする。

```bash
# profile.mdをVS Codeで作成・編集
git add profile.md
git commit -m "プロフィールを追加"
```

3. GitHubへプッシュし、GitHub上で「Pull Request」を作成する。

```bash
git push -u origin feature/add-profile
```

4. GitHubのブラウザ画面で「Compare & pull request」ボタンを押してプルリクエストを作成し、自分でマージする。 `main` ブランチに反映されることを確認する。

### Git コマンド早見表

| コマンド | 説明 |
|---------|------|
| `git init` | フォルダをGitリポジトリとして初期化 |
| `git status` | 現在の変更状況を確認 |
| `git add ファイル名` | 変更をステージングに追加 |
| `git add .` | すべての変更をステージングに追加 |
| `git commit -m "メッセージ"` | ステージングの変更を記録 |
| `git push` | GitHubにアップロード |
| `git pull` | GitHubから最新を取得 |
| `git checkout -b ブランチ名` | 新しいブランチを作成して切り替え |
| `git checkout main` | mainブランチに戻る |
| `git log --oneline` | コミット履歴を簡潔に表示 |

---

## 📅 DAY 2：環境をコンテナで揃える（Docker / SQL）

**目標：どのPCでも同じ開発環境を動かせる仕組み（Docker）と、データの扱い方（SQL）を学ぶ。**

### そもそも Docker とは？

チーム開発では「自分のPCでは動くけど、他の人のPCでは動かない」という問題がよく起きます。Dockerは、アプリの実行環境をまるごと「コンテナ」という箱に入れて、どこでも同じように動かせるようにするツールです。

| 用語 | 説明 |
|------|------|
| **コンテナ** | アプリの実行環境を閉じ込めた箱。軽量な仮想マシンのようなもの |
| **イメージ** | コンテナの設計図。これを元にコンテナが作られる |
| **docker-compose** | 複数のコンテナを一括で管理する仕組み。設定ファイル（YAML）で定義する |
| **ボリューム** | コンテナが消えてもデータを残しておく仕組み |

### そもそもデータベース（DB）とは？

データベースは、大量のデータを整理して保存し、効率よく検索・更新するための仕組みです。Excelのように行と列でデータを管理する「テーブル」に情報を格納します。データベースとのやり取りには **SQL** という言語を使います。

本プロジェクトでは **MySQL** というデータベースを使用します。

### 2-1. 環境構築

1. **Docker Desktop** をインストールし、起動することを確認する。
   - タスクバー（Windows）やメニューバー（Mac）にDockerのアイコン（クジラ）が表示されていればOKです。
2. **DBeaver**（https://dbeaver.io/download/ ）をインストールする。
   - DBeaverはデータベースの中身を視覚的に操作できるGUIツールです。
   - VS Codeの拡張機能「MySQL」でも代替可能です。

### 2-2. 課題：MySQLデータベースを立ち上げる

1. 以下の内容で `docker-compose.yml` を作成する。

```yaml
services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: intern_db
      MYSQL_USER: user
      MYSQL_PASSWORD: password
    ports:
      - "3306:3306"
```

> **補足**: `image: mysql:8.0` はMySQL 8.0のイメージを使うという意味です。`ports: "3306:3306"` はPC側のポート3306とコンテナ側のポート3306を紐づけています。

2. ターミナルで以下のコマンドを実行し、データベースを起動する。

```bash
docker compose up -d
```

> `-d` は「バックグラウンドで動かす（detached mode）」オプションです。

3. 起動を確認する。

```bash
# コンテナの状態を確認（STATUSが「Up」になっていればOK）
docker compose ps
```

4. DBeaverからデータベースに接続し、中身が見れることを確認する。
   - 接続先: `localhost`
   - ポート: `3306`
   - ユーザー名: `user`
   - パスワード: `password`
   - データベース名: `intern_db`

### 2-3. 課題：SQLの基本操作

DBeaverまたはターミナルから以下のSQLコマンドを実行し、その実行ログ（またはスクリーンショット）を保存してください。

> **ターミナルからMySQLに接続する場合:**
> ```bash
> docker compose exec db mysql -u user -p intern_db
> # パスワード: password
> ```

**1. テーブルを作成する（CREATE TABLE）**

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL
);
```

**2. データを挿入する（INSERT）**

```sql
INSERT INTO users (name, email) VALUES ('山田太郎', 'taro@example.com');
INSERT INTO users (name, email) VALUES ('鈴木花子', 'hanako@example.com');
```

**3. データを取得する（SELECT）**

```sql
-- 全件取得
SELECT * FROM users;

-- 条件を指定して取得
SELECT * FROM users WHERE name = '山田太郎';
```

**4. データを更新する（UPDATE）**

```sql
UPDATE users SET email = 'taro_new@example.com' WHERE id = 1;
```

**5. データを削除する（DELETE）**

```sql
DELETE FROM users WHERE id = 2;
```

### Docker コマンド早見表

| コマンド | 説明 |
|---------|------|
| `docker compose up -d` | コンテナをバックグラウンドで起動 |
| `docker compose down` | コンテナを停止・削除 |
| `docker compose ps` | コンテナの状態を確認 |
| `docker compose logs サービス名` | 指定サービスのログを確認 |
| `docker compose exec サービス名 コマンド` | 起動中のコンテナ内でコマンドを実行 |
| `docker compose up -d --build` | イメージを再ビルドして起動 |

### SQL コマンド早見表

| コマンド | 説明 | 例 |
|---------|------|-----|
| `CREATE TABLE` | テーブルを作成 | `CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(100));` |
| `INSERT INTO` | データを挿入 | `INSERT INTO users (name) VALUES ('太郎');` |
| `SELECT` | データを取得 | `SELECT * FROM users;` |
| `UPDATE` | データを更新 | `UPDATE users SET name = '花子' WHERE id = 1;` |
| `DELETE` | データを削除 | `DELETE FROM users WHERE id = 1;` |
| `DROP TABLE` | テーブルを削除 | `DROP TABLE users;` |

---

## 📅 DAY 3：TODOアプリを作る（実践）

**目標：ブラウザから操作できる、データベース連携型のTODOアプリを完成させる。**

これまで学んだ Git、Docker、SQLの知識を統合し、「画面（フロントエンド）」と「API（バックエンド）」が連携するWebアプリケーションを構築します。

### この課題で使う技術

| 技術 | 役割 | 説明 |
|------|------|------|
| **Next.js (React)** | フロントエンド | ブラウザに表示される画面を作るフレームワーク |
| **Tailwind CSS** | スタイリング | HTMLにクラス名を書くだけでデザインできるCSSフレームワーク |
| **FastAPI (Python)** | バックエンド | データベースとやり取りするAPI（窓口）を作るフレームワーク |
| **MySQL** | データベース | TODOデータを永続的に保存する |
| **Docker** | 環境構築 | 上記すべてをコンテナで一括管理 |

> **API（エーピーアイ）とは？** フロントエンド（画面）とバックエンド（サーバー）がデータをやり取りするための「窓口」です。例えば「TODOの一覧をください」という要求をAPIに送ると、データベースからデータを取得してJSON形式で返してくれます。

> **React / Next.js とは？** Reactは画面のパーツ（コンポーネント）を組み合わせてUIを作るライブラリです。Next.jsはReactをベースにした開発フレームワークで、ページのルーティングやサーバー側の機能を簡単に扱えるようにしたものです。

### 3-1. 開発環境の準備

インターン用の **テンプレートプロジェクト** が提供されています。Docker、Next.js、FastAPI、MySQLの環境が事前に構築済みです。これをベースにTODOアプリを作成してください。

**1. テンプレートをクローン（ダウンロード）する**

```bash
# リポジトリURLは別途案内します
git clone <提供されるリポジトリURL>
cd <プロジェクトフォルダ>
```

**2. Docker でサービスを一括起動する**

```bash
docker compose up -d
```

これにより以下の3つのサービスが自動で起動します。

| サービス | URL | 説明 |
|---------|-----|------|
| フロントエンド (Next.js) | http://localhost:3000 | ブラウザで画面を確認 |
| バックエンド (FastAPI) | http://localhost:8000 | APIの動作を確認 |
| MySQL | localhost:3306 | データベース |

**3. 動作確認**

- ブラウザで http://localhost:3000 を開き、画面が表示されることを確認する。
- ブラウザで http://localhost:8000 を開き、`{"status": "ok", "message": "API is running"}` が表示されることを確認する。

> **うまく起動しない場合**: `docker compose logs` でエラーログを確認してください。Docker Desktopが起動しているかも確認しましょう。

### 3-2. プロジェクト構成の理解

テンプレートプロジェクトの主要なフォルダ構成です。**★マーク**が主に編集するファイルです。

```
プロジェクト/
├── backend/                  ← バックエンド（Python / FastAPI）
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py           ← ★ APIのコードを書くファイル
│   ├── requirements.txt       ← Pythonライブラリの一覧（追加時はここに記載）
│   └── Dockerfile
│
├── frontend/                 ← フロントエンド（Next.js / React）
│   ├── app/
│   │   ├── globals.css        ← 全体のスタイル
│   │   ├── layout.tsx         ← 共通レイアウト（基本そのままでOK）
│   │   └── page.tsx           ← ★ TODOアプリの画面を書くファイル
│   ├── package.json           ← JavaScriptライブラリの一覧
│   ├── tailwind.config.ts     ← Tailwind CSSの設定
│   └── Dockerfile
│
├── docker-compose.yml         ← Docker設定（全サービスの定義）
└── README.md
```

> **ポイント**: まずは `backend/app/main.py` と `frontend/app/page.tsx` の2ファイルに集中しましょう。

### 3-3. データベースのセットアップ

TODOアプリ用のテーブルを作成します。ターミナルからMySQLに接続して以下のSQLを実行してください。

```bash
# MySQLに接続
docker compose exec mysql mysql -u intern_user -p intern_db
# パスワード: intern_password
```

```sql
CREATE TABLE todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    is_done BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

> テーブルが作成できたことを `SELECT * FROM todos;` で確認しましょう（まだデータは空です）。

### 3-4. バックエンドの実装（FastAPI）

`backend/app/main.py` を編集して、以下の3つのAPIエンドポイントを作成してください。

#### 実装するAPI

| メソッド | パス | 説明 |
|---------|------|------|
| **GET** | `/todos` | TODOの一覧をJSON形式で返す |
| **POST** | `/todos` | 新しいTODOをDBに追加する |
| **PATCH** | `/todos/{id}` | 指定したTODOの完了状態（`is_done`）を切り替える |

#### ステップ1：MySQLドライバの追加

FastAPIからMySQLに接続するために、`backend/requirements.txt` に以下を追記してください。

```
mysql-connector-python==9.1.0
```

追記後、コンテナを再ビルドします。

```bash
docker compose up -d --build backend
```

#### ステップ2：APIの実装

以下は `GET /todos` の実装例です。参考にしながら `POST` と `PATCH` も自分で実装してみてください。

```python
import mysql.connector
from fastapi import FastAPI

# MySQL接続の設定
def get_db_connection():
    return mysql.connector.connect(
        host="mysql",          # docker-compose内のサービス名
        user="intern_user",
        password="intern_password",
        database="intern_db"
    )

@app.get("/todos")
async def get_todos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM todos ORDER BY created_at DESC")
    todos = cursor.fetchall()
    cursor.close()
    conn.close()
    return todos
```

> **確認方法**: ブラウザで http://localhost:8000/todos にアクセスして、JSONが返ってくることを確認しましょう。最初は空の配列 `[]` が返ればOKです。

> **ヒント**: `POST` では `request body` からデータを受け取ります。FastAPIの公式ドキュメント（ https://fastapi.tiangolo.com/ja/tutorial/body/ ）や、AIに「FastAPIでPOSTリクエストを受け取る方法」と聞いてみましょう。

### 3-5. フロントエンドの実装（Next.js / React）

`frontend/app/page.tsx` を編集して、TODOアプリの画面を作成してください。

#### React の基本

Reactでは、画面の各パーツを **コンポーネント** という関数で作ります。HTMLに似た **JSX** という記法でUIを記述します。

```tsx
// Reactコンポーネントの基本形
export default function Home() {
  return (
    <main>
      <h1>TODOアプリ</h1>
      <p>ここにTODOリストを作ります</p>
    </main>
  );
}
```

動的なデータ（ユーザーの入力、APIのレスポンス等）を扱うには **state（状態）** を使います。

```tsx
"use client";  // ← ブラウザ側で動的に動かすために必要（ファイル先頭に書く）
import { useState } from "react";

export default function Home() {
  const [count, setCount] = useState(0);  // 状態の定義

  return (
    <main>
      <p>カウント: {count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
    </main>
  );
}
```

> **`"use client"` とは？** Next.jsでは、デフォルトでページはサーバー側で描画されます。`useState` などのユーザー操作に反応する機能を使うには、ファイルの先頭に `"use client";` と書いてブラウザ側で動作するよう指定する必要があります。

#### 実装する機能

1. **タスクの一覧表示** — APIから取得したTODOをリスト表示する
2. **タスクの追加** — テキスト入力欄と追加ボタンで新しいTODOをAPIに送信する
3. **タスクの完了切り替え** — チェックボックスやボタンで `is_done` を切り替える

#### ヒント：APIとの通信（fetch）

```tsx
// APIからTODO一覧を取得する例
const response = await fetch("http://localhost:8000/todos");
const todos = await response.json();

// 新しいTODOを追加する例
await fetch("http://localhost:8000/todos", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ title: "新しいタスク" }),
});
```

> **ページ読み込み時にデータを取得するには？** Reactの `useEffect` を使います。AIに「React useEffectでAPIからデータを取得する方法」と聞いてみましょう。

#### ヒント：Tailwind CSS でスタイリング

このプロジェクトでは **Tailwind CSS** を使ってデザインします。HTMLの `className` にクラス名を追加するだけでスタイルが適用されます。CSSファイルを別途書く必要はありません。

```tsx
// Tailwind CSS の使用例
<button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
  追加
</button>

<input
  className="border border-gray-300 rounded px-3 py-2 w-full"
  placeholder="タスクを入力..."
/>

<li className="flex items-center gap-2 p-2 border-b">
  <input type="checkbox" />
  <span>タスクの内容</span>
</li>
```

> **参考**: Tailwind CSSのクラス一覧は https://tailwindcss.com/docs で確認できます。よく使うクラスの例：
> - 余白: `p-4`（padding）, `m-2`（margin）, `gap-2`（要素間の隙間）
> - 文字: `text-lg`（大きめ）, `font-bold`（太字）, `text-gray-600`（灰色）
> - 背景: `bg-white`, `bg-blue-500`
> - レイアウト: `flex`（横並び）, `flex-col`（縦並び）, `items-center`（中央揃え）

---

## 提出について

### 提出物

1. **GitHubリポジトリ**: 以下のファイルを整理してプッシュしてください。
   - `backend/` — APIのソースコード
   - `frontend/` — Next.jsのソースコード
   - `docker-compose.yml`

2. **README.md** に以下を記載してください。
   - アプリの起動手順（`docker compose up -d` → ブラウザで http://localhost:3000 を開く、など）
   - 画面のスクリーンショット
   - 工夫した点（UIのデザイン、バリデーション、エラー処理など）
   - 3日間の学習を通じて一番難しかったこと

### 余力がある方へ（チャレンジ課題）

基本のTODOアプリが完成したら、以下の追加機能に挑戦してみてください。評価の加点対象になります。

- **DELETE /todos/{id}** — TODOの削除機能
- **バリデーション** — 空文字のタスクを追加できないようにする
- **ソート・フィルター** — 完了/未完了でフィルター、作成日時でソート
- **レスポンシブ対応** — スマホでも見やすいデザイン
- **ローディング表示** — APIの通信中にスピナーを表示
- **エラーハンドリング** — API通信失敗時にユーザーへメッセージを表示

---

## 💡 学習のヒント

- **「疎通」が最優先**: 最初から凝ったデザインにせず、まずは「ボタンを押したらAPIが呼ばれる」「画面に文字が出る」という最小限の連携（疎通）を最優先しましょう。
- **小さく動かして確認**: コードを大量に書いてから動かすのではなく、1つ機能を追加するたびにブラウザで確認する癖をつけましょう。
- **デバッグのコツ**:
  - ブラウザの「開発者ツール」（F12キー）→「Console」タブでJavaScriptのエラーを確認
  - バックエンドのエラーは `docker compose logs backend` で確認
  - SQLを直接DBeaver等で実行して、DB側の問題かプログラム側の問題か切り分ける
- **CORSエラーへの対策**: ブラウザからAPIを叩く際にCORSエラーが出た場合は、バックエンドの `CORSMiddleware` 設定を確認してください（テンプレートには `localhost:3000` への許可が設定済みです）。
- **AIの活用**: 「FastAPIでTODOのPOSTエンドポイントを作りたい」「Reactでリスト表示する方法」など、**具体的なパーツごと**にAIに質問するとスムーズです。
- **完璧主義を捨てる**: 24時間は短いです。まずは「動く」ことを最優先にしましょう。

---

## ❓ よくあるトラブルと対処法

### Docker関連

| トラブル | 対処法 |
|---------|--------|
| `docker compose up` でエラーが出る | Docker Desktopが起動しているか確認。タスクバー/メニューバーにクジラのアイコンがあるか確認 |
| ポートが既に使われている | `docker compose down` で停止してから再度 `docker compose up -d` |
| コンテナが起動しない | `docker compose logs サービス名` でエラーログを確認 |
| バックエンドの変更が反映されない | `docker compose restart backend` でコンテナを再起動 |
| フロントエンドの変更が反映されない | ブラウザをハードリロード（Ctrl+Shift+R / Cmd+Shift+R） |

### Git関連

| トラブル | 対処法 |
|---------|--------|
| `git push` で認証エラー | GitHubへの認証設定を確認。Personal Access Tokenの設定が必要な場合がある（GitHub設定 → Developer settings → Personal access tokens） |
| 間違えてコミットした | `git log --oneline` で履歴を確認し、`git revert コミットID` で取り消し |

### 開発関連

| トラブル | 対処法 |
|---------|--------|
| CORSエラーが出る | バックエンドの `allow_origins` にフロントエンドのURL（`http://localhost:3000`）が含まれているか確認 |
| APIから 404 が返る | エンドポイントのパス（`/todos` 等）のスペルミスがないか確認 |
| MySQLに接続できない | コンテナが起動しているか確認（`docker compose ps`）。ホスト名・ポート・パスワードを再確認 |
| `"use client"` 関連のエラー | `useState` や `useEffect` を使う場合、ファイルの先頭に `"use client";` が必要 |
| `npm install` 関連のエラー | Node.jsのバージョンを確認（v20以上推奨）。`node -v` で確認可能 |

---

## 📖 用語集

| 用語 | 説明 |
|------|------|
| **フロントエンド** | ユーザーが直接見る・操作する画面部分。ブラウザ上で動作する |
| **バックエンド** | サーバー側の処理。データベースとのやり取りやビジネスロジックを担当 |
| **API** | アプリケーション間でデータをやり取りするための窓口・仕組み |
| **JSON** | `{"key": "value"}` 形式のデータフォーマット。APIでのデータ交換に広く使われる |
| **エンドポイント** | APIの入口となるURL。例: `GET /todos`, `POST /todos` |
| **CRUD** | Create（作成）、Read（読取）、Update（更新）、Delete（削除）の略。データ操作の基本4種 |
| **コンポーネント** | Reactにおける画面の部品。関数として定義し、再利用可能なUIパーツを作る |
| **state（ステート）** | Reactコンポーネント内の「状態」データ。変更されると画面が自動的に再描画される |
| **JSX** | JavaScriptの中にHTMLのような記法を書けるReact独自の構文 |
| **TypeScript** | JavaScriptに「型」の仕組みを追加した言語。コードの間違いを事前に検出できる |
| **Tailwind CSS** | クラス名を組み合わせてスタイルを当てるCSSフレームワーク |
| **CORS** | 異なるオリジン（ドメイン:ポート）間でのリソース共有を制限するブラウザのセキュリティ機能 |

---

## 🔗 参考リンク集

### Git / GitHub
- [サル先生のGit入門](https://backlog.com/ja/git-tutorial/) — Git操作を図解で学べる定番サイト
- [GitHub公式ドキュメント（日本語）](https://docs.github.com/ja/get-started)

### Docker
- [Docker公式ドキュメント（日本語）](https://docs.docker.jp/)

### SQL / MySQL
- [SQL入門（Progate）](https://prog-8.com/courses/sql) — ブラウザ上でSQLを学べる

### React / Next.js
- [React公式チュートリアル（日本語）](https://ja.react.dev/learn) — Reactの基本を公式で学べる
- [Next.js公式ドキュメント](https://nextjs.org/docs)

### Python / FastAPI
- [FastAPI公式チュートリアル（日本語）](https://fastapi.tiangolo.com/ja/)

### Tailwind CSS
- [Tailwind CSS公式ドキュメント](https://tailwindcss.com/docs) — クラス名の検索に便利
