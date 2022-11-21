import random
from datetime import datetime, timedelta

def get_gregorian_start_date():
    """I know this isn't the start of the Gregorian calendar. I don't really
    care though."""
    return datetime.fromisoformat("1600-01-01")

def get_random_date():
    """Return a random date to guess."""
    return get_gregorian_start_date() + timedelta(days=random.randint(0, 500000))

def get_day_of_week_str_from_datetime(dt):
    """Given a datetime object, return the day of the week."""
    return dt.strftime("%A")

def is_correct_answer(dt, guess):
    """Given a guess, return True if the guess was correct, False otherwise."""
    valid_answers = {
        "Saturday": ["Sat", "Saturday", "0", "7"],
        "Sunday": ["Sun", "Sunday", "1"],
        "Monday": ["Mon", "Monday", "2"],
        "Tuesday": ["Tue", "Tuesday", "3"],
        "Wednesday": ["Wed", "Wednesday", "4"],
        "Thursday": ["Thu", "Thursday", "5"],
        "Friday": ["Fri", "Friday", "6"],
    }

    return guess in valid_answers[get_day_of_week_str_from_datetime(dt)]

for i in range(10):
    random_date = get_random_date()
    guess = input(random_date)
    print(is_correct_answer(random_date, guess))
