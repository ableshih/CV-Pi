```
https://www.youtube.com/watch?v=lAKyZd63_ns

DOWNLOADS
Marlin Firmware http://marlinfw.org
Alternative board support JSON files https://github.com/arduino/Arduino/wi...
U8Glib https://github.com/olikraus/u8glib 

Enjoying the videos? Support my work on Patreon! https://www.patreon.com/toms3dp


=====================
下載
----------------------
http://marlinfw.org/meta/download/
The latest release (1.1.x.zip … 1.1.9)

https://github.com/MarlinFirmware/Marlin/archive/1.1.x.zip

=====================
解壓
----------------------



=====================
找到對應的型號
----------------------
C:\Users\5578\Desktop\Marlin-1.1.x\Marlin-1.1.x\Marlin\example_configurations

C:\Users\5578\Desktop\Marlin-1.1.x\Marlin-1.1.x\Marlin\example_configurations\Creality\Ender-3

_Bootscreen.h
_Statusscreen.h
Configuration.h
Configuration_adv.h

C:\Users\5578\Desktop\Marlin-1.1.x\Marlin-1.1.x\Marlin
copy 到主程式目錄 覆蓋 四個檔案

=====================
編譯
----------------------
安裝 Arduino IDE

開啟 C:\Users\5578\Desktop\Marlin-1.1.x\Marlin-1.1.x\Marlin\Marlin.ino

按勾勾 Verify

會出現錯誤
**********
Arduino: 1.8.5 (Windows 10), Board: "Arduino/Genuino Mega or Mega 2560, ATmega2560 (Mega 2560)"

In file included from sketch\pins_SANGUINOLOLU_12.h:41:0,

                 from sketch\pins_MELZI.h:32,

                 from sketch\pins_MELZI_CREALITY.h:35,

                 from sketch\pins.h:207,

                 from sketch\MarlinConfig.h:40,

                 from sketch\ultralcd.cpp:23:

pins_SANGUINOLOLU_11.h:55: error: #error "Oops!  Make sure you have 'Sanguino' selected from the 'Tools -> Boards' menu."

   #error "Oops!  Make sure you have 'Sanguino' selected from the 'Tools -> Boards' menu."

    ^

In file included from sketch\ultralcd.cpp:96:0:

sketch\ultralcd_impl_DOGM.h:46:20: fatal error: U8glib.h: No such file or directory

 #include <U8glib.h>

                    ^

compilation terminated.

exit status 1
#error "Oops!  Make sure you have 'Sanguino' selected from the 'Tools -> Boards' menu."

This report would have more information with
"Show verbose output during compilation"
option enabled in File -> Preferences.
**********
C:\Users\5578\Desktop\Marlin-1.1.x\Marlin-1.1.x\Marlin\pins_SANGUINOLOLU_11.h
找到
https://raw.githubusercontent.com/Lauszus/Sanguino/master/package_lauszus_sanguino_index.json

貼到
Arduino IDE
File\Preferences\Additional Boards Manager URLs: https://raw.githubusercontent.com/Lauszus/Sanguino/master/package_lauszus_sanguino_index.json
按OK

Arduino IDE
Tools\Boards Manager\
輸入 sanguino
找到 點選 Install

重選板子
Arduino IDE
Tools\Boards\sanguino

重選處理器
#if !defined(__AVR_ATmega644P__) && !defined(__AVR_ATmega1284P__)
Arduino IDE
Tools\Processor\ATmega1284 or ATmega1284P(16 MHz)

Arduino IDE
按勾勾 Verify 會再度出現錯誤

少了 U8glib

olikraus U8glib

https://github.com/olikraus/u8glib

https://bintray.com/olikraus/u8glib/Arduino

https://bintray.com/olikraus/u8glib/download_file?file_path=u8glib_arduino_v1.18.1.zip

u8glib_arduino_v1.18.1.zip

Arduino IDE
Sketch\Include Library\Add .ZIP Library...

找看看有沒有 U8glib
Arduino IDE
Sketch\Include Library\

Arduino IDE
按勾勾 Verify 終於成功了

產生hex
Arduino IDE
Sketch\Verify/Compile

檔案所在
C:\Users\5578\AppData\Local\Temp\arduino_build_982146

=====================
燒到板子
----------------------
USB 接上印表機與電腦連線

Arduino IDE
Sketch\Upload

理論上不會成功

因為 為了節省成本 bootloader
=====================
bootloader ICSP
----------------------
https://www.youtube.com/watch?v=oZVTYpHnpIw

Arduino IDE
Tools\Programmer\USBtinyISP

Arduino IDE
Tools\Programmer\USBtinyISP

=====================
TH3D Studio
----------------------
http://www.wch.cn/download/CH341SER_EXE.html



=====================

----------------------



=====================

----------------------



=====================

----------------------



=====================

----------------------



=====================

----------------------


```
