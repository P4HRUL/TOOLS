#!/usr/bin/python2
#coding=utf-8

import os
import sys


logo = ('''\033[1;91m
$$$$$$$$\                  $$\           
\__$$  __|                 $$ |          
   $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$\ 
   $$ |$$  __$$\ $$  __$$\ $$ |$$  _____|
   $$ |$$ /  $$ |$$ /  $$ |$$ |\$$$$$$\  
\033[1;97m   $$ |$$ |  $$ |$$ |  $$ |$$ | \____$$\ 
   $$ |\$$$$$$  |\$$$$$$  |$$ |$$$$$$$  |
   \__| \______/  \______/ \__|\_______/ 

Coding By : Pahrul Aguspriana X

----------------------------------------
(1) Script Bruteforce Facebook
(2) Script Bot Facebook
(3) Script Theme Termux
(4) Script Encrypt Python          
(0) Log out               
----------------------------------------
''')

def x():
	os.system('clear')
	os.system('git clone https://github.com/P4HRUL/BRUTE')
	os.chdir('BRUTE')
	os.system('git pull')
	os.system('python BRUTE.py')
	
def xx():
	os.system('clear')
	os.system('git clone https://github.com/P4HRUL/BOT')
	os.chdir('BOT')
	os.system('git pull')
	os.system('python2 BOT.py')
	
def xxx():
	os.system('clear')
	os.system('git clone https://github.com/P4HRUL/THEME')
	os.chdir('THEME')
	os.system('git pull')
	os.system('python2 THEME.py')
	
def xxxx():
	os.system('clear')
	os.system('git clone https://github.com/P4HRUL/PYENC')
	os.chdir('PYENC')
	os.system('git pull')
	os.system('python2 PYENC.py')
	

def masuk():
	os.system('clear')
	print(logo)
	pilih()
	
def pilih():
	tanya = raw_input('(+) choose : ')
	if tanya == "":
		print ("")
		print "(+) Ngetik Apaan Lu bangsad !!!"
		exit()
	elif tanya == "1":
		x()
	elif tanya == "2":
		xx()
	elif tanya == "3":
		xxx()
	elif tanya == "4":
		xxxx()
	elif tanya == "0":
		exit()
	else:
		print ("")
		print "(+) Ngetik Apaan Lu bangsad !!!"
		exit()
		
masuk()

