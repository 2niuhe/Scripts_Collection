__author__ = 'Niuhe'
# -*- encoding: utf8 -*-
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

filename = ''


def author():
    showinfo('作者信息', '本软件由牛河完成')


def about():
    showinfo('版权信息.Copyright', '作者保留版权')


def openfile():
    global filename
    filename = askopenfilename(defaultextension='.txt')
    if filename == '':
        filename = None
    else:
        root.title('Filename:' + os.path.basename(filename))
        textPad.delete(1.0, END)
        with open(filename, 'r') as f:
            textPad.insert(1.0, f.read())


def new():
    global filename
    root.title('Untitled file')
    filename = None
    textPad.delete(1.0, END)


def save():
    global filename
    try:
        with open(filename, 'w') as f:
            msg = textPad.get(1.0, END)
            f.write(msg)
    except Exception:
        saveas()


def saveas():
    f = asksaveasfilename(initialfile='untitled.txt', defaultextension='.txt')
    global filename
    if f:
        filename = f
    else:
        return
    with open(f, 'w') as fh:
        msg = textPad.get(1.0, END)
        fh.write(msg)
    root.title('FileName:' + os.path.basename(f))


def cut():
    textPad.event_generate('<<Cut>>')


def copy():
    textPad.event_generate('<<Copy>>')


def paste():
    textPad.event_generate('<<Paste>>')


def undo():
    textPad.event_generate('<<Undo>>')


def redo():
    textPad.event_generate('<<Redo>>')


def selectAll():
    textPad.tag_add('sel', '1.0', END)


def search():
    topsearch = Toplevel(root)
    topsearch.title('Find')
    topsearch.geometry('300x30+200+250')
    label1 = Label(topsearch, text='Find')
    label1.grid(row=0, column=0, padx=5)
    entry1 = Entry(topsearch, width=20)
    entry1.grid(row=0, column=1, padx=5)
    button1 = Button(topsearch, text='查找')
    button1.grid(row=0, column=2)
    genSearch()

    
def genSearch():
        pass


root = Tk()
root.title('Niuhe Notebook')
root.geometry('500x500+100+100')

# Creat Menu
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command(label='新建', accelerator='Ctrl + N', command=new)
filemenu.add_command(label='打开', accelerator='Ctrl + O', command=openfile)
filemenu.add_command(label='保存', accelerator='Ctrl + S', command=save)
filemenu.add_command(label='另存为', accelerator='Ctrl + Shift + S', command=saveas)
menubar.add_cascade(label='文件', menu=filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label='撤销', accelerator='Ctrl + Z', command=undo)
editmenu.add_command(label='重做', accelerator='Ctrl + Y', command=redo)
editmenu.add_separator()
editmenu.add_command(label='剪切', accelerator='Ctrl + X', command=cut)
editmenu.add_command(label='复制', accelerator='Ctrl + C', command=copy)
editmenu.add_command(label='粘贴', accelerator='Ctrl + V', command=paste)
editmenu.add_separator()
editmenu.add_command(label='查找', accelerator='Ctrl + ', command=search)
editmenu.add_command(label='全选', accelerator='Ctrl + A', command=selectAll)
menubar.add_cascade(label='编辑', menu=editmenu)

aboutmenu = Menu(menubar)
aboutmenu.add_command(label='作者', command=author)
aboutmenu.add_command(label='版权', command=about)
menubar.add_cascade(label='关于', menu=aboutmenu)

toolbar = Frame(root, height=25, bg='light sea green')
shortButton = Button(toolbar, text='打开', command=openfile)
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolbar, text='保存', command=save)
shortButton.pack(side=LEFT)
toolbar.pack(fill=X, expand=NO)

# Status Bar
status = Label(root, text='Ln20', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# Line number&text
lnlabel = Label(root, width=2, bg='antique white')
lnlabel.pack(side=LEFT, fill=Y)

textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)

scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()
