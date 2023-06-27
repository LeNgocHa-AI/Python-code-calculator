import tkinter as tk
import math as m
from sympy import *

exp = "|"
output = ""
ans = 0
enter_eq = 0
mode = "d"
imag = "OFF"

def bar_left():
	global exp, enter_eq
	exp.replace(" ", "")
	if enter_eq == 0:
		if (exp == "|") or (exp == "| "):
			pass
		else:
			if exp[0] == "|":
				exp = exp[1 :] + "|"
				out1.config(text = exp)
			elif exp[-1] == "|":
				exp = exp[0 : len(exp) - 2] + "|" + exp[len(exp) - 2]
			else:
				head = exp[: exp.index("|")]
				end = exp[exp.index("|") + 1  :]
				end = head[-1] + end
				head = head[0 : -1]
				exp = head + "|" + end
	else:
		if (exp == "|") or (exp == "| "):
			pass
		else:
			exp = exp + "|"
			enter_eq = 0
	exp.replace(" ", "")
	out1.config(text = exp)
		
def bar_right():
	global exp, enter_eq
	exp.replace(" ", "")
	if enter_eq == 0:
		if (exp == "|") or (exp == "| "):
			pass
		else:
			if exp[0] == "|":
				exp = exp[1] + "|" + exp[2 :]
				out1.config(text = exp)
			elif exp[-1] == "|":
				exp = "|" + exp[0 : -1]
			else:
				head = exp[: exp.index("|")]
				end = exp[exp.index("|") + 1  :]
				head += end[0]
				end = end[1 :]
				exp = head + "|" + end
	else:
		if (exp == "|") or (exp == "| "):
			pass
		else:
			exp = "|" + exp
			enter_eq = 0
	exp.replace(" ", "")
	out1.config(text = exp)

def bar_add(var):
	global exp
	if exp == "":
		exp = "|"
	exp = exp[: exp.index("|")] + var + exp[exp.index("|") :]

def bar_del():
	global exp
	exp += " "
	if (exp == "|") or (exp == "| "):
		pass
	else:
		head = exp[: exp.index("|")]
		end = exp[exp.index("|") + 1 :]
		if head == "":
			end = end[1 : exp.index(" ")]
			exp = "|" + end
		else:
			head = head[0 : -1]
			end = end[0 : exp.index(" ")]
			exp = head + "|" + end
	exp.replace(" ", "")
	out1.config(text = exp)

def add(var):
	global exp, enter_eq
	if enter_eq != 0:
		exp = "|"
		enter_eq = 0
	bar_add(var)
	out1.config(text = exp)
	
def delete():
	global exp
	bar_del()
	exp.replace(" ", "")
	out1.config(text = exp)
	
def ac():
	global exp
	exp = "|"
	output = ""
	out1.config(text = exp)
	out2.config(text = output)
	
def MB10(var):
	if var >= 10**15:
		return str(output/(10**(len(str(round(var))) - 1))) + " × 10^" + str(len(str(round(var))) - 1)
					
	elif var <= -10**15:
		return str(var/(10**(len(str(round(var))) - 2))) + " × 10^" + str(len(str(round(var))) - 2)
			
	elif var == 0:
		return "0"
						
	elif (-10**(-4) < var < 10**(-4)):
		return str(var)[: str(var).index("e")] + " × 10^" + str(var)[str(var).index("e") + 1:]
	
	else:
		return str(var)

def sin(a):
	global mode
	if mode == "r":
		return m.sin(a)
	if mode == "d":
		return m.sin(m.radians(a))
		
def cos(a):
	global mode
	if mode == "r":
		return m.cos(a)
	if mode == "d":
		return m.cos(m.radians(a))
		
def tan(a):
	global mode
	if mode == "r":
		return m.tan(a)
	if mode == "d":
		return m.tan(m.radians(a))
		
def asin(a):
	global mode
	if mode == "r":
		return m.asin(a)
	if mode == "d":
		return m.degrees(m.asin(a))
		
def acos(a):
	global mode
	if mode == "r":
		return m.acos(a)
	if mode == "d":
		return m.degrees(m.acos(a))
		
