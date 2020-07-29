from tkinter import *
from tkinter.filedialog import *
import math
from tkinter import messagebox

# path='D:\\Geotools\\'
# F0F0F0
#path='/Users/swh/Documents/Geotools/'
#FFFFFF

root = Tk()
root.title('几何工具')
root.geometry('510x345')
font = ('黑体', 12)
path='D:\\Geotools\\'
n_x = 300
n_y = 0
w_x = 160
w_y = 110
s_x = n_x
s_y = 240
e_x = 435
e_y = w_y
up_x = 200
up_y = 0
cl_x = e_x
cl_y = 250
ok_x = cl_x
ok_y = 300
z_x = 240
z_y = 300
m_x = 330
m_y = z_y
jj = 20
color = '#FFFFFF'
hotkey = '<Control-KeyPress-z>'
bg='#9FBFFF'
canall_x=110
jianju=50
can_x=230
can_y=40

def twoD():
    global font
    global photo
    global bg
    btn1 = Button(root, text='三角形', command=sanjiao, font=font)
    btn1.grid(row=0, column=1, sticky=NSEW)
    btn2 = Button(root, text='圆形', command=yuan, font=font)
    btn2.grid(row=1, column=1, sticky=NSEW)
    btn3 = Button(root, text='椭圆', command=tuoyuan, font=font)
    btn3.grid(row=2, column=1, sticky=NSEW)
    btn4 = Button(root, text='矩形', command=juxing, font=font)
    btn4.grid(row=3, column=1, sticky=NSEW)
    btn5 = Button(root, text='四边形', command=pingxing, font=font)
    btn5.grid(row=4, column=1, sticky=NSEW)
    btn6 = Button(root, text='梯形', command=tixing, font=font)
    btn6.grid(row=5, column=1, sticky=NSEW)
    #btn7 = Button(root, text='', command=twoD, font=font)
    #btn7.grid(row=6, column=1, sticky=NSEW)
    #btn8 = Button(root, text='', command=twoD, font=font)
    #btn8.grid(row=7, column=1, sticky=NSEW)
    def sjin(event):
        btn1['background'] = bg
        btn2['background'] = 'SystemButtonFace'
        btn3['background'] = 'SystemButtonFace'
        btn4['background'] = 'SystemButtonFace'
        btn5['background'] = 'SystemButtonFace'
        btn6['background'] = 'SystemButtonFace'
        sanjiao()
    btn1.bind("<Enter>", sjin)
    def yin(event):
        btn2['background'] = bg
        btn1['background'] = 'SystemButtonFace'
        btn3['background'] = 'SystemButtonFace'
        btn4['background'] = 'SystemButtonFace'
        btn5['background'] = 'SystemButtonFace'
        btn6['background'] = 'SystemButtonFace'
        yuan()
    btn2.bind("<Enter>", yin)
    def tyin(event):
        btn3['background'] = bg
        btn2['background'] = 'SystemButtonFace'
        btn1['background'] = 'SystemButtonFace'
        btn4['background'] = 'SystemButtonFace'
        btn5['background'] = 'SystemButtonFace'
        btn6['background'] = 'SystemButtonFace'
        tuoyuan()
    btn3.bind("<Enter>", tyin)
    def jxin(event):
        btn4['background'] = bg
        btn2['background'] = 'SystemButtonFace'
        btn3['background'] = 'SystemButtonFace'
        btn1['background'] = 'SystemButtonFace'
        btn5['background'] = 'SystemButtonFace'
        btn6['background'] = 'SystemButtonFace'
        juxing()
    btn4.bind("<Enter>", jxin)
    def pxin(event):
        btn5['background'] = bg
        btn2['background'] = 'SystemButtonFace'
        btn3['background'] = 'SystemButtonFace'
        btn4['background'] = 'SystemButtonFace'
        btn1['background'] = 'SystemButtonFace'
        btn6['background'] = 'SystemButtonFace'
        pingxing()
    btn5.bind("<Enter>", pxin)
    def txin(event):
        btn6['background'] = bg
        btn2['background'] = 'SystemButtonFace'
        btn3['background'] = 'SystemButtonFace'
        btn4['background'] = 'SystemButtonFace'
        btn5['background'] = 'SystemButtonFace'
        btn1['background'] = 'SystemButtonFace'
        tixing()
    btn6.bind("<Enter>", txin)

