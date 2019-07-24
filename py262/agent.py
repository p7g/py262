'''
This module defines the ECMAScript Agent class
'''

from py262.utils import schrodinger_property

class Agent:
    '''https://ts39.es/ecma262/#sec-agents'''

    current_signifier = 0

    @classmethod
    def next_signifier(cls) -> int:
        '''Get the next signifier value'''
        value = cls.current_signifier
        cls.current_signifier += 1
        return value

    def __init__(self):
        self._signifier = type(self).next_signifier()
        self._little_endian = False
        self.execution_context_stack = []

    @property
    def running_execution_context(self):
        '''Get the execution context that is currently running'''
        return self.execution_context_stack[-1]

    @schrodinger_property
    def little_endian(self) -> bool:
        '''Check if the agent is little endian or not'''
        return self._little_endian

    @little_endian.setter  # type: ignore
    def little_endian(self, value):
        self._little_endian = value

    @property
    def signifier(self) -> int:
        '''Get the globally unique signifier of the agent'''
        return self._signifier


surrounding_agent = None


def set_surrounding_agent(agent):
    '''Set the surrounding agent to a different agent'''
    global surrounding_agent  # pylint: disable=global-statement
    surrounding_agent = agent
