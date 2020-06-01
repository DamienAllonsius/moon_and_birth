import math, datetime


def position(now=None):
    if now is None:
        now = datetime.datetime.now()

    diff = now - datetime.datetime(1962, 2, 5, 00, 10, 00)
    sec_in_day = 86400
    days = diff.days + (diff.seconds / sec_in_day)
    sinodic_month = 29.530588853
    lunations =  (days % sinodic_month)

    return lunations


def phase(pos):
    sixteenth = 29.530588853 / 16
    if pos <= sixteenth:
        return "New Moon"
    elif pos <= sixteenth * 3:
        return "Waxing Crescent"
    elif pos <= sixteenth * 5:
        return "First Quarter"
    elif pos <= sixteenth * 7: 
        return "Waxing Gibbous"
    elif pos <= sixteenth * 9: 
        return "Full Moon"
    elif pos <= sixteenth * 11: 
        return "Waning Gibbous"
    elif pos <= sixteenth * 13: 
        return "Last Quarter"
    elif pos <= sixteenth * 15: 
        return "Waning Crescent"
    else:
        return "New Moon"

def get_phase_from_date(date):
    return phase(position(date))
