import os
import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from math import sqrt as msqrt
import pickle
import time
globaldata={"docname":"testfile","doctime":"8/18","globaloffset":QPointF(100.,100.),"globalscale":1.0,"selctrlp":1,"ctrlp":{
    1:{"pos":QPointF(40,40),"id":1,"name":"testp","content":[
    #{"type":"text","str":"","statictext":""}
    # {"type":"pdfpage","filename":"test.pdf","page":1}
    ]}},"ctrlplinks":[]}
# content["statictext"]
# QStaticText
# globaldata={"docname":"testfile","doctime":"8/18","globaloffset":QPointF(100.,100.),"globalscale":1.0,"selctrlp":1,"ctrlp":{
    # 1:{"pos":QPointF(40,40),"id":1,"name":"testp","content":[]}},"ctrlplinks":[]}

# globaldata={"docname":"testfile","doctime":"8/18","globaloffset":QPointF(0.,0.),"globalscale":1.0,"selctrlp":2,"ctrlp":{
#     1:{"pos":QPointF(10,10),"id":1,"name":"testp","content":[{"type":"line","data":[
#     QPointF(10.0, 80.0),
#     QPointF(20.0, 10.0),
#     QPointF(80.0, 30.0)]},{"type":"text","pos":QPointF(10.0, 80.0),"str":"hello world! 1"}]},
#     2:{"pos":QPointF(100,100),"id":2,"name":"testp","content":[{"type":"line","data":[
#     QPointF(10.0, 80.0),
#     QPointF(20.0, 10.0),
#     QPointF(80.0, 30.0)]},{"type":"text","pos":QPointF(10.0, 80.0),"str":"hello world! 2"}]}},"ctrlplinks":[]}

