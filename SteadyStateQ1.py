import SupportSteadyState as Support
import Homework6 as SS
import Parameters as P

fairgame = SS.SetOfGames(
    id=1,
    prob_head=P.LOSS_PROB,
    n_games=P.TIME_STEPS
)

#Simulate the fair outcome
Fair_Game = fairgame.simulation()

unfairgame = SS.SetOfGames(
    id=2,
    prob_head=P.UNFAIR_LOSS_PROB,
    n_games=P.TIME_STEPS
)

#Simulate the unfair outcome
Unfair_Game = unfairgame.simulation()

#print the outcomes
Support.print_outcomes(Fair_Game,'When there is a 50% probability of heads')
Support.print_outcomes(Unfair_Game,'When there is a 45% probability of heads')

#print comparative outcomes
Support.print_comparative_outcomes(Fair_Game,Unfair_Game)