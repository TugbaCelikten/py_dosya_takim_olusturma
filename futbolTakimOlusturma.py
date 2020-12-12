import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap, QStandardItemModel
from PyQt5.QtWidgets import *

#------------------------
W_WIDTH = 1000
W_HEIGHT = 500
W_X = 200
W_Y = 150

#------------------------


class TakimOlustur(QWidget):
    def __init__(self):
        super().__init__()
        self.Form()
        self.show()

    #-----------------------------------------------------
    def Form(self):
        #-----form ayarlari--------
        self.resize(W_WIDTH, W_HEIGHT)
        self.move(W_X, W_Y)
        self.setWindowTitle("Takım Oluştur")
        # -----/form ayarlari--------

        # -----layout ayarlari--------
        self.btn_takim_olustur = QPushButton("TAKIM OLUŞTUR", self)
        self.lbl_fb = QLabel(" -----FENERBAHÇE-----")
        self.lbl_bjk = QLabel(" -----BEŞİKTAŞ-----")
        self.lbl_goz = QLabel(" -----GÖZTEPE-----")

        self.table_oyuncular = QTableWidget()
        self.table_oyuncular.setFixedWidth(W_WIDTH/4)
        self.table_oyuncular.setColumnCount(2)
        self.table_oyuncular.setHorizontalHeaderLabels(['İsim', 'Takım'])

        self.table_fb = QTableWidget()
        self.table_fb.setFixedWidth(W_WIDTH/4)
        self.table_fb.setColumnCount(2)
        self.table_fb.setHorizontalHeaderLabels(['Ad', 'Soyad'])

        self.table_bjk = QTableWidget()
        self.table_bjk.setFixedWidth(W_WIDTH/4)
        self.table_bjk.setColumnCount(2)
        self.table_bjk.setHorizontalHeaderLabels(['Ad', 'Soyad'])

        self.table_goz = QTableWidget()
        self.table_goz.setFixedWidth(W_WIDTH/4)
        self.table_goz.setColumnCount(2)
        self.table_goz.setHorizontalHeaderLabels(['Ad', 'Soyad'])

        self.gb_fv = QGridLayout()
        self.gb_fv.addWidget(self.lbl_fb,1,0)
        self.gb_fv.addWidget(self.lbl_bjk, 1, 1)
        self.gb_fv.addWidget(self.lbl_goz, 1, 2)
        self.gb_fv.addWidget(self.table_fb,2,0)
        self.gb_fv.addWidget(self.table_bjk, 2, 1)
        self.gb_fv.addWidget(self.table_goz, 2, 2)

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        v_layout.addWidget(self.btn_takim_olustur)
        v_layout.addWidget(self.table_oyuncular)

        h_layout.addStretch()
        h_layout.addLayout(v_layout)
        h_layout.addStretch()
        h_layout.addLayout(self.gb_fv)
        h_layout.addStretch()

        self.setLayout(h_layout)
        # -----/layout ayarlari--------

        self.OyuncuTabloOlustur()
        self.btn_takim_olustur.clicked.connect(self.TakimlaraAyir)

    def OyuncuTabloOlustur(self):
        self.file = open("futbolcular.txt", "r", encoding="utf-8")
        for bilgi_futbulcu in self.file:
            self.futbolcu = bilgi_futbulcu.split(",")
            self.isim = self.futbolcu[0]
            self.takim = self.futbolcu[1]
            self.bilgi =[self.isim,self.takim]
            self.addTableRow(self.table_oyuncular, self.bilgi)

    #------------------------
    def addTableRow(self, table, bilgi):
        row = table.rowCount()
        table.setRowCount(row + 1)
        col = 0
        for item in bilgi:
            cell = QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col +=1

    # ------------------------

    def TakimlaraAyir(self):
        self.file = open("futbolcular.txt", "r", encoding="utf-8")
        for oyuncuTakim in self.file:
            oyuncuTakim = oyuncuTakim[:-1]  # sondaki '\n' karakterini siliyoruz.
            self.lst_oyuncu_takim = oyuncuTakim.split(", ")  # her satiri , ile ayrilmis sekilde list icine aliyoruz.

            self.isim = self.lst_oyuncu_takim[0]  # her satir icin isimleri buluyoruz
            self.takim = self.lst_oyuncu_takim[1]  # her satir icin takimlari buluyoruz
            self.bilgi = list(self.isim.split(" "))
            if(self.takim == "Fenerbahçe"):
                self.addTableRow(self.table_fb, self.bilgi)
            elif(self.takim == "Beşiktaş"):
                self.addTableRow(self.table_bjk, self.bilgi)
            elif(self.takim == "Göztepe"):
                self.addTableRow(self.table_goz, self.bilgi)

#------------------------
app = QApplication(sys.argv)
takimOlustur = TakimOlustur()
sys.exit(app.exec_())