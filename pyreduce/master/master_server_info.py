from utils import get_logger, generate_unique_id

logger = get_logger(__name__)

class Agent:
    def __init__(self,
                 unique_id=None,
                 connection_time=None):
        self.unique_id = unique_id
        self.connection_time = connection_time
        self.system_info = None


class MasterServerInfo:
    def __init__(self):
        self._agents = dict()

    def register_agent(self, system_info, connection_time):
        unique_id = generate_unique_id()
        agent = Agent(unique_id, connection_time)
        agent.system_info = system_info
        self._agents[unique_id] = agent
        return unique_id

    def list_agents(self):
        for agent in self._agents:
            logger.info('Agent: %s connected at %s', agent.unique_id, agent.unique_id)

master_server_info = MasterServerInfo()