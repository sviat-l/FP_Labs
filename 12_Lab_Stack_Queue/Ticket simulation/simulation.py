"""
Implementation of the Airline Ticket Conter simulation
"""

import random
from arrays import Array
from arrayqueue import ArrayQueue as Queue
from simpeople import TicketAgent, Passenger


class TicketCounterSimulation:
    """
    Class to run Ticket Couner simulation
    """
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        """ init parameters for sumulation """
        # Parameters suplied by user
        self._ariveProb = 1.0/betweenTime
        self._serviseTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i+1)

        # computed during iteration
        self._totalWaitTime = 0
        self._numPassengers = 0

    def run(self):
        """ run the simulation using the parameters suplied earlier """
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndServise(curTime)

    def printResults(self):
        """ print the simulation results """
        numServed = self._numPassengers
        avgWait = float(self._totalWaitTime)/ numServed
        print('')
        print('Number of passengers served = ', numServed)
        print(f'Number of passengers remainig in line ={len(self._passengerQ)}')
        print(f' The average wait time was = {avgWait: .2f} minutes')

    def _handleArrival(self, curTime:int):
        """
        Handle arrivind process. Create a new passanger
        with stated chance. Add them to the queue
        """
        if random.random() < self._ariveProb:
            self._passengerQ.add(Passenger(self._numPassengers, curTime))
            self._numPassengers +=1

    def _handleBeginService(self, curTime:int):
        """
        Handle Servise. If there are people in a queue send them
        to the Ticket agent if there are free.
        """
        while not self._passengerQ.isEmpty():
            found_free_agent = False
            for agent in self._theAgents:
                if agent.isFree():
                    found_free_agent = True
                    person = self._passengerQ.pop()
                    agent.startServise(person, curTime + self._serviseTime)
                    self._totalWaitTime += curTime - person.timeArrived()
                    break
            if not found_free_agent:
                break


    def _handleEndServise(self, curTime:int):
        """
        Check if the agents have finished their work.
        End it, set the agent free
        """
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                agent.stopServise()


if __name__ == '__main__':
    random.seed(4500)
    simulation = TicketCounterSimulation(2, 10000, 1 ,3)
    simulation.run()
    simulation.printResults()
