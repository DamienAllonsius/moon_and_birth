import math, datetime


def position(now=None):
    if now is None:
        now = datetime.datetime.now()

    diff = now - datetime.datetime(2001, 1, 1)
    sec_in_day = 86400
    days = diff.days + (diff.seconds / sec_in_day)
    sinodic_month = 29.530589
    # lunations = 0.20439731 + (days / sinodic_month)
    lunations = (days / sinodic_month)

    return lunations


def phase(pos, lang="fr"):
    index = (pos * 8) + 0.5
    index = math.floor(index)
    if lang == "en":
        return {
            0: "New Moon",
            1: "Waxing Crescent",
            2: "First Quarter",
            3: "Waxing Gibbous",
            4: "Full Moon",
            5: "Waning Gibbous",
            6: "Last Quarter",
            7: "Waning Crescent"
        }[int(index) % 8]

    elif lang == "fr":
        return {
            0: "Nouvelle lune",
            1: "Premier croissant",
            2: "Premier quartier",
            3: "Lune gibbeuse croissante",
            4: "Pleine lune",
            5: "Lune gibbeuse décroissante",
            6: "Dernier quartier",
            7: "Dernier croissant"
        }[int(index) % 8]

    else:
        raise NotImplementedError("lang not implemented")


def get_phase_from_date(date, lang):
    return phase(position(date), lang)