def threeD():
    global font
    btn1 = Button(root, text='长方体', command=changfang, font=font)
    btn1.grid(row=0, column=1, sticky=NSEW)
    btn2 = Button(root, text='球体', command=qiu, font=font)
    btn2.grid(row=1, column=1, sticky=NSEW)
    btn3 = Button(root, text='柱体', command=zhu, font=font)
    btn3.grid(row=2, column=1, sticky=NSEW)
    btn4 = Button(root, text='锥体', command=zhui, font=font)
    btn4.grid(row=3, column=1, sticky=NSEW)
    btn5 = Button(root, text='', command=threeD, font=font)
    btn5.grid(row=4, column=1, sticky=NSEW)
    btn6 = Button(root, text='', command=threeD, font=font)
    btn6.grid(row=5, column=1, sticky=NSEW)
    #btn7 = Button(root, text='', command=threeD, font=font)
    #btn7.grid(row=6, column=1, sticky=NSEW)
    #btn8 = Button(root, text='', command=threeD, font=font)
    #btn8.grid(row=7, column=1, sticky=NSEW)
    def cfin(event):
        btn1['background'] = bg
        btn2['background'] = 'SystemButtonFace'
        btn3['background'] = 'SystemButtonFace'
        btn4['background'] = 'SystemButtonFace'
        changfang()
    btn1.bind("<Enter>", cfin)
    def qin(event):
        btn2['background'] = bg
        btn1['background'] = 'SystemButtonFace'
        btn3['background'] = 'SystemButtonFace'
        btn4['background'] = 'SystemButtonFace'
        qiu()
    btn2.bind("<Enter>", qin)
    def zhuin(event):
        btn3['background'] = bg
        btn2['background'] = 'SystemButtonFace'
        btn1['background'] = 'SystemButtonFace'
        btn4['background'] = 'SystemButtonFace'
        zhu()
    btn3.bind("<Enter>", zhuin)
    def zhuiin(event):
        btn4['background'] = bg
        btn2['background'] = 'SystemButtonFace'
        btn3['background'] = 'SystemButtonFace'
        btn1['background'] = 'SystemButtonFace'
        zhui()
    btn4.bind("<Enter>", zhuiin)

def sanjiao():
    global font
    global path
    global canall_x
    Canvas(root, width=1000, height=1000).place(x=canall_x, y=0)
    btn1=Button(root, text='直角', command=zhijiao, font=font)
    btn1.grid(row=0, column=2, sticky=NSEW)
    btn2=Button(root, text='普通', command=renyi, font=font)
    btn2.grid(row=1, column=2, sticky=NSEW)
    def zjin(event):
        btn1['background'] = bg
        btn2['background'] = 'SystemButtonFace'
        zhijiao()
    btn1.bind("<Enter>", zjin)
    def ryin(event):
        btn2['background'] = bg
        btn1['background'] = 'SystemButtonFace'
        renyi()
    btn2.bind("<Enter>", ryin)

def zhijiao():
    global font
    global path
    global n_x
    global n_y
    global w_x
    global w_y
    global s_x
    global s_y
    global e_x
    global e_y
    global up_x
    global up_y
    global cl_x
    global cl_y
    global ok_x
    global ok_y
    global jj
    global color
    global jianju

    def calc():
        if len(v1.get()) == 0:
            a = 0
        else:
            a = float(v1.get())
        if len(v2.get()) == 0:
            b = 0
        else:
            b = float(v2.get())
        if len(v3.get()) == 0:
            c = 0
        else:
            c = float(v3.get())
        if a != 0 and b != 0 and c == 0:
            c = (a ** 2 + b ** 2) ** 0.5
            v3.set(c)
        elif a != 0 and b == 0 and c != 0:
            b = (c ** 2 - a ** 2) ** 0.5
            v2.set(b)
        elif a == 0 and b != 0 and c != 0:
            a = (c ** 2 - b ** 2) ** 0.5
            v1.set(a)
        else:
            messagebox.showinfo('请输入任意两边的值', '请输入任意两边的值')
            qingkong()
        v4.set(a + b + c)
        v5.set(a * b * 0.5)

    def qingkong():
        v1.set('')
        v2.set('')
        v3.set('')

    global canall_x
    global can_x
    global can_y
    Canvas(root, width=1000, height=1000).place(x=canall_x+jianju, y=0)
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=can_x, y=can_y)
    global photo
    photo = PhotoImage(file=path + '2.1.1.png')
    canvas.create_image(100, 100, image=photo)

    Label(frame, text='直角边1', width=6, height=1, font=font).place(x=w_x, y=w_y)
    v1 = StringVar()
    Entry(frame, textvariable=v1, width=8, font=font).place(x=w_x, y=w_y + jj)

    Label(frame, text='直角边2', width=6, height=1, font=font).place(x=s_x, y=s_y)
    v2 = StringVar()
    Entry(frame, textvariable=v2, width=8, font=font).place(x=s_x, y=s_y + jj)

    Label(frame, text='斜边', width=6, height=1, font=font).place(x=e_x, y=e_y)
    v3 = StringVar()
    Entry(frame, textvariable=v3, width=8, font=font).place(x=e_x, y=e_y + jj)

    Button(frame, text='清空', command=qingkong, height=2, width=8, font=font, fg='red').place(x=cl_x, y=cl_y)
    Button(frame, text='确认', command=calc, height=2, width=8, font=font
           ).place(x=ok_x, y=ok_y)

    Label(frame, text='周长', width=6, height=1, font=font).place(x=z_x, y=z_y)
    v4 = DoubleVar()
    Entry(frame, textvariable=v4, width=8, font=font).place(x=z_x, y=z_y + jj)

    Label(frame, text='面积', width=6, height=1, font=font).place(x=m_x, y=m_y)
    v5 = DoubleVar()
    Entry(frame, textvariable=v5, width=8, font=font).place(x=m_x, y=m_y + jj)
    global hotkey

    def cal(event):
        calc()

    def clear(event):
        qingkong()

    root.bind('<Return>', cal)
    root.bind(hotkey, clear)

