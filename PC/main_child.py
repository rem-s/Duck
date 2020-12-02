from network.tcp import * 
from gui.qtwindow import *
from PyQt5.QtGui import QApplication

#画像処理初期化
ip = "127.0.0.1"
tcp_img = TCP(ip, 8894, server_flag=True)
tcp_sonic = TCP(ip, 8895, server_flag=True)
tcp_acc = TCP(ip, 8896, server_flag=True)
tcp_sound = TCP(ip, 8897, server_flag=True)

#PYQT初期化
app = QApplication.instance()
if app is None:
	app = QApplication([])
win = QtMultiWindow(tcp_sonic, tcp_acc, tcp_img, tcp_sound)

win.show()
sys.exit(app.exec_())

