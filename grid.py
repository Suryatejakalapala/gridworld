import numpy as np
import matplotlib.pyplot as plt

class GridWorld(object):
    def __init__(self , gridsize , items):
        self.step_reward = -1
        self.m = gridsize[0]
        self.n = gridsize[1]
        self.grid = np.zeros(gridsize)
        self.items = items

        self.state_space = list(range(self.m * self.n))

        self.action_space = {'U':-self.m , 'D':self.m , 'L':-1 , 'R': 1}
        self.actions = ['U' , 'D' , 'L' ,'R']

        self.P = self.int_P()

        def int_P(self):
            P = {}
            for state in self.state_space:
                for action in self.actions:
                    reward = self.step_reward
                    n_state = state + self.action_space[action]

                    if n_state in self.items.get('fire').get('loc'):
                        reward += self.items.get('fire').get('reward')
                    elif n_state in self.items.get('water').get('loc'):
                        reward += self.items.get('water').get('loc')
                    elif self.check_move(n_state , state):
                        n_state = state

                    P[(state , action)] = (n_state , reward)
            return P
        
        def check_terminal(self , state):
            return state in self.items.get('fire').get('loc') + self.items.get('water').get('loc')
        
        def check_move(self , n_state , oldState):
            if n_state not in self.state_space:
                return True
            elif oldState % self.m == 0 and n_state % self.m == self.m -1:
                return True
            elif oldState % self.m == self.m - 1 and n_state % self.m == 0:
                return True
            else:
                return False
            