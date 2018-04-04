import Parameters as P
import Homework6 as TS
import SupportTransientState as Support

multiFairGame = TS.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS),
    n_games_in_a_set=P.TIME_STEPS,
    prob_head=P.LOSS_PROB
)

multiplefair = multiFairGame.simulation()

multiUnfairGame = TS.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS,2*P.NUM_SIM_COHORTS),
    n_games_in_a_set=P.TIME_STEPS,
    prob_head=P.UNFAIR_LOSS_PROB
)

multipleunfair = multiUnfairGame.simulation()

#print outcomes of each cohort
Support.print_outcomes(multiFairGame,'When probability of heads is 0.5')
Support.print_outcomes(multiUnfairGame,'When probability of heads is 0.45')


#print comparative outcomes
Support.print_comparative_outcomes(multiUnfairGame, multiFairGame)