def atan(a):
	global mode
	if mode == "r":
		return m.atan(a)
	if mode == "d":
		return m.degrees(m.atan(a))
		
def mode_degree(degree):
	global mode
	if degree == "d":
		button_d_mode.config(state = "disabled")
		button_r_mode.config(state = "normal")
		mode = "d"
	if degree == "r":
		button_r_mode.config(state = "disabled")
		button_d_mode.config(state = "normal")
		mode = "r"
	
def on_imag_num():
	global imag
	button_ON_imagnum_mode.config(state = "disabled")
	button_OFF_imagnum_mode.config(state = "normal")
	imag = "ON"
	
def off_imag_num():
	global imag
	button_OFF_imagnum_mode.config(state = "disabled")
	button_ON_imagnum_mode.config(state = "normal")
	imag = "OFF"

def solve():
	global exp, output, ans, enter_eq, x, y, z
	exp += " "
	k = ""
	real_exp = ""
	for i in exp:
		try:
			k += str(int(i))
		except:
			try:
				if i == ".":
					k += "."
				else:
					k = str(int(k))
			except:
				pass
			if i != ".":
				real_exp += k + i
				k = ""
	exp = real_exp
	input = ""
	error = 0
	enter_eq += 1
	if (exp == "| ") or (exp == "|"):
		pass
		exp = "|"
	else:
		for i in exp:
			
			if i == "×":
				input += "*"
				
			elif i == "÷":
				input += "/"
				
			elif i == "^":
				input += "**"
				
			elif i == "π":
				try:
					if ((input[-1] != "+") and (input[-1] != "-") and (input[-1] != "*") and (input[-1] != "/") and (input[-1] != "(")):
						input += "*pi"
					else:
						input += "pi"
				except:
					input += "pi"
			
			elif i == "e":
				try:
					if ((input[-1] != "+") and (input[-1] != "-") and (input[-1] != "*") and (input[-1] != "/") and (input[-1] != "(")):
						input += "*2.71828182845904523536"
					else:
						input += "2.71828182845904523536"
				except:
					input += "2.71828182845904523536"
						
			elif i == ".":
				if input == "":
					input += "0."
				else:
					try:
						int(input[-1])
						input += "."
					except:
						input += "0."	
					
			elif i == "|":
				try:
					exp = exp[: exp.index("|")] + exp[exp.index("|") + 1 :]
					out1.config(text = exp)
				except:
					exp = exp[: exp.index("|")]
					
			elif i == "∆":
				try:
					if ((input[-1] != "+") and (input[-1] != "-") and (input[-1] != "*") and (input[-1] != "/") and (input[-1] != "(")):
						input += "*(" + str(ans) + ")"
					else:
						input += "(" + str(ans) + ")"
				except:
					input += "(" + str(ans) + ")"
					
			elif i == "√":
				try:
					if ((input[-1] != "+") and (input[-1] != "-") and (input[-1] != "*") and (input[-1] != "/") and (input[-1] != "(")):
						input += "*sqrt"
					else:
						input += "sqrt"
				except:
					input += "sqrt"
			
			elif i == "s":
				try:
					if ((input[-1] != "+") and (input[-1] != "-") and (input[-1] != "*") and (input[-1] != "/") and (input[-1] != "(") and (input[-1] != "a")  and (input[-1] != "o")):
						input += "*s"
					else:
						input += "s"
				except:
					input += "s"
					
			elif i == "c":
				try:
					if ((input[-1] != "+") and (input[-1] != "-") and (input[-1] != "*") and (input[-1] != "/") and (input[-1] != "(")  and (input[-1] != "a")):
						input += "*c"
					else:
						input += "c"
				except:
					input += "c"
					
			elif i == "t":
				try:
					if ((input[-1] != "+") and (input[-1] != "-") and (input[-1] != "*") and (input[-1] != "/") and (input[-1] != "(") and (input[-1] != "a")):
						input += "*t"
					else:
						input += "t"
				except:
					input += "t"
					
			elif i == "a":
				try:
					if ((input[-1] != "+") and (input[-1] != "-") and (input[-1] != "*") and (input[-1] != "/") and (input[-1] != "(") and (input[-1] != "a")  and (input[-1] != "t")):
						input += "*a"
					else:
						input += "a"
				except:
					input += "a"

			else:
				input += i
		if imag == "OFF":
			try:
				output = str(eval(input))
				output.replace("sqrt", "√")
				output.replace("*", "×")
				ans_real = output
				output = MB10(output)
			except:
				error += 1
		
		elif imag == "ON":
			try:
				output = str(eval(input))
				output.replace("sqrt", "√")
				output.replace("I", "i")
				output.replace("*", "×")
				ans_real = output
			except:
				error += 1

		for i in range(1, len(exp)):
			try:
				int(exp[i])
				if (exp[i - 1] == "π") or (exp[i - 1] == "e") or (exp[i - 1] == "∆") or (exp[i - 1] == ")"):
					error += 1
				else:
					pass
			except:
				pass
	
		if error == 0:
			out2.config(text = "= " + str(output))
			exp.replace(" ", "")
			ans = ans_real
			out1.config(text = exp)
			button_Ans.config(text = "∆ = " + str(output))
		else:
			out2.config(text = "ERROR!!!")