class mynote(QWidget):
    def __init__(self, parent=None, **kwargs):
        super(mynote, self).__init__(parent)
        self.setWindowIcon(QIcon("application-lonenote.lonenote.png"))
        # print(QIcon("application-lonenote.lonenote.png"))
        # self.setWindowIcon(QIcon("path844.svg"))
        self.setAttribute(Qt.WA_InputMethodEnabled, False)
        # self.setAttribute(Qt.WA_KeyCompression, True)
        # self.setFocusPolicy(Qt.WheelFocus)
        # self.ly1=QVBoxLayout(self)
        # self.ly1.setContentsMargins(0,0,0,0)
        # self.ly1.setSpacing(0)
        # label1 = QLabel("Hello World!")
        # label1.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        # label2 = QLabel("Hello World!")
        # label2.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        # label2.setMaximumHeight(30)
        # # label3=QLabel("Lonenote")
        # bt1=QPushButton(self)
        # bt1.setText("addp")
        # bt1.mousePressEvent=self.addp
        # bt1.setStyleSheet(u"font-size:22px")
        # bt2=QPushButton(self)
        # bt2.setText("save")
        # bt2.mousePressEvent=self.savefile
        # bt2.setStyleSheet(u"font-size:22px")
        # bt3=QPushButton(self)
        # bt3.setText("delp")
        # bt3.mousePressEvent=self.delp
        # bt3.setStyleSheet(u"font-size:22px")
        # bt4=QPushButton(self)
        # bt4.setText("+img")
        # bt4.mousePressEvent=self.addimg
        # bt4.setStyleSheet(u"font-size:22px")
        # wg2=QWidget(self)
        # self.ly2=QHBoxLayout(wg2)
        # self.ly2.setContentsMargins(0,0,0,0)
        # self.ly2.setSpacing(0)
        # wg3=QWidget(self)
        # wg3.setMaximumWidth(70)
        # wg3.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        # self.ly2.addWidget(wg3)
        # self.ly3=QVBoxLayout(wg3)
        # self.ly3.setContentsMargins(0,0,0,0)
        # self.ly3.setSpacing(0)
        # self.ly3.addWidget(bt1)
        # self.ly3.addWidget(bt3)
        # self.ly3.addWidget(bt2)
        # self.ly3.addWidget(bt4)
        # self.vsp1=QSpacerItem(60,10,QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.ly3.addItem(self.vsp1)
        # self.wg4=QWidget(self)
        # # wg4.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        # self.ly2.addWidget(self.wg4)
        # # self.rd=
        # self.ly1.addWidget(wg2)
        # self.ly1.addWidget(label2)
        # self.pool = Pool(4)
        # self.pool.map
 #       apply_stylesheet(self, theme='dark_teal.xml')
        # qtex.
        self.themcol2="#465E65"
        self.themcol1="#C99E8C"
        self.setStyleSheet('''
        background-color: '''+self.themcol2+''';
        font-size:16px;
        color:'''+self.themcol1+''';
QPushButton {
    background-color: '''+self.themcol2+''';
}
        ''')
        # self.setStyleSheet("background-color: transparent")

        self.ly2=QVBoxLayout(self)
        self.ly2.setContentsMargins(0,0,0,0)
        self.ly2.setSpacing(0)
        self.wg4=QWidget(self)
        # self.wg4.setStyleSheet("background-color: transparent")
        # self.wg4.setAttribute(Qt.WA_NoSystemBackground,True)
        # self.setAttribute(Qt.WA_NoSystemBackground,True)
        # self.setAttribute(Qt.WA_OpaquePaintEvent,False)
        # self.wg4.setAttribute(Qt.WA_TranslucentBackground,True)
        # self.setAttribute(Qt.WA_TranslucentBackground,True)
        self.wg4.setAttribute(Qt.WA_OpaquePaintEvent,True)
        # self.setAttribute(Qt.WA_OpaquePaintEvent,True)
        # self.setAttribute(Qt.WA_StyledBackground)

        # self.wg4.setAutoFillBackground(False)
        # self.setAutoFillBackground(False)
        # self.wg4.repaint()
        # self.setAttribute(Qt.WRepaintNoErase)
        # WRepaintNoErase
        # self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        # self.wg4.setAutoFillBackground(True)
        # self.wg4.setBackgroundRole(QColor(100,100,100))
        # self.wg4.setStyleSheet(u"background-color: rgb(255, 170, 0)")
        # self.wg4.att
        bt0=QPushButton(self)
        bt00=QPushButton(self)
        bt0.setText("hide")
        bt0.mousePressEvent=self.switchhide
        bt0.setStyleSheet(u"font-size:15px")
        # bt0.setMaximumSize(80,40)
        bt0.setFixedHeight(32)
        bt0.setFixedWidth(80)
        # self.ly2.addWidget(bt0)
        self.ly2.addWidget(self.wg4)
        self.wg1=QWidget(self.wg4)
        self.wg1.setFixedWidth(80)


        # self.ly1=QVBoxLayout(self.wg1)
        # self.ly0.addItem(bt0)
        # self.lywg11=QVBoxLayout(self.wg1)
        # self.wg11=QWidget(self.wg1)
        # self.lywg11.addWidget(bt0)
        # self.lywg11.addWidget(self.wg11)
        # self.lywg11.setContentsMargins(0,0,0,0)
        # self.lywg11.setSpacing(0)

        self.ly1=QVBoxLayout(self.wg1)
        self.ly1.setContentsMargins(0,0,0,0)
        self.ly1.setSpacing(0)
        # self.ly0.addLayout(self.ly1)
        # self.wg1.setMaximumSize(80,400)
        # self.wg1.setAcceptDrops(True)


        bt1=QPushButton(self)
        bt1.setText("addp")
        bt1.mousePressEvent=self.addp
        bt1.setStyleSheet(u"font-size:15px")
        bt2=QPushButton(self)
        bt2.setText("save")
        bt2.mousePressEvent=self.savefile
        bt2.setStyleSheet(u"font-size:15px")
        bt3=QPushButton(self)
        bt3.setText("delp")
        bt3.mousePressEvent=self.delp
        bt3.setStyleSheet(u"font-size:15px")
        bt4=QPushButton(self)
        bt4.setText("+img")
        bt4.mousePressEvent=self.addimg
        bt4.setStyleSheet(u"font-size:15px")
        bt5=QPushButton(self)
        bt5.setText("topdf")
        bt5.mousePressEvent=self.saveaspdf
        bt5.setStyleSheet(u"font-size:15px")
        bt7=QPushButton(self)
        bt7.setText("find")
        bt7.mousePressEvent=self.findsel
        bt7.setStyleSheet(u"font-size:15px")
        bt8=QPushButton(self)
        bt8.setText("text")
        bt8.mousePressEvent=self.showted
        bt8.setStyleSheet(u"font-size:15px")
        # bt11=QPushButton(self)
        # bt11.setText("透明")
        # bt11.mousePressEvent=self.touming
        # self.qtouming=False
        # bt11.setStyleSheet(u"font-size:15px")
        # self.cb1=QCheckBox(self)
        # self.cb1.setText("Pen?")
        # self.cb1.checkState
        # self.
        self.ly1.addWidget(bt00)
        self.ly1.addWidget(bt1)
        self.ly1.addWidget(bt4)
        self.ly1.addWidget(bt2)
        self.ly1.addWidget(bt5)
        self.ly1.addWidget(bt3)
        self.ly1.addWidget(bt7)
        self.ly1.addWidget(bt8)
        # self.bt1=bt1
        # self.bt2=bt2
        # self.bt3=bt3
        # self.bt4=bt4
        # self.bt5=bt5
        # self.bt7=bt7
        # self.bt8=bt8
        # self.ly1.addWidget(bt11)
        # self.ly1.addWidget(qtex)
        ass=app.screens()
        bt6=QPushButton(self)
        # for ii in ass:
        self.rblist=[]
        if(len(ass)==1):
            pass
        else:
            self.rblist=[]
            for ii in range(0,len(ass)):
                self.rblist.append(QRadioButton(bt6))
                self.ly1.addWidget(self.rblist[ii])
                self.rblist[ii].setText("screen"+str(ii))
            self.rblist[0].setChecked(True)
        # rb1=QRadioButton(self)
        # rb1.isChecked
        bt6.setText("pscn")
        bt6.mousePressEvent=self.prtscn
        bt6.setStyleSheet(u"font-size:15px")
        self.ly1.addWidget(bt6)
        bt9=QPushButton(self)
        bt9.setText("w")
        bt9.setStyleSheet(u"font-size:15px")
        bt9.mousePressEvent=self.setcolw
        bt10=QPushButton(self)
        bt10.setText("b")
        bt10.setStyleSheet(u"font-size:15px")
        bt10.mousePressEvent=self.setcolb
        self.ly1.addWidget(bt9)
        self.ly1.addWidget(bt10)
        # self.btlist=[bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9,bt10]
        self.pencol="#ffffff"
        # self.pencol="#465E65"

        # rb2=QRadioButton(self)
        # rb1.setChecked(True)
        # rb1.setText("0")

        # self.ly1.addWidget(rb1)
        # self.ly1.addWidget(rb2)
        # self.qrdcol1=QRadioButton(self)
        # self.qrdcol1.setChecked(True)
        # self.qrdcol1.setText("hhhh")
        # self.qrdcol2=QRadioButton(self)
        # self.qrdcol2.setText("hhhh")
        # self.ly1.addWidget(self.qrdcol1)
        # self.ly1.addWidget(self.qrdcol2)


        # self.ly1.addWidget(self.cb1)
        self.setGeometry(100,100,500,500)
        # label.show()
        if(openfile==""):
            self.setWindowTitle("Lonenote")
        else:
            (ofp,off)=os.path.split(openfile)
            self.setWindowTitle(off)
        self.show()

        self.qm=QMainWindow(self)
        # qqm=QWindow(self)
        self.qm.setGeometry(200,200,400,400)

        # nw=QWidget(qm)
        # print(qm.layout())
        qmmb=self.qm.menuBar()
        # qmmb.
        file=qmmb.addMenu("all")
        ftomark=QAction("tomarkdown",self.qm,Shortcut="Ctrl+S",triggered=self.ftomarkdown)
        # ftomark.setShortcut("Ctrl+S")
        freview=QAction("review",self.qm,Shortcut="Ctrl+w",triggered=self.freview)
        fquit=QAction("quit",self.qm,Shortcut="Ctrl+q",triggered=self.fquit)
        file.addAction(ftomark)
        file.addAction(freview)
        file.addAction(fquit)
        # file.triggered(ftomark)
        # self.ly3=QVBoxLayout(qm)
        # self.ly3.setContentsMargins(0,0,0,0)
        # self.ly3.setSpacing(0)
        # qm.setLayout(self.ly3)

        # self.ly3.addWidget(self.qtex)
        self.qtex=QTextEdit(self.qm)
        # self.qm.setAttribute(Qt.WA_InputMethodEnabled,True)
        # self.qm.inputMethodEvent=self.myQInputMethodEvent
        # self.qtex.setAttribute(Qt.WA_InputMethodEnabled,True)
        # self.setAttribute(Qt.WA_InputMethodEnabled,True)
        self.qtex.setAttribute(Qt.WA_InputMethodEnabled, True)
        # self.qtex.setAttribute(Qt.WA_KeyCompression, True)
        # self.qtex.setFocusPolicy(Qt.WheelFocus)
        # Qt.WA_InputMethodEnabled
        # self.qm.setAttribute(Qt.WA_InputMethodEnabled, True)
        # self.qm.setAttribute(Qt.WA_KeyCompression, True)
        # self.qm.setFocusPolicy(Qt.WheelFocus)
        # QWidget.QWidget.setAttribute(Qt.WA_InputMethodEnabled, True)
        # self.qtex.inputMethodEvent=self.myQInputMethodEvent
        # self.qtex.event=self.myQInputMethodEvent
        self.qtex.toMarkdown()
        # qm.layout().addWidget(self.qtex)
        self.qtex.acceptRichText()
        # self.qtex.setGeometry(0,0,100,100)
        # self.qtex.show()
        self.qm.setCentralWidget(self.qtex)
        # self.qm.show()

        # print()
        self.r=1.0
        self.t=QPointF(0,0)
        self.rc2=globaldata["globalscale"]
        self.tc2=globaldata["globaloffset"]
        self.beginrc2=self.rc2
        self.begintc2=self.tc2
        self.rf=1.0
        self.tf=QPointF(0,0)
        self.ppc2=QPointF(0,0)
        # self.beginppc2
        # self.pc22=QPointF(100.,100.)
        # self.rc1=1.
        # self.rc2=1.
        # self.tc1=QPointF(0,0)
        # self.tc2=QPointF(0,0)
        # self.t=QPointF(0,0)
        # self.r=1.
        # self.beginr=1.
        # self.begint=QPointF(0,0)
        self.wg4.mousePressEvent=self.shou1press
        self.wg4.mouseMoveEvent=self.shou1move
        self.wg4.mouseReleaseEvent=self.shou1song
        # self.wg4.paintEvent=self.testdraw
        self.wg4.paintEvent=self.mydrawp
        self.pingeventfinished=self.shou1song_shou
        self.pingeventstarted=self.shou1press_shou
        self.pingeventmove=self.shou1move_shou
        self.wheelEvent=self.whevent

        self.tapg=self.grabGesture(Qt.TapGesture)
        self.pinchg=self.grabGesture(Qt.PinchGesture)
        # 平移
        self.pang=self.grabGesture(Qt.PanGesture)

        self.wg4.tabletEvent=self.tabletEvent_pen

        # self.linkarrmode=True
        self.beginarr=0
        self.linkarrmode=False
        self.drawpartq=False
        self.inbutton=False
        self.erabegin=QPointF(0,0)
        self.eramove=QPointF(0,0)
        self.qdrawEraser=False
        self.listshowctrlps=[]

        self.bcol=QColor(49,54,59)
        self.meshcol=QColor(255,255,255)
        # self.saveaspdf()
    # def myQInputMethodEvent(self,event):
    #     print("hhhh")
        # return self.event(event)
    # def touming(self,event):
    #     self.inbutton=True
    #     print("tto")
    #     # self.setAttribute(Qt.WA_TranslucentBackground,True)
    #     # self.wg4.setAttribute(Qt.WA_TranslucentBackground,True)
    #     # if(not self.qtouming):
    #     #     # self.setAttribute(Qt.WA_)
    #     #     self.setAttribute(Qt.WA_TranslucentBackground,False)
    #     #     # self.wg4.setAttribute(Qt.WA_OpaquePaintEvent,True)
    #     # else:
    #     #     self.setAttribute(Qt.WA_TranslucentBackground,False)
    #         # self.wg4.setAttribute(Qt.WA_OpaquePaintEvent,True)
    #     # pix=QPixmap(100,100)
    #     # self.
    #     self.wg4.update()
    #     # self.update()
    def switchhide(self,event):#设置白色
        # self.inbutton=True
        # for bbt in self.btlist:
        #     if(bbt.isHidden()):
        #         bbt.show()
        #     else:
        #         bbt.hide()
        # self.ly1.
        if(self.wg1.isHidden()):
            self.wg1.show()
        else:
            self.wg1.hide()
    def setcolw(self,event):#设置白色
        self.inbutton=True
        self.pencol="#ffffff"
        self.bcol=QColor(49,54,59)
        self.meshcol=QColor(255,255,255)
        self.themcol2="#465E65"
        self.themcol1="#C99E8C"
        self.setStyleSheet('''
        background-color: '''+self.themcol2+''';
        font-size:16px;
        color:'''+self.themcol1+''';
QPushButton {
    background-color: '''+self.themcol2+''';
}
        ''')
        self.wg4.update()
    def setcolb(self,event):#设置蓝色
        self.inbutton=True
        # self.pencol="#007acc"
        self.pencol="#000000"
        self.bcol=QColor(255,255,255)
        self.meshcol=QColor(0,0,0)
        self.themcol2="#FFFFFF"
        self.themcol1="#000000"
        self.setStyleSheet('''
        background-color: '''+self.themcol2+''';
        font-size:16px;
        color:'''+self.themcol1+''';
QPushButton {
    background-color: '''+self.themcol2+''';
}
        ''')
        self.wg4.update()
    def showted(self,event):
        # qhavetext=False
        for content in globaldata["ctrlp"][globaldata["selctrlp"]]["content"]:
            if(content["type"]=="text"):
                # content["statictext"]=QStaticText(self.qtex.toHtml())
                # qhavetext=True
                print(content["str"])
                self.qtex.setPlainText(content["str"])
                break
        # if(not qhavetext):
        # self.qtex.setPlainText())
        self.qm.show()
        # self.qm.setAttribute(Qt.WA_InputMethodEnabled,True)
        # self.qtex.setAttribute(Qt.WA_InputMethodEnabled,True)
        # self.qtex.inputMethodEvent=self.myQInputMethodEvent
    def ftomarkdown(self):
        # print("clicked")
        # self.qtex.setMarkdown(self.qtex.toMarkdown())
        # print(self.qtex.toMarkdown())
        self.qtex.setPlainText(self.qtex.toMarkdown())
        # self.qtex.setText(self.qtex.toMarkdown())
    def freview(self):
        self.qtex.setMarkdown(self.qtex.toMarkdown())
        # content=globaldata["ctrlp"][globaldata["selctrlp"]]["content"]
        qhavetext=False
        for content in globaldata["ctrlp"][globaldata["selctrlp"]]["content"]:
            if(content["type"]=="text"):
                content["statictext"]=self.qtex.toHtml()
                content["str"]=self.qtex.toMarkdown()
                qhavetext=True
                break
        if(not qhavetext):
            globaldata["ctrlp"][globaldata["selctrlp"]]["content"].append({"type":"text","str":self.qtex.toMarkdown(),"statictext":self.qtex.toHtml()})
            print(self.qtex.toMarkdown())
        self.wg4.update()
    def fquit(self):
        self.freview()
        self.qm.hide()
    def whevent(self,event:QWheelEvent):#滚轮
        # self.beginrc2=self.rc2
        # self.begintc2=self.tc2
        # self.beginppc2=event.centerPoint()-self.pos()-self.wg4.pos()
        self.rf=(1+event.pixelDelta().y()/120./5)
        self.ppc2=event.position()
        self.updatac2()
        # self.rc2=self.beginrc2*self.rf
        # self.tc2=self.ppc2-self.rf*(self.ppc2-self.tf-self.begintc2)

        # self.ppc2=event.position()
        # self.rc2=self.rc2*(1+event.pixelDelta().y()/120./5)
        # self.beginrc2=self.rc2
                # self.rf=1.0
        # self.tf=QPointF(0,0)
        self.wg4.update()
        self.beginrc2=self.rc2
        self.begintc2=self.tc2
        self.rf=1.0
        self.wg4.update()


    def findsel(self,event):
        self.inbutton=True
        self.r=1.0
        self.t=QPointF(0,0)
        self.rc2=1.0
        self.tc2=-1*globaldata["ctrlp"][globaldata["selctrlp"]]["pos"]+QPointF(140,140)
        self.beginrc2=self.rc2
        self.begintc2=self.tc2
        self.rf=1.0
        self.tf=QPointF(0,0)
        self.ppc2=QPointF(0,0)
        # print(self.qtex.toMarkdown())
        self.wg4.update()
    def prtscn(self,event):
        self.inbutton=True
        # self.showMinimized()
        for ii in range(0,len(self.rblist)):
            if(self.rblist[ii].isChecked()):
                imgg=app.screens()[ii].grabWindow(0).toImage()
                ba = QByteArray()
                buffer = QBuffer(ba)
                buffer.open(QIODevice.WriteOnly)
                imgg.save(buffer,"PNG")
                imgg=QImage()
                imgg.loadFromData(ba,"PNG")
                # content["img"]=ba
                # print(imgg)
                break
        if(len(self.rblist)==0):
            imgg=app.screens()[0].grabWindow(0).toImage()
            ba = QByteArray()
            buffer = QBuffer(ba)
            buffer.open(QIODevice.WriteOnly)
            imgg.save(buffer,"PNG")
            imgg=QImage()
            imgg.loadFromData(ba,"PNG")
        for i in range(1,100000):
            if(globaldata["ctrlp"].get(i)==None):
                iid=i
                break
        # iid=len(globaldata["ctrlp"])+1
        ppos=globaldata["ctrlp"][globaldata["selctrlp"]]["pos"]+QPointF(100,100)
        # print(iid,ppos)
        globaldata["ctrlplinks"].append({"idline":[globaldata["selctrlp"],iid]})
        globaldata["selctrlp"]=iid
        globaldata["ctrlp"][iid]={"pos":ppos,"id":iid,"name":"testp","content":[{"type":"img","img":imgg}]}
        # self.showMinimized()
        # self.setFocus()
        self.showMaximized()
        self.wg4.update()
    def saveaspdf(self,event):
        # print
        self.inbutton=True
        # print("file")
        globaldata["globalscale"]=self.rc2
        globaldata["globaloffset"]=self.tc2
        global openfile
        if(openfile==""):
            # print("~/Documents/"+time.strftime("%y-%m-%d-%H:%M:%S",time.localtime())+".lonenote")
            geet=QFileDialog.getSaveFileName(self,"文件", os.exanduser("~/Documents/")+time.strftime("%y-%m-%d-%H-%M-%S",time.localtime())+".lonenote")
            openfile=geet[0]
        else:
            geet=[openfile]
        print(geet[0]+".pdf")
        file=QFile(geet[0]+".pdf")
        file.open(QIODevice.WriteOnly)
        pdf=QPdfWriter(file)
        pdf.setPageSize(QPageSize(QSizeF( self.wg4.width(),self.wg4.height()),QPageSize.Point))
        pdf.setResolution(72)
        # pdf.newPage()
        # pdf.setPageSize(QPagedPaintDevice.newPage())
        pter=QPainter()
        pter.begin(pdf)
        bs=QBrush(self.bcol)
        # pen=QPen(QColor(100,0,100))
        pter.setBrush(bs)
        pter.drawRect(-20,-20,self.wg4.width()+40,self.wg4.height()+40)
        self.drawgolbaldata(pter,True)
        # self.drawgolbaldata(pdf)
        pter.end()
        # pdf.newPage

        file.close()
    def addp(self,event):
        self.inbutton=True
        for i in range(1,100000):
            if(globaldata["ctrlp"].get(i)==None):
                iid=i
                break
        # iid=len(globaldata["ctrlp"])+1
        ppos=globaldata["ctrlp"][globaldata["selctrlp"]]["pos"]+QPointF(10,0)
        # print(iid,ppos)
        globaldata["selctrlp"]=iid
        globaldata["ctrlp"][iid]={"pos":ppos,"id":iid,"name":"testp","content":[]}
        self.wg4.update()
    def delp(self,event):
        self.inbutton=True
        if(len(globaldata["ctrlp"])==1):
            return 0
        idd=globaldata["selctrlp"]
        # print(list(globaldata["ctrlp"].keys())[-1])
        # print(globaldata["selctrlp"])
        del(globaldata["ctrlp"][idd])
        globaldata["selctrlp"]=list(globaldata["ctrlp"].keys())[-1]
        ddl=[]
        ctrlpp=globaldata["ctrlplinks"]
        for line in range(0,len(ctrlpp)):
            if(ctrlpp[line]["idline"][0]==idd or ctrlpp[line]["idline"][1]==idd ):
                ddl.append(line)
        # print(ddl)
        ddl.reverse()
        for dd in ddl:
            del(ctrlpp[dd])
        # print(globaldata["ctrlplinks"])
        self.wg4.update()
    def addimg(self,event):
        self.inbutton=True
        if(not QGuiApplication.clipboard().image().isNull()):
            # print(QGuiApplication.clipboard().image())
            globaldata["ctrlp"][globaldata["selctrlp"]]["content"].append({"type":"img","img":QGuiApplication.clipboard().image()})
            # self.painter.drawImage(QPoint(10,10),QGuiApplication.clipboard().image())
            self.wg4.update()
        else:
            print("null img")
    def savefile(self,event):
        self.inbutton=True
        # print("file")
        globaldata["globalscale"]=self.rc2
        globaldata["globaloffset"]=self.tc2
        global openfile
        if(openfile==""):
            # print("~/Documents/"+time.strftime("%y-%m-%d-%H:%M:%S",time.localtime())+".lonenote")
            print(os.getenv("home"))
            geet=QFileDialog.getSaveFileName(self,"文件", os.environ["HOME"]+"/Documents/"+time.strftime("%y-%m-%d-%H-%M-%S",time.localtime())+".lonenote")
            openfile=os.path.splitext(geet[0])[0]+".lonenote"
        else:
            geet=[openfile]
        # print(geet)
        (ofp,off)=os.path.split(openfile)
        self.setWindowTitle(off)
        with open (openfile, 'wb')as f:
            totaldel=0
            for ctrlp in globaldata["ctrlp"].values():
                for content in ctrlp["content"]:
                    if(content["type"]=="img"):
                        ba = QByteArray()
                        buffer = QBuffer(ba)
                        buffer.open(QIODevice.WriteOnly)
                        content["img"].save(buffer,"PNG")
                        content["img"]=ba
                    elif(content["type"]=="line"):
                        ctdata=content["data"]
                        dell=[]
                        for iiin in range(0,len(ctdata)-2):
                            # QPoint().toTuple()
                            # print((ctdata[iiin+2]-ctdata[iiin]).toTuple())
                            if(self.disdel(ctdata[iiin].x(),ctdata[iiin].y(),ctdata[iiin+1].x(),ctdata[iiin+1].y(),ctdata[iiin+2].x(),ctdata[iiin+2].y())<1.0001):
                                dell.append(iiin+1)
                                # print()
                        dell.reverse()
                        totaldel=totaldel+len(dell)
                        for dd in dell:
                            del(ctdata[dd])
                        # print(len(dell))
            print(totaldel)
            # image = QImage()
            # ba = QByteArray()
            # buffer = QBuffer(ba)
            # buffer.open(QIODevice.WriteOnly)
            # image.save(buffer, "PNG")
            pickle.dump(globaldata,f)
            f.close()
        for ctrlp in globaldata["ctrlp"].values():
            for content in ctrlp["content"]:
                if(content["type"]=="img"):
                    iimg=QImage()
                    iimg.loadFromData(content["img"],"PNG")
                    # ba = QByteArray()
                    # buffer = QBuffer(ba)
                    # buffer.open(QIODevice.WriteOnly)
                    content["img"]=iimg
                    # content["img"]=ba
            # print(globaldata)
        # with open (geet[0],'rb')as f:
        #     print(pickle.load(f))
        #     f.close()
    # def qimgtoqbt():
    def disdel(self,x1,y1,x2,y2,x3,y3):#缩小文件体积
        mm=msqrt((x3-x1)**2+(y3-y1)**2)
        if(mm<0.000001):
            # print("min")
            return 1.
        elif(mm>10):
            return 2.
        return (msqrt((x2-x1)**2+(y2-y1)**2)+msqrt((x3-x2)**2+(y3-y2)**2))/mm
    def subgraph(self):#暂未使用
        begin=globaldata["selctrlp"]
        graph=globaldata["ctrlplinks"]
        subgraphset={begin}
        subgraphsetl=1
        while(True):
            for ii in graph:
                if(ii[0] in subgraphset):
                    subgraphset.add(ii[[1]])
            if(len(subgraphset)==subgraphsetl):
                break
            else:
                subgraphsetl=len(subgraphset)
        print(subgraphset)
        return subgraphset
    def event(self,event):#事件分流,手势事件
        if (event.type() == QEvent.Gesture):
            self.gevent(event)
        return super(mynote, self).event(event)
    def gevent(self,event:QGestureEvent):#处理手势事件
        # if(len(event.gestures())!=1):
        #     print(len(event.gestures()))
        #     print(event.gestures())
        for gev in event.gestures():
            # if(gev.gestureType()==Qt.GestureType.PanGesture):
            #     self.pangevent(gev)
            if(gev.gestureType()==Qt.GestureType.PinchGesture):#处理捏事件
                self.pingevent(gev)
        return super(mynote, self).event(event)
    def pingevent(self,event:QPinchGesture):#处理捏事件
        # print(event)
        if(event.state()==Qt.GestureFinished):
            self.pingeventfinished(event)#self.pingeventfinished=self.shou1song_shou
        elif(event.state()==Qt.GestureStarted):
            self.pingeventstarted(event)#self.pingeventstarted=self.shou1press_shou
        elif(event.state()==Qt.GestureUpdated):
            self.pingeventmove(event)#self.pingeventmove=self.shou1move_shou
        else:
            pass
