import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat
import Parameters as P

def print_outcomes(sim_output, strategy_name):

    rewards_mean_CI_text=Format.format_estimate_interval(
        estimate=sim_output.get_ave_reward(),
        interval=sim_output.get_CI_reward(alpha=P.ALPHA),
        deci=1
    )

    print(strategy_name)
    print("Estimate of mean game rewards and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          rewards_mean_CI_text)


def print_comparative_outcomes(sim_output_fair_game,sim_output_unfair_game):
    increase=Stat.DifferenceStatIndp(
        name='Increase in game rewards',
        x=sim_output_unfair_game(),
        y_ref=sim_output_fair_game()
    )

    estimate_CI=Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=P.ALPHA),deci=1)

    print("Average increase in game rewards and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)


