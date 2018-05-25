import json
import pendulum
import socket

from config import DiscoveryConfig
from .exceptions import TimeOutException
from .exceptions import TimeStampException
from .exceptions import PasswordMagicException
from utils.logutils import get_logger
from utils import auth_utils

MODULE_NAME = "agent"

logger = get_logger(MODULE_NAME)


def discover(magic=DiscoveryConfig.MAGIC,
             port=DiscoveryConfig.PORT,
             password=DiscoveryConfig.PASSWORD,
             timeout=5):
    logger.info("Looking for a server discovery")

    # Prepare password
    if password:
        password = auth_utils.prepare_text(password)

    # Build message
    msg = dict()
    msg['magic'] = magic
    msg['timestamp'] = pendulum.now().timestamp()

    msg = json.dumps(msg)
    try:
        # Send discover
        # create UDP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # this is a broadcast socket
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        crypted_message = auth_utils.crypt(msg, password)
        logger.warning('Generated Crypted message from client: %s', crypted_message)
        s.sendto(auth_utils.crypt(msg, password), ('<broadcast>', port))
        s.settimeout(timeout)

        data, addr = s.recvfrom(1024)  # wait for a packet
    except socket.timeout:
        logger.info("No servers found")

        raise TimeOutException("No servers found")

    msg = auth_utils.decrypt(data, password)

    # Get a correlates response
    if msg.startswith(magic):
        msg_details = msg[len(magic):]

        logger.debug("Got service announcement from '%s' with response: %s" %
                  ("%s:%s" % addr, msg_details))

        if msg_details.startswith("#ERROR#"):
            error_details = msg_details[len("#ERROR#"):]

            logger.debug("Response from server: %s" % error_details)

            if "timestamp" in error_details:
                raise TimeStampException(error_details)
            elif "password" in error_details:
                raise PasswordMagicException(error_details)
        else:
            undecoded_msg = msg_details[len("#OK#"):]

            # Decode the json
            ok_details = json.loads(undecoded_msg)

            return ok_details, "%s:%s" % addr
