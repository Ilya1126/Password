import tkinter as tk

win=tk.Tk()
win.title('Калькулятор')
win.geometry('240x270')
win['bg']='#33ffe6'
win.resizable(0, 0)

def add_digit(digit):
    value=calc.get() + str(digit)
    calc.delete(0, 'end')
    calc.insert(0, value)

def mk_dt_bt(digit):
    return tk.Button(win, text=digit, bd=10, fg='red',font=('Arial', 13), command=lambda : add_digit(digit))

def mk_op_bt(operation):
    return tk.Button(win, text=operation, bd=10, fg='red',font=('Arial', 13), command=lambda: add_digit(operation))

def mk_cl_bt(operation):
    return tk.Button(win, text=operation, bd=10, fg='red',font=('Arial', 13), command=lambda: add_digit(operation))

calc=tk.Entry(win, font=('Arial', 15), width=15, justify=tk.RIGHT)
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx=5)

mk_dt_bt('1').grid(row=1, column=0, sticky='wens', padx=5, pady=5)
mk_dt_bt('2').grid(row=1, column=1, sticky='wens', padx=5, pady=5)
mk_dt_bt('3').grid(row=1, column=2, sticky='wens', padx=5, pady=5)
mk_dt_bt('4').grid(row=2, column=0, sticky='wens', padx=5, pady=5)
mk_dt_bt('5').grid(row=2, column=1, sticky='wens', padx=5, pady=5)
mk_dt_bt('6').grid(row=2, column=2, sticky='wens', padx=5, pady=5)
mk_dt_bt('7').grid(row=3, column=0, sticky='wens', padx=5, pady=5)
mk_dt_bt('8').grid(row=3, column=1, sticky='wens', padx=5, pady=5)
mk_dt_bt('9').grid(row=3, column=2, sticky='wens', padx=5, pady=5)
mk_dt_bt('0').grid(row=4, column=0, sticky='wens', padx=5, pady=5)
mk_op_bt('+').grid(row=1, column=3, sticky='wens', padx=5, pady=5)
mk_op_bt('-').grid(row=2, column=3, sticky='wens', padx=5, pady=5)
mk_op_bt('*').grid(row=3, column=3, sticky='wens', padx=5, pady=5)
mk_op_bt('/').grid(row=4, column=3, sticky='wens', padx=5, pady=5)
mk_cl_bt('=').grid(row=4, column=2, sticky='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
