#!/usr/bin/python2
#coding=utf-8

import os
import sys
import time

def slowprint(s):
    try:
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.001)
    except (KeyboardInterrupt, EOFError):
        run('Nonaktif!!!')

load = ('''
\033[1;92m    __                    ___
   / /   ____  ____ _____/ (_)___  ____ _
  / /   / __ \/ __ `/ __  / / __ \/ __ `/
 / /___/ /_/ / /_/ / /_/ / / / / / /_/ / _ _
/_____/\____/\__,_/\__,_/_/_/ /_/\__, (_|_|_)
                                /____/\033[1;97m
''')

logo = ('''
\033[1;97m$$$$$$$$\                  $$\           
\__$$  __|                 $$ |          
   $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$\ 
   $$ |$$  __$$\ $$  __$$\ $$ |$$  _____|
   $$ |$$ /  $$ |$$ /  $$ |$$ |\$$$$$$\  
   $$ |$$ |  $$ |$$ |  $$ |$$ | \____$$\ 
   $$ |\$$$$$$  |\$$$$$$  |$$ |$$$$$$$  |
   \__| \______/  \______/ \__|\_______/ 
                                                                                  
\033[41;1m Coding By : Pahrul Aguspriana X \033[00;1m

---------------------------------------
(1) script bruteforce facebook
(2) script bot facebook
(3) script theme termux
(4) script encrypt python
(5) script share post facebook
(6) script get token facebook
(0) log out
----------------------------------------
''')

def x():
	os.system('clear')
	print(load)
	os.system('git clone https://github.com/P4HRUL/BRUTE')
	os.chdir('BRUTE')
	os.system('git pull')
	os.system('python BRUTE.py')
	
def xx():
	os.system('clear')
	print(load)
	os.system('git clone https://github.com/P4HRUL/BOT')
	os.chdir('BOT')
	os.system('git pull')
	os.system('python2 BOT.py')
	
def xxx():
	os.system('clear')
	print(load)
	os.system('git clone https://github.com/P4HRUL/THEME')
	os.chdir('THEME')
	os.system('git pull')
	os.system('python2 THEME.py')
	
def xxxx():
	os.system('clear')
	print(load)
	os.system('git clone https://github.com/P4HRUL/PYENC')
	os.chdir('PYENC')
	os.system('git pull')
	os.system('python2 PYENC.py')
	
def xxxxx():
	os.system('clear')
	print(load)
	os.system('git clone https://github.com/P4HRUL/SHARE')
	os.chdir('SHARE')
	os.system('git pull')
	os.system('python SHARE.py')
	
def xxxxxx():
	os.system('clear')
	print(load)
	os.system('git clone https://github.com/P4HRUL/TOKEN')
	os.chdir('TOKEN')
	os.system('git pull')
	os.system('python TOKEN.py')
	

def masuk():
	os.system('clear')
	slowprint(logo)
	pilih()
	
def pilih():
	pahrul = raw_input('(+) choose : ')
	if pahrul == "":
		print ("")
		print "(+) Ngetik Apaan Lu bangsad !!!"
		exit()
	elif pahrul == "1":
		x()
	elif pahrul == "2":
		xx()
	elif pahrul == "3":
		xxx()
	elif pahrul == "4":
		xxxx()
	elif pahrul == "5":
		xxxxx()
	elif pahrul == "6":
		xxxxxx()
	elif pahrul == "0":
		exit()
	else:
		print ("")
		print "(+) Ngetik Apaan Lu bangsad !!!"
		exit()
		
masuk()

