from glusterd_plus.peers import Peer


class Connection:
    def __init__(self, url):
        self.url = url

    def list_peers(self):
        return Peer.list(self)

    def add_peer(self, name):
        return Peer.add(self, name)

    def peer(self, name):
        return Peer(self, name)
