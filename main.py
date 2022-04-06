# from msilib.schema import Directory
from pickle import GLOBAL
import re
from tkinter import W
from typing import Any
from unittest import case
import urllib.request
from PyQt5 import uic, QtWidgets, QtGui
from pytube import YouTube
import time
import threading

import os


titulo = []

link_videos = []

def limpar():

    global link_videos
    link_videos.clear()
    titulo.clear()
    forme.status.setText("")
    forme.status_2.setText("")
    forme.status_5.setText("")
    forme.status_6.setText("")
    forme.status_7.setText("")
    forme.status_8.setText("")
    forme.status_15.setText("")
    forme.status_16.setText("")
    forme.status_17.setText("")
    forme.status_18.setText("")
    
    
def play():
    global titulo
    nome = titulo[0]
    nome_2= nome.replace(" ","\ ")
    nome_3= nome_2.replace("(","\(")
    nome_4= nome_3.replace(")","\)")
    nome_5= nome_4.replace(",","")
    os.system('vlc download/'+nome_5+'.mp4')

def play1():
    global titulo
    nome = titulo[1]
    nome_2= nome.replace(" ","\ ")
    nome_3= nome_2.replace("(","\(")
    nome_4= nome_3.replace(")","\)")
    nome_5= nome_4.replace(",","")
    os.system('vlc download/'+nome_5+'.mp4')
    
def play2():
    global titulo
    nome = titulo[2]
    nome_2= nome.replace(" ","\ ")
    nome_3= nome_2.replace("(","\(")
    nome_4= nome_3.replace(")","\)")
    nome_5= nome_4.replace(",","")
    os.system('vlc download/'+nome_5+'.mp4')
    
def play3():
    global titulo
    nome = titulo[3]
    nome_2= nome.replace(" ","\ ")
    nome_3= nome_2.replace("(","\(")
    nome_4= nome_3.replace(")","\)")
    nome_5= nome_4.replace(",","")
    os.system('vlc download/'+nome_5+'.mp4')
    
def play4():
    global titulo
    nome = titulo[4]
    nome_2= nome.replace(" ","\ ")
    nome_3= nome_2.replace("(","\(")
    nome_4= nome_3.replace(")","\)")
    nome_5= nome_4.replace(",","")
    os.system('vlc download/'+nome_5+'.mp4')
    
def play5():
    global titulo
    nome = titulo[5]
    nome_2= nome.replace(" ","\ ")
    nome_3= nome_2.replace("(","\(")
    nome_4= nome_3.replace(")","\)")
    nome_5= nome_4.replace(",","")
    os.system('vlc download/'+nome_5+'.mp4')
    
def play6():
    global titulo
    nome = titulo[6]
    nome_2= nome.replace(" ","\ ")
    nome_3= nome_2.replace("(","\(")
    nome_4= nome_3.replace(")","\)")
    nome_5= nome_4.replace(",","")
    os.system('vlc download/'+nome_5+'.mp4')
    
def play7():
    global titulo
    nome = titulo[7]
    nome_2= nome.replace(" ","\ ")
    nome_3= nome_2.replace("(","\(")
    nome_4= nome_3.replace(")","\)")
    nome_5= nome_4.replace(",","")
    os.system('vlc download/'+nome_5+'.mp4')
    
def play8():
    global titulo
    nome = titulo[8]
    nome_2= nome.replace(" ","\ ")
    nome_3= nome_2.replace("(","\(")
    nome_4= nome_3.replace(")","\)")
    nome_5= nome_4.replace(",","")
    os.system('vlc download/'+nome_5+'.mp4')
    
def play9():
    global titulo
    nome = titulo[9]
    nome_2= nome.replace(" ","\ ")
    nome_3= nome_2.replace("(","\(")
    nome_4= nome_3.replace(")","\)")
    nome_5= nome_4.replace(",","")
    os.system('vlc download/'+nome_5+'.mp4')
    



