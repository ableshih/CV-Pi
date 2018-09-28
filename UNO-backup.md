```
http://www.ladyada.net/learn/avr/avrdude.html
https://www.youtube.com/watch?v=Jw-ZSkzd-uY

https://reprap.org/wiki/Geeetech_GT2560
https://www.geeetech.com/gt2560-3d-printer-controller-board-p-915.html
http://www.geeetech.com/Documents/Users%20Manual%20of%20GT2560.pdf
https://www.geeetech.com/Documents/Users%20Manual%20of%20GT2560.pdf


1.找到
C:\Program Files (x86)\Arduino\hardware\tools\avr\bin\avrdude.exe
2.找到
C:\Program Files (x86)\Arduino\hardware\tools\avr\etc\avrdude.conf
3. cd Program Files (x86)\Arduino\hardware\tools\avr\bin\
4. 接上板子
5. 執行 Repetier-Host
按 連接 讓 Repetier-Host 自動抓到 comport & baudRate 
6. open C:\Program Files (x86)\Arduino\hardware\arduino\avr\boards.txt
找到相對應的板子 
.upload.protocol=arduino (就是 -c arduino -P)
-p m328p -c (如下表找到對應IC型號)

avrdude: AVR Part "uno" not found.

Valid parts are:
  uc3a0512 = AT32UC3A0512
  c128     = AT90CAN128
  c32      = AT90CAN32
  c64      = AT90CAN64
  pwm2     = AT90PWM2
  pwm216   = AT90PWM216
  pwm2b    = AT90PWM2B
  pwm3     = AT90PWM3
  pwm316   = AT90PWM316
  pwm3b    = AT90PWM3B
  1200     = AT90S1200
  2313     = AT90S2313
  2333     = AT90S2333
  2343     = AT90S2343
  4414     = AT90S4414
  4433     = AT90S4433
  4434     = AT90S4434
  8515     = AT90S8515
  8535     = AT90S8535
  usb1286  = AT90USB1286
  usb1287  = AT90USB1287
  usb162   = AT90USB162
  usb646   = AT90USB646
  usb647   = AT90USB647
  usb82    = AT90USB82
  m103     = ATmega103
  m128     = ATmega128
  m1280    = ATmega1280
  m1281    = ATmega1281
  m1284    = ATmega1284
  m1284p   = ATmega1284P
  m1284rfr2 = ATmega1284RFR2
  m128rfa1 = ATmega128RFA1
  m128rfr2 = ATmega128RFR2
  m16      = ATmega16
  m161     = ATmega161
  m162     = ATmega162
  m163     = ATmega163
  m164p    = ATmega164P
  m168     = ATmega168
  m168p    = ATmega168P
  m168pb   = ATmega168PB
  m169     = ATmega169
  m16u2    = ATmega16U2
  m2560    = ATmega2560
  m2561    = ATmega2561
  m2564rfr2 = ATmega2564RFR2
  m256rfr2 = ATmega256RFR2
  m32      = ATmega32
  m324p    = ATmega324P
  m324pa   = ATmega324PA
  m325     = ATmega325
  m3250    = ATmega3250
  m328     = ATmega328
  m328p    = ATmega328P
  m329     = ATmega329
  m3290    = ATmega3290
  m3290p   = ATmega3290P
  m329p    = ATmega329P
  m32m1    = ATmega32M1
  m32u2    = ATmega32U2
  m32u4    = ATmega32U4
  m406     = ATMEGA406
  m48      = ATmega48
  m48p     = ATmega48P
  m48pb    = ATmega48PB
  m64      = ATmega64
  m640     = ATmega640
  m644     = ATmega644
  m644p    = ATmega644P
  m644rfr2 = ATmega644RFR2
  m645     = ATmega645
  m6450    = ATmega6450
  m649     = ATmega649
  m6490    = ATmega6490
  m64rfr2  = ATmega64RFR2
  m8       = ATmega8
  m8515    = ATmega8515
  m8535    = ATmega8535
  m88      = ATmega88
  m88p     = ATmega88P
  m88pb    = ATmega88PB
  m8u2     = ATmega8U2
  t10      = ATtiny10
  t11      = ATtiny11
  t12      = ATtiny12
  t13      = ATtiny13
  t15      = ATtiny15
  t1634    = ATtiny1634
  t20      = ATtiny20
  t2313    = ATtiny2313
  t24      = ATtiny24
  t25      = ATtiny25
  t26      = ATtiny26
  t261     = ATtiny261
  t28      = ATtiny28
  t4       = ATtiny4
  t40      = ATtiny40
  t4313    = ATtiny4313
  t43u     = ATtiny43u
  t44      = ATtiny44
  t45      = ATtiny45
  t461     = ATtiny461
  t5       = ATtiny5
  t84      = ATtiny84
  t85      = ATtiny85
  t861     = ATtiny861
  t88      = ATtiny88
  t9       = ATtiny9
  x128a1   = ATxmega128A1
  x128a1d  = ATxmega128A1revD
  x128a1u  = ATxmega128A1U
  x128a3   = ATxmega128A3
  x128a3u  = ATxmega128A3U
  x128a4   = ATxmega128A4
  x128a4u  = ATxmega128A4U
  x128b1   = ATxmega128B1
  x128b3   = ATxmega128B3
  x128c3   = ATxmega128C3
  x128d3   = ATxmega128D3
  x128d4   = ATxmega128D4
  x16a4    = ATxmega16A4
  x16a4u   = ATxmega16A4U
  x16c4    = ATxmega16C4
  x16d4    = ATxmega16D4
  x16e5    = ATxmega16E5
  x192a1   = ATxmega192A1
  x192a3   = ATxmega192A3
  x192a3u  = ATxmega192A3U
  x192c3   = ATxmega192C3
  x192d3   = ATxmega192D3
  x256a1   = ATxmega256A1
  x256a3   = ATxmega256A3
  x256a3b  = ATxmega256A3B
  x256a3bu = ATxmega256A3BU
  x256a3u  = ATxmega256A3U
  x256c3   = ATxmega256C3
  x256d3   = ATxmega256D3
  x32a4    = ATxmega32A4
  x32a4u   = ATxmega32A4U
  x32c4    = ATxmega32C4
  x32d4    = ATxmega32D4
  x32e5    = ATxmega32E5
  x384c3   = ATxmega384C3
  x384d3   = ATxmega384D3
  x64a1    = ATxmega64A1
  x64a1u   = ATxmega64A1U
  x64a3    = ATxmega64A3
  x64a3u   = ATxmega64A3U
  x64a4    = ATxmega64A4
  x64a4u   = ATxmega64A4U
  x64b1    = ATxmega64B1
  x64b3    = ATxmega64B3
  x64c3    = ATxmega64C3
  x64d3    = ATxmega64D3
  x64d4    = ATxmega64D4
  x8e5     = ATxmega8E5
  ucr2     = deprecated, use 'uc3a0512'


  
for UNO
avrdude -C ..\etc\avrdude.conf -p m328p -c arduino -P COM6 -b 115200 -U flash:r:flash_backup.hex:i
avrdude -C ..\etc\avrdude.conf -p m328p -c arduino -P COM6 -b 115200 -U eeprom:r:eeprom_backup.hex:i

for mage
avrdude -C ..\etc\avrdude.conf -p m2560 -c wiring -P COM6 -b 115200 -U flash:r:flash_backup.hex:i
avrdude -C ..\etc\avrdude.conf -p m2560 -c wiring -P COM6 -b 115200 -U eeprom:r:eeprom_backup.hex:i

---------------------------
uno

C:\Program Files (x86)\Arduino\hardware\tools\avr\bin>avrdude -C ..\etc\avrdude.conf -p m328p -c arduino -P COM6 -b 115200 -U flash:r:c:\tools\flash_backup.hex:i

avrdude: AVR device initialized and ready to accept instructions

Reading | ################################################## | 100% 0.02s

avrdude: Device signature = 0x1e950f (probably m328p)
avrdude: reading flash memory:

Reading | ################################################## | 100% 6.11s

avrdude: writing output file "c:\tools\flash_backup.hex"

avrdude: safemode: Fuses OK (E:00, H:00, L:00)

avrdude done.  Thank you.


C:\Program Files (x86)\Arduino\hardware\tools\avr\bin>
-----------------------------
Arduino IDE 改 code 並燒入 使 fw 變動

再用 XLoader.exe 把備份 fw 燒入 看是否與原來 fw 一致



============================
-C = avrdude.conf file location
-p = board type
-c = board upload protocol
-P = COM port
-b = baud rate speed
-U = memory
:r = read
:filename.hex:i

```



















