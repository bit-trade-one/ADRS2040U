# ADRS2040U の動作確認
　本ドキュメントでは，ADRS2040UをRaspberry Pi 4に搭載し，動作確認を行います．  
　ADRS2040UとRaspberry PiのインタフェースはI2C，SPI，およびSWDが接続されていますが，ここではI2Cを使用します．  
　センサーは，高精度摂氏直読温度センサLM35を使用し，Raspberry Pi PicoのADCを使用して温度データを読み取ります．  
　取得した温度データはI2C経由でRaspberry Pi 4で受取り，コンソールに結果を表示します．  

# ハードウェアの構成

全体構成を図1に示します．(開発機のためピンヘッダが実装されています。)    
![image](https://user-images.githubusercontent.com/85532743/209271090-6c88725f-baed-40f3-8746-a23dc9d075ec.png)

### ADRS2040U  
　ADRS2040UにはRaspberry Pi Pico互換のピンコネクタJ7，J9があります。J9にLM35をジャンパワイヤー等で図2の様に接続します．  
 ![image](https://user-images.githubusercontent.com/85532743/209271102-fdab27ed-0a72-4ed9-8a02-e979335039ce.png)  
 
### Raspberry Pi 4    
　Raspberry Pi 4のGPIOコネクタにADRS2040Uを搭載します．  


# ソフトウェアの構成

### DRS2040U
　ADRS2040UのファームウェアはMicroPython上で動作するものとします．  
 MicroPythonのIDEはRaspberry Pi 4に標準でインストールされているThonnyを使用します．
### Raspberry Pi 4
　Raspberry Pi 4の実行環境は，標準でインストールされているPython3とします．  
 動作確認用のデモソフトはPythonで作成し，コンソール(LXTerminal)上で実行，および結果の確認を行います．

# ソフトウェアのインストールと初期設定

###  ADRS2040U　
　ADRS2040UにMicroPythonを，以下の手順で書込みます．  
① ADRS2040Uの切離し  
　ADRS2040UをRaspberry Pi 4から切離します．  
② BOOTモードでの起動  
　BOOTSELボタンを押しながらWindows PC等のUSBに接続します．ADRS2040Uが新たなドライブとして認識され，ドライブを開くと図3の様なフォルダが表示されます．  
 ![image](https://user-images.githubusercontent.com/85532743/209271127-14efdf54-2035-45dd-8116-347ff10f9477.png)  
③ ブラウザの表示  
　INDEX.HTMをダブルクリックすると，図4の様にWebブラウザにRaspberry Piのホームページが表示されます．  
![image](https://user-images.githubusercontent.com/85532743/209271412-ccc582df-0405-4395-aa56-c2a1dded8fea.png)  

④ MicroPythonのダウンロード  
　Raspberry Pi DocumentationからMicroPythonを選択し，次に図5の画面でRaspberry Pi Picoを選択し，デスクトップ等適当なフォルダにMicroPythonのファームウェアをダウンロードします．  
 ![image](https://user-images.githubusercontent.com/85532743/209271507-db2a20ad-1e55-41cd-aee6-c98c166f38b6.png)  

⑤ MicroPythonの書込み  
　ダウンロードしたMicroPythonのファームウェアを図6のフォルダにドラッグアンドドロップします．  
 ![image](https://user-images.githubusercontent.com/85532743/209271558-cbf2c10c-2893-40b0-a9e6-c02d4e5b8c2d.png)  

 
⑥ ADRS2040U接続  
　ADRS2040UをRaspberry Pi 4に装着します．  
### Raspberry Pi 4
　Raspberry Pi 4の起動用のSDカードは，Windows PC等にインストールしたRaspberry Pi Imagerで作成します．ここでは，2022年9月時点で最新のものを使用しています．(図7)  
 ![image](https://user-images.githubusercontent.com/85532743/209271587-5d43eee3-1430-4d06-a5ec-87141252a533.png)  

・Raspberry Pi OS Full(32-bit)
・リリース時　2022-09-06
　書込み後，SDカードをRaspberry Pi 4に装着・起動します．  
 Raspberry Piメニューの「設定」「Raspberry Piの設定」を起動し 図8の様に「SPI」，「I2C」の設定をONにします．  
 また，必要に応じて「SSH」や「VNC]のボタンをONにしてください．  
![image](https://user-images.githubusercontent.com/85532743/209271632-9547ea00-0035-4f87-9897-76054670f94e.png)  

# 接続の確認

　ADRS2040UをRaspberry Pi 4に搭載し，USB Type-CコネクタでADRS2040UとRasuperry Pi4を接続し，電源を投入します．  
　次に，Raspberry Piメニューの「プログラミング」から「Thonny Python IDE」を起動します．(図9)  
 ![image](https://user-images.githubusercontent.com/85532743/209271663-2413db8b-9559-414c-82ad-d9d0e302ad46.png)  

　Thonny IDEにより，接続されているADRS2040UのMicroPythonと自動接続されていれば，ウィンドウ右下に「MicroPython(Raspberry Pi Pico」と表示され，  
  図9の様にShellにMicroPythonの起動メッセージとプロンプトが表示されます．  
　もし，MicroPythonが接続されていない場合は，ウインドウ右下をクリックし，図10の様に表示されるメニューから「MicroPython(Raspberry Pi Pico」を選択します．  
　また，「MicroPython(Raspberry Pi Pico」を選択できない場合には，ハードウェアやMicroPythonの書込みを再確認してください．  
 ![image](https://user-images.githubusercontent.com/85532743/209271687-308bed3f-9b97-4988-9c57-25cf3a5e3f91.png)  

# 動作確認用サンプルプログラムについて

・ADRS2040U  
　ADRS2040U側で動作させるサンプルプログラムは以下の２つのモジュールから構成します．(表1)  
 
 表1 モジュール一覧 

 | 関数名 | 機能 |
 | --- | --- | 
 | i2cSlave.py | Raspberry Pi PicoのMicroPythonでi2cスレーブデバイスを実現するためのモジュール | 
 | main.py | I2cアドレス0x41として初期化し、マスタからの以下のコマンドに従い、LM35データの取得やLEDのON/OFFを行う | 
 
① i2cSlave.py(リスト1)  
　Raspberry Pi PicoのMicroPythonでI2Cのスレーブデバイスを実現するためのモジュールです．  
 danjperron氏によって[Raspberry Piフォーラムに投稿](https://forums.raspberrypi.com/viewtopic.php?t=302978#p1823668)されたi2cSlave.pyモジュールに表2に示すの2つの関数を追加しています．
 
  表2 追加関数
 
 | 関数名 | 機能 |
 | --- | --- | 
 | getWord() | 2バイトデータの読出し関数 | 
 | putWord() | 2バイトデータの書込み | 
 
② main.py(リスト2)  
　I2cスレーブアドレス(0x41)としてデバイスを初期化し，マスタからのコマンドに従い，LEDの点灯/消灯制御やLM35の温度データの取得を行います．  
 使用できるコマンドとパラメータの種類を表2に示します．  
・Raspberry Pi 4  
　Raspberry Pi側のソフトをリスト3に示します．  
 
 表3 i2c コマンドとパラメータ

 | コマンド | パラメータ | 機能 |
 | --- | --- | --- | 
 | 0x10 | なし | LM35温度データの取得(WORDデータ) | 
 | 0x20 | 0x0000 | オンボードLEDの消灯 | 
 | 0x20 | 0x0001 | オンボードLEDの点灯 | 
 
　以下の処理を1秒毎に実施します．  
① LEDを点灯  
② 温度データ(2バイト)の読出しとコンソール表示  
③ LEDのを消灯  

# 動作確認用サンプルプログラムの実行

　サンプルプログラム3種を，図11の様にRaspberry Pi 4上に準備します．
 [サンプルプログラムはこちらより取得可能です。](https://github.com/bit-trade-one/ADRS2040U/tree/master/Sample/ADRS2040U_SampleSource)  
 ![image](https://user-images.githubusercontent.com/85532743/209272535-6ad654c6-fb1a-4411-8d3b-6c0ce8a0028f.png)  

　Thonnyを開き，3つのファイルをオープンします．Thonnyの「表示」メニューから「ファイル」を選択しておくことにより，図12の様にファイルの一覧表示とファイルの操作を行うことができます．
 ![image](https://user-images.githubusercontent.com/85532743/209272564-f5793041-ff09-4cfe-b63c-e7f68cf83797.png)  
 
　ADRS2040Uで動作させるプログラム２種(i2cSlave.py，main.py)を順に左側のファイル一覧から選択し，右クリックで表示されるメニューの「Upload to /」でADRS2040Uに転送します．  
 転送されたファイルは図13の様に左下のファイル一覧の「Raspberry Pi Pico」のペインに表示されます．  
 
 ![image](https://user-images.githubusercontent.com/85532743/209272595-e23230f5-268c-47c5-a95b-597865fcc67f.png)  

　ADRS2040U上でmain.py等がすでに起動していると，Thonnyでファイル操作等ができない場合があります．  
 Thonnyの「表示」「Shell」でShellを表示すると，「Backend terminated or disconnected. Use 'Stop/Restart' to restart」などの文字列が表示されている場合は，  
 ADRS2040UがThonnyの制御下でないことを示しています．この場合は，一旦Stopアイコンで実行中のプログラムを停止した後，ファイル操作を行ってください．  
　転送が完了したら，左下のペインのmain.pyを選択し、実行ボタンでプログラムを起動します．  
　Raspberry Pi 4側で動くADRS2040U_test.pyについては，コンソール(LXTerminal)から次のコマンドで直接実行します．  
 
```
$ python3 ADRS2040U_test.py
```

# 実行結果の確認

  ADRS2040U側のプログラム，およびRaspberry Pi 4側のプログラムの両方を実行後，コンソールには図14の様にLM35の温度計測結果が1秒毎に表示されます．    
  ![image](https://user-images.githubusercontent.com/85532743/209272682-cfb868fc-6df1-45ae-a931-18aabe76e9de.png)  
  
　実行中のI2Cバスの状態をロジックアナライザで観測した結果を図15に示します． 
  コマンド0x20でLEDを点灯し，コマンド0x10で2バイトの温度データを取得し，コマンド0x20でLEDを消灯しています．  
  ![image](https://user-images.githubusercontent.com/85532743/209273785-50d680af-cbc4-453c-ad37-dff82153d16c.png)  


# まとめ

 今回I2Cバスを使用して，ADRS2040UとRaspberry Pi 4の通信を実施しましたが，本ボードには他にSPIバスも利用可能です．  
 また，本ボードにはありませんが，シリアル通信を利用することも可能です．使用目的に合致したインタフェースを持つオリジナルHAT開発の参考にしていただければ幸いです．  
