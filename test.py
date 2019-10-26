def btn_click(item):
    global expression
    expressions = expression + str(item)
    return expressions
    # input_text.set(expressions)  # this sets a tkinter label to the value


# the btn_clear function  clears the input field
def btn_clear():
    global expression
    # clear = expression * ' '
    # input_text.set(' ')


#     btn_equal calculates the expression present in the input method
def btn_equal():
    global expression
    result = str(eval(expression))  # eval function evaluates the string expression directly
    # you can also implement your own function to evaluate the expression instesd of the eval function
    # input_text.set(result)


expression = 'me'
print(expression)

for item in range(0,10):
    btn_click(item)
    print(btn_click(item))

