# フロントエンド (Next.js)

TODOアプリの画面を提供するフロントエンドです。詳細はルートの [README.md](../README.md) を参照してください。

## コード品質

### ESLint

コードチェックには [ESLint](https://eslint.org/)（Next.js 標準設定）を使用しています。
Dev Container 内で以下を実行できます。

```bash
cd frontend

# リント（コードチェック）
npm run lint
```

設定は `eslint.config.mjs`（ESLint 9 flat config）で行っており、`eslint-config-next` の core-web-vitals と TypeScript 設定を利用しています。

### Prettier（フォーマッター）

Dev Container では Prettier 拡張機能が導入されており、保存時に自動でフォーマットされます。
フォーマットの設定はエディタのデフォルトを使用しています。
