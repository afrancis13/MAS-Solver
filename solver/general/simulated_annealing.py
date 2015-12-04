import math
import matplotlib.pyplot as plt

from random import sample, uniform

from solver.staff.scorer_single import scoreSolution


class SimulatedAnnealingSolver(object):
    '''
    TODO: Run experiments to find optimal values of T and delta T!

    The idea is to  pick an ordering originally and score it using the
    functions provided by the staff. The initial ordering will be generated
    by the library function that calculates an approximate solution to the
    feedback arc set problem and by the two approximation, which will be run
    10000 times on each instance.

    Then we flip one or two nodes in the ordering randomly, run the scoring
    function. Assign,

    delta = score(s') - score(s)

    If delta is negative:
        The new path is worse. So we
        choose it with (low) probability e^{-delta/T}.

    If delta is positive:
        The new path is better. So, we replace the old solution with the new
        one.

    All the while we keep track of our best solution and its score.
    '''
    def __init__(self, initial_ordering, adj_matrix):
        self.adj_matrix = adj_matrix
        self.ordering = initial_ordering
        self.vertices = [i for i in range(len(self.adj_matrix))]
        self.t = 0.0005
        self.delta_t = -0.0000001

    def maximum_acyclic_subgraph(self):
        '''
        See the docstring for the class.
        '''
        best_ordering = self.ordering
        best_score = scoreSolution(self.adj_matrix, self.ordering)
        
        # If interested in seeing a visualization of the simulated annealing,
        # uncomment the commented lines in this function.
        # scores_to_plot = [best_score]
        
        for i in range(10000):
            flip_one, flip_two = sample(self.vertices, 2)
            new_ordering = self.ordering[::]
            new_ordering[flip_one], new_ordering[flip_two] = new_ordering[flip_two], new_ordering[flip_one]

            initial_score = scoreSolution(self.adj_matrix, self.ordering)
            new_score = scoreSolution(self.adj_matrix, new_ordering)
            delta = new_score - initial_score

            if delta < 0:
                fractional_exp = float(delta / self.t)
                p = math.exp(fractional_exp)

                sample_p = uniform(0, 1)
                if sample_p < p:
                    self.ordering = new_ordering
            elif delta == 0:
                p = 0.5
                sample_p = uniform(0, 1)
                if sample_p < p:
                    self.ordering = new_ordering
            else:
                self.ordering = new_ordering
                if new_score > best_score:
                    best_ordering = new_ordering
                    best_score = new_score

            if self.t > 0:
                self.t -= self.delta_t

            # scores_to_plot.append(best_score)

        # plt.plot([t for t in range(10001)], scores_to_plot, 'ro')
        # plt.show()

        return best_ordering
