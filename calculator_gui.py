from tkinter import *

main_window = Tk()

main_window.geometry('415x325')  # size of the window width:- 500, height:- 375
main_window.resizable(0, 0)  # this prevents from resizing the windows
main_window.title('Calculator')


################################## functions ####################################

# the btn_click function continously updates the input field whenever you enter a number

def btn_click(item):
    global expression
    expressions = expression + str(item)
    input_text.set(expressions)  # this sets a tkinter label to the value


# the btn_clear function  clears the input field
def btn_clear():
    global expression
    # clear = expression * ' '
    input_text.set(' ')


#     btn_equal calculates the expression present in the input method
def btn_equal():
    global expression
    result = str(eval(expression))  # eval function evaluates the string expression directly
    # you can also implement your own function to evaluate the expression instesd of the eval function
    input_text.set(result)


expression = ''
# 'StringVar()' is used to get the instance of input field
input_text = StringVar()

# creating a frame for the input field
input_frame = Frame(main_window, width=312, height=50, bd=0, bg='#000', highlightbackground='black',
                    highlightcolor='black')
input_frame.pack(side=TOP)

# creating an input field inside the frame
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg='#fff', bd=0)
input_field.grid(row=0, column=0)

input_field.pack(ipady=10)  # ipady is  internal padding to the height of the input field

# creating another frame for the button below the input_frame
btn_frame = Frame(main_window, width=312, height=324, bg='grey')
btn_frame.pack()

# first row
clear = Button(btn_frame, text='C', fg='black', width=32, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_clear)
clear.grid(row=0, columnspan=3)

divide = Button(btn_frame, text='/', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_click)
divide.grid(row=0, column=3)

# second row
seven = Button(btn_frame, text='7', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_click(7))
seven.grid(row=1, column=0)

eight = Button(btn_frame, text='8', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_click(8))
eight.grid(row=1, column=1)

nine = Button(btn_frame, text='9', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_click(9))
nine.grid(row=1, column=2)

multiply = Button(btn_frame, text='x', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_click)
multiply.grid(row=1, column=3)

# third row
four = Button(btn_frame, text='4', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_click(4))
four.grid(row=2, column=0)

five = Button(btn_frame, text='5', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_click(5))
five.grid(row=2, column=1)

six = Button(btn_frame, text='6', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_click(6))
six.grid(row=2, column=2)

minus = Button(btn_frame, text='-', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_click)
minus.grid(row=2, column=3)

# fourth row
one = Button(btn_frame, text='1', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_click(1))
one.grid(row=3, column=0)

two = Button(btn_frame, text='2', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_click(2))
two.grid(row=3, column=1)

three = Button(btn_frame, text='3', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_click(3))
three.grid(row=3, column=2)

plus = Button(btn_frame, text='+', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=btn_click)
plus.grid(row=3, column=3)

# fifth row
zero = Button(btn_frame, text='0', fg='black', width=21, height=3, bd=0, bg='#fff', cursor='hand2',
              command=btn_click(0)).grid(row=4, columnspan=2)
point = Button(btn_frame, text='.', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
               command=btn_click).grid(row=4, column=2)
equal = Button(btn_frame, text='=', fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
               command=btn_equal).grid(row=4, column=3)

mainloop()
