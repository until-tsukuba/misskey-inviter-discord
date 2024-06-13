# misskey-inviter-discord
![GitHub License](https://img.shields.io/github/license/until-tsukuba/misskey-inviter-discord)

Misskeyの招待コードを、Discord上から自動で発行できるようにするbotです。このbotが導入されたDiscordサーバーにおいては`/invite`を実行することにより、招待コードが発行されます。

このbotを導入するには、Misskeyサーバーの管理者権限と導入するDiscordサーバーの管理者権限の**双方が必要**です。

## 導入方法
1. Python3が動作する環境を用意する
2. poetryが動作する環境を用意する
3. [Discord Developer Portal](https://discord.com/developers/applications)を開き、「New Application」をクリックする
4. 適切な名称等の設定を行った上で、OAuth2画面から「bot」を選択し、「Send Message」と「Use Slash Command」のチェックボックスをonにする
5. ここで得られたトークンを記録する（環境変数 `DISCORD_TOKEN` として使用します）
6. Misskeyサーバーの設定画面→API（`/settings/api`）より、「招待コードを操作する」をonにしたアクセストークンを発行する
7. 発行されたアクセストークンを記録する（環境変数 `MISSKEY_TOKEN` として使用します）
8. Misskeyサーバーのドメインを確認する（例: `mi.tsukuba.dev`、環境変数 `MISSKEY_HOST` として使用します）
9. `poetry install`を行う
10. `env DISCORD_TOKEN=AAA MISSKEY_TOKEN=BBB MISSKEY_HOST=CCC poetry run main.py`を実行する
11. Discordサーバーへbotを追加する
12. `/invite`をDiscord上で入力する

## 管理
[UNTIL.](https://until-tsukuba.github.io/)