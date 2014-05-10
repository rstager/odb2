import curses
import time
stdscr = curses.initscr()
supported=range(0,79)

cnt=0
while True:
	(l,c)=stdscr.getmaxyx()
	fmt="{:3d},{:3d}:{:"+str(c/3)+"."+str(c/3)+"s}"
	i=0
	for t in supported:
		s=fmt.format(1,i,str(t+cnt))
		stdscr.addstr(i%l,c/3*int(i/l),s)
		stdscr.refresh()
		i+=1
	time.sleep(1)
	cnt+=1