def renyi():
    global font
    global path
    global n_x
    global n_y
    global w_x
    global w_y
    global s_x
    global s_y
    global e_x
    global e_y
    global up_x
    global up_y
    global cncl_x
    global cncl_y
    global ok_x
    global ok_y
    global jj
    global color
    global jianju

    def calc():
        if len(v1.get()) == 0:
            a = 0
        else:
            a = float(v1.get())
        if len(v2.get()) == 0:
            b = 0
        else:
            b = float(v2.get())
        if len(v3.get()) == 0:
            c = 0
        else:
            c = float(v3.get())
        p = (a + b + c) / 2
        v4.set(p * 2)
        v5.set((p * (p - a) * (p - b) * (p - c)) ** 0.5)

    def qingkong():
        v1.set('')
        v2.set('')
        v3.set('')

    global canall_x
    global can_x
    global can_y
    Canvas(root, width=1000, height=1000).place(x=canall_x+jianju, y=0)
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=can_x, y=can_y)
    global photo
    photo = PhotoImage(file=path + '2.1.2.png')
    canvas.create_image(100, 100, image=photo)

    Label(frame, text='边1', width=6, height=1, font=font).place(x=w_x, y=w_y)
    v1 = StringVar()
    Entry(frame, textvariable=v1, width=8, font=font).place(x=w_x, y=w_y + jj)

    Label(frame, text='边2', width=6, height=1, font=font).place(x=s_x, y=s_y)
    v2 = StringVar()
    Entry(frame, textvariable=v2, width=8, font=font).place(x=s_x, y=s_y + jj)

    Label(frame, text='边3', width=6, height=1, font=font).place(x=e_x, y=e_y)
    v3 = StringVar()
    Entry(frame, textvariable=v3, width=8, font=font).place(x=e_x, y=e_y + jj)

    Button(frame, text='清空', command=qingkong, height=2, width=8, font=font, fg='red').place(x=cl_x, y=cl_y)
    Button(frame, text='确认', command=calc, height=2, width=8, font=font
           ).place(x=ok_x, y=ok_y)

    Label(frame, text='周长', width=6, height=1, font=font).place(x=z_x, y=z_y)
    v4 = DoubleVar()
    Entry(frame, textvariable=v4, width=8, font=font).place(x=z_x, y=z_y + jj)

    Label(frame, text='面积', width=6, height=1, font=font).place(x=m_x, y=m_y)
    v5 = DoubleVar()
    Entry(frame, textvariable=v5, width=8, font=font).place(x=m_x, y=m_y + jj)

    global hotkey

    def cal(event):
        calc()

    def clear(event):
        qingkong()

    root.bind('<Return>', cal)
    root.bind(hotkey, clear)

def yuan():
    global font
    global path
    global n_x
    global n_y
    global w_x
    global w_y
    global s_x
    global s_y
    global e_x
    global e_y
    global up_x
    global up_y
    global cl_x
    global cl_y
    global ok_x
    global ok_y
    global jj
    global color

    def calc():
        if len(v1.get()) == 0:
            r = 0
        else:
            r = float(v1.get())
        v4.set(2 * r * math.pi)
        v5.set(math.pi * r * r)

    def qingkong():
        v1.set('')

    global canall_x
    global can_x
    global can_y
    Canvas(root, width=1000, height=1000).place(x=canall_x, y=0)
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=can_x, y=can_y)
    global photo
    photo = PhotoImage(file=path + '2.2.png')
    canvas.create_image(100, 100, image=photo)


    Label(frame, text='半径', width=6, height=1, font=font).place(x=w_x, y=w_y)
    v1 = StringVar()
    Entry(frame, textvariable=v1, width=8, font=font).place(x=w_x, y=w_y + jj)

    Button(frame, text='清空', command=qingkong, height=2, width=8, font=font, fg='red').place(x=cl_x, y=cl_y)
    Button(frame, text='确认', command=calc, height=2, width=8, font=font
           ).place(x=ok_x, y=ok_y)

    Label(frame, text='周长', width=6, height=1, font=font).place(x=z_x, y=z_y)
    v4 = DoubleVar()
    Entry(frame, textvariable=v4, width=8, font=font).place(x=z_x, y=z_y + jj)

    Label(frame, text='面积', width=6, height=1, font=font).place(x=m_x, y=m_y)
    v5 = DoubleVar()
    Entry(frame, textvariable=v5, width=8, font=font).place(x=m_x, y=m_y + jj)

    global hotkey

    def cal(event):
        calc()

    def clear(event):
        qingkong()

    root.bind('<Return>', cal)
    root.bind(hotkey, clear)

