from datetime import datetime
from time import mktime
from .gameapp import GameApp
from .gameexceptions import NotEnoughDiskSpace


class GameServer:

    def __init__(self, hdd=200):
        #: Server IP
        self.ip = "127.0.0.1"
        self.ram = 2
        self.cpu = 2
        self.hdd = hdd
        self.internet_speed = 5
        self.apps = []
        self.logfile = ""
        self.installations = {}
        self.money = 100

    def start_app_install(self, app):
        if app.size > self.hdd:
            raise NotEnoughDiskSpace
        else:
            # Now in Unix-time
            now = mktime(datetime.now().timetuple())

            # Time when installation will be finished
            self.installations[app] = now + app.size * (0.5 / self.cpu)

    def install_app(self, app):
        self.apps.append(app)
        self.hdd -= app.size / 1000 # MB -> GB
        self.logfile += "[{}] installed app '{}'\n".format(datetime.now().ctime(), app.name)

    def is_app_installed(self, app):
        """ Check installed app or not """

        if app in self.apps:
            return True

        # Now in Unix-time
        now = mktime(datetime.now().timetuple())

        if app in self.installations:
            if self.installations[app] < now:
                self.installations.pop(app)
                self.install_app(app)
                return True
        return False

    def is_hackable(self, server):
        """ Check can attacker hack victim or not """

        firewall_ver = 0

        for app in server.apps:
            if app.type == "firewall":
                firewall_ver = app.version

        for app in self.apps:
            if app.type == "cracker" and app.version > firewall_ver:
                return True

        return False