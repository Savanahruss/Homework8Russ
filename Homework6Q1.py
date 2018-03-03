import numpy as np
import scr.SamplePathClass as SamplePathSupport
import scr.StatisticalClasses as Stat


class Game(object):
    def __init__(self, id, prob_head):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(id)
        self._probHead = prob_head  # probability of flipping a head
        self._countWins = 0  # number of wins, set to 0 to begin

    def simulate(self, n_of_flips):
        count_tails = 0  # number of consecutive tails so far, set to 0 to begin
        # flip the coin 20 times
        for i in range(n_of_flips):
            # in the case of flipping a heads
            if self._rnd.random_sample() < self._probHead:
                if count_tails >= 2:  # if the series is ..., T, T, H
                    self._countWins += 1  # increase the number of wins by 1
                count_tails = 0  # the tails counter needs to be reset to 0 because a heads was flipped
            # in the case of flipping a tails
            else:
                count_tails += 1  # increase tails count by one

    def get_reward(self):
        # calculate the reward from playing a single game
        return 100*self._countWins - 250


class SetOfGames:
    def __init__(self, prob_head, n_games):
        self._lose_count=0
        self._gameRewards = [] # create an empty list where rewards will be stored
        # simulate the games
        self._value = self._gameRewards
        self._maxi = 0
        self._mini = 0
        self._losslist=[]



        for n in range(n_games):
            # create a new game
            game = Game(id=n, prob_head=prob_head)
            # simulate the game with 20 flips
            game.simulate(20)
            # store the reward

            self._gameRewards.append(game.get_reward())

        self._sumStat_expectedrewards = Stat.SummaryStat('Game Reward', self._gameRewards)
        self._sumStat_probabilityloss = Stat.SummaryStat('Probability of Loss', self._losslist)

    def get_game_rewards(self):
        return self._gameRewards

    def get_loss_count(self):
        for value in self._gameRewards:
            if value < 0:
                self._lose_count+=1
        return self._lose_count / len(self._gameRewards)

    def get_loss_list(self):
        for value in self._gameRewards:
            if value < 0:
                self._losslist.append(game.get_loss_count)

        return self._losslist

    def get_ave_reward(self):
        """ returns the average reward from all games"""
        return sum(self._gameRewards) / len(self._gameRewards)

    def get_maximum(self):
        for value in self._gameRewards:
            if value>self._maxi:
                self._maxi = value
        return self._maxi

    def get_minimum(self):
        for value in self._gameRewards:
            if value<self._mini:
                self._mini = value
        return self._mini

    def get_CI_game_reward(self,alpha):
        return self._sumStat_expectedrewards.get_t_CI(alpha)

    def get_CI_loss_probability(self,alpha):
        return self._sumStat_probabilityloss.get_t_CI(alpha)



# run trail of 1000 games to calculate expected reward
games = SetOfGames(prob_head=0.5, n_games=1000)


# print the average reward
print('Expected reward when the probability of head is 0.5:', games.get_ave_reward())
print('The maximum value of rewards is:', games.get_maximum())
print('The minimum value of rewards is:', games.get_minimum())
print('The probability of losing is:', games.get_loss_count())
#print(games.get_loss_list())

print('The 95% Confidence Interval for expected game rewards is:', games.get_CI_game_reward(alpha=0.05))
print('The 95% Confidence Interval for probability loss is:', get_CI_loss_probability(alpha=0.05))

