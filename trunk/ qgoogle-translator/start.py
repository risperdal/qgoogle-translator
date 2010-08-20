#!/usr/bin/env python
# -*- coding: utf-8 -*-

#A small google translator application which written in python programming language
#Copyright (C) 2010  h4ckinger dot gmail dot com
#www.h4ckinger.org

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, re, urllib
import simplejson as json
from PyQt4 import QtCore, QtGui
from Ui_gtranslator import Ui_MainWindow


import simplejson as json
class startTree(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()
        self.base_uri = "http://ajax.googleapis.com/ajax/services/language/translate"
        self.langs = {'chinese': 'zh', 'german': 'de', 'chinese_traditional': 'zh-TW', 'belarusian': 'be', 'galician': 'gl', 'macedonian': 'mk', 'urdu': 'ur', 'polish': 'pl', 'swahili': 'sw', 'icelandic': 'is', 'turkish': 'tr', 'romanian': 'ro', 'oriya': 'or', 'uighur': 'ug', 'sanskrit': 'sa', 'khmer': 'km', 'hungarian': 'hu', 'bihari': 'bh', 'catalan': 'ca', 'laothian': 'lo', 'kyrgyz': 'ky', 'finnish': 'fi', 'serbian': 'sr', 'croatian': 'hr', 'portuguese': 'pt-PT', 'czech': 'cs', 'basque': 'eu', 'japanese': 'ja', 'amharic': 'am', 'persian': 'fa', 'tajik': 'tg', 'estonian': 'et', 'telugu': 'te', 'marathi': 'mr', 'pashto': 'ps', 'gujarati': 'gu', 'dutch': 'nl', 'dhivehi': 'dv', 'french': 'fr', 'armenian': 'hy', 'sinhalese': 'si', 'afrikaans': 'af', 'filipino': 'tl', 'uzbek': 'uz', 'albanian': 'sq', 'vietnamese': 'vi', 'latvian': 'lv', 'italian': 'it', 'inuktitut': 'iu', 'slovak': 'sk', 'spanish': 'es', 'esperanto': 'eo', 'tibetan': 'bo', 'hindi': 'hi', 'danish': 'da', 'bulgarian': 'bg', 'georgian': 'ka', 'malay': 'ms', 'bengali': 'bn', 'russian': 'ru', 'thai': 'th', 'tamil': 'ta', 'tagalog': 'tl', 'malayalam': 'ml', 'indonesian': 'id', 'kannada': 'kn', 'mongolian': 'mn', 'hebrew': 'iw', 'arabic': 'ar', 'swedish': 'sv', 'cherokee': 'chr', 'slovenian': 'sl', 'azerbaijani': 'az', 'sindhi': 'sd', 'korean': 'ko', 'ukrainian': 'uk', 'lithuanian': 'lt', 'norwegian': 'no', 'maltese': 'mt', 'kazakh': 'kk', 'chinese_simplified': 'zh-CN', 'kurdish': 'ku', 'nepali': 'ne', 'guarani': 'gn', 'punjabi': 'pa', 'greek': 'el', 'burmese': 'my', 'english': 'en'}
        self.comboDoldur()
    def comboDoldur(self):
        self.ui.comboBox.addItems(self.langs.keys())
        self.ui.comboBox_2.addItems(self.langs.keys())
        self.ui.comboBox.setCurrentIndex(self.ui.comboBox.findText("turkish"))
        self.ui.comboBox_2.setCurrentIndex(self.ui.comboBox_2.findText("english"))
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
    def translate(self, src, to, phrase):
        src = self.langs.get(src, src)
        to =  self.langs.get(to, to)
        args={
            'v':'1.0', 
            'langpair': '%s%%7C%s' % (src, to),
            'q': urllib.quote_plus(phrase),
        }
        argstring = '%s' % ('&'.join(['%s=%s' % (k,v) for (k,v) in args.iteritems()]))
        resp = json.load(urllib.urlopen('%s?%s' % (self.base_uri, argstring)))
        try:
            return resp['responseData']['translatedText']
        except:
            return phrase

    @QtCore.pyqtSlot()
    def on_pushButton_2_clicked(self):
        src=str(self.ui.comboBox.currentText())
        to=str(self.ui.comboBox_2.currentText())
        metin=str(self.ui.plainTextEdit.toPlainText().toUtf8())
        sonuc=self.translate(src, to, metin)
        self.ui.plainTextEdit_2.setPlainText(sonuc)
    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        ilk=self.ui.comboBox.currentIndex()
        iki=self.ui.comboBox_2.currentIndex()
        self.ui.comboBox.setCurrentIndex(iki)
        self.ui.comboBox_2.setCurrentIndex(ilk)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = startTree()
    myapp.show()
    sys.exit(app.exec_())