def tuoyuan():
    global font
    global path
    global n_x
    global n_y
    global w_x
    global w_y
    global s_x
    global s_y
    global e_x
    global e_y
    global up_x
    global up_y
    global cl_x
    global cl_y
    global ok_x
    global ok_y
    global jj
    global color

    def calc():
        if len(v1.get()) == 0:
            a = 0
        else:
            a = float(v1.get())
        if len(v2.get()) == 0:
            b = 0
        else:
            b = float(v2.get())
        v5.set(math.pi * a * b)

    def qingkong():
        v1.set('')
        v2.set('')

    global canall_x
    global can_x
    global can_y
    Canvas(root, width=1000, height=1000).place(x=canall_x, y=0)
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=can_x, y=can_y)
    global photo
    photo = PhotoImage(file=path + '2.3.png')
    canvas.create_image(100, 100, image=photo)


    Label(frame, text='半短轴', width=6, height=1, font=font).place(x=w_x, y=w_y)
    v1 = StringVar()
    Entry(frame, textvariable=v1, width=8, font=font).place(x=w_x, y=w_y + jj)

    Label(frame, text='半长轴', width=6, height=1, font=font).place(x=s_x, y=s_y)
    v2 = StringVar()
    Entry(frame, textvariable=v2, width=8, font=font).place(x=s_x, y=s_y + jj)

    Button(frame, text='清空', command=qingkong, height=2, width=8, font=font, fg='red').place(x=cl_x, y=cl_y)
    Button(frame, text='确认', command=calc, height=2, width=8, font=font
           ).place(x=ok_x, y=ok_y)

    Label(frame, text='面积', width=6, height=1, font=font).place(x=m_x, y=m_y)
    v5 = DoubleVar()
    Entry(frame, textvariable=v5, width=8, font=font).place(x=m_x, y=m_y + jj)

    global hotkey

    def cal(event):
        calc()

    def clear(event):
        qingkong()

    root.bind('<Return>', cal)
    root.bind(hotkey, clear)

def juxing():
    global font
    global path
    global n_x
    global n_y
    global w_x
    global w_y
    global s_x
    global s_y
    global e_x
    global e_y
    global up_x
    global up_y
    global cl_x
    global cl_y
    global ok_x
    global ok_y
    global jj
    global color

    def calc():
        if len(v1.get()) == 0:
            a = 0
        else:
            a = float(v1.get())
        if len(v2.get()) == 0:
            b = 0
        else:
            b = float(v2.get())
        v4.set(a * 2 + b * 2)
        v5.set(a * b)

    def qingkong():
        v1.set('')
        v2.set('')

    global canall_x
    global can_x
    global can_y
    Canvas(root, width=1000, height=1000).place(x=canall_x, y=0)
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=can_x, y=can_y)
    global photo
    photo = PhotoImage(file=path + '2.4.png')
    canvas.create_image(100, 100, image=photo)

    Label(frame, text='宽', width=6, height=1, font=font).place(x=w_x, y=w_y)
    v1 = StringVar()
    Entry(frame, textvariable=v1, width=8, font=font).place(x=w_x, y=w_y + jj)

    Label(frame, text='长', width=6, height=1, font=font).place(x=s_x, y=s_y)
    v2 = StringVar()
    Entry(frame, textvariable=v2, width=8, font=font).place(x=s_x, y=s_y + jj)

    Button(frame, text='清空', command=qingkong, height=2, width=8, font=font, fg='red').place(x=cl_x, y=cl_y)
    Button(frame, text='确认', command=calc, height=2, width=8, font=font
           ).place(x=ok_x, y=ok_y)

    Label(frame, text='周长', width=6, height=1, font=font).place(x=z_x, y=z_y)
    v4 = DoubleVar()
    Entry(frame, textvariable=v4, width=8, font=font).place(x=z_x, y=z_y + jj)

    Label(frame, text='面积', width=6, height=1, font=font).place(x=m_x, y=m_y)
    v5 = DoubleVar()
    Entry(frame, textvariable=v5, width=8, font=font).place(x=m_x, y=m_y + jj)

    global hotkey

    def cal(event):
        calc()

    def clear(event):
        qingkong()

    root.bind('<Return>', cal)
    root.bind(hotkey, clear)