def pesquisa():
    threading.Thread(target=limpar).start()
    n = 0
    n_2 = 0

    global link_videos
    pesquisa = str(forme.lineEdit.text())
    pesquisa_k = "karaoke+"+ pesquisa.replace(" ", "+")
    # print(pesquisa_k)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+pesquisa_k)
    id_videos = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    
    base = "https://www.youtube.com/watch?v="
    link_img = []
    global titulo
    
    

    for i in id_videos: 
        n += 1
        if n <= 10:
              
            link_videos.append(base+i)
        else:
            break
    
    # print('urls montadas')
    for i in link_videos:
        # n_2 = n_2 + 1
        if n_2 <=10:
            
            yt = YouTube(i)
            link_img.append(yt.thumbnail_url)
            titulo.append(yt.title)
            urllib.request.urlretrieve(link_img[n_2], "imag"+str(n_2)+".jpg")
            # limpar()
            if n_2 == 0:
                forme.label.setText(titulo[0])                
                forme.img.setPixmap(QtGui.QPixmap("imag0.jpg"))      
            elif n_2 == 1:
                forme.label_2.setText(titulo[1])
                forme.img_2.setPixmap(QtGui.QPixmap("imag1.jpg"))
            elif n_2 == 2:
                forme.label_5.setText(titulo[2])                
                forme.img_5.setPixmap(QtGui.QPixmap("imag2.jpg"))
            elif n_2 == 3:
                forme.label_6.setText(titulo[3])                
                forme.img_6.setPixmap(QtGui.QPixmap("imag3.jpg"))
            elif n_2 == 4:
                forme.label_7.setText(titulo[4])                
                forme.img_7.setPixmap(QtGui.QPixmap("imag4.jpg"))
            elif n_2 == 5:
                forme.label_8.setText(titulo[5])                
                forme.img_8.setPixmap(QtGui.QPixmap("imag5.jpg"))
            elif n_2 == 6:
                forme.label_15.setText(titulo[6])                
                forme.img_15.setPixmap(QtGui.QPixmap("imag6.jpg"))
            elif n_2 == 7:
                forme.label_16.setText(titulo[7])                
                forme.img_16.setPixmap(QtGui.QPixmap("imag7.jpg"))
            elif n_2 == 8:
                forme.label_17.setText(titulo[8])                
                forme.img_17.setPixmap(QtGui.QPixmap("imag8.jpg"))
            elif n_2 == 9:
                forme.label_18.setText(titulo[9])         
                forme.img_18.setPixmap(QtGui.QPixmap("imag9.jpg"))
            else:
                pass
            n_2 += 1
        else:
            pass
        


    forme.lineEdit.setText("")
    
    print('acabou a pesquisa')


def download_0():
    forme.status.setText("BAIXANDO...")
    # forme.label_3
    url = link_videos[0]
    video = YouTube(url) 
    stream = video.streams.get_highest_resolution()   
    stream.download(output_path='download')
    forme.status.setText("CONCLUIDO")
    # QtWidgets.QFileDialog.getOpenFileName("download/Quando a chuva passar - Ivete - Karaokê Violão.mp4")
    print('ok')

def download_1():

    forme.status_2.setText("BAIXANDO...")
    url = link_videos[1]
    video = YouTube(url) 
    stream = video.streams.get_highest_resolution()   
    stream.download(output_path='download')
    forme.status_2.setText("CONCLUIDO")
def download_2():
    forme.status_5.setText("BAIXANDO...")
    url = link_videos[2]
    video = YouTube(url) 
    stream = video.streams.get_highest_resolution()   
    stream.download(output_path='download')
    forme.status_5.setText("CONCLUIDO")

def download_3():
    forme.status_6.setText("BAIXANDO...")

    url = link_videos[3]
    video = YouTube(url) 
    stream = video.streams.get_highest_resolution()   
    stream.download(output_path='download')
    forme.status_6.setText("CONCLUIDO")

