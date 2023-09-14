# 概要
大学の授業で作成したホットペッパーAPIを使用したcgiプログラム<br>
現在地から近いお店を検索できたり、お気に入りのお店を保存することができます。
また、お店をなかなか決められない人のためのランダムでお店を選んでくれる機能もあります。

## 課題
ランチや夕食を食べる店を決めるときに、時間がかかってしまう。
ご飯を食べようと思ったときに、すぐ決められるようなプログラムがあれば便利だと考えた。

## 機能
・現在地から近いお店を条件に合わせて検索できる 昼と夜で検索条件が変わる
・ランダムでお店を選んでくれる
・
・金欠大学生のためのクーポン情報表示

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
URLにアクセス
URL: http://localhost:8000/view/index.html

## 使用した技術
- Python 3.9.4
- API <br>
ホットペッパーのグルメサーチAPI<br>
https://webservice.recruit.co.jp/doc/hotpepper/reference.html<br>
geolocationAPI <br>https://developers.google.com/maps/documentation/geolocation/overview?hl=ja

## 実際の画面
検索画面<br>
<img width="500" alt="スクリーンショット 2023-09-15 0 32 03" src="https://github.com/iwatanabee/restaurant-finder-app/assets/83575309/151dc59e-1b70-4337-82e9-c15b93be03f1">

結果画面<br>
<img width="500" alt="スクリーンショット 2023-09-15 0 32 51" src="https://github.com/iwatanabee/restaurant-finder-app/assets/83575309/120ca275-28f4-4aab-b492-d7d23f0118be">

