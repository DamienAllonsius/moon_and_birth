"""
compute P(data | H_0) where H_0 is : moon has no effect on date of birth
"""

from extract_data import get_moon_phases_number_births
from matplotlib import pyplot as plt
from scipy import stats


def plot_birth(moon_phases):
    x = list(moon_phases.keys())
    y = list(moon_phases.values())

    plt.bar(x, y)
    plt.ylim([min(y)*0.95, max(y)*1.05])
    plt.title(f"phases of the moon on the birth dates of {sum(y)} French citizens from 1968 to 2018 (source: INSEE) ")
    plt.savefig("moon_phases.png")
    plt.show()


if __name__ == "__main__":
    lang = "fr"
    moon_phases = get_moon_phases_number_births("naissances_clean_2.csv", lang)
    if lang == "en":
        fm = "Full Moon"
    elif lang == "fr":
        fm = "Pleine lune"
    else:
        raise NotImplementedError()
    # H0 : the moon has no effect on birth rate
    proba_full_moon_H0 = 1 / 8
    total_births = sum(list(moon_phases.values()))
    expected = total_births * proba_full_moon_H0
    full_moon = moon_phases[fm]
    print(f"total births {total_births}")

    print(f"full moon : {full_moon} & expected : {expected} & diff : {abs(full_moon - expected)}")
    print(f"")
    p_value = 1-stats.binom.cdf(full_moon, total_births, proba_full_moon_H0)

    limit = 0.01
    if p_value < limit:
        print(f"p-value: {p_value} => H0 rejected")
    else:
        print(f"p-value: {p_value} => H0 not rejected")

    print(moon_phases)
    plot_birth(moon_phases)
