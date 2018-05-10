https://github.com/rockowitz/ddcutil

Query and change Linux monitor settings using DDC/CI and USB http://www.ddcutil.com

install step
https://github.com/rivy/ddccontrol
https://github.com/rivy/ddccontrol-db 


$ ddcutil --help
$ man 1 ddcutil

$ ddcutil detect

# ddcutil getvcp 10
# ddcutil vcpinfo 0x10

# ddcutil getvcp known

# ddcutil setvcp 10 50
# ddcutil setvcp 10 0x32

VCP 10  C 50 100

VCP 60 SNC x03

VCP DF CND xff xff x02 x00

VCP 73 T x01020304

VCP 84 ERR

$ ddcutil vcpinfo

$ ddcutil detect --verbose

$ ddcutil capabilities --display 4 --verbose

$ ddcutil getvcp known --bus 6

ddcutil vcpinfo profile --terse

ddcutil setvcp 60 01020304F1F2FEFF

ddcutil vcpinfo table

# ddcutil vcpinfo 60 --verbose

$ ddcutil interrogate




# Python API
Symbol names begin with "ddcs_" or "DDCS_" (for DDCutil Swig).

Currently Python 2.7 only.

Generated files: - _ddc_swig.so - ddc_swig.py

Normally installed to ${pkgexecdir}/dist-packages ??

Issue: Depending on $(prefix) value, make install will install these files to ... If installed to /usr/local... python will not mormally see these files. Directory ... must be added to the Python path. This can be done in one several ways: - Modify PYTHONPATH globally. See generatd fragment src/swig/... - Modify PYTHONPATH for a single Python invocation. See generated script src/swig/... - Modify PTYHONPATH within a Python script. See commented out lines in sample script src/swig/test_swig.py

For a fuller discussion on modifying PYTHONPATH, see http://ask.xmodulo.com/change-syspath-pythonpath-python.html.


PyDDC: Python frontend for setting backlight brightness with ddcutil (Linux)
http://www.itdadao.com/articles/c19a1118355p0.html

PyDDC
https://github.com/mdoege/PyDDC

用cron 執行bashrc 裡定義的function
http://www.dlifep.com/2017/12/07/%E7%94%A8-cron-%E6%89%A7%E8%A1%8C-bashrc-%E9%87%8C%E5%AE%9A%E4%B9%89%E7%9A%84-function/

https://passthroughpo.st/switching-monitor-inputs-software-ddc/

https://wiki.archlinux.org/index.php/backlight

DDC/CI protocol in Windows C# code
https://github.com/rivy/DDCMonitorManager
https://github.com/alexhorn/BrightnessControl

https://livelace.org/posts/2018/Jan/06/ddc-dell/

https://displaylink.org/forum/showthread.php?t=65289

http://www.omgubuntu.co.uk/2017/05/adjust-external-monitor-brightness-ubuntu
https://github.com/lordamit/Brightness














Subcommand	Function
detect	report monitors detected
capabilities	report a monitor's capabilities string
vcpinfo (feature-code-or-group)	list VCP features codes that ddcutil knows how to interpret
getvcp feature-code-or-group	report a single VCP feature value, or a group of values
setvcp feature-code new-value	set a single VCP feature value
dumpvcp filename	save color related VCP feature values to a file
loadvcp filename	restore color related VCP feature values from a file
environment	explore the ddcutil installation environment (other than USB)
usbenv	explore USB aspects of the ddcutil installation environment
probe	explore the capabilities string and probe the features of a single monitor
interrogate	collect maximal information for problem diagnosis
chkusbmon /dev/hiddevN	used by udev rules to test if a USB device represents a monitor







ddcutil --help
man 1 ddcutil

# ./configure
# make
# sudo make install

