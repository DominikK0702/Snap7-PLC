from PyLcSnap7.DataTypes import *


class SmartTags:
    def __init__(self, client):
        """
        Wrapper around all Plc Datatypes
        :param client:
        """
        self._client = client

    def Bool(self, db, start, offset):
        return Bool(self._client, db, start, offset)

    def BoolArray(self, db, start, length):
        return BoolArray(self._client, db, start, length)









