import tkinter.messagebox
from tkinter import *


class Calculator:

    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title('Average finder')

        self.input_frame = Frame(self.main)
        self.button_frame = Frame(self.main)
        self.output_frame = Frame(self.main, width=200, height=50, bg='green')

        self.label1 = Label(self.input_frame, text='Enter the first Number: ').grid(row=0, column=0)
        self.label2 = Label(self.input_frame, text='Enter the second number: ').grid(row=1, column=0)
        self.label3 = Label(self.input_frame, text='Enter the Third number: ').grid(row=2, column=0)

        self.entry1 = Entry(self.input_frame)
        self.entry1.grid(row=0, column=1)

        self.entry2 = Entry(self.input_frame)
        self.entry2.grid(row=1, column=1)

        self.entry3 = Entry(self.input_frame)
        self.entry3.grid(row=2, column=1)

        self.result = StringVar()
        self.output_place = Entry(self.output_frame, textvariable=self.result, width=50, bg='green')
        self.output_place.pack(side=TOP)

        self.average_button = Button(self.button_frame, text='Average', command=self.average).pack()
        self.clear_button = Button(self.button_frame, text='clear', command=self.clear_field).pack()

        self.input_frame.pack()
        self.output_frame.pack()
        self.button_frame.pack()

        mainloop()

    def average(self):
        num1 = float(self.entry1.get())
        num2 = float(self.entry2.get())
        num3 = float(self.entry3.get())

        average = (num1 + num2 + num3) / 3

        self.result.set(average)

    def clear_field(self):
        average = ''
        self.result.set(average)


solve = Calculator()
