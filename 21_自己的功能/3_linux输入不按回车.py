import sys
import tty
import termios

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

    def stop_no_block(self):
        fd = sys.stdin.fileno()
        termios.tcsetattr(fd, termios.TCSADRAIN, self.old_settings)
        self.old_settings = None
        

if __name__ == "__main__":
    sync_read = Noblock_terminal()
    cmd = '0'
    while True:
        cmd = sync_read.get_char()
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

        sys.stdout.write("\033[80D")
    sync_read.stop_no_block()
