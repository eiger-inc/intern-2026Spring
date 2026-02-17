# 2027・2028年度新卒採用インターンシップ：事前課題

本課題では、TODOアプリの開発に取り組んでいただきます。開発環境はテンプレートリポジトリとして用意してありますので、クローンしてすぐに開発を始められます。

**完成まで到達しなくても問題ありません。** 各ステップごとに区切りがあるので、できたところまで提出してください。

> **AI活用について**: 本課題ではAIツール（ChatGPT、GitHub Copilot等）の利用をOKとしています。ただし「コピペして終わり」ではなく、**生成されたコードの意味を理解する**ことを心がけてください。

---

## 事前準備

### 必要なツールのインストール

以下のツールを事前にインストールしてください。すべて無料で利用できます。

| ツール | 用途 |
|--------|------|
| **Cursor or Visual Studio Code (VS Code)** | コードエディタ |
| **Git** | バージョン管理 |
| **Docker Desktop** | コンテナ環境 |
| **GitHub アカウント** | コード共有 |

> **Windowsの方へ**: Gitインストール時に「Git Bash」も一緒にインストールされます。ターミナル操作はGit Bashを使うのがおすすめです。また、Docker Desktopの設定で「Use the WSL 2 based engine」が有効になっていることを確認してください。

> **Macの方へ**: ターミナル.appが最初から使えます。Gitは `xcode-select --install` コマンドでもインストール可能です。

### テンプレートのセットアップ

**1. テンプレートをクローン（ダウンロード）する**

```bash
# リポジトリURLは別途案内します
git clone https://github.com/eiger-inc/intern-2026Spring.git
cd <プロジェクトフォルダ>
```

**2. Dev Container で開発環境を起動する**

VS Code（または Cursor）でプロジェクトフォルダを開き、以下の手順で Dev Container を起動します。

1. 拡張機能「Dev Containers」をインストール（初回のみ）
2. 画面左下の `><` アイコンをクリック → **「Open Folder in Container」** を選択
3. フォルダが表示されるので、そのまま開くを選択
4. Intern Development...が表示されるのでそのままエンター
5. 初回はコンテナのビルドに数分かかります。完了すると自動的にすべてのサービスが起動します

これにより以下の3つのサービスが自動で起動します。

| サービス | URL | 説明 |
|---------|-----|------|
| フロントエンド (Next.js) | http://localhost:3000 | ブラウザで画面を確認 |
| バックエンド (FastAPI) | http://localhost:8000 | APIの動作を確認 |
| Swagger UI | http://localhost:8000/docs | APIの仕様確認・テスト実行 |
| MySQL | localhost:3306 | データベース |

**3. 動作確認**

- ブラウザで http://localhost:3000 を開き、画面が表示されることを確認する
- ブラウザで http://localhost:8000 を開き、`{"status": "ok", "message": "API is running"}` が表示されることを確認する
- ブラウザで http://localhost:8000/docs を開き、Swagger UI（API仕様書）が表示されることを確認する

> **うまく起動しない場合**: Docker Desktopが起動しているか確認してください。VS Codeの出力パネル（「Dev Containers」）でエラーログを確認できます。

---

## プロジェクト構成

```
プロジェクト/
├── backend/                  ← バックエンド（Python / FastAPI）
│   ├── app/
│   │   ├── __init__.py
│   │   ├── database.py        ← DB接続設定
│   │   ├── models.py          ← ★ テーブル定義（SQLAlchemy モデル）
│   │   ├── schemas.py         ← ★ リクエスト/レスポンスの型定義
│   │   └── main.py            ← ★ APIのコードを書くファイル
│   ├── alembic/               ← DBマイグレーション
│   │   ├── versions/          ← マイグレーションファイル
│   │   └── env.py
│   ├── alembic.ini
│   ├── requirements.txt       ← Pythonライブラリの一覧
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
└── README.md                  ← このファイル
```