app = tk.Tk()

out1 = tk.Label(app, text = exp, bg = "black", fg = "white", anchor = "w")
out1.place(x = 0, y = 0, height = 120, width = 720)

#----------expression input screen----------

out2 = tk.Label(app, text = output, bg = "black", fg = "white", anchor = "e")
out2.place(x = 0, y = 120, height = 120, width = 720)

#-----------output screen----------

button_Ans = tk.Button(app, text = "∆ = 0", bg = "black", fg = "white", anchor = "w", wraplength = 330, font = ("Arial", 5), command = lambda: add("∆"))
button_Ans.place(x= 345, y = 260, height = 60, width = 420)

button_left = tk.Button(app, text = "<", bg = "white", command = lambda: bar_left())
button_left.place(x = 15, y = 255, height = 70, width = 150)

button_right = tk.Button(app, text = ">", bg = "white", command = lambda: bar_right())
button_right.place(x = 185, y = 255, height = 70, width = 150)

#----------navigation bar button---------

button_1 = tk.Button(app, text = "1", bg = "white", command = lambda: add("1"))
button_1.place(x = 15, y = 325, height = 100, width = 100)

button_2 = tk.Button(app, text = "2", bg = "white", command = lambda: add("2"))
button_2.place(x = 125, y = 325, height = 100, width = 100)

button_3 = tk.Button(app, text = "3", bg = "white", command = lambda: add("3"))
button_3.place(x = 235, y = 325, height = 100, width = 100)

button_del = tk.Button(app, text = "Del", bg = "white", command = lambda: delete())
button_del.place(x = 345, y = 325, height = 100, width = 100)

button_ac = tk.Button(app, text = "AC", bg = "white", command = lambda: ac())
button_ac.place(x = 455, y = 325, height = 100, width = 100)

#---------------line 1---------------

button_4 = tk.Button(app, text = "4", bg = "white", command = lambda: add("4"))
button_4.place(x = 15, y = 435, height = 100, width = 100)

button_5 = tk.Button(app, text = "5", bg = "white", command = lambda: add("5"))
button_5.place(x = 125, y = 435, height = 100, width = 100)

button_6 = tk.Button(app, text = "6", bg = "white", command = lambda: add("6"))
button_6.place(x = 235, y = 435, height = 100, width = 100)

button_time = tk.Button(app, text = "×", bg = "white", command = lambda: add("×"))
button_time.place(x = 345, y = 435, height = 100, width = 100)

button_div = tk.Button(app, text = "÷", bg = "white", command = lambda: add("÷"))
button_div.place(x = 455, y = 435, height = 100, width = 100)

#---------------line 2---------------

button_7 = tk.Button(app, text = "7", bg = "white", command = lambda: add("7"))
button_7.place(x = 15, y = 545, height = 100, width = 100)

button_8 = tk.Button(app, text = "8", bg = "white", command = lambda: add("8"))
button_8.place(x = 125, y = 545, height = 100, width = 100)

button_9 = tk.Button(app, text = "9", bg = "white", command = lambda: add("9"))
button_9.place(x = 235, y = 545, height = 100, width = 100)