def download_4():
    forme.status_7.setText("BAIXANDO...")

    url = link_videos[4]
    video = YouTube(url) 
    stream = video.streams.get_highest_resolution()   
    stream.download(output_path='download')
    forme.status_7.setText("CONCLUIDO")

def download_5():
    forme.status_8.setText("BAIXANDO...")

    url = link_videos[5]
    video = YouTube(url) 
    stream = video.streams.get_highest_resolution()   
    stream.download(output_path='download')
    forme.status_8.setText("CONCLUIDO")

def download_6():
    forme.status_15.setText("BAIXANDO...")

    url = link_videos[6]
    video = YouTube(url) 
    stream = video.streams.get_highest_resolution()   
    stream.download(output_path='download')
    forme.status_15.setText("CONCLUIDO")

def download_7():
    forme.status_16.setText("BAIXANDO...")

    url = link_videos[7]
    video = YouTube(url) 
    stream = video.streams.get_highest_resolution()   
    stream.download(output_path='download')
    forme.status_16.setText("CONCLUIDO")

def download_8():
    forme.status_17.setText("BAIXANDO...")

    url = link_videos[8]
    video = YouTube(url) 
    stream = video.streams.get_highest_resolution()   
    stream.download(output_path='download')
    forme.status_17.setText("CONCLUIDO")

def download_9():
    forme.status_18.setText("BAIXANDO...")

    url = link_videos[9]
    video = YouTube(url) 
    stream = video.streams.get_highest_resolution()   
    stream.download(output_path='download')
    forme.status_18.setText("CONCLUIDO")



app = QtWidgets.QApplication([])
forme = uic.loadUi("pesquisa.ui")
forme.show()



def t_0():
    threading.Thread(target=download_0).start()
def t_1():
    threading.Thread(target=download_1).start()
def t_2():
    threading.Thread(target=download_2).start()
def t_3():
    threading.Thread(target=download_3).start()
def t_4():
    threading.Thread(target=download_4).start()
def t_5():
    threading.Thread(target=download_5).start()
def t_6():
    threading.Thread(target=download_6).start()
def t_7():
    threading.Thread(target=download_7).start()
def t_8():
    threading.Thread(target=download_8).start()
def t_9():
    threading.Thread(target=download_9).start()

def pesquisa_0():
    threading.Thread(target=pesquisa).start()
    
def tocar():
    threading.Thread(target=play).start()
def tocar1():
    threading.Thread(target=play1).start()
def tocar2():
    threading.Thread(target=play2).start()
def tocar3():
    threading.Thread(target=play3).start()
def tocar4():
    threading.Thread(target=play4).start()
def tocar5():
    threading.Thread(target=play5).start()
def tocar6():
    threading.Thread(target=play6).start()
def tocar7():
    threading.Thread(target=play7).start()
def tocar8():
    threading.Thread(target=play8).start()
def tocar9():
    threading.Thread(target=play9).start()



forme.pushButton_2.clicked.connect(pesquisa_0)
forme.pushButton.clicked.connect(t_0)
forme.pushButton_3.clicked.connect(t_1)
forme.pushButton_6.clicked.connect(t_2)
forme.pushButton_7.clicked.connect(t_3)
forme.pushButton_8.clicked.connect(t_4)
forme.pushButton_9.clicked.connect(t_5)
forme.pushButton_16.clicked.connect(t_6)
forme.pushButton_17.clicked.connect(t_7)
forme.pushButton_18.clicked.connect(t_8)
forme.pushButton_19.clicked.connect(t_9)
# forme.play.setEnable(True)
forme.play.clicked.connect(tocar)

forme.play_2.clicked.connect(tocar1)
forme.play_3.clicked.connect(tocar2)
forme.play_4.clicked.connect(tocar3)
forme.play_5.clicked.connect(tocar4)
forme.play_6.clicked.connect(tocar5)
forme.play_7.clicked.connect(tocar6)
forme.play_8.clicked.connect(tocar7)
forme.play_9.clicked.connect(tocar8)
forme.play_10.clicked.connect(tocar9)



app.exec_()
