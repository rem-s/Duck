from network.tcp import * 
from control.gui.qtwindow import *
from PyQt5.QtGui import QApplication

#画像処理初期化
tcp_sonic = TCP("192.168.0.68", 37546, server_flag=True)
tcp_acc = TCP("192.168.0.68", 37547, server_flag=True)
tcp_img = TCP("192.168.0.68", 37548, server_flag=True)

#PYQT初期化
app = QApplication.instance()
if app is None:
	app = QApplication([])
recorder = VoiceRecorder()
#recorder.setDeviceIndex(1)
win = QtMultiWindow(tcp_sonic, tcp_acc, tcp_img, recorder)

win.show()
sys.exit(app.exec_())