#!/usr/bin/env python3
import sys
import dbus

def main():
    #bus = dbus.SystemBus()
    bus = dbus.SessionBus()
    bus_name="com.example.SampleService"
    object_path='/SomeObject'
    remote_obj = bus.get_object(bus_name,object_path)
    hello_obj = remote_obj.HelloWorld("You are my eye")
    print(hello_obj)

if __name__ == '__main__':
    main()
