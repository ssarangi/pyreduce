# Master Server configuration
class Master:
    def __init__(self, ip="localhost", port=50051):
        self._server_str = ip
        self._port = port

    def __str__(self):
        return self._server_str + ":" + str(self._port)

    __repr__ = __str__