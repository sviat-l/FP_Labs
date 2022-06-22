"""
Store and process infromation related to the airline people
"""

class TicketAgent:
    """ Class to store and manage information related
    to an airline ticket agent """
    def __init__(self, idNum):
        """ Create a ticket agent object. Init it's data"""
        self._idNum = idNum
        self._passanger = None
        self._stopTime = -1

    def idNum(self):
        """ get the ticket agent's id number """
        return self._idNum

    def isFree(self):
        """ Determines if the ticket agent is free to assist the passanger """
        return self._passanger is None

    def isFinished(self, curTime):
        """ determines if the ticket agent has finished helping the passanger """
        return self._passanger is not None and self._stopTime == curTime

    def startServise(self, passanger, stopTime):
        """ Indicates the ticket agent begun assisting a passanger"""
        self._passanger = passanger
        self._stopTime = stopTime

    def stopServise(self):
        """ Indicates the ticket agent has finished helping the passanger"""
        thePassanger = self._passanger
        self._passanger = None
        return thePassanger


class Passenger:
    """ Class to store and manage information related to an airline passanger """
    def __init__(self, idNum, arrivalTime):
        """ init the passenger object data """
        self._idNum = idNum
        self._arrivalTime = arrivalTime

    def idNum(self):
        """ get the passenger's id number """
        return self._idNum

    def timeArrived(self):
        """ get the pasanger's arrival time """
        return self._arrivalTime
