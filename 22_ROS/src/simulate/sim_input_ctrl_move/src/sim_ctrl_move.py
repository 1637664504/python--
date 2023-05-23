#!/usr/bin/env python3
#coding=utf-8

''' 
功能:
    实现输入w,s,a,d命令控制底盘移动
'''

import sys
import tty
import termios
import select

# ROS
import rospy
from geometry_msgs.msg import Twist

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

    def select_cmd(self,timeout):
        read_list = [sys.stdin]
        cmd = '0'
        read_ret,write_ret,err_ret = select.select(read_list,[],[],timeout)
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

class Sim_ctrl_move:
    def __init__(self,config):
        if not config:
            raise Exception("请配置config")
        self.config={}
        self.config['topic'] = config['topic']
        self.config['timeout'] = config['timeout']
        rospy.init_node('sim_ctrl_move', anonymous=True,disable_signals=True)
        self.pub_twist = rospy.Publisher(self.config['topic'], Twist, queue_size=10)

    def help(self):
        info = \
'''
\033[80D     w 前进
\033[80D a 右转      d 左转
\033[80D     s 后退 \n
\033[80D c 退出 \n
\033[80D h 帮助
'''
        print(info)
        # print('\033[80D        w 前进')
        # print('\033[80D a 右转        d 左转')
        # print('\033[80D        s 后退')

    def publisher_cmdvel(self,x:float,z:float):
        var = Twist()
        var.linear.x = x
        var.angular.z = z
        # 平面移动机器人常常 linear.y和linear.z为0, linear.x 表示前方
        #           angular.z代表平面机器人的角速度，因为此时z轴为旋转轴
        self.pub_twist.publish(var)
        
    def loop_run(self):
        nterm = Noblock_terminal()
        while True:
            # cmd = nterm.get_char()
            x:float = 0
            z:float = 0
            cmd = nterm.select_cmd(self.config['timeout'])
            if cmd == 'w':
                print("前进")
                x= 0.1
            elif cmd == 's':
                print("后退")
                x= -0.1
            # elif cmd == 'q':
            #     print("右前")
            # elif cmd == 'e':
            #     print('左前')
            elif cmd == 'a':
                print('左转')
                z= 0.2
            elif cmd == 'd':
                print('右转')
                z= -0.2
            elif cmd == 'h':
                self.help()
            elif cmd == 'c':
                print('退出')
                break

            self.publisher_cmdvel(x,z)
            # 回到行首
            sys.stdout.write("\033[80D")
        nterm.stop_no_block()

if __name__ == "__main__":
    config={
        'topic': '/cmd_vel',    # Twist topic话题
        'timeout': 0.5,         # 松开按键0.5s之后, 再发送停止指令
    }
    sim_ctrl = Sim_ctrl_move(config)
    sim_ctrl.loop_run()
