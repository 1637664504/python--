#!/usr/bin/env python3
#coding=utf-8

import sys
import tty
import termios
import select

class Noblock_terminal:
    def __init__(self):
        fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(fd)
        tty.setraw(sys.stdin.fileno(), termios.TCSANOW)

    def __exit__(self):
        if self.old_settings:
            self.stop_no_block()

    def get_char(self):
        ch = sys.stdin.read(1)
        # sys.stdout.write(ch)
        return ch
    
    def select_cmd(self):
        read_list = [sys.stdin]
        cmd = '0'
        read_ret,write_ret,err_ret = select.select(read_list,[],[],0.5)
        if read_ret:
            for fd in read_ret:
                if fd == sys.stdin:
                    cmd = sys.stdin.read(1)
                else:
                    print("unknow fd")
        else:
            print("read timeout")

        return cmd

    def stop_no_block(self):
        fd = sys.stdin.fileno()
        termios.tcsetattr(fd, termios.TCSADRAIN, self.old_settings)
        self.old_settings = None
        

if __name__ == "__main__":
    nterm = Noblock_terminal()
    cmd = '0'
    read_list = [sys.stdin]
    while True:
        # cmd = nterm.get_char()
        cmd = nterm.select_cmd()
        if cmd == 'w':
            print("前进")
        elif cmd == 's':
            print("后退")
        elif cmd == 'q':
            print("右前")
        elif cmd == 'e':
            print('左前')
        elif cmd == 'a':
            print('左转')
        elif cmd == 'd':
            print('右转')
        elif cmd == 'c':
            print('退出')
            break

        # 回到行首
        sys.stdout.write("\033[80D")
    nterm.stop_no_block()