**★マーク**が主に編集するファイルです。

### テンプレートに含まれているもの

テンプレートには **サンプルとして「Items」のシンプルなCRUD API** が実装されています。

- **`items` テーブル** — `id` と `name` だけのシンプルなテーブル（コンテナ起動時に自動作成）
- **サンプル API** — `GET /items`（一覧）、`POST /items`（追加）、`DELETE /items/{id}`（削除）
- **Swagger UI** — http://localhost:8000/docs でAPIの仕様確認・テスト実行ができます

> このサンプルAPIのコードを参考にして、TODO用のAPIを自分で作成するのが本課題の流れです。

> **Swagger UI とは？** ブラウザ上でAPIのエンドポイントを一覧表示し、実際にリクエストを送ってテストできるツールです。まずはここでサンプルAPIの動作を確認してみましょう。

### 使用技術

| 技術 | 役割 | 説明 |
|------|------|------|
| **Next.js (React)** | フロントエンド | ブラウザに表示される画面を作るフレームワーク |
| **Tailwind CSS** | スタイリング | HTMLにクラス名を書くだけでデザインできるCSSフレームワーク |
| **FastAPI (Python)** | バックエンド | データベースとやり取りするAPI（窓口）を作るフレームワーク |
| **SQLAlchemy** | ORM | PythonコードでDBを操作するためのライブラリ |
| **Alembic** | マイグレーション | テーブル構造の変更をコードで管理するツール |
| **MySQL** | データベース | TODOデータを永続的に保存する |
| **Docker** | 環境構築 | 上記すべてをコンテナで一括管理 |

### MySQL 接続情報

| 項目 | 値 |
|------|-----|
| ホスト | mysql（コンテナ内）/ localhost（ホストから） |
| ポート | 3306 |
| ユーザー | intern_user |
| パスワード | intern_password |
| データベース | intern_db |

### DBマイグレーション

テーブルはコンテナ起動時に `alembic upgrade head` で自動作成されます。

新しいマイグレーションを作成する場合:

```bash
# VS Code のターミナルで実行
cd backend

# 初回のみライブラリのインストールが必要です
pip install -r requirements.txt

# マイグレーション実行
alembic revision --autogenerate -m "説明"
alembic upgrade head
```

---

## 課題：TODOアプリの開発

以下のステップに分かれています。**Step 1 から順に取り組み、できたところまで提出してください。**

| ステップ | 内容 | 概要 |
|---------|------|------|
| **Step 1** | バックエンド（API） | サンプルAPIを参考に、TODO用のモデル・マイグレーション・APIエンドポイントを作成する |
| **Step 2-1** | フロントエンド（一覧表示） | APIから取得したTODOをブラウザに一覧表示する |
| **Step 2-2** | フロントエンド（追加機能） | テキスト入力＋ボタンで新しいTODOを追加できるようにする |
| **Step 2-3** | フロントエンド（完了切替） | チェックボックス等でTODOの完了/未完了を切り替える |
| **Step 3** | スタイリング | Tailwind CSS で見た目を整える |
| **チャレンジ** | 追加機能（任意） | 削除・編集・フィルターなど自由に機能追加 |

---

### Step 1：サンプルAPIを理解し、TODO用のAPIを作る（バックエンド）

このステップでは、テンプレートのサンプルAPI（Items）を参考に、TODO用のAPIを自分で作成します。

#### 1-1. サンプルAPIを読んで理解する

まず、以下のファイルを読み、サンプルAPIがどのように動いているか理解してください。

| ファイル | 内容 |
|---------|------|
| `backend/app/models.py` | `items` テーブルの定義（SQLAlchemy モデル） |
| `backend/app/schemas.py` | リクエスト/レスポンスの型定義（Pydantic） |
| `backend/app/main.py` | APIエンドポイントの実装 |
| `backend/app/database.py` | DB接続の設定 |

