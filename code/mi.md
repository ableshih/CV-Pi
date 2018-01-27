Raspberry Pi 的應用 - Siri + HomeKit 讓我們的家電變自動也更智慧
http://blog.itist.tw/2017/11/how-to-building-apple-smart-home-solution-by-homebridge-on-raspberry-pi.html

 
从米家到 HomeKit，你只需要一个树莓派
https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DQ3V_UTvlcUE&h=ATMOkcMcSU4DP6_a51uQrD7eKLUGALGxjFj-AzB2oLQGUoF686DX-0nbow6m8JXJyYWmjceSvK_DlQXL8xd0hncAfITxaMg9FRX37wZEKXUfI-XlVbdS-KAvJRBn2Ir1Lu-9gsX1Z5sG5ryziXUICNph5kodYw

 ESP8266 控制
 http://benjenq.pixnet.net/blog/post/45202620-%E5%8F%AA%E7%AE%A1%E5%87%BA%E4%B8%80%E5%BC%B5%E5%98%B4%EF%BC%9A%E7%94%A8-siri-%E6%8E%A7%E5%88%B6%E5%AE%B6%E8%A3%A1%E7%9A%84%E8%80%81%E5%AE%B6%E9%9B%BB



https://github.com/snOOrz/homebridge-aqara

new git
https://github.com/YinHangCode/homebridge-mi-aqara

install
https://github.com/nfarina/homebridge/wiki/Running-Homebridge-on-a-Raspberry-Pi

 
 
sudo apt-get update
sudo apt-get upgrade 
sudo apt-get install git make

check g++ ver

> g++-4.9 -v
...
gcc version 4.9.2 (Raspbian 4.9.2-10) 
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -

sudo apt-get install -y nodejs 
sudo apt-get install libavahi-compat-libdnssd-dev 
sudo npm install -g homebridge
homebridge
ctrl+c
cd ~/.homebridge
nano config.json
https://sspai.com/post/38358

 {"bridge":{"name":"Homebridge","username":"CC:22:3D:E3:CE:23","port":51826,"pin":"233-62-666"},"platforms":[{"platform":"MiAqaraPlatform","sid":[""],"password":[""]}]} 

手機操作


開 米家 關於 一直點空白處直到出現 新的選項 選 網關信息

找到 mac addr 記錄
再按加密 找到 passwrd 16碼

都要小寫 塡入 config.json mac=sid password=password

sudo npm install -g homebridge-mi-aqara

homebridge
 
沒黃色訊息表示完成

apple 手機操作 加 homekit 進行配對

homebridge -D debug

https://github.com/nfarina/homebridge/blob/master/README.md

