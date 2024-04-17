<p align="center">
  <img width="700" alt="スクリーンショット 2023-09-15 0 31 40" src="https://github.com/iwatanabee/restaurant-finder-app/assets/83575309/425870ed-09f0-4cd4-835a-c13bf5667694"><br>
</p>  

# 概要
大学の授業で作成したホットペッパーAPIを使用したcgiプログラム<br>
現在地から近いお店を検索できたり、お気に入りのお店を保存することができます。
また、お店をなかなか決められない人のためのランダムでお店を選んでくれる機能もあります。

## 課題
データベースとAPIを使ってcgiプログラムを作成する課題が出たで、前から興味があったホットペッパーAPIのグルメサーチAPIを使用してアプリを作ってみようと思った。
ランチや夕食を食べる店を決めるときに、時間がかかってしまうので、ご飯を食べようと思ったときに、すぐ決められるようなプログラムがあれば便利だと考えた。

## 機能
・現在地から近いお店を条件に合わせて検索できる 昼と夜で検索条件が変わる
・ランダムでお店を選んでくれる
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
- Python 3.9.4 (課題のため)
- API <br>
ホットペッパーのグルメサーチAPI　(無料で利用できるのが、これだけだった)<br> 
https://webservice.recruit.co.jp/doc/hotpepper/reference.html<br>
geolocationAPI (現在地を取得する用)<br>
https://developers.google.com/maps/documentation/geolocation/overview?hl=ja

## 実際の画面

<p align="center">
  検索画面<br>
  <img width="700" alt="スクリーンショット 2023-09-15 0 31 40" src="https://github.com/iwatanabee/restaurant-finder-app/assets/83575309/425870ed-09f0-4cd4-835a-c13bf5667694">
</p>

<p align="center">
  結果画面<br>
  <img width="700" alt="スクリーンショット 2023-09-16 20 49 59" src="https://github.com/iwatanabee/restaurant-finder-app/assets/83575309/12c9ba1b-f392-4941-8e06-63a0e303605e">
</p>

