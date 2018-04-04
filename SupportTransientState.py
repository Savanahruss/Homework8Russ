import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat
import Parameters as P

def print_outcomes(multi_cohort, strategy_name):
    reward_mean_PI_text= Format.format_estimate_interval(
        estimate=multi_cohort.get_mean_total_reward(),
        interval=multi_cohort.get_PI_total_reward(alpha=P.ALPHA),deci=1)

    print(strategy_name)
    print("Estimate of mean game reward and {:.{prec}%} prediction interval:".format(1-P.ALPHA, prec=0),
          reward_mean_PI_text)


def print_comparative_outcomes(multi_cohort_unfair_game, multi_cohort_fair_game):

    increase=Stat.DifferenceStatIndp(
        name='Increase in mean game reward',
        x=multi_cohort_unfair_game(),
        y_ref=multi_cohort_fair_game()
    )

    #estimate and CI
    estimate_CI=Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=P.ALPHA),deci=1)

    print("Expected increase in mean game reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA,prec=1),
          estimate_CI)













