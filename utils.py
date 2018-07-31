import subprocess


class SessionAction(object):

    @classmethod
    def lock(cls):
        return 'lock'

    @classmethod
    def logout(cls):
        return 'session-quit'

    @classmethod
    def reboot(cls):
        return 'dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.Reboot boolean:false'

    @classmethod
    def power_off(cls):
        return 'dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.PowerOff boolean:false'

    @classmethod
    def suspend(cls):
        return 'dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.Suspend boolean:false'
