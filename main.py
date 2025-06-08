# coding: utf-8
import sys
from pathlib import Path
import darkdetect 
import os
import yt_dlp

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtMultimedia import QMediaContent

from qfluentwidgets import setTheme, Theme, PushButton
from qfluentwidgets.multimedia import SimpleMediaPlayBar, StandardMediaPlayBar, VideoWidget, MediaPlayer
from qframelesswindow import AcrylicWindow


class Demo1(AcrylicWindow):

    def __init__(self):
        dark = darkdetect.isDark()
        super().__init__()
        setTheme(Theme.DARK)
        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=dark, isAlt=True)
        self.vBoxLayout = QVBoxLayout(self)
        self.resize(500, 300)

        self.simplePlayBar = SimpleMediaPlayBar(self)
        self.vBoxLayout.addWidget(self.simplePlayBar)

        url = "https://music.youtube.com/watch?v=5rAD0XelfFY&si=nO4-MGlpUYgY5hoU"
        ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
        'skip_download': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            stream_url = info['url']  
            #print("Stream URL:", stream_url)
        qurl = QUrl(stream_url)
        self.simplePlayBar.player.setSource(qurl)



        
        # # local music
        url = QUrl.fromLocalFile("resources\dejame_entrar.mp3")
        #self.simplePlayBar.player.setSource(url)

        #self.standardPlayBar.play()




if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication([])
    demo1 = Demo1()
    demo1.show()
    sys.exit(app.exec())