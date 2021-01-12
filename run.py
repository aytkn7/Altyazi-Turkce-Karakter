import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

def change(path):
	with open(path, 'r') as f:
		f = f.read()
		table = f.maketrans('ýðþÝÞÐ','ığşİŞĞ')
		fixed = f.translate(table)
		new_file_path = '/'.join(path.split('/')[:-1]) + '/fixed_' + path.split('/')[-1]
		with open(new_file_path, 'w', encoding='utf-8') as f:
			f.write(fixed)

if file_path.endswith('.srt'):
	change(file_path)
else:
	print('choose srt file')