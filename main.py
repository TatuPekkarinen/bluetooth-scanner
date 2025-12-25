import asyncio
import datetime
import threading 
import sys

from bleak import BleakScanner
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


async def bt_scanner():
    device_list = []
    devices = await BleakScanner.discover()
    for device in devices:
        device_list.append(str(device))
    return device_list

def window():
    def bt_updates():
        system_date = datetime.datetime.now()
        main_label.setText(f"BLUETOOTH DEVICES / {system_date}\n{"\n".join(asyncio.run(bt_scanner()))}")

    app = QApplication(sys.argv)

    window = QWidget()
    main_label = QLabel(window)
    window.setGeometry(1000,1000,1000,1000)
    app.setStyleSheet("QLabel{font-size: 19pt;}")

    timer = QtCore.QTimer()
    timer.timeout.connect(bt_updates)
    timer.setInterval(5)
    timer.start()
    
    bt_updates()

    window.setWindowTitle("tt-bluetooth-scanner")

    window.show()
    sys.exit(app.exec_())
   
def main():
    window()

if __name__ == "__main__":
    main()