#
#self.ppc2=event.centerPoint()-self.pos()-self.wg4.pos()
#self.rf=event.totalScaleFactor()
# self.tc0=QPointF(0,0)
# self.r=self.rc2
# self.t=self.tc2+self.tc0*self.rc2

# self.movepbeginp=event.position() #鼠标拖拽画布
# self.beginrc2=self.rc2
# self.begintc2=self.tc2
#
    def shou1press(self,event):#self.wg4.mousePressEvent=self.shou1press
        # print("mousep")
        if(self.inbutton):#按钮不触发绘制
            return 0
        # if(self.linkarrmode):
        #     self.linkarrp(event)
        #     return 0
        # print(event.position())
        # pp-((event.posF()-self.wg4.pos()-self.t)/self.r)
        self.tc0=QPointF(0,0)
        self.r=self.rc2
        self.t=self.tc2+self.tc0*self.rc2
        self.qtouchctrlp=0 #选中的控制点
        
        # print((event.position()-self.t)/self.r)
        for ctrlp in globaldata["ctrlp"].values():# 控制点的拖拽，画布不拖拽
            if((ctrlp["pos"]-(event.position()-self.tc2)/self.rc2).manhattanLength()<60):
                globaldata["selctrlp"]=ctrlp["id"]
                # print(globaldata["selctrlp"])
                self.linkarrmode=True
                self.linkarrp(event,True)
                self.wg4.update()
                self.qtouchctrlp=globaldata["selctrlp"]

        if(self.qtouchctrlp!=0):
            pass
        else:
            self.movepbeginp=event.position()
            self.beginrc2=self.rc2
            self.begintc2=self.tc2
    def shou1press_shou(self,event:QPinchGesture):
        self.beginrc2=self.rc2
        self.begintc2=self.tc2
        # self.beginppc2=event.centerPoint()-self.pos()-self.wg4.pos()
    def shou1move(self,event):#self.wg4.mouseMoveEvent=self.shou1move
        if(self.inbutton):
            return 0
        # print("mov")
        if(self.linkarrmode):
            # print("search")
            self.linkarrp(event,False)
            # return 0
        # print("mov")
        if(self.qtouchctrlp!=0):
            self.tc0=QPointF(0,0)
            self.r=self.rc2
            self.t=self.tc2+self.tc0*self.rc2
            globaldata["ctrlp"][self.qtouchctrlp]["pos"]=(event.position()-self.tc2)/self.rc2
            self.wg4.update()
        else:
            self.tf=event.position()-self.movepbeginp
            self.wg4.update()
    def shou1move_shou(self,event:QPinchGesture):
        self.ppc2=event.centerPoint()-self.pos()-self.wg4.pos()
        self.rf=event.totalScaleFactor()
    def updatac2(self):
        self.rc2=self.beginrc2*self.rf
        self.tc2=self.ppc2-self.rf*(self.ppc2-self.tf-self.begintc2)
    def shou1song(self,event):
        # print("son")
        if(self.inbutton):
            self.inbutton=False
            return 0
        self.rf=1.0
        self.tf=QPointF(0,0)
        self.beginrc2=self.rc2
        self.begintc2=self.tc2
        self.linkarrmode=False
        self.beginarr=0
    def shou1song_shou(self,event):
        self.rf=1.0
        self.tf=QPointF(0,0)
        self.beginrc2=self.rc2
        self.begintc2=self.tc2

    def getc0(self,inp):
        self.tc0=QPointF(0,0)
        self.r=self.rc2
        self.t=self.tc2+self.tc0*self.rc2
        return (inp-self.t)/self.r
    def getc1(self,inp):
        # self.tc0=QPointF(0,0)
        # self.r=self.rc2
        # self.t=self.tc2+self.tc0*self.rc2
        return (inp-self.tc2)/self.rc2
    def linkarrp(self,event,onlybegin):#控制点之间的连线，数据形式为"ctrlplinks":[{"idline":[1,2]}]
        self.tc0=QPointF(0,0)
        self.r=self.rc2
        self.t=self.tc2+self.tc0*self.rc2
        for ctrlp in globaldata["ctrlp"].values():
            if((ctrlp["pos"]+-(event.position()-self.tc2)/self.rc2).manhattanLength()<60):
                if(self.beginarr==0):#初始化beginarr
                    self.beginarr=ctrlp["id"]#获取鼠标当前位置的ctrlp
                    # print("self.beginarr",self.beginarr)
                else:
                    if(onlybegin):
                        return 0
                    if(self.beginarr==ctrlp["id"]):
                        continue
                    tmp=[self.beginarr,ctrlp["id"]]#连接起始控制点和当前点
                    # print("tmp",tmp)
                    qdel=-1
                    for link in range(0,len(globaldata["ctrlplinks"])):
                        if(globaldata["ctrlplinks"][link]["idline"]==tmp):#如果存在则标记为删除，
                            qdel=link
                            break
                    if(qdel!=-1):
                        del(globaldata["ctrlplinks"][qdel])
                    else:#未标记为删除则加入
                        globaldata["ctrlplinks"].append({"idline":tmp})
                    self.beginarr=0
                    self.linkarrmode=False
                    self.wg4.update()

                # globaldata["selctrlp"]=ctrlp["id"]
                # print(globaldata["selctrlp"])
                # self.update()
                # self.qtouchctrlp=globaldata["selctrlp"]
    # def linkarrm(self,event):
    # def linkarrr(self,event):
    def begindrawline(self,event):
        globaldata["ctrlp"][globaldata["selctrlp"]]["content"].append({"type":"line","data":[]})
        self.nowdrawline=globaldata["ctrlp"][globaldata["selctrlp"]]["content"][-1]

    def intline(self,event):
        self.tc0=globaldata["ctrlp"][globaldata["selctrlp"]]["pos"]
        self.r=self.rc2
        self.t=self.tc2+self.tc0*self.rc2
        # print(self.r)
        # print(self.t)
        self.nowdrawline["data"].append((event.position()-self.t)/self.r)
        # print(event.posF()-self.wg4.pos())
        self.drawpartq=True
        self.wg4.update()
        # print("dd?")
        # self.wg4.repaint(1,1,100,100)
    def endline(self,event):
        pass
    # def penpress(self,event):
    #     self.begindrawline(event)
    # def pinrange(x,y):

    def tabletEvent_pen(self,event:QTabletEvent):
        # print(event.pointerType())
        # print("kkk")
        if(event.pointerType()==QPointingDevice.PointerType.Eraser):
            if(event.type()==QEvent.Type.TabletPress):
                # print("p")
                self.tc0=globaldata["ctrlp"][globaldata["selctrlp"]]["pos"]
                self.updatac2()
                self.r=self.rc2
                self.t=self.tc2+self.tc0*self.rc2
                self.erabegin=((event.position()-self.t)/self.r)
                # event.position()
                print(self.erabegin)
            elif(event.type()==QEvent.Type.TabletRelease):
                self.tc0=globaldata["ctrlp"][globaldata["selctrlp"]]["pos"]
                self.updatac2()
                self.r=self.rc2
                self.t=self.tc2+self.tc0*self.rc2
                # event.pos()
                # event.globalPos
                mmm=((event.position()-self.t)/self.r)
                if(mmm.x()>self.erabegin.x()):
                    mmmx=mmm.x()
                    nnnx=self.erabegin.x()
                else:
                    mmmx=self.erabegin.x()
                    nnnx=mmm.x()
                if(mmm.y()>self.erabegin.y()):
                    mmmy=mmm.y()
                    nnny=self.erabegin.y()
                else:
                    mmmy=self.erabegin.y()
                    nnny=mmm.y()
                # mmmx=mmm.x()
                # mmmy=mmm.y()
                # nnnx=self.erabegin.x()
                # nnny=self.erabegin.y()
                dellist=[]
                select=globaldata["ctrlp"][globaldata["selctrlp"]]["content"]
                # tmppp=((event.posF()-self.t)/self.r)
                for line in range(len(select)-1,-1,-1):
                    if(select[line]["type"]=="line"):
                        for pp in select[line]["data"]:
                            if(((mmmx>pp.x()>nnnx))and(mmmy>pp.y()>nnny)):
                                dellist.append(line)
                                break
                    # if(dellist!=[]):
                    #     break
                # if(len(dellist)!=0):
                #     print(dellist)
                # dellist.reverse()
                # print(dellist)
                for i in dellist:
                    del(select[i])
                self.drawpartq=False
                self.wg4.update()
                self.qdrawEraser=False
            else:
                self.tc0=globaldata["ctrlp"][globaldata["selctrlp"]]["pos"]
                self.updatac2()
                self.r=self.rc2
                self.t=self.tc2+self.tc0*self.rc2
                self.eramove=((event.position()-self.t)/self.r)
                self.qdrawEraser=True
                self.drawpartq=True
                self.wg4.update()
            # self.tc0=globaldata["ctrlp"][globaldata["selctrlp"]]["pos"]
            self.r=self.rc2
            self.t=self.tc2+self.tc0*self.rc2
            # dellist=[]
            # select=globaldata["ctrlp"][globaldata["selctrlp"]]["content"]
            # tmppp=((event.posF()-self.t)/self.r)
            # for line in range(len(select)-1,-1,-1):
            #     if(select[line]["type"]=="line"):
            #         for pp in select[line]["data"]:
            #             if((pp-tmppp).manhattanLength()<10):
            #                 dellist.append(line)
            #                 break
            #     if(dellist!=[]):
            #         break
            # # if(len(dellist)!=0):
            # #     print(dellist)
            # dellist.reverse()
            # for i in dellist:
            #     del(select[i])
            # self.wg4.update()
                            # QPoint(0,0).manhattanLength
        else:
            if(event.type()==QEvent.Type.TabletPress):
                # print("press")
                # print(self.selectctrlpid)
                # globaldata["ctrlp"][self.selectctrlpid]["content"].append({"type":"line","data":[]})
                # self.nowdraw=globaldata["ctrlp"][self.selectctrlpid]["content"][-1]
                self.begindrawline(event)
            elif(event.type()==QEvent.Type.TabletRelease):
                # print("release")
                # pass
                self.endline(event)
            else:
                self.intline(event)
            # print("app")
            # print(event.globalPosition().x())
            # self.nowdraw["data"].append((event.globalPosition().x()-self.pos().x()-self.wg4.pos().x()-self.offset.x())/self.scale[0])
            # self.nowdraw["data"].append((event.globalPosition().y()-self.pos().y()-self.wg4.pos().y()-self.offset.y())/self.scale[0])
            # self.nowdraw["data"].append((event.posF()-self.wg4.pos()-self.offset)/self.scale[0])
            # # print(event.posF()-self.wg4.pos())
            # # self.nowdraw["data"].append((event.position()-self.wg4.pos()-self.offset)/self.scale[0])
            # self.renderpart([self.selectctrlpid,-1])
            # self.wg4.update()

        # globaldata["ctrlp"][0]["content"][0]["data"]=globaldata["ctrlp"][0]["content"][0]["data"]
        # print(event)
        # print(event.globalPosition())
        event.accept()
    # def drawEraser(self):

    def penmove(self,event):
        self.nowpendraw
        self.updataqt()

    def pensong(self,event):
        self.globaldata
        self.nowpendraw
    def mydrawp(self,event):
        # print("paintEvent")
        if(self.drawpartq):
            # print("drawpart")
            # self.drawgolbaldatatoscreen(event)
            self.drawpart(event)
        else:
            self.drawgolbaldatatoscreen(event)
    def drawpart(self,event):
        # print("drawpart")
        pter=QPainter(self.wg4)
        pen=pter.pen()
        pen.setColor(QColor(self.pencol))
        # pen.setJoinStyle(Qt.RoundJoin)
        pen.setCapStyle(Qt.RoundCap)
        pen.setWidth(2)
        pter.setPen(pen)
        # bs=QBrush(QColor(49,54,59))
        # # pen=QPen(QColor(100,0,100))
        # pter.setBrush(bs)
        # pter.drawRect(-5,-5,self.wg4.width()+10,self.wg4.height()+10)
        pter.setRenderHints(QPainter.Antialiasing )
        pter.resetTransform()
        pter.translate(self.tc2)
        pter.scale(self.rc2,self.rc2)
        # self.drawlinks(event,pter)
        # for ctrlp in globaldata["ctrlp"].values():
        ctrlp=globaldata["ctrlp"][globaldata["selctrlp"]]
        pter.resetTransform()
        pter.translate(self.tc2)
        pter.scale(self.rc2,self.rc2)
        # self.drawctrlpoint(ctrlp,globaldata["selctrlp"],pter,ctrlp["pos"].x(),ctrlp["pos"].y())
        self.tc0=ctrlp["pos"]
        self.updatac2()
        self.r=self.rc2
        self.t=self.tc2+self.tc0*self.rc2
        pter.resetTransform()
        pter.translate(self.t)
        pter.scale(self.r,self.r)
        # for content in ctrlp["content"]:
        self.drawpartq=False
        if(self.qdrawEraser):
            self.tc0=globaldata["ctrlp"][globaldata["selctrlp"]]["pos"]
            self.updatac2()
            self.r=self.rc2
            self.t=self.tc2+self.tc0*self.rc2
            pter.resetTransform()
            pter.translate(self.t)
            pter.scale(self.r,self.r)
            if(self.erabegin.x()<self.eramove.x()):
                xx=self.erabegin.x()
                ww=self.eramove.x()-self.erabegin.x()
            else:
                xx=self.eramove.x()
                ww=self.erabegin.x()-self.eramove.x()
            if(self.erabegin.y()<self.eramove.y()):
                yy=self.erabegin.y()
                hh=self.eramove.y()-self.erabegin.y()
            else:
                yy=self.eramove.y()
                hh=self.erabegin.y()-self.eramove.y()
            # pter.drawRect(QRect(self.erabegin,self.eramove))
            bs=QBrush(QColor(0,0,0,0))#透明
            # bs=QBrush(QColor(49,54,59))
        # pen=QPen(QColor(100,0,100))
            pter.setBrush(bs)
            pter.drawRect(QRectF(xx,yy,ww,hh))
        if(len(ctrlp["content"])==0):
            return 0
        content=ctrlp["content"][-1]
        if(content["type"]=="line"):
            # if(len(content["data"])>10):
            #     pter.drawLines(content["data"])
            #     pter.drawLines(content["data"][1:])
            # else:
            pter.drawPolyline(content["data"])
            # elif(content["type"]=="text"):
            #     pter.drawText(content["pos"],content["str"])
            #     # self.drawtext(content)
            # elif(content["type"]=="img"):
            #     pter.drawImage(QPointF(30,0),content["img"])
    def drawgolbaldatatoscreen(self,event):
        # print("global")
        # print(self.wg4.width(),self.wg4.height())
        pter=QPainter(self.wg4)
        # pter.begin(self.wg4)
        # bs=QBrush(QColor(0,0,0,0))
        bs=QBrush(self.bcol)
        # bs=QBrush(QColor(49,54,59))
        # bs=QBrush(QColor(0,0,0,10))
        # pen=QPen(QColor(100,0,100))
        pter.setBrush(bs)
        # pter.setCompositionMode(QPainter.CompositionMode_SourceOut)
        # pter.setCompositionMode(QPainter.CompositionMode_Clear)
        pter.drawRect(-5,-5,self.wg4.width()+10,self.wg4.height()+10)
        # pter.fillRect(5,5,self.wg4.width()+10,self.wg4.height()+10,Qt.SolidPattern)
        # pter.fillRect()
        self.tc0=globaldata["ctrlp"][globaldata["selctrlp"]]["pos"]
        self.updatac2()
        self.r=self.rc2
        self.t=self.tc2+self.tc0*self.rc2
        pter.resetTransform()
        pter.translate(self.t)
        pter.scale(self.r,self.r)
        pen=pter.pen()
        pen2=pter.pen()
        # pen2.setWidth(1)
        pen2.setWidthF(0.1)
        pen2.setColor(self.meshcol)
        # pen2.setStyle(Qt.DotLine)
        pter.setPen(pen2)
        sizex=200
        sizey=200
        for i in range(sizex):
            pter.drawLine(QPointF(40+i*20,0),QPointF(40+i*20,sizey*20))
        for i in range(sizey):
            pter.drawLine(QPointF(40,i*20),QPointF(40+sizex*20,i*20))
        pter.setPen(pen)

        self.drawgolbaldata(pter)
    def drawgolbaldata(self,pter:QPainter,allshow=False):
        # print("global")
        self.listshowctrlp()
        pen=pter.pen()
        pen.setWidth(2)
        # if(self.qrdcol1.isChecked()):
        pen.setColor(QColor(self.pencol))
        # print(self.pencol)
        # elif(self.qrdcol2.isChecked()):
            # pen.setColor(QColor("#007acc"))

        # pter.drawStaticText(QPoint(140,140), QStaticText('K<sub>max</sub>=K<sub>2</sub> &middot; 3'))
        # pen.setJoinStyle(Qt.RoundJoin)
        pen.setCapStyle(Qt.RoundCap)
        pter.setPen(pen)
        pter.setRenderHints(QPainter.Antialiasing )
        showx=[(-50-self.tc2.x())/self.rc2,(50+self.wg4.width()-self.tc2.x())/self.rc2]
        showy=[(-50-self.tc2.y())/self.rc2,(50+self.wg4.height()-self.tc2.y())/self.rc2]
        selid=globaldata["selctrlp"]
        tmpvv=list(globaldata["ctrlp"].values())
        selwhere=0
        for tmpp in range(0,len(tmpvv)):
            # print(tmpvv)
            if((tmpvv[tmpp])["id"]==selid):
                selwhere=tmpp
                break
        tmpvv=tmpvv[0:selwhere]+tmpvv[selwhere+1:len(tmpvv)]+[tmpvv[selwhere]]
        # print("tmpvv",tmpvv)
        for ctrlp in tmpvv:
            # self.qshowbylink(ctrlp["id"])
            if((not allshow)and( not self.qshowbylink(ctrlp["id"]))):
                continue
            # if(ctrlp["id"]==selid):
            #     print(selid)
            # pter.resetTransform()
            # pter.translate(self.tc2)
            # pter.scale(self.rc2,self.rc2)
            # self.drawctrlpoint(ctrlp,globaldata["selctrlp"],pter,ctrlp["pos"].x(),ctrlp["pos"].y())
            self.tc0=ctrlp["pos"]
            thisct0x=self.tc0.x()
            thisct0y=self.tc0.y()
            self.updatac2()
            self.r=self.rc2
            self.t=self.tc2+self.tc0*self.rc2
            pter.resetTransform()
            pter.translate(self.t)
            pter.scale(self.r,self.r)
            pterdrawLines=pter.drawLines
            # mmpfun=functools.partial(self.mapdrawfun,pter)
            # map(mmpfun,ctrlp["content"])
            # for cc in ctrlp["content"]:
                # mmpfun(cc)
            # pter.end()
    # def mapdrawfun(pter:QPainter,content):
            # showy=[-50-1*self.tc2/self.rc2,(50+self.wg4.height()-self.tc2)/self.rc2]
            for content in ctrlp["content"]:
                if(content["type"]=="line"):
                    # if(len(content["data"])>10):
                    # QtConcurrent.QtConcurrent.
                    xxx=content["data"][0].x()+thisct0x
                    yyy=content["data"][0].y()+thisct0y
                    if(showx[0]<xxx<showx[1] and showy[0]<yyy<showy[1]):
                        # if(content["data"][0])
                        pter.drawLines(content["data"])
                        # pter.drawLines(content["data"])
                        pter.drawLines(content["data"][1:])
                    # else:
                    #     pter.drawPolyline(content["data"])
                elif(content["type"]=="text"):
                    pter.drawStaticText(QPointF(40,0),QStaticText( content["statictext"]))
                    # pter.drawText(content["pos"],content["statictext"])
                    # self.drawtext(content)
                elif(content["type"]=="img"):
                    pter.drawImage(QPointF(30,0),content["img"])
                # elif(content["type"]=="pdfpage"):
                #     pter.drawImage(QPointF(30,0),content["img"])
                    # {"type":"pdfpage","filename":"test.pdf","page":1}
        # if(self.qdrawEraser):
        #     self.tc0=globaldata["ctrlp"][globaldata["selctrlp"]]["pos"]
        #     self.updatac2()
        #     self.r=self.rc2
        #     self.t=self.tc2+self.tc0*self.rc2
        #     pter.resetTransform()
        #     pter.translate(self.t)
        #     pter.scale(self.r,self.r)
        #     if(self.erabegin.x()<self.eramove.x()):
        #         xx=self.erabegin.x()
        #         ww=self.eramove.x()-self.erabegin.x()
        #     else:
        #         xx=self.eramove.x()
        #         ww=self.erabegin.x()-self.eramove.x()
        #     if(self.erabegin.y()<self.eramove.y()):
        #         yy=self.erabegin.y()
        #         hh=self.eramove.y()-self.erabegin.y()
        #     else:
        #         yy=self.eramove.y()
        #         hh=self.erabegin.y()-self.eramove.y()
        #     # pter.drawRect(QRect(self.erabegin,self.eramove))
        #     pter.drawRect(QRectF(xx,yy,ww,hh))
            # print(QRectF(xx,yy,ww,hh),self.erabegin,self.eramove)
        for ctrlp in tmpvv:
            # self.qshowbylink(ctrlp["id"])
            # if((not allshow)and( not self.qshowbylink(ctrlp["id"]))):
            #     continue
            pter.resetTransform()
            pter.translate(self.tc2)
            pter.scale(self.rc2,self.rc2)
            self.drawctrlpoint(ctrlp,globaldata["selctrlp"],pter,ctrlp["pos"].x(),ctrlp["pos"].y())
        pter.resetTransform()
        pter.translate(self.tc2)
        pter.scale(self.rc2,self.rc2)
        self.drawlinks(pter)
    def drawlinks(self,pter:QPainter):
        # print(globaldata["ctrlplinks"])
        for link in globaldata["ctrlplinks"]:
            # print(link)
            # print(globaldata["ctrlp"][link[0]])
            pp=[globaldata["ctrlp"][link["idline"][0]]["pos"],globaldata["ctrlp"][link["idline"][1]]["pos"]]
            tmp=(pp[1]-pp[0])
            lll=msqrt(tmp.x()**2+tmp.y()**2)
            if(lll>10):
                ppll=[pp[0]+20*tmp/lll,pp[1]-20*tmp/lll]
                tmp2=pp[0]+20*tmp/lll
                # print(tmp2)
                pter.drawArc(QRect(tmp2.x()-7,tmp2.y()-7,14,14),0,16*360)
                pter.drawLines(ppll)
    def drawctrlpoint(self,ctrlp,sid,painter:QPainter,x,y):
        pen2=painter.pen()
        pen2.setColor(self.themcol1)
        # pen2.setStyle(Qt.DotLine)
        painter.setPen(pen2)
        if(ctrlp["id"]==sid):
            painter.drawLines([
                QPointF(x   ,y+20),
                QPointF(x   ,y+40),
                QPointF(x   ,y+40),
                QPointF(x+10,y+40+20),
                QPointF(x+10,y+40+20),
                QPointF(x   ,y+40+20+20),
                QPointF(x   ,y+40+20+20),
                QPointF(x-10,y+40+20),
                QPointF(x-10,y+40+20),
                QPointF(x   ,y+40)
                ])
            painter.drawLines([
                QPointF(x   ,y+50      ),
                QPointF(x+10,y+50+20   ),
                QPointF(x+10,y+50+20   ),
                QPointF(x   ,y+50+20+20),
                QPointF(x   ,y+50+20+20),
                QPointF(x-10,y+50+20   ),
                QPointF(x-10,y+50+20   ),
                QPointF(x   ,y+50      )
                ])
        # mypen=self.painter.pen()
        # mypen.setColor(QColor(255,255,255))
        # mypen.setWidth(2)
        # mypen.setStyle(Qt.SolidLine)
        # mypen.setCapStyle(Qt.RoundCap)
        # self.painter.setPen(mypen)
        # self.painter.drawText(QPoint(px,py),"0")
        # painter.drawRect(QRectF(x-20,y-20,40,40))
        painter.drawArc(QRectF(x-20,y-20,40,40),0,16*360)
        self.myoption =QTextOption(Qt.AlignCenter)
        self.myoption.setWrapMode(QTextOption.WrapAnywhere)
        painter.drawText(QRectF(x-20,y-20,40,40),str(ctrlp["id"]),self.myoption)
        # self.painter.drawRect(QRectF(px+100/2-80/2,py+100/2-50/2, 80,50))
    def testdraw(self,event):
        pter=QPainter(self.wg4)
        # self.setpc0(QPointF(0,0))
        self.tc0=QPointF(0,0)
        self.updatac2()
        self.r=self.rc2
        self.t=self.tc2+self.tc0*self.rc2
        pter.resetTransform()
        pter.translate(self.t)
        pter.scale(self.r,self.r)
        pter.drawText(QPoint(100,100),"0")
        pter.drawText(QPoint(5,5),"-1")
        pter.drawLine(QPoint(0,0),QPoint(100,100))

        self.tc0=QPointF(200,200)
        self.updatac2()
        self.r=self.rc2
        self.t=self.tc2+self.tc0*self.rc2
        pter.resetTransform()
        pter.translate(self.t)
        pter.scale(self.r,self.r)
        pter.drawText(QPoint(100,100),"0")
        pter.drawText(QPoint(5,5),"-1")
        pter.drawLine(QPoint(0,0),QPoint(100,100))
        # self.pc0=QPointF(100,100)
        # self.updataccc()
        # # print("get:",self.t)
        # pter.resetTransform()
        # pter.scale(self.r,self.r)
        # pter.translate(self.t)
        # pter.drawText(QPoint(100,100),"1")
        # pter.drawText(QPoint(300,300),"2")
        # pter.drawLine(QPointF(0,0),QPointF(100,100))

    def updataqt(self,event):
        pass
    def listshowctrlp(self):
        self.listshowctrlps=[globaldata["selctrlp"]]
        for ctrlp in globaldata["ctrlp"].values():
            tmpp=ctrlp["pos"]*self.rc2+self.tc2
            xxx=tmpp.x()
            yyy=tmpp.y()
            if((-50<xxx<self.wg4.width()+50) and(-50<yyy<self.wg4.height()+50)):
                self.listshowctrlps.append(ctrlp["id"])
        # print(self.listshowctrlps)
    def qshowbylink(self,id):
        # print(id)
        if(id==globaldata["selctrlp"]):
            # print(id)
            return True
        idlinks=[id]
        for itoi in globaldata["ctrlplinks"]:
            if(itoi["idline"][0]==id):
                idlinks.append(itoi["idline"][1])
            if(itoi["idline"][1]==id):
                idlinks.append(itoi["idline"][0])
        for shp in self.listshowctrlps:
            for selp in idlinks:
                if(selp==shp):
                    # print(id)
                    return True
        return False



