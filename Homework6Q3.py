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
        self._losslist = []

    def simulation(self, n_games,prob_head):
        for n in range(n_games):
            # create a new game
            game = Game(id=n, prob_head=prob_head)
            # simulate the game with 20 flips
            game.simulate(20)
            # store the reward

            self._gameRewards.append(game.get_reward())

        for value in self._gameRewards:
            if value < 0:
                self._lose_count+=1
                i=1
                self._losslist.append(i)
            elif value > 0:
                i=0
                self._losslist.append(i)
        return SetOfGamesOutcomes(self)


    def get_game_rewards(self):
        return self._gameRewards

    def get_loss_list(self):
        return self._losslist

    def get_ave_reward(self):
        """ returns the average reward from all games"""
        return sum(self._gameRewards) / len(self._gameRewards)


class SetOfGamesOutcomes:
    def __init__(self, simulated_cohort):

        self._simCohort = simulated_cohort
        self._sumStat_expectedrewards = Stat.SummaryStat('Game Reward', self._simCohort.get_game_rewards())
        self._sumStat_probabilityloss = Stat.SummaryStat('Probability of Loss', self._simCohort.get_loss_list())


    def get_CI_reward(self, alpha):
        return self._sumStat_expectedrewards.get_t_CI(alpha)


    def get_CI_loss(self,alpha):
        return self._sumStat_probabilityloss.get_t_CI(alpha)


class MultiSetGame:
    def __init__(self,ns_games, probs_head):
        self._ns_games=ns_games
        self._probs_head=probs_head
        self._expectedrewards=[]
        self._meanexpectedRewards=[]
        self._sumStat_meanexpectedRewards=None

    def simulate(self,n_coin_flips):
        for i in range(len(self._ns_games)):
            trial= SetOfGamesGame(self._ns_games[i], self._probs_head[i])
            trial_outcome = trial.simulation()
            self._expectedrewards.append(trial.get_game_rewards())
            self._meanexpectedRewards.append(trial.get_ave_reward())

        self._sumStat_meanexpectedRewards=Stat.SummaryStat('Mean game rewards',self._meanexpectedRewards)

    def get_overall_mean_reward(self):
        return self._meanexpectedRewards.get_mean()

    def get_PI_mean_reward(self,alpha):
        return self._sumStat_meanexpectedRewards.get_PI(alpha)


# run trail of 1000 games to calculate expected reward
games = SetOfGames(prob_head=0.5, n_games=1000)
hw6trial = games.simulation(n_games=1000, prob_head=0.5)

PROB_HEADS=0.05
NUMGAMES=1000
ALPHA=0.05
NUMCOINFLIP=20
GAMBGAMES=10


multigame=MultiSetGame(ns_games=[GAMBGAMES]*NUMGAMES, probs_head=[PROB_HEADS]*NUMGAMES)
multigame.simulate(NUMCOINFLIP)
print('The mean reward the Gambler would get after 10 games is', multigame.get_overall_mean_reward())
print('The 95% Projection Interval for expected game rewards is', multigame.get_PI_mean_reward(alpha=0.05))

# print the average reward
#print('Expected reward when the probability of head is 0.5:', games.get_ave_reward())
#print('The maximum value of rewards is:', games.get_maximum())
#print('The minimum value of rewards is:', games.get_minimum())
#print('The probability of losing is:', games.get_loss_count())


print('The 95% Confidence Interval for expected game rewards is:', hw6trial.get_CI_reward(alpha=0.05))
print('The 95% Confidence Interval for probability loss is:', hw6trial.get_CI_loss(alpha=0.05))

