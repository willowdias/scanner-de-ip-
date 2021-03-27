from logging import error
from os import close
import sys
from time import sleep, time
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QLabel, QComboBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QIcon
from tela import*
from PyQt5.QtWidgets import *
import socket
import subprocess
import threading
import urllib.request as urllib2
from requests import*
import random
import re, uuid

import random
class sistema(QMainWindow,QDialog,):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("iconescanner/inicial.ico"))
         #PAGINA   
        self.ui.tela1.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))
        self.ui.tela2.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page2))
        # comboxIP==
        self.comobox_ip()                                  
        #
        self.ui.BT_VER.clicked.connect(self.mostra)
        self.ui.BT_Scanner.clicked.connect(self.scanner)
        self.ui.BT_deleta.clicked.connect(self.limpar)
        self.ui.ip.clicked.connect(self.ip_selecionado)
        self.ui.ip_3.clicked.connect(self.ip_digitado)

    def scanner(self):#scanner e salvar
        self.CARREGANGO()       
        try:
            nomedopc = socket.gethostname()#nome do computador
            ip_interno = socket.gethostbyname(nomedopc)#ip local
            ip_externo = get('https://api.ipify.org').text#ip na web
            macdopc=(':'.join(re.findall('..', '%012x' % uuid.getnode())))
            #ip=str(self.ui.lineEdit.text())       
                
            numRows = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(numRows)
            self.ui.tableWidget.setItem(numRows, 0, QTableWidgetItem(nomedopc))
            self.ui.tableWidget.setItem(numRows, 1, QTableWidgetItem(ip_interno))
            self.ui.tableWidget.setItem(numRows, 2, QTableWidgetItem(ip_externo))
            self.ui.tableWidget.setItem(numRows, 3, QTableWidgetItem(macdopc))
            b=[('COMPUTADOR: {}'.format(nomedopc)),
            ('IP_LOCAL: {}'.format(ip_interno)),
            ('IP_EXTERNO: {}'.format(ip_externo)),
            ('MAC-DO-PC: {}'.format(macdopc))
            ,'']
            

            with open('scanner.txt','a')as arquivo:
                for valor in b:
                    arquivo.write(str(valor)+'\n')
            #opcao pra selectionar texto        
            #buttonReply=QMessageBox.question(self, 'OPEN', "DESEJA  ABRI", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            #if buttonReply==QMessageBox.Yes:
             #   self.abrir()
                
                        
                    
        except:error    
        
    def CARREGANGO(self):#barra de carregamento
        import time, sys
            
        for i in range(25, 101):
            sys.stdout.write("\r{}".format(i))
            sys.stdout.flush()
            time.sleep(0.0001)
            self.ui.progressBar.setValue(i)                     
    def carrega_ip(self):
        for i in range(0,100):
            sleep(0.001)
            self.ui.progressBar_2.setValue(i)  
    def limpar(self):#limpar
        id=self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(id)
    
    def mostra(self):#abrir txt
       filename = QFileDialog.getOpenFileName(self,'Open File')
       if filename[0]:
           f = open(filename[0],'r')
           with f:
               data = f.read()
               self.ui.textEdit.setText(data)             

    def ip_selecionado(self):
        
        from ipaddress import IPv4Address
        from os import write
        from ping3 import ping
        while True:
            ip_inicial=self.ui.ip_inicial.currentText()
            ip_final=self.ui.ip_final.currentText()
            
            if ip_inicial=="" or ip_final=="":
                return QMessageBox.about(self, "Title", "SELECIONER UM IP OU DIGITE")
                
            inicial = IPv4Address(ip_inicial)
            final = IPv4Address(ip_final)           
            ips = [str(IPv4Address(ip)) for ip in range(int(inicial), int(final))]
            
                    
            try:

                for ip in ips:
                    self.carrega_ip()                   
                    t = ping(ip, timeout=1)                           
                    status = 'OFFLINE' if t is None else 'ONLINE'
                    for i in range(1):                                              
                        self.ui.listWidget_2.addItem(f' IP: {ip}   STATUS: [{status}]')                        
                        b=[('COMPUTADOR: {} STATUS: {}'.format(ip,status)),'']                          
                        with open('ip.txt','a')as arquivo:#salvar arquivo
                            for valor in b:
                                arquivo.write(str(valor)+'\n')    

                
            except PermissionError:
                print('Usuario nao possui privilegios de Administrador!')
            break   
    def comobox_ip(self):
        iplista_inicial = ["192.168.1.1", "192.168.2.1", "192.168.3.1", "192.168.4.1"]
        iplista_final= ["192.168.1.10", "192.168.2.10", "192.168.3.10", "192.168.4.10"]
        self.ui.ip_inicial.addItems(iplista_inicial)
        self.ui.ip_final.addItems(iplista_final)        
    def ip_digitado(self):#ip digitado
       
        try:
            from ipaddress import IPv4Address
            from os import write
            from ping3 import ping
            while True:
                ip_inicial=self.ui.lineEdit.text()           
                ip_final=self.ui.lineEdit_2.text()
                self.porta()
                if ip_inicial=="" or ip_final=="":
                    return QMessageBox.about(self, "Title", "CAMPO VAZIO PREENCHA/ OU SELECIONE")
                    
                inicial = IPv4Address(ip_inicial)
                final = IPv4Address(ip_final)           
                ips = [str(IPv4Address(ip)) for ip in range(int(inicial), int(final))]
                
                        
                try:
                    for ip in ips:
                        self.carrega_ip()                     
                        t = ping(ip, timeout=1)                    
                        status = 'OFFLINE' if t is None else 'ONLINE'
                        for i in range(1):
                            self.ui.listWidget_2.addItem(f' IP: {ip}   STATUS: [{status}]')
                            b=[('COMPUTADOR: {} STATUS: {}'.format(ip,status)),'']                          
                            with open('ip.txt','a')as arquivo:#salvar arquivo
                                for valor in b:
                                    arquivo.write(str(valor)+'\n')    


                    ip_inicial=self.ui.lineEdit.setText("")           
                    ip_final=self.ui.lineEdit_2.setText("")
                except PermissionError:
                    print('Usuario nao possui privilegios de Administrador!')
                break   
        except:error    
    def porta(self):#rastrea porta
        ip = self.ui.lineEdit.text() # entrada para IP, caso use linux digite entre aspas
        portas = [11,10,21,22,25,3022,80,8080,8090,9043,443,8043,8443,9443,110,985,9080,9090] # lista de portas a serem scaneadas


        for porta in portas:
            self.carrega_ip()
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET (representa o tipo de endereço), SOCK_STREAM (indica que socket é do tipo TCP)
            cliente.settimeout(2) # limite de tempo suportado
            conexao = cliente.connect_ex((ip, porta)) 
            
            # condição (se conexão for igual a 0 porta aberta se não porta fechada)
            with open("porta.txt", 'a') as f: # inserir caminho onde será salvo o arquivo
            #with open("C:\\teste.txt", 'a') as f: # Windows
                if conexao == 0:
                    f.write(str(porta) + " ," + " >> Aberta")
                    f.writelines('\n') # pula a linha
                    self.ui.listWidget_2.addItem(f' IP: {ip} PORTA: {str(porta) +  " >> Aberta"}\n') 
                else:
                    f.write(str(porta)  + " >> Fechada") 
                    f.writelines('\n')  
                    self.ui.listWidget_2.addItem(f' IP {ip} PORTA:{str(porta) +  " >> Fechada"}\n') 
            
            #self.ui.listWidget_2.addItem(f'IP: {ip} Porta: {str(porta)} TIPO {str(conexao==0)}')

            f.close()       
            
import sys    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = sistema()
    ex.show()
    sys.exit(app.exec_())



    
