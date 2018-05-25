from typing import Union

from .pcollection import PCollection
from .ptable import PTable
from .pindexedtable import PIndexedTable
from .master import Master
from ..utils.logutils import get_logger

logger = get_logger(__name__)

class Pipeline:
    def __init__(self):
        self._materialized_entities = []

    def materialize_on_pipeline(self, parallel_entity: Union[PCollection, PTable, PIndexedTable]):
        """
        Materialize/Execute the entity on the MR pipeline.
        :param parallel_entity: Could be a PCollection / PTable / PIndexedTable etc kind of entity
        """
        self._materialized_entities.append(parallel_entity)

    def execute(self, master : Master):
        """
        Executes the current pipeline, passing the MR graph to the server.
        :param master: If None, a new master can be created.
        """
        if master is None:
            raise NotImplemented("A new server creation is not yet implement")

        logger.info("Master Node Connection: ", master)
        logger.info("Web Server for job progress: ", master)