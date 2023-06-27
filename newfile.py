import tkinter as tk

exp = ""
output = ""

def add(var):
	global exp
	exp += var
	out1.config(text = exp)
	
def delete():
	global exp
	exp = exp[0 : len(exp) - 1]
	out1.config(text = exp)
	
def ac():
	global exp
	exp = ""
	out1.config(text = exp)
	
def solve():
	global exp, output
	input = ""
	if exp == "":
		pass
	else:
		for i in exp:
			
			if i == "×":
				input += "*"
				
			elif i == "÷":
				input += "/"
				
			elif i == "π":
				if (input[-1] != "+") and (input[-1] != "-") and (input[-1] != "*") and (input[-1] != "/"):
					if len(input) == 0:
						input += "3.14159265358979323846"
					else:
						input += "*3.14159265358979323846"
				else:
					input += "3.14159265358979323846"
			
			elif i == "e":
				if (input[-1] != "+") and (input[-1] != "-") and (input[-1] != "*") and (input[-1] != "/"):
					if len(input) == 0:
						input += "2.71828182845904523536"
					else:
						input += "*2.71828182845904523536"
				else:
					input += "2.71828182845904523536"
					
			else:
				input += i
				
		output = "= " + str(eval(input))
		out2.config(text = output)
		exp = ""

app = tk.Tk()

out1 = tk.Label(app, text = exp, bg = "black", fg = "white", anchor = "w")
out1.place(x = 0, y = 0, height = 120, width = 720)
#expression input screen

out2 = tk.Label(app, text = output, bg = "black", fg = "white", anchor = "e")
out2.place(x = 0, y = 120, height = 120, width = 720)
#output screen

button_1 = tk.Button(app, text = "1", bg = "white", command = lambda: add("1"))
button_1.place(x = 15, y = 250, height = 100, width = 100)

button_2 = tk.Button(app, text = "2", bg = "white", command = lambda: add("2"))
button_2.place(x = 125, y = 250, height = 100, width = 100)

button_3 = tk.Button(app, text = "3", bg = "white", command = lambda: add("3"))
button_3.place(x = 235, y = 250, height = 100, width = 100)

button_del = tk.Button(app, text = "Del", bg = "white", command = lambda: delete())
button_del.place(x = 345, y = 250, height = 100, width = 100)

button_ac = tk.Button(app, text = "AC", bg = "white", command = lambda: ac())
button_ac.place(x = 455, y = 250, height = 100, width = 100)

#---------------line 1---------------

button_4 = tk.Button(app, text = "4", bg = "white", command = lambda: add("4"))
button_4.place(x = 15, y = 360, height = 100, width = 100)

button_5 = tk.Button(app, text = "5", bg = "white", command = lambda: add("5"))
button_5.place(x = 125, y = 360, height = 100, width = 100)

button_6 = tk.Button(app, text = "6", bg = "white", command = lambda: add("6"))
button_6.place(x = 235, y = 360, height = 100, width = 100)

button_time = tk.Button(app, text = "×", bg = "white", command = lambda: add("×"))
button_time.place(x = 345, y = 360, height = 100, width = 100)

button_div = tk.Button(app, text = "÷", bg = "white", command = lambda: add("÷"))
button_div.place(x = 455, y = 360, height = 100, width = 100)

#---------------line 2---------------

button_7 = tk.Button(app, text = "7", bg = "white", command = lambda: add("7"))
button_7.place(x = 15, y = 470, height = 100, width = 100)

button_8 = tk.Button(app, text = "8", bg = "white", command = lambda: add("8"))
button_8.place(x = 125, y = 470, height = 100, width = 100)

button_9 = tk.Button(app, text = "9", bg = "white", command = lambda: add("9"))
button_9.place(x = 235, y = 470, height = 100, width = 100)

button_plus = tk.Button(app, text = "+", bg = "white", command = lambda: add("+"))
button_plus.place(x = 345, y = 470, height = 100, width = 100)

button_minus = tk.Button(app, text = "-", bg = "white", command = lambda: add("-"))
button_minus.place(x = 455, y = 470, height = 100, width = 100)

#---------------line 3---------------

button_0 = tk.Button(app, text = "0", bg = "white", command = lambda: add("0"))
button_0.place(x = 15, y = 580, height = 100, width = 100)

button_dot = tk.Button(app, text = ".", bg = "white", command = lambda: add("."))
button_dot.place(x = 125, y = 580, height = 100, width = 100)

button_pi = tk.Button(app, text = "π", bg = "white", command = lambda: add("π"))
button_pi.place(x = 235, y = 580, height = 100, width = 100)

button_euler = tk.Button(app, text = "e", bg = "white", command = lambda: add("e"))
button_euler.place(x = 345, y = 580, height = 100, width = 100)

button_exe = tk.Button(app, text = "=", bg = "white", command = lambda: solve())
button_exe.place(x = 455, y = 580, height = 100, width = 100)

#---------------line 4---------------

app.mainloop()