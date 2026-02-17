# バックエンド (FastAPI)

TODOアプリのAPIを提供するバックエンドです。詳細はルートの [README.md](../README.md) を参照してください。

## コード品質（Ruff）

コードチェックとフォーマットには [Ruff](https://docs.astral.sh/ruff/) を使用しています。
Dev Container 内で以下を実行できます。

```bash
cd backend

# コードチェック
ruff check .

# 自動修正（修正可能な問題を自動で修正）
ruff check . --fix

# フォーマット
ruff format .
```

設定は `pyproject.toml` の `[tool.ruff]` セクションで管理しています。