def pingxing():
    global font
    global path
    global n_x
    global n_y
    global w_x
    global w_y
    global s_x
    global s_y
    global e_x
    global e_y
    global up_x
    global up_y
    global cl_x
    global cl_y
    global ok_x
    global ok_y
    global jj
    global color

    def calc():
        if len(v1.get()) == 0:
            a = 0
        else:
            a = float(v1.get())
        if len(v2.get()) == 0:
            b = 0
        else:
            b = float(v2.get())
        v5.set(a * b)

    def qingkong():
        v1.set('')
        v2.set('')

    global canall_x
    global can_x
    global can_y
    Canvas(root, width=1000, height=1000).place(x=canall_x, y=0)
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=can_x, y=can_y)
    global photo
    photo = PhotoImage(file=path + '2.5.png')
    canvas.create_image(100, 100, image=photo)

    Label(frame, text='高', width=6, height=1, font=font).place(x=w_x, y=w_y)
    v1 = StringVar()
    Entry(frame, textvariable=v1, width=8, font=font).place(x=w_x, y=w_y + jj)

    Label(frame, text='底', width=6, height=1, font=font).place(x=s_x, y=s_y)
    v2 = StringVar()
    Entry(frame, textvariable=v2, width=8, font=font).place(x=s_x, y=s_y + jj)

    Button(frame, text='清空', command=qingkong, height=2, width=8, font=font, fg='red').place(x=cl_x, y=cl_y)
    Button(frame, text='确认', command=calc, height=2, width=8, font=font
           ).place(x=ok_x, y=ok_y)

    Label(frame, text='面积', width=6, height=1, font=font).place(x=m_x, y=m_y)
    v5 = DoubleVar()
    Entry(frame, textvariable=v5, width=8, font=font).place(x=m_x, y=m_y + jj)
    global hotkey

    def cal(event):
        calc()

    def clear(event):
        qingkong()

    root.bind('<Return>', cal)
    root.bind(hotkey, clear)

def tixing():
    global font
    global path
    global n_x
    global n_y
    global w_x
    global w_y
    global s_x
    global s_y
    global e_x
    global e_y
    global up_x
    global up_y
    global cl_x
    global cl_y
    global ok_x
    global ok_y
    global jj
    global color

    def calc():
        if len(v1.get()) == 0:
            a = 0
        else:
            a = float(v1.get())
        if len(v2.get()) == 0:
            b = 0
        else:
            b = float(v2.get())
        if len(v3.get()) == 0:
            h = 0
        else:
            h = float(v3.get())
        v5.set((a + b) * h * 0.5)

    def qingkong():
        v1.set('')
        v2.set('')
        v3.set('')

    global canall_x
    global can_x
    global can_y
    Canvas(root, width=1000, height=1000).place(x=canall_x, y=0)
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=can_x, y=can_y)
    global photo
    photo = PhotoImage(file=path + '2.6.png')
    canvas.create_image(100, 100, image=photo)

    Label(frame, text='上底', width=6, height=1, font=font).place(x=n_x, y=n_y)
    v1 = StringVar()
    Entry(frame, textvariable=v1, width=8, font=font).place(x=n_x, y=n_y + jj)

    Label(frame, text='下底', width=6, height=1, font=font).place(x=s_x, y=s_y)
    v2 = StringVar()
    Entry(frame, textvariable=v2, width=8, font=font).place(x=s_x, y=s_y + jj)

    Label(frame, text='高', width=6, height=1, font=font).place(x=w_x, y=w_y)
    v3 = StringVar()
    Entry(frame, textvariable=v3, width=8, font=font).place(x=w_x, y=w_y + jj)

    Button(frame, text='清空', command=qingkong, height=2, width=8, font=font, fg='red').place(x=cl_x, y=cl_y)
    Button(frame, text='确认', command=calc, height=2, width=8, font=font
           ).place(x=ok_x, y=ok_y)

    Label(frame, text='面积', width=6, height=1, font=font).place(x=m_x, y=m_y)
    v5 = DoubleVar()
    Entry(frame, textvariable=v5, width=8, font=font).place(x=m_x, y=m_y + jj)
    global hotkey

    def cal(event):
        calc()

    def clear(event):
        qingkong()

    root.bind('<Return>', cal)
    root.bind(hotkey, clear)

def changfang():
    global font
    global path
    global n_x
    global n_y
    global w_x
    global w_y
    global s_x
    global s_y
    global e_x
    global e_y
    global up_x
    global up_y
    global cl_x
    global cl_y
    global ok_x
    global ok_y
    global jj
    global color

    def calc():
        if len(v1.get()) == 0:
            a = 0
        else:
            a = float(v1.get())
        if len(v2.get()) == 0:
            b = 0
        else:
            b = float(v2.get())
        if len(v3.get()) == 0:
            c = 0
        else:
            c = float(v3.get())

        v4.set(2 * a * b + 2 * b * c + 2 * c * a)
        v5.set(a * b * c)

    def qingkong():
        v1.set('')
        v2.set('')
        v3.set('')

    global canall_x
    global can_x
    global can_y
    Canvas(root, width=1000, height=1000).place(x=canall_x, y=0)
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=can_x, y=can_y)
    global photo
    photo = PhotoImage(file=path + '3.1.png')
    canvas.create_image(100, 100, image=photo)

    Label(frame, text='宽', width=6, height=1, font=font).place(x=w_x, y=w_y)
    v1 = StringVar()
    Entry(frame, textvariable=v1, width=8, font=font).place(x=w_x, y=w_y + jj)

    Label(frame, text='长', width=6, height=1, font=font).place(x=s_x, y=s_y)
    v2 = StringVar()
    Entry(frame, textvariable=v2, width=8, font=font).place(x=s_x, y=s_y + jj)

    Label(frame, text='高', width=6, height=1, font=font).place(x=e_x, y=e_y)
    v3 = StringVar()
    Entry(frame, textvariable=v3, width=8, font=font).place(x=e_x, y=e_y + jj)

    Button(frame, text='清空', command=qingkong, height=2, width=8, font=font, fg='red').place(x=cl_x, y=cl_y)
    Button(frame, text='确认', command=calc, height=2, width=8, font=font
           ).place(x=ok_x, y=ok_y)

    Label(frame, text='表面积', width=6, height=1, font=font).place(x=z_x, y=z_y)
    v4 = DoubleVar()
    Entry(frame, textvariable=v4, width=8, font=font).place(x=z_x, y=z_y + jj)

    Label(frame, text='体积', width=6, height=1, font=font).place(x=m_x, y=m_y)
    v5 = DoubleVar()
    Entry(frame, textvariable=v5, width=8, font=font).place(x=m_x, y=m_y + jj)
    global hotkey

    def cal(event):
        calc()

    def clear(event):
        qingkong()

    root.bind('<Return>', cal)
    root.bind(hotkey, clear)

