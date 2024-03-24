class Peer:
    def __init__(self, conn, name):
        self.conn = conn
        self.name = name

    @classmethod
    def list(cls, conn):
        return "list_peers"

    @classmethod
    def add(cls, conn, name):
        return f"added {name}"

    def remove(self):
        return f"removed {self.name}"
