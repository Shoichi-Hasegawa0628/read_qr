# 'read_qr' Package

The `read_qr` is to read qr.

*   Maintainer: Shoichi Hasegawa ([hasegawa.shoichi@em.ci.ritsumei.ac.jp](mailto:hasegawa.shoichi@em.ci.ritsumei.ac.jp)).
*   Author: Shoichi Hasegawa ([hasegawa.shoichi@em.ci.ritsumei.ac.jp](mailto:hasegawa.shoichi@em.ci.ritsumei.ac.jp)).

**Content:**

*   [Setup](#Setup)
*   [Launch](#launch)
*   [Files](#files)
*   [References](#References)


## Setup

*   pip install pyzbar
*   pip install qrcode
*   apt-get install python3-zbar

## Launch

~~~
roslaunch read_qr read_qr.launch
~~~

## Files

 - `README.md`: Read me file (This file)

 - `read_qr.py`: Read QR-code by using image topic.

 - `generate2read_qr.py`:  Generate QR-code by input sentense, and read QR-code by using image.

## References
