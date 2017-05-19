# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """

  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()

  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]
    
    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm 
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
    
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    actions = util.Stack()
    visited = []

    start_state = problem.getStartState()
    visited.append(start_state)

    route = generalDepthFirstSearch(problem, actions, visited, start_state)

    final_route = []
    if route != 0:
        while not route.isEmpty():
            final_route.append(route.pop())

    return final_route[::-1]

def generalDepthFirstSearch(problem, actions, visited, current_state):

    if problem.isGoalState(current_state):
        return actions

    successors = problem.getSuccessors(current_state)
    for node in successors[::-1]:
        state = node[0]
        action = node[1]
        if state in visited:
            continue

        visited.append(state)
        actions.push(action)
        route = generalDepthFirstSearch(problem, actions, visited, state)
        if route != 0:
            return actions
        actions.pop()

    return 0

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    queue = util.Queue()
    visited = []

    start_state = problem.getStartState()
    visited.append(start_state)

    for node in problem.getSuccessors(start_state):
        queue.push(node)

    route = generalBreadthFirstSearch(problem, queue, visited)

    final_route = []
    if route != 0:
        while not route.isEmpty():
            final_route.append(route.pop())

    return final_route[::-1]



#def generalBreadthFirstSearch(problem, state_queue, visited, current_state):
#
#    successors = problem.getSuccessors(current_state)
#
#    for (state, action, _) in successors:
#        if problem.isGoalState(state):
#            return [action]
#        visited.append(state)
#        state_queue.push(action)
#
#    while not state_queue.isEmpty():
#        generalBreadthFirstSearch(problem, state_queue, visited, state_queue.pop())
from game import Directions
def generalBreadthFirstSearch(problem, queue, visited):

    new_queue = util.Queue()

    while not queue.isEmpty():
        node = queue.pop()
        for (s, a, c) in problem.getSuccessors(node[0]):
            if problem.isGoalState(s):
                return [s], [a]
            else:
                if s in visited:
                    continue
                new_queue.push((s, a, c))
                visited.append(s)

    states, actions = generalBreadthFirstSearch(problem, new_queue, visited)

    if states != 0 and actions != 0:
        last_state = states[-1]
        successors =


    return 0, 0



    #successors = problem.getSuccessors(current_state)
#
    #for node in successors:
    #    state = node[0]
    #    action = node[1]
    #    if problem.isGoalState(state):
    #        return [action]
    #    else:
    #        if state in visited:
    #            continue
    #        queue.push((state, action))
    #        visited.append(state)
#
    #while not queue.isEmpty():
    #    node = queue.pop()
    #    state = node[0]
    #    action = node[1]
    #    route = generalBreadthFirstSearch(problem, state, queue, visited)
    #    if route != 0:
    #        route.append(action)
    #        return route
#
    #return 0

      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