def qiu():
    global font
    global path
    global n_x
    global n_y
    global w_x
    global w_y
    global s_x
    global s_y
    global e_x
    global e_y
    global up_x
    global up_y
    global cl_x
    global cl_y
    global ok_x
    global ok_y
    global jj
    global color

    def calc():
        if len(v1.get()) == 0:
            r = 0
        else:
            r = float(v1.get())
        v4.set(4 * r * r * math.pi)
        v5.set(4 * math.pi * r * r * r / 3)

    def qingkong():
        v1.set('')

    global canall_x
    global can_x
    global can_y
    Canvas(root, width=1000, height=1000).place(x=canall_x, y=0)
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=can_x, y=can_y)
    global photo
    photo = PhotoImage(file=path + '3.2.png')
    canvas.create_image(100, 100, image=photo)


    Label(frame, text='半径', width=6, height=1, font=font).place(x=w_x, y=w_y)
    v1 = StringVar()
    Entry(frame, textvariable=v1, width=8, font=font).place(x=w_x, y=w_y + jj)

    Button(frame, text='清空', command=qingkong, height=2, width=8, font=font, fg='red').place(x=cl_x, y=cl_y)
    Button(frame, text='确认', command=calc, height=2, width=8, font=font
           ).place(x=ok_x, y=ok_y)

    Label(frame, text='表面积', width=6, height=1, font=font).place(x=z_x, y=z_y)
    v4 = DoubleVar()
    Entry(frame, textvariable=v4, width=8, font=font).place(x=z_x, y=z_y + jj)

    Label(frame, text='体积', width=6, height=1, font=font).place(x=m_x, y=m_y)
    v5 = DoubleVar()
    Entry(frame, textvariable=v5, width=8, font=font).place(x=m_x, y=m_y + jj)
    global hotkey

    def cal(event):
        calc()

    def clear(event):
        qingkong()

    root.bind('<Return>', cal)
    root.bind(hotkey, clear)

def zhu():
    global font
    global path
    global canall_x
    Canvas(root, width=1000, height=1000).place(x=canall_x, y=0)
    btn1=Button(frame, text='圆柱', command=yuanzhu, font=font)
    btn1.grid(row=2, column=2, sticky=NSEW)
    btn2=Button(frame, text='棱柱', command=lengzhu, font=font)
    btn2.grid(row=3, column=2, sticky=NSEW)
    def yzin(event):
        btn1['background'] = bg
        btn2['background'] = 'SystemButtonFace'
        yuanzhu()
    btn1.bind("<Enter>", yzin)
    def lzin(event):
        btn2['background'] = bg
        btn1['background'] = 'SystemButtonFace'
        lengzhu()
    btn2.bind("<Enter>", lzin)

