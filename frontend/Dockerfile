FROM node:20-slim

WORKDIR /app

# 依存関係のインストール
COPY package.json package-lock.json* ./
RUN npm cache clean --force && \
    npm install

# アプリケーションコードのコピー
COPY . .

# ポート公開
EXPOSE 3000

# 開発サーバー起動
CMD ["npm", "run", "dev"]