Swagger UI（http://localhost:8000/docs）でサンプルAPIを実際に動かしてみましょう。

1. **POST /items** — `{"name": "テスト"}` を送信してアイテムを追加する
2. **GET /items** — 追加したアイテムが一覧に表示されることを確認する
3. **DELETE /items/{item_id}** — アイテムを削除する

#### 1-2. TODO用のモデルとマイグレーションを作成する

サンプルの `Item` モデルを参考に、`Todo` モデルを作成してください。

**`todos` テーブルに必要なカラム:**

| カラム名 | 型 | 説明 |
|---------|-----|------|
| `id` | INT (AUTO_INCREMENT) | 主キー |
| `title` | VARCHAR(255) | タスクの内容 |
| `is_done` | BOOLEAN (デフォルト: FALSE) | 完了フラグ |
| `created_at` | DATETIME (デフォルト: 現在時刻) | 作成日時 |

##### 実装の手順

1. `backend/app/models.py` に `Todo` クラスを追加する（`Item` クラスを参考に）
2. `backend/app/schemas.py` に TODO 用のスキーマを追加する
3. Alembic でマイグレーションファイルを作成する

```bash
# VS Code のターミナルで実行
cd backend

# 初回のみライブラリのインストールが必要です
pip install -r requirements.txt

# マイグレーション実行
alembic revision --autogenerate -m "create todos table"
alembic upgrade head
```

> **ヒント**: `Item` モデルには `id` と `name` しかありませんが、TODO には `is_done`（Boolean）と `created_at`（DateTime）が追加で必要です。SQLAlchemy の型については、AIに「SQLAlchemy で Boolean カラムを定義する方法」と聞いてみましょう。

#### 1-3. TODO用のAPIエンドポイントを作成する

以下の3つのエンドポイントを `backend/app/main.py` に追加してください。

| メソッド | パス | 説明 |
|---------|------|------|
| **GET** | `/todos` | TODO一覧をJSON形式で返す |
| **POST** | `/todos` | 新しいTODOを追加する |
| **PATCH** | `/todos/{todo_id}` | TODOの完了状態（`is_done`）を切り替える |

> サンプルの Items API（`GET /items`, `POST /items`, `DELETE /items/{id}`）の実装を参考にしてください。`PATCH` はサンプルにはないので、自分で考えて実装してみましょう。

##### 動作確認

Swagger UI（http://localhost:8000/docs）で以下を確認してください。

- `POST /todos` でTODOを追加できる
- `GET /todos` でTODO一覧が取得できる
- `PATCH /todos/{todo_id}` で完了状態を切り替えられる

##### ✅ Step 1 の完了条件

- `todos` テーブルが作成されている
- `GET /todos` でTODO一覧が取得できる
- `POST /todos` で新しいTODOを追加できる
- `PATCH /todos/{todo_id}` でTODOの完了状態を切り替えられる

**ここまでできたら、コミット＆プッシュしましょう。**

---

### Step 2：画面の作成とAPI連携（フロントエンド）

このステップでは、Step 1 で作ったAPIと連携する画面を作成します。

#### 2-1. TODO一覧の表示

`frontend/app/page.tsx` を編集して、APIから取得したTODOをリスト表示してください。

実装方法については、React や Next.js の公式ドキュメント、または本ドキュメント末尾の「参考リンク集」を参照してください。

##### ✅ Step 2-1 の完了条件

- ブラウザでTODOの一覧が表示される

#### 2-2. TODOの追加機能

テキスト入力欄と追加ボタンを作り、新しいTODOをAPIに送信できるようにしてください。

```tsx
// 新しいTODOを追加する例
await fetch("http://localhost:8000/todos", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ title: "新しいタスク" }),
});
```

##### ✅ Step 2-2 の完了条件

- テキスト入力欄にタスク名を入力し、追加ボタンを押すとTODOが追加される
- 追加後、一覧に新しいTODOが表示される