def yuanzhu():
    global font
    global path
    global n_x
    global n_y
    global w_x
    global w_y
    global s_x
    global s_y
    global e_x
    global e_y
    global up_x
    global up_y
    global cl_x
    global cl_y
    global ok_x
    global ok_y
    global jj
    global color
    global jianju
    def calc():
        if len(v1.get()) == 0:
            h = 0
        else:
            h = float(v1.get())
        if len(v2.get()) == 0:
            r = 0
        else:
            r = float(v2.get())
        v4.set(2 * math.pi * r * h)
        v5.set(math.pi * r * r * h)

    def qingkong():
        v1.set('')
        v2.set('')

    global canall_x
    global can_x
    global can_y
    Canvas(root, width=1000, height=1000).place(x=canall_x+jianju, y=0)
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=can_x, y=can_y)
    global photo
    photo = PhotoImage(file=path + '3.3.1.png')
    canvas.create_image(100, 100, image=photo)

    Label(frame, text='高', width=6, height=1, font=font).place(x=w_x, y=w_y)
    v1 = StringVar()
    Entry(frame, textvariable=v1, width=8, font=font).place(x=w_x, y=w_y + jj)

    Label(frame, text='底半径', width=6, height=1, font=font).place(x=s_x, y=s_y)
    v2 = StringVar()
    Entry(frame, textvariable=v2, width=8, font=font).place(x=s_x, y=s_y + jj)

    Button(frame, text='清空', command=qingkong, height=2, width=8, font=font, fg='red').place(x=cl_x, y=cl_y)
    Button(frame, text='确认', command=calc, height=2, width=8, font=font
           ).place(x=ok_x, y=ok_y)

    Label(frame, text='侧面积', width=6, height=1, font=font).place(x=z_x, y=z_y)
    v4 = DoubleVar()
    Entry(frame, textvariable=v4, width=8, font=font).place(x=z_x, y=z_y + jj)

    Label(frame, text='体积', width=6, height=1, font=font).place(x=m_x, y=m_y)
    v5 = DoubleVar()
    Entry(frame, textvariable=v5, width=8, font=font).place(x=m_x, y=m_y + jj)
    global hotkey

    def cal(event):
        calc()

    def clear(event):
        qingkong()

    root.bind('<Return>', cal)
    root.bind(hotkey, clear)

def lengzhu():
    global font
    global path
    global n_x
    global n_y
    global w_x
    global w_y
    global s_x
    global s_y
    global e_x
    global e_y
    global up_x
    global up_y
    global cl_x
    global cl_y
    global ok_x
    global ok_y
    global jj
    global color
    global jianju

    def calc():
        if len(v1.get()) == 0:
            h = 0
        else:
            h = float(v1.get())
        if len(v2.get()) == 0:
            s = 0
        else:
            s = float(v2.get())
        v5.set(s * h)

    def qingkong():
        v1.set('')
        v2.set('')

    global canall_x
    global can_x
    global can_y
    Canvas(root, width=1000, height=1000).place(x=canall_x+jianju, y=0)
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=can_x, y=can_y)
    global photo
    photo = PhotoImage(file=path + '3.3.2.png')
    canvas.create_image(100, 100, image=photo)

    Canvas(frame, width=120, height=60, bg=color).place(x=z_x, y=z_y)

    Label(frame, text='高', width=6, height=1, font=font).place(x=w_x, y=w_y)
    v1 = StringVar()
    Entry(frame, textvariable=v1, width=8, font=font).place(x=w_x, y=w_y + jj)

    Label(frame, text='底面积', width=6, height=1, font=font).place(x=s_x, y=s_y)
    v2 = StringVar()
    Entry(frame, textvariable=v2, width=8, font=font).place(x=s_x, y=s_y + jj)

    Button(frame, text='清空', command=qingkong, height=2, width=8, font=font, fg='red').place(x=cl_x, y=cl_y)
    Button(frame, text='确认', command=calc, height=2, width=8, font=font
           ).place(x=ok_x, y=ok_y)

    Label(frame, text='体积', width=6, height=1, font=font).place(x=m_x, y=m_y)
    v5 = DoubleVar()
    Entry(frame, textvariable=v5, width=8, font=font).place(x=m_x, y=m_y + jj)
    global hotkey

    def cal(event):
        calc()

    def clear(event):
        qingkong()

    root.bind('<Return>', cal)
    root.bind(hotkey, clear)

def zhui():
    global font
    global path
    global canall_x
    Canvas(root, width=1000, height=1000).place(x=canall_x, y=0)
    btn1=Button(frame, text='圆锥', command=yuanzhui, font=font)
    btn1.grid(row=3, column=2, sticky=NSEW)
    btn2=Button(frame, text='棱锥', command=lengzhui, font=font)
    btn2.grid(row=4, column=2, sticky=NSEW)
    def yziin(event):
        btn1['background'] = bg
        btn2['background'] = 'SystemButtonFace'
        yuanzhui()
    btn1.bind("<Enter>", yziin)
    def lziin(event):
        btn2['background'] = bg
        btn1['background'] = 'SystemButtonFace'
        lengzhui()
    btn2.bind("<Enter>", lziin)

