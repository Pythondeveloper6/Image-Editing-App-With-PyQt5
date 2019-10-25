
## PyQT4
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *

#PyQT 5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#######################
import sys
import os
from PyQt5.uic import loadUiType
from os import path
from datetime import datetime
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw , ImageFont


## Load UI FIle
FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"editing.ui"))

## Empty List Contains The Images Names
Images = []

class App_Window(QMainWindow , FORM_CLASS):
    def __init__(self):
        QMainWindow. __init__(self)
        self.setupUi(self)
        self.InitUi()
        self.Handel_Buttons()
        self.Handel_file_Menu()


    ## Handel Changes In Run Time
    def InitUi(self):
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget_2.tabBar().setVisible(False)
        self.tabWidget_2.tabCloseRequested.connect(self.Close_Tab)
        self.groupBox.hide()
        self.groupBox_2.hide()
        self.groupBox_3.hide()
        self.groupBox_4.hide()




    ## Handel All The Buttons In The App
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.Apply_Filter)
        self.pushButton_2.clicked.connect(self.Crop)
        self.pushButton_4.clicked.connect(self.Write_Text)
        self.pushButton_5.clicked.connect(self.Apply_Maping)


    ## Handel Menus Method
    def Handel_file_Menu(self):
        self.actionOpen_Images.triggered.connect(self.Load_Images)
        self.actionApply_Filter.triggered.connect(self.Show_Filters)
        self.actionCrop_Image.triggered.connect(self.Show_Crop)
        self.actionWrite_Text_On_Imge.triggered.connect(self.Show_Write_Text)
        self.actionMappin_An_Image.triggered.connect(self.Show_Maping_Tools)


    ##Load The Images Method
    def Load_Images(self):
        global Images
        image =  QFileDialog.getOpenFileNames(self, 'Upload Your Image ', '/',"Image files (*.jpg *.gif *.png)")
        images = list(image)
        images.pop()  # delete last value
        self.tabWidget_2.tabBar().setVisible(True)
        names = []
        print(images)
        print('ـــــــــــــــــــــــــــــــــ')
        for x  in images :
            name = 1
            for y in x :
                print(y)
                Images.append(y)
                tab = QWidget()
                lb = QLabel(tab)
                lb.resize(800,400)
                self.tabWidget_2.addTab(tab ,'Image'+str(name))
                name += 1

                pixmap = QPixmap(y)
                lb.setPixmap((pixmap).scaled(lb.size(), Qt.KeepAspectRatio ,Qt.SmoothTransformation))
        self.tabWidget_2.removeTab(0)




    ## Show The Hidden Filters
    def Show_Filters(self):
        self.groupBox_2.hide()
        self.groupBox.show()




    ## Apply The Selected Filter To The Image Ans Save It
    def Apply_Filter(self):
        global Images
        tab = self.tabWidget_2.currentIndex()
        image = Images[tab]

        pr_image = Image.open(image)

        if self.comboBox_2.currentIndex() == 0 :
            new_image = pr_image.filter(ImageFilter.BLUR)
            new_image.save('BLUR.jpg')

        elif self.comboBox_2.currentIndex() == 1 :
            new_image = pr_image.filter(ImageFilter.DETAIL)
            new_image.save('DETAIL.jpg')

        elif self.comboBox_2.currentIndex() == 2 :
            new_image = pr_image.filter(ImageFilter.CONTOUR)
            new_image.save('CONTOUR.jpg')


        elif self.comboBox_2.currentIndex() == 3 :
            new_image = pr_image.filter(ImageFilter.EDGE_ENHANCE)
            new_image.save('EDGE_ENHANCE.jpg')

        elif self.comboBox_2.currentIndex() == 4 :
            new_image = pr_image.filter(ImageFilter.EDGE_ENHANCE_MORE)
            new_image.save('EDGE_ENHANCE_MORE.jpg')


        elif self.comboBox_2.currentIndex() == 5 :
            new_image = pr_image.filter(ImageFilter.SMOOTH_MORE)
            new_image.save('SMOOTH_MORE.jpg')


        elif self.comboBox_2.currentIndex() == 6 :
            new_image = pr_image.filter(ImageFilter.EMBOSS)
            new_image.save('EMBOSS.jpg')


        elif self.comboBox_2.currentIndex() == 7 :
            new_image = pr_image.filter(ImageFilter.FIND_EDGES)
            new_image.save('FIND_EDGES.jpg')


        elif self.comboBox_2.currentIndex() == 8 :
            new_image = pr_image.filter(ImageFilter.SMOOTH)
            new_image.save('SMOOTH.jpg')


        elif self.comboBox_2.currentIndex() == 9 :
            new_image = pr_image.filter(ImageFilter.SHARPEN)
            new_image.save('SHARPEN.jpg')





    ## Show Crop Tools
    def Show_Crop(self):
        self.groupBox.hide()
        self.groupBox_2.show()




    ## Crop The Image
    def Crop(self):
        tab = self.tabWidget_2.currentIndex()
        image = Images[tab]
        pr_image = Image.open(image)

        top     = int(self.lineEdit.text())
        left  = int(self.lineEdit_2.text())
        width    = int(self.lineEdit_3.text())
        height   = int(self.lineEdit_4.text())

        area = (left, top, left+width, top+height)
        cropped_img = pr_image.crop(area)
        cropped_img.save('croped.jpg')




    ## SHow Write Text Tools
    def Show_Write_Text(self):
        self.groupBox.hide()
        self.groupBox_2.hide()
        self.groupBox_3.show()
        print('Done')




    ## Write Text On Image
    def Write_Text(self):
        tab = self.tabWidget_2.currentIndex()
        image = Images[tab]
        pr_image = Image.open(image)

        text = self.lineEdit_8.text()
        x    = int(self.lineEdit_9.text())
        y    = int(self.lineEdit_10.text())
        f_size = int(self.lineEdit_11.text())

        draw = ImageDraw.Draw(pr_image)

        ##Load The Default Font
        font = ImageFont.load_default()

        #font_path = '/usr/share/fonts/TTF/DejaVuSansCondensed-BoldOblique.ttf'
        #font =  ImageFont.truetype ( font_path, f_size )

        draw.text((x, y), text, (255, 255, 255), font=font)
        pr_image.save('Text-On-Image.jpg')




    ## Show Mapping Tools
    def Show_Maping_Tools(self):
        self.groupBox.hide()
        self.groupBox_2.hide()
        self.groupBox_3.hide()
        self.groupBox_4.show()




    ## Apply Maping
    def Apply_Maping(self):
        width      = int(self.lineEdit_12.text())
        height     = int(self.lineEdit_13.text())

        img = Image.new('RGB', (width, height), "black")  # create a new black image
        pixels = img.load()  # create the pixel map

        for i in range(img.size[0]):  # for every pixel:
            for j in range(img.size[1]):
                pixels[i, j] = (i, j, 100)  # set the colour accordingly

        img.save('mapping.jpg')

        #pr_image = Image.open('mapping.jpg')


    ## Close Any Tab Using The [x] Button
    def Close_Tab(self):
        index = self.tabWidget_2.currentIndex() # the tap i openning now
        self.tabWidget_2.removeTab(index)




## App Main Function
def main():
    app = QApplication(sys.argv)
    window = App_Window()
    window.show()
    app.exec_()


# Start The Main
if __name__ == "__main__":
    main()