import pytest
from hackyou.gameexceptions import NotEnoughDiskSpace
from hackyou.gameapp import GameApp
from hackyou.gameserver import GameServer


def test_download_app():
    """ Trying to download app """

    server = GameServer()
    app = GameApp(filetype="cracker")

    server.download_app(app)

    assert True == server.has_app(app)


def test_download_big_app():
    """ Trying to download app with size > disk space """

    server = GameServer()

    app = GameApp(filetype="cracker", size=(server.hdd * 1000) + 1)

    with pytest.raises(NotEnoughDiskSpace):
        server.start_app_download(app)


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

    attacker.download_app(brute)
    victim.download_app(firewall)

    assert True == attacker.is_hackable(victim)


def test_crack_server_with_pure_firewall():
    """ Trying to crack victim server with firewall > brute """

    attacker = GameServer()
    victim = GameServer()

    firewall = GameApp(filetype="firewall", version=2)
    brute = GameApp(filetype="cracker", version=1)

    attacker.download_app(brute)
    victim.download_app(firewall)

    assert False == attacker.is_hackable(victim)