def yuanzhui():
    global font
    global path
    global n_x
    global n_y
    global w_x
    global w_y
    global s_x
    global s_y
    global e_x
    global e_y
    global up_x
    global up_y
    global cl_x
    global cl_y
    global ok_x
    global ok_y
    global jj
    global color
    global jianju

    def calc():
        if len(v1.get()) == 0:
            h = 0
        else:
            h = float(v1.get())
        if len(v2.get()) == 0:
            r = 0
        else:
            r = float(v2.get())
        l = (h ** 2 + r ** 2) ** 0.5
        v4.set(math.pi * r * l)
        v5.set(math.pi * r * r * h / 3)

    def qingkong():
        v1.set('')
        v2.set('')

    global canall_x
    global can_x
    global can_y
    Canvas(root, width=1000, height=1000).place(x=canall_x+jianju, y=0)
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=can_x, y=can_y)
    global photo
    photo = PhotoImage(file=path + '3.4.1.png')
    canvas.create_image(100, 100, image=photo)

    Label(frame, text='高', width=6, height=1, font=font).place(x=w_x, y=w_y)
    v1 = StringVar()
    Entry(frame, textvariable=v1, width=8, font=font).place(x=w_x, y=w_y + jj)

    Label(frame, text='底半径', width=6, height=1, font=font).place(x=s_x, y=s_y)
    v2 = StringVar()
    Entry(frame, textvariable=v2, width=8, font=font).place(x=s_x, y=s_y + jj)

    Button(frame, text='清空', command=qingkong, height=2, width=8, font=font, fg='red').place(x=cl_x, y=cl_y)
    Button(frame, text='确认', command=calc, height=2, width=8, font=font
           ).place(x=ok_x, y=ok_y)

    Label(frame, text='侧面积', width=6, height=1, font=font).place(x=z_x, y=z_y)
    v4 = DoubleVar()
    Entry(frame, textvariable=v4, width=8, font=font).place(x=z_x, y=z_y + jj)

    Label(frame, text='体积', width=6, height=1, font=font).place(x=m_x, y=m_y)
    v5 = DoubleVar()
    Entry(frame, textvariable=v5, width=8, font=font).place(x=m_x, y=m_y + jj)
    global hotkey

    def cal(event):
        calc()

    def clear(event):
        qingkong()

    root.bind('<Return>', cal)
    root.bind(hotkey, clear)

def lengzhui():
    global font
    global path
    global n_x
    global n_y
    global w_x
    global w_y
    global s_x
    global s_y
    global e_x
    global e_y
    global up_x
    global up_y
    global cl_x
    global cl_y
    global ok_x
    global ok_y
    global jj
    global color
    global jianju

    def calc():
        if len(v1.get()) == 0:
            h = 0
        else:
            h = float(v1.get())
        if len(v2.get()) == 0:
            s = 0
        else:
            s = float(v2.get())
        v5.set(s * h / 3)

    def qingkong():
        v1.set('')
        v2.set('')

    global canall_x
    global can_x
    global can_y
    Canvas(root, width=1000, height=1000).place(x=canall_x+jianju, y=0)
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=can_x, y=can_y)
    global photo
    photo = PhotoImage(file=path + '3.4.2.png')
    canvas.create_image(100, 100, image=photo)

    Label(frame, text='高', width=6, height=1, font=font).place(x=w_x, y=w_y)
    v1 = StringVar()
    Entry(frame, textvariable=v1, width=8, font=font).place(x=w_x, y=w_y + jj)

    Label(frame, text='底面积', width=6, height=1, font=font).place(x=s_x, y=s_y)
    v2 = StringVar()
    Entry(frame, textvariable=v2, width=8, font=font).place(x=s_x, y=s_y + jj)

    Button(frame, text='清空', command=qingkong, height=2, width=8, font=font, fg='red').place(x=cl_x, y=cl_y)
    Button(frame, text='确认', command=calc, height=2, width=8, font=font
           ).place(x=ok_x, y=ok_y)

    Label(frame, text='体积', width=6, height=1, font=font).place(x=m_x, y=m_y)
    v5 = DoubleVar()
    Entry(frame, textvariable=v5, width=8, font=font).place(x=m_x, y=m_y + jj)
    global hotkey

    def cal(event):
        calc()

    def clear(event):
        qingkong()

    root.bind('<Return>', cal)
    root.bind(hotkey, clear)

def info():
    global path
    global font
    info = Toplevel()
    info.geometry('400x300')
    info.title('版本信息')
    canvas = Canvas(info, width=400, height=300)
    canvas.pack()
    global photo
    photo = PhotoImage(file=path + 'logo.png')
    canvas.create_image(200, 100, image=photo)
    canvas.create_text(196, 220, text='Geotools(2020)')
    canvas.create_text(200, 245, text='作者：佘维华', font=font)
    canvas.create_text(201, 270, text='版本：1.1', font=font)

def createContextMenu(event):
    contextMenu.post(event.x_root, event.y_root)

frame = Frame(root).grid(row=0, column=3)
btn1 = Button(root, text='二维', command=twoD, height=10, width=5, font=font)
btn1.grid(row=0, column=0, sticky=NSEW, rowspan=3)
btn2 = Button(root, text='三维', command=threeD, height=10, width=5, font=font)
btn2.grid(row=3, column=0, sticky=NSEW, rowspan=3)
def twod(event):
    btn1['background'] = bg
    btn2['background'] = 'SystemButtonFace'
    twoD()
btn1.bind("<Enter>", twod)
def threed(event):
    btn2['background'] = bg
    btn1['background'] = 'SystemButtonFace'
    threeD()
btn2.bind("<Enter>", threed)
contextMenu = Menu(root)
contextMenu.add_command(label="版本信息", command=info)
contextMenu.add_command(label="确认:回车")
contextMenu.add_command(label="清空:Ctrl+z")
root.bind("<Button-3>", createContextMenu)

root.mainloop()
