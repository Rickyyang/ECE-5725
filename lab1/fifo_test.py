import os
while input != 'q':
	input = raw_input("please type in:")
	
	if input == 'play':
		os.system("mplayer -input file=mplayer bigbuckbunny320p.mp4")
	if input == 'pause':
		os.system("echo 'pause' > mplayer")
	elif input == 'quit':
		os.system("echo 'quit' > mplayer")
os.system("echo 'quit' > mplayer")