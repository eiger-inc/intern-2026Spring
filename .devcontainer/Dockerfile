FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Pythonとpipをインストール
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ruffをインストール（--break-system-packagesフラグを使用）
RUN pip3 install --break-system-packages --no-cache-dir ruff==0.1.15

# シンボリックリンクを作成（pythonとpipコマンドを使えるように）
RUN ln -s /usr/bin/python3 /usr/local/bin/python && \
    ln -s /usr/bin/pip3 /usr/local/bin/pip
