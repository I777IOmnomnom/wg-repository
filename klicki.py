#!/usr/bin/env python

from Tkinter import *


class KlickiException(Exception):
    pass


class Klicki_Klicki_Bunti_bunti():
    def __main__(self):
        """
        @brief: Main calling funtion
        """
        self.wg_frontend()

        return

    def wg_frontend(self):
        """
        @brief: First frontend dialog linking to applications
        """
        tk = Tk()
        img = PhotoImage(file="/home/robby/GIT/lib/pictures/boerse-logo.gif")
        w_1 = Label(tk, image=img).pack()
        tk.mainloop()


if __name__ == '__main__':
    kkbb = Klicki_Klicki_Bunti_bunti()
    kkbb.__main__()
