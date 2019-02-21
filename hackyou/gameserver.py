from datetime import datetime
from time import time
from .gameapp import GameApp
from .gameexceptions import NotEnoughDiskSpace


class GameServer:

    def __init__(self):

        # Server IP
        self.ip = "127.0.0.1"

        # RAM memory (in GB)
        self.ram = 2

        # CPU (in GHz)
        self.cpu = 2

        # Hard-drive size (in GB)
        self.hdd = 200

        # Internet Speed (MB per second)
        self.internet_speed = 5

        # App list
        self.apps = []

        # Logfile
        self.logfile = ""

        # Downloads dict:
        # { app : unix-timestamp }
        # app            - instance of GameApp class
        # unix-timestamp - time when download will succeed
        self.downloads = {}

        # Money
        # TODO: do smth with it
        self.money = 100

    def start_app_download(self, app):
        """ 
            Starting app downloading: 
            1) calculating amount of time, required for download 
            2) adding to downloads
        """
        if self.hdd - app.size / 1000 < 0:
            raise NotEnoughDiskSpace
        else:
            now = time()
            self.downloads[app] = now + app.size / self.internet_speed

    def download_app(self, app):
        """
            Just adds app to app list    
        """
        self.apps.append(app)
        self.hdd -= app.size / 1000  # MB -> GB
        self.logfile += "[{}] downloaded app '{}' ({} MB)\n".format(
            datetime.now().ctime(), app.name, app.size)

    def has_app(self, app):
        """ 
            Check has server app in apps list or not
        """

        if app in self.apps:
            return True

        # If app not in app list, maybe it's downloading?

        if app in self.downloads and self.downloads[app] < time():
            self.downloads.pop(app)
            self.download_app(app)
            return True
        return False

    def is_hackable(self, server):
        """ 
            Check can attacker hack victim or not 
        """

        firewall_ver = 0

        for app in server.apps:
            if app.type == "firewall":
                firewall_ver = app.version

        for app in self.apps:
            if app.type == "cracker" and app.version > firewall_ver:
                return True

        return False
