#!/usr/bin/env python3
from gi.repository import GLib

import dbus
import dbus.service
import dbus.mainloop.glib

class SomeObject(dbus.service.Object):
    @dbus.service.method("com.example.SampleInterface",
                         in_signature='s', out_signature='as')
    def HelloWorld(self, hello_message):
        print("service:", str(hello_message))
        return ["Hello", " from example-service.py", "with unique name",
                session_bus.get_unique_name()]

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus_name = "com.example.SampleService"
    object_path = '/SomeObject'
    
    #session_bus = dbus.SystemBus()
    session_bus = dbus.SessionBus()
    #name = dbus.service.BusName("com.example.SampleService", session_bus)
    name = dbus.service.BusName(bus_name,session_bus)
    obj = SomeObject(session_bus,object_path)

    mainloop = GLib.MainLoop()
    print("Running example service.")
    mainloop.run()