#### 2-3. TODOの完了切り替え

チェックボックスやボタンで、TODOの完了状態（`is_done`）を切り替えられるようにしてください。

##### ✅ Step 2-3 の完了条件

- TODOの完了/未完了を切り替えられる
- 完了したTODOが視覚的に区別できる（取り消し線、色の変化など）

**ここまでできたら、コミット＆プッシュしましょう。**

---

### Step 3：見た目を整える（スタイリング）

Tailwind CSS を使って、TODOアプリの見た目を整えてください。デザインは自由です。

##### Tailwind CSS の使い方

HTMLの `className` にクラス名を追加するだけでスタイルが適用されます。CSSファイルを別途書く必要はありません。

```tsx
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

##### ✅ Step 3 の完了条件

- TODOアプリとして見やすいデザインになっている

**ここまでできたら、コミット＆プッシュしましょう。**

---

### チャレンジ課題（余力がある方向け）

基本のTODOアプリが完成したら、以下の追加機能に挑戦してみてください。

#### 機能追加（難易度：中〜高）
- **タスクの削除** — `DELETE /todos/{todo_id}` を実装してタスクを削除できるようにする
- **タスクの編集** — 登録済みのタスクの内容を修正できるようにする
- **期限日の設定** — タスクに締め切り日時を設定・表示できるようにする（DBのカラム追加が必要）
- **優先度の設定** — 「高・中・低」などの優先度を付与して、優先度順に並び替えられるようにする

#### UI/UX改善（難易度：低〜中）
- **バリデーション** — 空文字のタスクを追加できないようにする
- **ソート・フィルター** — 完了/未完了でフィルター、作成日時でソート
- **レスポンシブ対応** — スマホでも見やすいデザイン
- **ローディング表示** — APIの通信中にスピナーを表示
- **エラーハンドリング** — API通信失敗時にユーザーへメッセージを表示

---

## 提出について

**できたところまでで構いません。** 以下のいずれかの方法で提出してください。

**提出フォーム**: https://form.run/@terravie-a2tcMnqDLhl9wXImoSjB

| 提出方法 | 手順 |
|---------|------|
| **GitHub リポジトリ** | コードをプッシュし、リポジトリのURLをフォームに記入 |
| **ZIP ファイル** | プロジェクトフォルダをZIPに圧縮し、フォームからアップロード |

この `README.md` を編集して、以下を記載してください。
- どのステップまで完了したか
- 工夫した点や苦労した点

---

## 💡 学習のヒント

- **「疎通」が最優先**: 最初から凝ったデザインにせず、まずは「ボタンを押したらAPIが呼ばれる」「画面に文字が出る」という最小限の連携（疎通）を最優先しましょう。
- **サンプルAPIを活用**: テンプレートの Items API のコードを読んで、構造を理解してから TODO の実装に取りかかりましょう。
- **小さく動かして確認**: コードを大量に書いてから動かすのではなく、1つ機能を追加するたびにブラウザで確認する癖をつけましょう。
- **Swagger UI を活用**: フロントエンドを作る前に、まず Swagger UI（http://localhost:8000/docs）でAPIの動作を確認しましょう。APIが正しく動いていることを確認してからフロントエンドの開発に進むと、問題の切り分けが楽になります。
- **デバッグのコツ**:
  - ブラウザの「開発者ツール」（F12キー）→「Console」タブでJavaScriptのエラーを確認
  - バックエンドのエラーは VS Code のターミナルで確認
  - Swagger UI でAPIを直接叩いて、DB側の問題かフロントエンド側の問題か切り分ける
- **CORSエラーへの対策**: ブラウザからAPIを叩く際にCORSエラーが出た場合は、バックエンドの `CORSMiddleware` 設定を確認してください（テンプレートには `localhost:3000` への許可が設定済みです）。
- **AIの活用**: 「SQLAlchemy で Boolean カラムを定義する方法」「Reactでリスト表示する方法」など、**具体的なパーツごと**にAIに質問するとスムーズです。
- **完璧主義を捨てる**: まずは「動く」ことを最優先にしましょう。

---

## ❓ よくあるトラブルと対処法

### Docker / Dev Container 関連

| トラブル | 対処法 |
|---------|--------|
| Dev Container が起動しない | Docker Desktopが起動しているか確認 |
| ポートが既に使われている | Docker Desktop でコンテナを停止してから再度「Reopen in Container」 |
| コンテナが起動しない | VS Code の出力パネル（Dev Containers）でエラーログを確認 |
| バックエンドの変更が反映されない | ファイルを保存すると自動で反映されます（ホットリロード） |
| フロントエンドの変更が反映されない | ブラウザをハードリロード（Ctrl+Shift+R / Cmd+Shift+R） |
| 環境がおかしくなった / 原因不明のエラー | コマンドパレット（Ctrl+Shift+P / Cmd+Shift+P）→「Dev Containers: Rebuild Container」でコンテナを再構築 |

### Git関連

| トラブル | 対処法 |
|---------|--------|
| `git push` で認証エラー | GitHubへの認証設定を確認。Personal Access Tokenの設定が必要な場合がある |
| 間違えてコミットした | `git log --oneline` で履歴を確認し、`git revert コミットID` で取り消し |

### 開発関連

| トラブル | 対処法 |
|---------|--------|
| CORSエラーが出る | バックエンドの `allow_origins` に `http://localhost:3000` が含まれているか確認 |
| APIから 404 が返る | エンドポイントのパスのスペルミスがないか確認 |
| MySQLに接続できない | コンテナが起動しているか確認 |
| `"use client"` 関連のエラー | `useState` や `useEffect` を使う場合、ファイルの先頭に `"use client";` が必要 |

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
| **ORM** | Object-Relational Mapping。SQLを直接書かずにPythonコードでDBを操作する仕組み |
| **マイグレーション** | テーブルの作成・変更をコードで管理する仕組み。チームで構造変更を共有しやすい |
| **Swagger UI** | APIの仕様をブラウザで確認・テストできるツール。FastAPIに標準搭載 |
| **コンポーネント** | Reactにおける画面の部品。関数として定義し、再利用可能なUIパーツを作る |
| **state（ステート）** | Reactコンポーネント内の「状態」データ。変更されると画面が自動的に再描画される |
| **JSX** | JavaScriptの中にHTMLのような記法を書けるReact独自の構文 |
| **TypeScript** | JavaScriptに「型」の仕組みを追加した言語。コードの間違いを事前に検出できる |
| **Tailwind CSS** | クラス名を組み合わせてスタイルを当てるCSSフレームワーク |
| **CORS** | 異なるオリジン（ドメイン:ポート）間でのリソース共有を制限するブラウザのセキュリティ機能 |
| **Docker** | アプリの実行環境をコンテナという箱に入れて、どこでも同じように動かせるツール |
| **Dev Container** | VS Code からDockerコンテナ内で開発できる仕組み。環境構築の手間を省ける |

---

## 🔗 参考リンク集

### Git / GitHub
- [サル先生のGit入門](https://backlog.com/ja/git-tutorial/)
- [GitHub公式ドキュメント（日本語）](https://docs.github.com/ja/get-started)

### Docker
- [Docker公式ドキュメント（日本語）](https://docs.docker.jp/)

### SQL / MySQL
- [SQL入門（Progate）](https://prog-8.com/courses/sql)

### React / Next.js
- [React公式チュートリアル（日本語）](https://ja.react.dev/learn)
- [Next.js公式ドキュメント](https://nextjs.org/docs)

### Python / FastAPI
- [FastAPI公式チュートリアル（日本語）](https://fastapi.tiangolo.com/ja/)

### Tailwind CSS
- [Tailwind CSS公式ドキュメント](https://tailwindcss.com/docs)
