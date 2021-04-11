from ui_calc import*
import sys
class Window(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.evaluate)
        self.show()
    def evaluate(self):
        v1=self.lineEdit.text()
        v2=self.lineEdit_3.text()
        op=self.comboBox.currentText()
        self.lineEdit_2.setText(str(eval(v1+op+v2)))
if __name__ == '__main__':
     app = QApplication(sys.argv)
     mainWin = Window()
     sys.exit(app.exec_())
