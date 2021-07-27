import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import subprocess
import datetime


DURATION_INT = 3


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.time_left_int = DURATION_INT
        self.widget_counter_int = 0

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox)

        self.time_passed_qll = QtWidgets.QLabel()
        vbox.addWidget(self.time_passed_qll)
        self.starter_button = QtWidgets.QPushButton(text='start')
        self.stoper_button = QtWidgets.QPushButton('stop')
        vbox.addWidget(self.starter_button)
        vbox.addWidget(self.stoper_button)
        self.starter_button.clicked.connect(self.timer_start)
        self.stoper_button.clicked.connect(self.stoper)

    def timer_start(self):
        self.time_left_int = DURATION_INT

        self.my_qtimer = QtCore.QTimer(self)
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)

        self.update_gui()

    def timer_timeout(self):
        self.time_left_int -= 1

        if self.time_left_int == 0:
            #self.widget_counter_int = (self.widget_counter_int + 1) % 4
            #self.time_left_int = DURATION_INT
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, 'as.mp3'])
            self.my_qtimer.stop()
        self.update_gui()

    def update_gui(self):
        self.time_passed_qll.setText(str( str(datetime.timedelta(seconds=self.time_left_int))))

    def stoper(self):
       self.my_qtimer.stop()

app = QtWidgets.QApplication(sys.argv)
main_window = MyMainWindow()
main_window.show()
sys.exit(app.exec_())
