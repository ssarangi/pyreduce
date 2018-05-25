from .discover import discover
from config.discovery_cfg import DiscoveryConfig

def execute_agent():
    discover(magic=DiscoveryConfig.MAGIC,
             port=DiscoveryConfig.PORT,
             password=DiscoveryConfig.PASSWORD,
             timeout=5)