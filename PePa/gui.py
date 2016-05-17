#!/usr/bin/python
import sys
from pen_and_papierer.dice import Dice
from PySide import QtCore, QtGui

# Creates the background application which is responsible for handling all PySide elements.
app = QtGui.QApplication(sys.argv)
width = app.desktop().screenGeometry().width()
height = app.desktop().screenGeometry().height()

# Creates the main window which is used to handle widgets.
mw = QtGui.QMainWindow()
mw.resize(960, 1080)
mw.setWindowTitle('Cthulhu')

# Paints the main window in light grey. The main window should never appear to the user!
p = mw.palette()
p.setColor(mw.backgroundRole(), QtCore.Qt.lightGray)
mw.setPalette(p)

mw.show()


class GuiException(Exception):
    pass


class Gui():
    def __init__(self):
        self.dice = Dice()
        pass

    def init(self):
        self.name_p1 = input("What's the 1st players real - investigator name?")
        self.attr1_p1 = input("What's {} strength?").format(self.name_p1)
        self.attr2_p1 = input("What's {} constitution?").format(self.name_p1)
        self.attr3_p1 = input("What's {} height").format(self.name_p1)
        self.attr4_p1 = input("What's {} dexterity?").format(self.name_p1)
        self.attr5_p1 = input("What's {} look").format(self.name_p1)
        self.attr6_p1 = input("What's {} inteligence").format(self.name_p1)
        self.attr7_p1 = input("What's {} mana?").format(self.name_p1)
        self.attr8_p1 = input("What's {} education?").format(self.name_p1)

        self.name_p2 = input("What's the 2nd players real - investigator name?")
        self.attr1_p2 = input("What's {} strength?").format(self.name_p2)
        self.attr2_p2 = input("What's {} constitution?").format(self.name_p2)
        self.attr3_p2 = input("What's {} height").format(self.name_p2)
        self.attr4_p2 = input("What's {} dexterity?").format(self.name_p2)
        self.attr5_p2 = input("What's {} look").format(self.name_p2)
        self.attr6_p2 = input("What's {} inteligence").format(self.name_p2)
        self.attr7_p2 = input("What's {} mana?").format(self.name_p2)
        self.attr8_p2 = input("What's {} education?").format(self.name_p2)

        self.name_p3 = input("What's the 3rd players real - investigator name?")
        self.attr1_p3 = input("What's {} strength?").format(self.name_p3)
        self.attr2_p3 = input("What's {} constitution?").format(self.name_p3)
        self.attr3_p3 = input("What's {} height").format(self.name_p3)
        self.attr4_p3 = input("What's {} dexterity?").format(self.name_p3)
        self.attr5_p3 = input("What's {} look").format(self.name_p3)
        self.attr6_p3 = input("What's {} inteligence").format(self.name_p3)
        self.attr7_p3 = input("What's {} mana?").format(self.name_p3)
        self.attr8_p3 = input("What's {} education?").format(self.name_p3)

        self.name_p4 = input("What's the 4th players real - investigator name?")
        self.attr1_p4 = input("What's {} strength?").format(self.name_p4)
        self.attr2_p4 = input("What's {} constitution?").format(self.name_p4)
        self.attr3_p4= input("What's {} height").format(self.name_p4)
        self.attr4_p4 = input("What's {} dexterity?").format(self.name_p4)
        self.attr5_p4 = input("What's {} look").format(self.name_p4)
        self.attr6_p4 = input("What's {} inteligence").format(self.name_p4)
        self.attr7_p4 = input("What's {} mana?").format(self.name_p4)
        self.attr8_p4 = input("What's {} education?").format(self.name_p4)

        self.name_p5 = input("What's the 5th players real - investigator name?")
        self.attr1_p5 = input("What's {} strength?").format(self.name_p5)
        self.attr2_p5 = input("What's {} constitution?").format(self.name_p5)
        self.attr3_p5 = input("What's {} height").format(self.name_p5)
        self.attr4_p5 = input("What's {} dexterity?").format(self.name_p5)
        self.attr5_p5 = input("What's {} look").format(self.name_p5)
        self.attr6_p5 = input("What's {} inteligence").format(self.name_p5)
        self.attr7_p5 = input("What's {} mana?").format(self.name_p5)
        self.attr8_p5 = input("What's {} education?").format(self.name_p5)

        self.name_p6 = input("What's the 6th players real - investigator name?")
        self.attr1_p6 = input("What's {} strength?").format(self.name_p6)
        self.attr2_p6 = input("What's {} constitution?").format(self.name_p6)
        self.attr3_p6 = input("What's {} height").format(self.name_p6)
        self.attr4_p6 = input("What's {} dexterity?").format(self.name_p6)
        self.attr5_p6 = input("What's {} look").format(self.name_p6)
        self.attr6_p6 = input("What's {} inteligence").format(self.name_p6)
        self.attr7_p6 = input("What's {} mana?").format(self.name_p6)
        self.attr8_p6 = input("What's {} education?").format(self.name_p6)

        self.gui()

        return

    def gui(self, roll=None):
        '''

        :return:
        '''
        wid = self.create_widget()

        self.push_button_dice('d4', wid, 25, 25)
        self.push_button_dice('d6', wid, 150, 25)
        self.push_button_dice('d8', wid, 275, 25)
        self.push_button_dice('d10', wid, 400, 25)
        self.push_button_dice('d20', wid, 525, 25)
        self.push_button_dice('d100', wid, 650, 25)

        self.push_button_name(str(self.name_p1), wid, 25, 150)
        self.push_button_attr(str(self.attr1_p1), wid, 10, 210)
        self.push_button_attr(str(self.attr2_p1), wid, 135, 210)
        self.push_button_attr(str(self.attr3_p1), wid, 260, 210)
        self.push_button_attr(str(self.attr4_p1), wid, 385, 210)
        self.push_button_attr(str(self.attr5_p1), wid, 510, 210)
        self.push_button_attr(str(self.attr6_p1), wid, 635, 210)
        self.push_button_attr(str(self.attr7_p1), wid, 760, 210)

        self.push_button_name(str(self.name_p2), wid, 25, 150)
        self.push_button_attr(str(self.attr1_p2), wid, 10, 210)
        self.push_button_attr(str(self.attr2_p2), wid, 135, 210)
        self.push_button_attr(str(self.attr3_p2), wid, 260, 210)
        self.push_button_attr(str(self.attr4_p2), wid, 385, 210)
        self.push_button_attr(str(self.attr5_p2), wid, 510, 210)
        self.push_button_attr(str(self.attr6_p2), wid, 635, 210)
        self.push_button_attr(str(self.attr7_p2), wid, 760, 210)

        self.push_button_name(str(self.name_p3), wid, 25, 150)
        self.push_button_attr(str(self.attr1_p3), wid, 10, 210)
        self.push_button_attr(str(self.attr2_p3), wid, 135, 210)
        self.push_button_attr(str(self.attr3_p3), wid, 260, 210)
        self.push_button_attr(str(self.attr4_p3), wid, 385, 210)
        self.push_button_attr(str(self.attr5_p3), wid, 510, 210)
        self.push_button_attr(str(self.attr6_p3), wid, 635, 210)
        self.push_button_attr(str(self.attr7_p3), wid, 760, 210)

        self.push_button_name(str(self.name_p4), wid, 25, 150)
        self.push_button_attr(str(self.attr1_p4), wid, 10, 210)
        self.push_button_attr(str(self.attr2_p4), wid, 135, 210)
        self.push_button_attr(str(self.attr3_p4), wid, 260, 210)
        self.push_button_attr(str(self.attr4_p4), wid, 385, 210)
        self.push_button_attr(str(self.attr5_p4), wid, 510, 210)
        self.push_button_attr(str(self.attr6_p4), wid, 635, 210)
        self.push_button_attr(str(self.attr7_p4), wid, 760, 210)

        self.push_button_name(str(self.name_p5), wid, 25, 150)
        self.push_button_attr(str(self.attr1_p5), wid, 10, 210)
        self.push_button_attr(str(self.attr2_p5), wid, 135, 210)
        self.push_button_attr(str(self.attr3_p5), wid, 260, 210)
        self.push_button_attr(str(self.attr4_p5), wid, 385, 210)
        self.push_button_attr(str(self.attr5_p5), wid, 510, 210)
        self.push_button_attr(str(self.attr6_p5), wid, 635, 210)
        self.push_button_attr(str(self.attr7_p5), wid, 760, 210)

        self.push_button_name(str(self.name_p6), wid, 25, 150)
        self.push_button_attr(str(self.attr1_p6), wid, 10, 210)
        self.push_button_attr(str(self.attr2_p6), wid, 135, 210)
        self.push_button_attr(str(self.attr3_p6), wid, 260, 210)
        self.push_button_attr(str(self.attr4_p6), wid, 385, 210)
        self.push_button_attr(str(self.attr5_p6), wid, 510, 210)
        self.push_button_attr(str(self.attr6_p6), wid, 635, 210)
        self.push_button_attr(str(self.attr7_p6), wid, 760, 210)

        if roll is not None:
            self.push_button_dice(str(roll), wid, 775, 25)
        else:
            pass

        wid.show()

        return

    def create_widget(self):
        global mw
        wid = QtGui.QWidget(mw)
        wid.resize(960, 1080)
        wid.setWindowTitle('Cthulhu')

        p = wid.palette()
        p.setColor(wid.backgroundRole(), QtCore.Qt.lightGray)
        wid.setPalette(p)

        return wid

    def push_button_dice(self, dice, parent, x , y):
        '''

        :param x:
        :param y:
        :param parent:
        :param name:
        :param function:
        :return:
        '''
        qbtn = QtGui.QPushButton(dice, parent)
        qbtn.setStyleSheet("QPushButton { font-size: 32pt }" )
        qbtn.clicked.connect(lambda: self.dice_roll(dice, parent))
        qbtn.resize(100, 100)
        qbtn.move(x, y)

        return qbtn

    def push_button_name(self, dice, parent, x , y):
        '''

        :param x:
        :param y:
        :param parent:
        :param name:
        :param function:
        :return:
        '''
        qbtn = QtGui.QPushButton(dice, parent)
        qbtn.setStyleSheet("QPushButton { font-size: 32pt }" )
        qbtn.clicked.connect(lambda: self.do_nothing())
        qbtn.resize(850, 50)
        qbtn.move(x, y)

        return qbtn

    def push_button_attr(self, dice, parent, x , y):
        '''

        :param x:
        :param y:
        :param parent:
        :param name:
        :param function:
        :return:
        '''
        qbtn = QtGui.QPushButton(dice, parent)
        qbtn.setStyleSheet("QPushButton { font-size: 30pt }" )
        qbtn.clicked.connect(lambda: self.do_nothing())
        qbtn.resize(115, 70)
        qbtn.move(x, y)

        return qbtn


    def dice_roll(self, dice, parent):
        roll = self.dice.get_dice_roll(dice)
        parent.hide()

        self.gui(roll)

        return

    def do_nothing(self):
        return

if __name__ == '__main__':
    Gui().init()
    sys.exit(app.exec_())