openfile=""

# print(time.time())
# app=1
app = QApplication(sys.argv)
if __name__ == '__main__':
    # 创建了一个QApplication对象，对象名为app，带两个参数argc,argv
    # 所有的PyQt5应用必须创建一个应用（Application）对象。sys.argv参数是一个来自命令行的参数列表。
    # global app

    print(sys.argv)
    if(len(sys.argv)!=1):
        openfile=sys.argv[1]
        with open (openfile,'rb')as f:
            globaldata=pickle.load(f)
            for ctrlp in globaldata["ctrlp"].values():
                for content in ctrlp["content"]:
                    if(content["type"]=="img"):
                        iimg=QImage()
                        iimg.loadFromData(content["img"],"PNG")
                        # ba = QByteArray()
                        # buffer = QBuffer(ba)
                        # buffer.open(QIODevice.WriteOnly)
                        content["img"]=iimg
                        # content["img"]=iimg.scaledToHeight(int(iimg.height()/1.45))
                        # content["img"]=ba
            # print(globaldata)
            f.close()
    # 窗口组件初始化
    # print(app.allWindows())
    pet = mynote()
    # 1. 进入时间循环；
    # 2. wait，直到响应app可能的输入；
    # 3. QT接收和处理用户及系统交代的事件（消息），并传递到各个窗口；
    # 4. 程序遇到exit()退出时，机会返回exec()的值。
    app.exec()
    # pet.pool.close()
    # pet.pool.join()
    sys.exit()
    
