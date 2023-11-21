from select import select
import serial
import os, time, sys, termios, atexit, tty

class GetChar:
    def __init__(self):
        # Save the terminal settings
        self.fd = sys.stdin.fileno()
        self.new_term = termios.tcgetattr(self.fd)
        self.old_term = termios.tcgetattr(self.fd)
  
        # New terminal setting unbuffered
        self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)
  
        # Support normal-terminal reset at exit
        atexit.register(self.set_normal_term)      
      
    def set_normal_term(self):
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)
  
    def getch(self):        # get 1 byte from stdin
        """ Returns a keyboard character after getch() has been called """
        return sys.stdin.read(1)
  
    def chk_stdin(self):    # check keyboard input
        """ Returns True if keyboard character was hit, False otherwise. """
        dr, dw, de = select([sys.stdin], [], [], 0)
        return dr


if __name__ == '__main__':

    try:
        sp  = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        kb  = GetChar()
        dat = ""
        print("type '1' for turn on led, type'0' for turn off led...")
        
        while True:
            
            ch = kb.getch()
            
            if   ch == '1':
                sp.write(b'1') 
                print("led  on")
                
            elif ch == '0':
                sp.write(b'0') 
                print("led off")              
                
            
            else:
                pass
            
    except KeyboardInterrupt:
        pass
