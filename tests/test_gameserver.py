import pytest
from hackyou.gameexceptions import NotEnoughDiskSpace
from hackyou.gameapp import GameApp
from hackyou.gameserver import GameServer


def test_install_app():
    """ Trying to install app """

    server = GameServer()
    app = GameApp(filetype="cracker")

    server.install_app(app)

    assert True == server.is_app_installed(app)


def test_install_big_app():
    """ Trying install to server app with size > disk space """

    server = GameServer()

    app = GameApp(filetype="cracker", size=(server.hdd * 1000) + 1)

    with pytest.raises(NotEnoughDiskSpace):
        server.start_app_install(app)


def test_crack_server_without_brute():
    """ Trying to crack victim server without 'brute' """
    attacker = GameServer()
    victim = GameServer()

    assert False == attacker.is_hackable(victim)


def test_crack_server_with_brute():
    """ Trying to crack victim server with firewall version < brute version """

    attacker = GameServer()
    victim = GameServer()

    firewall = GameApp(filetype="firewall")
    brute = GameApp(filetype="cracker", version=2)

    attacker.install_app(brute)
    victim.install_app(firewall)

    assert True == attacker.is_hackable(victim)

def test_crack_server_with_pure_firewall():
    """ Trying to crack victim server with firewall > brute """

    attacker = GameServer()
    victim = GameServer()

    firewall = GameApp(filetype="firewall", version=2)
    brute = GameApp(filetype="cracker", version=1)

    attacker.install_app(brute)
    victim.install_app(firewall)

    assert False == attacker.is_hackable(victim)
