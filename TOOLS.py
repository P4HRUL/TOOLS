#!/usr/bin/python2
#coding=utf-8

import os
import sys


logo = ('''\n\033[1;91m\n$$$$$$$$\                  $$\           \n\__$$  __|                 $$ |          \n   $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$\ \n   $$ |$$  __$$\ $$  __$$\ $$ |$$  _____|\n   $$ |$$ /  $$ |$$ /  $$ |$$ |\$$$$$$\  \n\033[1;97m   $$ |$$ |  $$ |$$ |  $$ |$$ | \____$$\ \n   $$ |\$$$$$$  |\$$$$$$  |$$ |$$$$$$$  |\n   \__| \______/  \______/ \__|\_______/ \n\n\033[41;1m Coding By : Pahrul Aguspriana X \033[00;1m\n\n----------------------------------------\n(1) Script Bruteforce Facebook\n(2) Script Bot Facebook\n(3) Script Theme Termux\n(4) Script Encrypt Python          \n(5) Script Spam Sms ( unlimited )\n(0) Log out               \n----------------------------------------\n''')

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
	
def xxxxx():
	os.system('clear')
	os.system('git clone https://github.com/P4HRUL/SPAMMER')
	os.chdir('SPAMMER')
	os.system('git pull')
	os.system('python SPAMMER.py')
	

def masuk():
	os.system('clear')
	print(logo)
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
	elif pahrul == "0":
		exit()
	else:
		print ("")
		print "(+) Ngetik Apaan Lu bangsad !!!"
		exit()
		
masuk()

