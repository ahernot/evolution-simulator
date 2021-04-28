


class Gene:

    def __init__ (self):
        self.id = 0  # gene id
        self.var_id = 0  # gene variation id

        # list of affinities with other genes (all variations at once): the way in which genes interact will affect the probability of death of an individual

        self.var_probability = 0.03  # probability of mutation into a new variation during breeding
        self.dominance = 0.3  # dominance of the variation; will win out over any variation with a lesser dominance




# breeding:
# for each gene id: pick a parent at random, based on dominance (the one of the two with the highest dominance)
#   then mutate it with var_probability probability: in that case, slight variation of the parameters (affinities, etc) at random (OF COURSE DETERMINISTIC PSEUDO RANDOM TO HAVE REPRODUCIBLE RESULTS)
#   then create offspring with these parameters



# individual's health = 1 - global_death_probability  >> will affect breeding
# breeding only during sexual maturity too, but can change
# so need to have specialised genes: sexual genes, appearance genes, etc. => fertility…
