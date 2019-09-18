# -*- coding: utf-8 -*-
# @Time    : 2019-09-18 17:48
# @Author  : 王碧野
# @FileName: pyqt_demo.py
# @Software: PyCharm


import sys
from PyQt5.QtCore import QThread, QTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLCDNumber, QPushButton

# 定义全局变量, 因为需要修改 sec 的值, 用 global 修饰
global sec
sec = 0


class WorkThread(QThread):

    trigger = pyqtSignal()

    def __int__(self):
        super().__init__()

    def run(self):
        for i in range(2000000000):
            pass

        # 循环完毕后发出信号
        self.trigger.emit()


def count_time():
    global sec
    sec += 1
    # LED显示数字+1
    lcdNumber.display(sec)


def work():
    # 计时器每秒计数
    timer.start(1000)
    # 计时开始
    workThread.start()
    # 当获得循环完毕的信号时，停止计数
    workThread.trigger.connect(time_stop)


def time_stop():
    timer.stop()
    print("运行结束用时", lcdNumber.value())
    global sec
    sec = 0


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(300, 120)

    # 垂直布局类QVBoxLayout
    layout = QVBoxLayout(window)

    # 加个显示屏
    lcdNumber = QLCDNumber()
    layout.addWidget(lcdNumber)
    button = QPushButton("测试")
    layout.addWidget(button)

    timer = QTimer()
    workThread = WorkThread()

    button.clicked.connect(work)

    # 每次计时结束，触发 countTime
    timer.timeout.connect(count_time)

    window.show()
    sys.exit(app.exec_())
