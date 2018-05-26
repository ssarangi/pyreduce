# Default Discovery service for server on the same network
# Inspired by the project PyDiscover. Code brought into this repo to better understand and suit
# my needs. (https://github.com/cr0hn/PyDiscover)
import asyncio
import json
import pendulum

from constants import KEYS
from utils import auth_utils
from utils import logutils
from utils import network
from config import DiscoveryConfig, GRPCConfig
logger = logutils.get_logger(__name__)


class DiscoverServerProtocol(asyncio.Protocol):
    magic = None
    server_ip = None
    password = None
    answer = None
    disable_hidden = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = auth_utils.decrypt(data, self.password)
        message = json.loads(message)

        # Get a correlate query
        if message['magic'].startswith(self.magic):
            # Check the timestamp and if there's more than 20 seconds between send -> not response
            try:
                message_sent_timestamp = pendulum.from_timestamp(message['timestamp'])
            except TypeError:
                logger.debug('Received invalid timestamp in package from %s:%s', addr)
                if self.disable_hidden:
                    self.transport.sendto(auth_utils.crypt('%s#ERROR#%s' %
                                                           (self.magic, 'Invalid Timestamp'),
                                                           self.password),
                                          addr)
                    return

            # Check if packet was generated before 20 seconds
            if (pendulum.now() - message_sent_timestamp).in_seconds() < 20:
                if self.disable_hidden:
                    self.transport.sendto(auth_utils.crypt("%s#ERROR#%s" % (
                        self.magic, "Timestamp is too old"), self.password), addr)
                    logger.debug('Received outdated package from %s:%s', addr)
                    return

            # Timestamp is correct
            logger.debug('Received %r from %s', message, addr)
            self.transport.sendto(
                auth_utils.crypt("%s#OK#%s" % (self.magic, self.answer), self.password), addr)
        else:
            logger.warning('MAGIC incorrect: %s', message)
            if self.disable_hidden:
                self.transport.sendto(
                    ("%s#ERROR#%s" % (self.magic, "Invalid MAGIC or Password")).encode(), addr)
            logger.debug('Received bad magic or password from %s' % addr)


def server_discover(loop,
                    magic=DiscoveryConfig.MAGIC,
                    listen_ip=DiscoveryConfig.IP,
                    port=DiscoveryConfig.PORT,
                    password=DiscoveryConfig.PASSWORD,
                    disable_hidden=False):
    server_ip = network.get_ip_address()
    logger.info('Starting Discover Server at port %s', port)

    if password:
        password = auth_utils.prepare_text(password)

    config = dict()
    config[KEYS.GRPC_SERVER_PORT] = GRPCConfig.PORT
    config[KEYS.GRPC_SERVER_IP] = network.get_ip_address()
    _answer = json.dumps(config)

    # Setup Protocol
    DiscoverServerProtocol.magic = magic
    DiscoverServerProtocol.server_ip = server_ip
    DiscoverServerProtocol.password = password
    DiscoverServerProtocol.disable_hidden = disable_hidden
    DiscoverServerProtocol.answer = _answer

    transport = None
    try:
        # Start running the server
        listen = loop.create_datagram_endpoint(DiscoverServerProtocol,
                                               local_addr=(listen_ip, port),
                                               allow_broadcast=True)
        transport, protocol = loop.run_until_complete(listen)
        loop.run_forever()
    except:
        pass
    finally:
        logger.info('Shutting down Discovery Server')
        if transport is not None:
            transport.close()
        loop.close()
