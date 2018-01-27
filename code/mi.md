Raspberry Pi 的應用 - Siri + HomeKit 讓我們的家電變自動也更智慧
https://l.facebook.com/l.php?u=http⋯⋯
 
从米家到 HomeKit，你只需要一个树莓派
https://l.facebook.com/l.php?u=http⋯⋯
 ESP8266 控制  
https://l.facebook.com/l.php?u=http⋯⋯



https://github.com/snOOrz/homebridg⋯⋯
new git
https://github.com/YinHangCode/home⋯⋯
install
https://github.com/nfarina/homebrid⋯⋯
 
 
sudo apt-get update
sudo apt-get upgrade 
sudo apt-get install git make

check g++ ver

> g++-4.9 -v
...
gcc version 4.9.2 (Raspbian 4.9.2-10) 
curl -sL https://l.facebook.com/l.php?u=https%3A%2F%2Fdeb.nodesource.com%2Fsetup_8.x&h=ATO8fjq3LcPXfhGVVArWpLuQg_KUXhnloIcUEf9-Ykmf3RpxqjanewtkcshTPy3uA6Ho18wbFJj86-gCD-NOkqeJxRtMyQKDKLHGdkLGSgfFVEaSLefy6pRrqCeWBmsgMWQxH_cyUtNz2WrNELz-v7_5GlEckw | sudo -E bash -
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
https://github.com/nfarina/homebrid⋯
