# 概要
大学の授業で作成したホットペッパーAPIを使用したcgiプログラム<br>
現在地から近いお店を検索できたり、お気に入りのお店を保存することができます
## 課題
ランチや夕食を食べる店を決めるときに、いろいろなサイトを見たり、時間がかかってしまう。
ご飯を食べようと思ったときに、複数の条件で店を検索プログラムがあれば便利だと考えた。
現在地の緯度と経度を入力して近くの店を条件に合わせて、調べられたら良いと思った。

Siri→
・いちいちサイトに飛ばないと情報が見れないので、まとめて情報を表示できたらいい
・金欠大学生クーポン情報がない

## 使い方
このレポジトリをクローンします
```
git clone https://github.com/iwatanabee/restaurant-finder-app.git
```
.envファイルを作成し、APIキーを設定
``` .env
API_KEY='取得したAPIキー'
```
サーバーを立てて、実行
```
python server.py
```


## 使用した技術
- Python 3.9.4
- API <br>
ホットペッパーのグルメサーチAPI<br>
https://webservice.recruit.co.jp/doc/hotpepper/reference.html<br>
geolocationAPI <br>https://developers.google.com/maps/documentation/geolocation/overview?hl=ja

## 実際の画面
検索画面<br>
<img width="500" alt="スクリーンショット 2023-09-11 18 10 46" src="https://github.com/iwatanabee/restaurant-finder-app/assets/83575309/0a8385ad-1ae1-45bc-b8d2-628f228e4144">
<br>
結果画面<br>
<img width="500" alt="スクリーンショット 2023-09-11 18 11 04" src="https://github.com/iwatanabee/restaurant-finder-app/assets/83575309/d8524ac2-649c-4490-9491-52e557ccf65c">