button_plus = tk.Button(app, text = "+", bg = "white", command = lambda: add("+"))
button_plus.place(x = 345, y = 545, height = 100, width = 100)

button_minus = tk.Button(app, text = "-", bg = "white", command = lambda: add("-"))
button_minus.place(x = 455, y = 545, height = 100, width = 100)

#---------------line 3---------------

button_0 = tk.Button(app, text = "0", bg = "white", command = lambda: add("0"))
button_0.place(x = 15, y = 656, height = 100, width = 100)

button_dot = tk.Button(app, text = ".", bg = "white", command = lambda: add("."))
button_dot.place(x = 125, y = 655, height = 100, width = 100)

button_pi = tk.Button(app, text = "π", bg = "white", command = lambda: add("π"))
button_pi.place(x = 235, y = 655, height = 100, width = 100)

button_euler = tk.Button(app, text = "e", bg = "white", command = lambda: add("e"))
button_euler.place(x = 345, y = 655, height = 100, width = 100)

button_exe = tk.Button(app, text = "=", bg = "white", command = lambda: solve())
button_exe.place(x = 455, y = 655, height = 100, width = 100)

#---------------line 4---------------

#___________basic math operations__________



button_sin = tk.Button(app, text = "sin(", bg = "white", command = lambda: add("sin("))
button_sin.place(x = 15, y = 765, height = 100, width = 100)

button_cos = tk.Button(app, text = "cos(", bg = "white", command = lambda: add("cos("))
button_cos.place(x =125, y = 765, height = 100, width = 100)

button_tan = tk.Button(app, text = "tan(", bg = "white", command = lambda: add("tan("))
button_tan.place(x = 235, y = 765, height = 100, width = 100)

button_open_parenthesis = tk.Button(app, text = "(", bg = "white", command = lambda: add("("))
button_open_parenthesis.place(x = 345, y = 765, height = 100, width = 100)

button_sqrt = tk.Button(app, text = "√", bg = "white", command = lambda: add("√("))
button_sqrt.place(x = 455, y = 765, height = 100, width = 100)

button_asin = tk.Button(app, text = "asin(", bg = "white", command = lambda: add("asin("))
button_asin.place(x = 15, y = 875, height = 100, width = 100)

button_acos = tk.Button(app, text = "acos(", bg = "white", command = lambda: add("acos("))
button_acos.place(x =125, y = 875, height = 100, width = 100)

button_atan = tk.Button(app, text = "atan(", bg = "white", command = lambda: add("atan("))
button_atan.place(x = 235, y = 875, height = 100, width = 100)

button_close_parenthesis = tk.Button(app, text = ")", bg = "white", command = lambda: add(")"))
button_close_parenthesis.place(x = 345, y = 875, height = 100, width = 100)

button_sqrt = tk.Button(app, text = "^", bg = "white", command = lambda: add("^"))
button_sqrt.place(x = 455, y = 875, height = 100, width = 100)



degree_mode_txt = tk.Label(app, text = "Degree mode", fg = "blue", font = ("Arial", 5))
degree_mode_txt.place(x = 575, y = 320)

button_d_mode = tk.Button(app, text = "d", fg = "blue", command = lambda: mode_degree("d"), state = "disabled")
button_d_mode.place(x = 575, y = 350, height = 50, width = 50)

button_r_mode = tk.Button(app, text = "r", fg = "blue", command = lambda: mode_degree("r"), state = "normal")
button_r_mode.place(x = 635, y = 350, height = 50, width = 50)

text_imagnum_mode = tk.Label(app, text = "Imaginary number mode", fg = "blue", font = ("Arial", 4))
text_imagnum_mode.place(x = 555, y = 415)

button_ON_imagnum_mode = tk.Button(app, text = "ON", fg = "blue", command = lambda: on_imag_num(), state = "normal")
button_ON_imagnum_mode.place(x = 575, y = 450, height = 50, width = 50)

button_OFF_imagnum_mode = tk.Button(app, text = "OFF", fg = "blue", command = lambda: off_imag_num(), state = "disabled")
button_OFF_imagnum_mode.place(x = 635, y = 450, height = 50, width = 50)

app.mainloop()
