---
theme: "theme/solarslide.css"
revealOptions:
    transition: "slide"
title: "工研コンテスト2022 電子ティンホイッスル2"
---

# 電子ティンホイッスル <br> ver.BLE-MIDI

ESP32に頼りまくって作る電子民族管楽器

新規性の二度漬け
Ⅲ類3年 鈴木 (Suzuke)

---

## 自己紹介

![](img/10-02-12-31-47.png)

* 鈴木輝 (Suzuke)
* 2年 Ⅲ類物理工学プログラム
* 死にかけツイッター：@suzukeh1
* https://slide.suzuke.dev/
* 逆RTAやりがち (今回もね)

今回が工研の活動として2回目の制作(たぶん)

---

## 電子ティンホイッスル...？

<img src="https://cdn.discordapp.com/attachments/843919142930874408/891508649611108362/image0.jpg" style="width: 60%; border: none; box-shadow:none;transform:rotate(0deg)"/>

ArduinoとBMP180(大気圧センサ)かで作った電子民族管楽器

---

## やりたかったこと

大ざっぱに：**電子ティンホイッスル**が作りたい

<small>既存の電子管楽器例</small><br>
<img src="https://m.media-amazon.com/images/I/71tTTeWg3xL._AC_SL1500_.jpg" style="width: 5%; border: none; box-shadow:none;transform:rotate(0deg)"/> &emsp; <img src="https://static.roland.com/assets/images/products/gallery/aerophone_dr_gal.jpg" style="width: 8%; border: none; box-shadow:none;transform:rotate(0deg)"/>

--

そもそも
### ティンホイッスルとは

アイルランド周辺でよく用いられる民族楽器

非常に簡単な構造と奏法

イメージとしては、簡単すぎるリコーダー

--

民族楽器なので、電子化の波はあるものの未達<br>(バグパイプは既にある)

→じゃあこれは新規性アリだよね！！！

--

### 真面目な理由

* 音を抑える方法がほとんどなく、夜は練習できない
* 運指・奏法が簡単なので、DAW等の操作にも使えるかも？
* そもそも自分がキーボードできないので↑にメリットを感じた

---

### 去年の達成状況

* 軽押下圧のボタン or タッチセンサによる**素早い運指操作**<br>
→1MΩの抵抗を用いたタッチセンサで達成<br>
→とはいえ、機構が雑すぎて発表日以降全然動作せず<br>

* **MIDI送信**によるソフトシンセやDAWの操作<br>
→原因不明で動作せず未達成 MIDI部単体は動作

* **息の強さ**でオクターブ操作<br>
→大気圧センサを使用

--

(去年のスライド)
### MIDI

**mocoLUFA**=Arduino UnoをUSB-MIDIデバイス化するファームウェア

単純にスケッチに書いて送信→Winダメ Macいける<br>怪しい雰囲気だができた

各センサ部の処理に合わせて、送信 →死

**!!!未解決!!!**

そもそもNanoとかLeonardなら、ファームウェアなしでUSBMIDIライブラリを使えばできるかも？

--

(去年のスライド)
### ブレス
たぶん一番新規性がマシなところ

息の強さでオクターブ切り替えをするのがメインのものがなさそう (やろうと思えばできそうだが)

物理的にも、これにBMP180を入れてあるだけ<br>
<img src="https://www.packplus.jp/html/user_data/assets/img/product/1018128-1.jpg" style="width: 20%; border: none; box-shadow:none;transform:rotate(0deg)"/>
<img src="https://akizukidenshi.com/img/goods/C/M-12854.jpg" style="width: 30%; border: none; box-shadow:none;transform:rotate(0deg)"/>


でも結構感度はいい

---

### 何が変わったのか？

* まともなタッチセンサ

* BLE-MIDI対応

* 見た目が**素晴らしい**ブレスセンサ部


--

### ESP32とBMP180使ってます！！！！

なんか見たな...

![](img/10-02-13-26-33.png)

---

実演と解説

---

### 展望

~~見た目ぐらいじゃね...?~~

* 若干の遅延がある<br>
とはいえ、BLE-MIDIの遅延ってこんなもんなのでしょうがない感じ<br>
あとはUSB-MIDIにするぐらいか（ライブラリ変えるだけ）

* ベロシティ対応

---

# 〜完〜