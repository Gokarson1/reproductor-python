# coding: utf-8
import sys
from pathlib import Path
import darkdetect 

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

from qfluentwidgets import setTheme, Theme, PushButton
from qfluentwidgets.multimedia import SimpleMediaPlayBar, StandardMediaPlayBar, VideoWidget
from qframelesswindow import AcrylicWindow


class Demo1(AcrylicWindow):

    def __init__(self):
        dark = darkdetect.isDark()
        super().__init__()
        setTheme(Theme.DARK)
        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=dark, isAlt=True)
        self.vBoxLayout = QVBoxLayout(self)
        self.resize(500, 300)

        # self.player = QMediaPlayer(self)
        # self.player.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        # self.player.setPosition()

        self.simplePlayBar = SimpleMediaPlayBar(self)
        self.standardPlayBar = StandardMediaPlayBar(self)

        self.vBoxLayout.addWidget(self.simplePlayBar)
        self.vBoxLayout.addWidget(self.standardPlayBar)

        # online music
        url = QUrl("https://files.cnblogs.com/files/blogs/677826/beat.zip?t=1693900324")
        self.simplePlayBar.player.setSource(url)

        # local music
        url = QUrl.fromLocalFile(str(Path('resource/aiko - シアワセ.mp3').absolute()))
        self.standardPlayBar.player.setSource(url)

        # self.standardPlayBar.play()


class Demo2(AcrylicWindow):

    def __init__(self):
        super().__init__()
        dark = darkdetect.isDark()
        self.vBoxLayout = QVBoxLayout(self)
        self.videoWidget = VideoWidget(self)
        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=dark, isAlt=True)

        self.videoWidget.setVideo(QUrl('https://media.w3.org/2010/05/sintel/trailer.mp4'))
        self.videoWidget.play()

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.addWidget(self.videoWidget)
        self.resize(800, 450)


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication([])
    demo1 = Demo1()
    demo1.show()
    demo2 = Demo2()
    demo2.show()
    sys.exit(app.exec())