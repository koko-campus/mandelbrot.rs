# 「Rust」 × 「マンデルブロ集合」

超軽量な次世代システムプログラミング言語、「**Rust**」を用いて高精度のマンデルブロ集合を描写します。  

![マンデルブロ集合サンプル](output/0000.png)


# 環境情報

| 機能 | バージョン |
| ---- | ---- |
| Linux / Ubuntu | 20.04.5 |
| Rust | 1.63.0 |


# 環境構築


```bash
# イロイロ最新に
sudo apt update
sudo apt upgrade
```


## Rust インストール

```bash
curl https://sh.rustup.rs -sSf | sh
# インストール設定はデフォルト(1)で!!!
# 次に環境変数(PATH)を設定します。
export PATH="$HOME/.cargo/bin:$PATH"
# 最後に正しくインストール、パスの設定がされたか、以下のコマンドで確認します。
cargo --version
# -> cargo 1.63.0
rustc 1.63.0
# -> rustc 1.63.0
rustdoc --version
# -> rustdoc 1.63.0
```


## python インストール

```bash
sudo apt install python3
sudo apt install pip3
```


# 動画の作成

```bash
ffmpeg -r 30 -i seeds/a/%08d.png -vcodec libx264 -pix_fmt yuv420p -r 60 ./fruits/★★★.mp4
```



