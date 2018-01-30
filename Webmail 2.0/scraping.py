from selenium import webdriver
from robobrowser import RoboBrowser
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import inside_ui
import display
import webmail
import com
from sys import argv,exit
import pickle
import os


class wind(QWidget,webmail.Ui_Form):

    def __init__(self,parent=None):
        super(wind,self).__init__(parent)
        self.setupUi(self)
        self.c=0
        self.nLink=0
        self.pLink=0
        self.br=0
        self.pr=0
        self.bro=0
        self.b=0
        self.addA = 0
        self.msg=0
        self.tag = []
        self.lo.clicked.connect(self.do)
        self.br = webdriver.PhantomJS()
        ur = 'https://webmail.daiict.ac.in'
        QCoreApplication.processEvents()
        self.br.get(ur)
        QCoreApplication.processEvents()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ref)
        self.timer.start(120000)
        if os.path.isfile('helper.pickle'):
            with open('helper.pickle','rb') as f:
                d = pickle.load(f)
            self.rem.setChecked(True)
            self.user.setText(d['username'])
            self.pas.setText(d['password'])
            self.lo.hide()
            self.show()
            self.do()
        else:
            self.show()

    def ref(self):
        if self.br.current_url == 'https://webmail.daiict.ac.in/':
            self.br.execute_script('location.reload()')
        else:
            self.inb()
    def do(self):
        if True:
            usr = self.user.text()
            p = self.pas.text()

            user = self.br.find_element_by_id('username')
            user.send_keys(usr)

            pas = self.br.find_element_by_id('password')
            pas.send_keys(p)

            sub = self.br.find_element_by_xpath("//input[@type='submit']")
            QCoreApplication.processEvents()
            sub.click()
            QCoreApplication.processEvents()
            if self.br.current_url !='https://webmail.daiict.ac.in/':
                if self.rem.isChecked():
                    d = {'username':usr,'password':p}
                    with open('helper.pickle','wb') as f:
                        pickle.dump(d, f, protocol=pickle.HIGHEST_PROTOCOL)
                elif os.path.isfile('helper.pickle'):
                    os.remove('helper.pickle')
                self.user.hide()
                self.pas.hide()
                self.bro = RoboBrowser(parser='html.parser')
                self.bro.open('https://webmail.daiict.ac.in')
                fo = self.bro.get_form(action='/')
                fo['username'].value = usr
                fo['password'].value = p
                QCoreApplication.processEvents()
                self.bro.submit_form(fo)
                QCoreApplication.processEvents()
                self.c = inside(self)
                self.c.pre.setEnabled(False)
                self.c.nex.clicked.connect(self.n)
                self.c.pre.clicked.connect(self.p)
                self.c.de.clicked.connect(self.d)
                self.c.sa.clicked.connect(lambda:self.c.mails.selectAll())
                self.c.cs.clicked.connect(lambda:self.c.mails.clearSelection())
                self.c.ba.clicked.connect(self.bac)
                self.c.inbox.clicked.connect(self.inb)
                self.c.sent.clicked.connect(self.showSent)
                self.c.junk.clicked.connect(self.ju)
                self.c.thrash.clicked.connect(self.th)
                self.c.se.clicked.connect(self.search)
                self.c.compose.clicked.connect(self.comp)
                self.c.out.clicked.connect(self.logOut)
                self.c.mails.itemDoubleClicked.connect(self.showMail)
                self.c.sendB.clicked.connect(self.send)
                self.c.cancel.clicked.connect(lambda :self.inb())
                self.c.draft.clicked.connect(self.dr)

                self.doo()
            else:
                self.user.clear()
                self.pas.clear()
                user = self.br.find_element_by_id('username')
                pas = self.br.find_element_by_id('password')
                user.clear()
                pas.clear()
                stat = QLabel(self)
                stat.setText('Username or Password incorrect')
                stat.setGeometry(0,0,890,40)
                stat.setStyleSheet('background-color:red;color:white;font-size:16pt;Text-align:center')
                stat.show()
                QTimer.singleShot(3000,lambda:stat.hide())
    def logOut(self):
        self.br.find_element_by_link_text('Log Out').click()
        self.br.get('https://webmail.daiict.ac.in')
        if self.b!=0:
            self.hid()
            self.c.ba.hide()
            self.b=0
        if self.msg!=0:
            self.msg.line.hide()
            self.msg.line_2.hide()
            self.msg.line_3.hide()
            self.msg.msgTo.hide()
            self.msg.textEdit.hide()
            self.msg.su.hide()
            self.c.cancel.hide()
            self.c.sendB.hide()
            self.c.draft.hide()
            self.pr.hide()
            self.msg=0

        self.c.back.hide()
        self.c.inbox.hide()
        self.c.compose.hide()
        self.c.sent.hide()
        self.c.scrollAreaWidgetContents.hide()
        self.c.nex.hide()
        self.c.pre.hide()
        self.c.cs.hide()
        self.c.de.hide()
        self.c.label.hide()
        self.c.nm.hide()
        self.c.sa.hide()
        self.c.junk.hide()
        self.c.thrash.hide()
        self.c.search.hide()
        self.c.se.hide()
        self.c.out.hide()
        self.user.show()
        self.pas.show()
        self.lo.show()

    def dr(self):
        form = self.br.find_element_by_xpath("//form[@name='composeForm']")
        input = form.find_elements_by_tag_name('input')

        subject = input[13]
        subject.send_keys(self.msg.su.text())

        to = form.find_element_by_tag_name('textarea')
        toText = self.msg.msgTo.text().split(',')
        for i in range(len(toText)):
            if '@' not in toText[i]:
                toText[i] = toText[i] + '@daiict.ac.in'

        to.send_keys(','.join(toText))

        self.br.find_element_by_id('body_ifr').send_keys(' ' + self.msg.textEdit.toPlainText())

        input[5].click()

    def search(self):
        t = self.c.search.text()
        f = self.br.find_element_by_id('searchField')
        f.send_keys(t)
        s = self.br.find_element_by_class_name('SearchButton')
        QCoreApplication.processEvents()
        s.click()
        QCoreApplication.processEvents()
        self.doo()

    def ju(self):
        s = self.br.find_element_by_id('FLDR4')
        QCoreApplication.processEvents()
        s.click()
        QCoreApplication.processEvents()
        self.doo()
    def th(self):
        s = self.br.find_element_by_id('FLDR3')
        QCoreApplication.processEvents()
        s.click()
        QCoreApplication.processEvents()
        self.doo()

    def inb(self):
        s = self.br.find_element_by_id('FLDR2')
        QCoreApplication.processEvents()
        s.click()
        QCoreApplication.processEvents()
        self.doo()
    def showSent(self):

        s = self.br.find_element_by_id('FLDR5')
        QCoreApplication.processEvents()
        s.click()
        QCoreApplication.processEvents()
        self.doo()
    def d(self):
        dlt = self.br.find_element_by_id('SOPDELETE')
        ind = self.c.mails.selectedIndexes()
        for i in ind:
            self.br.find_element_by_id('C' + str(i.row())).click()
        QCoreApplication.processEvents()
        dlt.click()
        QCoreApplication.processEvents()
        self.doo()
    def bac(self):
        self.br.back()
        self.doo()
    def n(self):

        self.nLink = self.br.find_element_by_id('NEXT_PAGE')
        QCoreApplication.processEvents()
        self.nLink.click()
        QCoreApplication.processEvents()
        self.doo()

    def p(self):
        self.pLink = self.br.find_element_by_id('PREV_PAGE')
        QCoreApplication.processEvents()
        self.pLink.click()
        QCoreApplication.processEvents()
        self.doo()

    def doo(self):
        self.tag = []
        for i in range(25):
            QCoreApplication.processEvents()
            try:
                a = self.br.find_element_by_id('R' + str(i))
                self.tag.append(a)
            except:
                pass
        QCoreApplication.processEvents()
        try:
            self.nLink = self.br.find_element_by_id('NEXT_PAGE')
            self.c.nex.setEnabled(True)
        except:
            self.c.nex.setEnabled(False)
        try:
            self.pLink = self.br.find_element_by_id('PREV_PAGE')
            self.c.pre.setEnabled(True)
        except:
            self.c.pre.setEnabled(False)
        self.c.mails.clear()
        QCoreApplication.processEvents()
        for i in enumerate(self.tag):
            lab = QListWidgetItem()
            lab.setText(self.tag[i[0]].text)
            self.c.mails.insertItem(i[0], lab)
        self.c.mails.show()
        if self.b!=0:
            self.hid()
            self.c.sa.show()
            self.c.cs.show()
            self.c.de.show()
            self.c.ba.hide()
            self.c.nex.show()
            self.c.pre.show()
            self.b=0
        if self.msg!=0:
            self.msg.line.hide()
            self.msg.line_2.hide()
            self.msg.line_3.hide()
            self.msg.msgTo.hide()
            self.msg.textEdit.hide()
            self.msg.su.hide()
            self.c.cancel.hide()
            self.c.sendB.hide()
            self.c.draft.hide()
            self.pr.hide()
            self.c.sa.show()
            self.c.cs.show()
            self.c.de.show()
            self.c.nex.show()
            self.c.pre.show()
            self.msg=0
    def comp(self):
        if self.msg==0:
            com = self.br.find_element_by_xpath("//*[contains(text(),'Compose')]")
            com.click()
            self.msg = message(self.c.scrollAreaWidgetContents)
            self.c.cancel.show()
            self.c.sendB.show()
            self.c.draft.show()
            self.c.nex.hide()
            self.c.pre.hide()
            self.c.sa.hide()
            self.c.cs.hide()
            self.c.de.hide()
            self.c.mails.hide()
            if self.b!=0:
                self.hid()
                self.b=0
            self.pr = QWidget(self)
            self.pr.setGeometry(0, 364, 207, 236)
            self.attach = [0]*8
            for i in range(8):
                self.attach[i] = QPushButton(self.pr)
                self.attach[i].setStyleSheet('Text-align:left')
                self.attach[i].setGeometry(0, 30 * i, 211, 32)
                self.attach[i].setText('No Attachments')

            self.attach[0].clicked.connect(lambda:self.sendA(0))
            self.attach[1].clicked.connect(lambda: self.sendA(1))
            self.attach[2].clicked.connect(lambda: self.sendA(2))
            self.attach[3].clicked.connect(lambda: self.sendA(3))
            self.attach[4].clicked.connect(lambda: self.sendA(4))
            self.attach[5].clicked.connect(lambda: self.sendA(5))
            self.attach[6].clicked.connect(lambda: self.sendA(6))
            self.attach[7].clicked.connect(lambda: self.sendA(7))
            self.pr.show()
    def sendA(self,i):
        if self.attach[i].text()!='No Attachments':
            self.attach[i].setText('No Attachments')
            self.addA-=1
        else:
            a = QFileDialog.getOpenFileName()[0]
            if a:
                self.attach[i].setText(a)
                self.addA+=1


    def send(self):

        form = self.br.find_element_by_xpath("//form[@name='composeForm']")
        input = form.find_elements_by_tag_name('input')
        add = input[6]
        if self.addA!=0:
            add.click()
            td = self.br.find_element_by_xpath('//td[@class="ZhAppContent"]')
            inp = td.find_elements_by_tag_name('input')
            for i in range(8):
                if self.attach[i].text() != 'No Attachments':
                    inp[i].clear()
                    inp[i].send_keys(self.attach[i].text())
                    self.addA-=1
            done = self.br.find_element_by_xpath('//input[@value="Done"]')
            done.click()

        form = self.br.find_element_by_xpath("//form[@name='composeForm']")
        input = form.find_elements_by_tag_name('input')

        send = input[1]

        subject = input[13]
        if not self.msg.su.text():
            subject.send_keys('No Subject')
        else:
            subject.send_keys(self.msg.su.text())

        to = form.find_element_by_tag_name('textarea')
        toText = self.msg.msgTo.text().split(',')
        for i in range(len(toText)):
            if '@' not in toText[i]:
                toText[i] = toText[i] + '@daiict.ac.in'
        to.send_keys(','.join(toText))

        te = self.br.find_element_by_id('body_ifr')
        self.msg.textEdit.setHtml(self.msg.textEdit.toPlainText())
        te.send_keys(' '+self.msg.textEdit.toHtml())
        send.click()
        try:
            if self.br.find_element_by_class_name('Status').text == ' Your message has been sent.':
                self.doo()
            else:
                stat = QLabel(self)
                stat.setText('Could not send message due to invalid address(es)')
                stat.setGeometry(0, 0, 890, 40)
                stat.setStyleSheet('background-color:red;color:white;font-size:16pt;')
                stat.show()
                QTimer.singleShot(3000, lambda: stat.hide())
                com = self.br.find_element_by_xpath("//*[contains(text(),'Compose')]")
                com.click()




        except:
            pass
    def hid(self):
        self.b.From.hide()
        self.pr.hide()
        self.b.subject.hide()
        self.b.read.hide()
        self.b.line.hide()
        self.b.line_2.hide()
        self.b.line_3.hide()


    def showMail(self,item):

        self.c.nex.hide()
        self.c.pre.hide()
        self.c.ba.show()
        self.c.sa.hide()

        self.c.cs.hide()
        self.c.de.hide()
        self.tag[self.c.mails.currentRow()].click()
        a = self.br.find_elements_by_xpath("//td[@class='MsgHdrValue']")
        self.b = read(self.c.scrollAreaWidgetContents)
        self.b.From.setText(a[0].text)
        self.b.subject.setText(a[1].text)
        self.pr = QWidget(self)
        self.pr.setGeometry(0,364,207,236)
        self.attach=[]
        for i in range(8):
            but = QPushButton(self.pr)
            but.setStyleSheet('Text-align:left')
            but.setGeometry(0,30*i,211,32)
            but.setText('No Attachments')
            self.attach.append(but)
        self.pr.show()

        try:
            d = self.br.find_element_by_id('iframeBody')
            att = d.find_elements_by_tag_name('tbody')
            self.attach[0].clicked.connect(lambda :self.downl(0))
            for i in enumerate(att):
                self.attach[i[0]].setText(i[1].text.split('\n')[0])
                self.attach[i[0]].clicked.connect(lambda: self.downl(i[0]))
        except:
            pass
        d = self.br.find_element_by_id('iframeBody')
        try:
            fr = d.find_element_by_tag_name('iframe')
            self.br.switch_to.frame(fr)
            self.b.read.setText(self.br.page_source)
            self.br.switch_to.default_content()

        except:
            self.b.read.setText(d.text)
        self.c.mails.hide()
    def downl(self,i):
        if self.attach[i].text()!='No Attachments':
            nm = self.attach[i].text()
            d = self.br.find_element_by_id('iframeBody')
            att = d.find_elements_by_tag_name('tbody')
            a = att[i].find_element_by_link_text('Download').get_attribute('href')
            req = self.bro.sess9ion.get(a,stream=True)
            with open('Downloads/'+nm,'wb') as f:
                f.write(req.content)

class inside(QWidget,inside_ui.Ui_Form):
    def __init__(self,parent=None):
        super(inside,self).__init__(parent)
        self.setupUi(parent)
        self.show()
class read(QWidget,display.Ui_Form):
    def __init__(self,parent=None):
        super(read,self).__init__(parent)
        self.setupUi(parent)
class message(QWidget,com.Ui_Form):
    def __init__(self,parent=None):
        super(message,self).__init__(parent)
        self.setupUi(parent)
class myEventFilter(QObject):
    def __init__(self,timer):
        super(myEventFilter,self).__init__()
        self.timer = timer
    def eventFilter(self, Qobject, Qevent):
        if Qevent.type() == QEvent.MouseButtonPress or Qevent.type() ==QEvent.MouseButtonDblClick or Qevent.type() ==QEvent.KeyPress:
            self.timer.stop()
            self.timer.start(120000)
            print("HEY THERE")
        return QObject.eventFilter(self,Qobject,Qevent)


app = QApplication(argv)
wi = wind()
fil = myEventFilter(wi.timer)
wi.installEventFilter(fil)
exit(app.exec_())
