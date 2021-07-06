### 操作方法
(windowsの場合は異なるかも。)
1. 仮想環境の構築
   ```
   python3 -m venv venv
   ```
   (2つ目の)venvは任意の名前(よく使われるのはvenv)
2. 仮想環境の有効化
   ```
   source sample/bin/active
   ```
3. 必要なライブラリをインストール
   ```
   pip install -r requirements.txt
   ```
4. 実行
   ```
   python sakiscashbook.py
   ```

### コード変更内容について
+ 関数に戻り値のヒンティングをつけました。pythonでは必要ありませんが、意識して付随させたほうが理解が深まるかと思います。いずれもNoneタイプで戻り値を使用することがなかったので、呼び出し元の変数も削除しました。
+ レイアウトを少し整えました。
+ F-string formattingに統一しました。

###　その他
+ README.mdを追加しました。通常はこのレポジトリの説明や動作説明などユーザに読んでほしいことを記載します。
+ .gitignoreを追加しました。ここに記されているファイルはgitの追跡対象から外れます。仮想環境内にインストールしたライブラリなどが対象です。
+ requirements.txtを追加しました。これは仮想環境内にインストールしたライブラリの一覧です。pip freeze -> requirements.txtで作成できます。これにより他のユーザは同様のライブラリ環境を構築することができます。

###　Next Challenge
ご興味がありましたら、挑んでみてください。
+ インプットの金額指定に数字以外が入力された場合のエラー対応。
+ detailsの一覧表示。およびdetailsごとの合計金額の表示。(発展)そのグラフ表示。
+ "Create a new file"
