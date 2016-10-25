
"""
Poniższy kod został napisany przez uczestników spotkania PyLadies w dniu 24 X 2016.
"""


import person

crew_names = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O',
]

# 'D' - dyżur dzienny
# 'N' - dyżur nocny
# 'U' - urlop
# '.' - dzień wolny

schedules = [
    'D.........UUUUUU..............N',
    '.D...........................N.',
    '..D.........................N..',
    '...D.................UUUUUUN...',
    '....D.....................N....',
    '.....D...................N.....',
    '......D.................N......',
    '.......D...............N.......',
    '........D.............N........',
    'UUU...UUUUUUU........N.........',
    '..........D.........N..........',
    '...........D..UUUUUUUU.........',
    '............D.....N............',
    '.............D...N.............',
    '..............D.N..............',
]

person_per_day = 3  # liczba osób na dyżurze dziennym
person_per_night = 2  # liczba osób na dyżurze nocnym
number_of_working_days = 13  # liczba dyżurów w ciągu miesiąca


def fill_team_schedules(crew_names, schedules, number_of_working_days, person_per_day, person_per_night):
    """Funkcja służąca do automatycznego wypełniania grafuku pracy.

    Funkcja wypełnia automatycznie grafiki pracy (schedule) dla poszczególnych osób z załogi (crew)
    Wszystkie osoby (w postaci instancji Person) należy zebrać w listę (team).
    Wypełnianie grafiku pracy odbywa się na podstawie ustawionych parametrów.

    :param crew_names: załoga
    :param schedules: lista grafików pracy dla poszczególnych osób z crew

    :param number_of_working_days: maksymalna liczba dni pracujących w miesiącu dla jednej osoby
    :param person_per_day: - liczba osób pracujących w dzień
    :param person_per_night: - liczba osób pracujących w nocy
    """

    # tworzenie drużyny złożonej z instancji Person
    team = [person.Person(name, schedule) for name, schedule in zip(crew_names, schedules)]

    # TODO poniżej Twoje rozwiązanie

    for day_nr in range(31):
        while find_cnt_day_shifts(team, day_nr) < person_per_day:
            for person_ in team:
                if person_.is_day_free and not person_.month_is_full(number_of_working_days):
                    person_.take_one_day_work(day_nr, 'D')

        while find_cnt_night_shifts(team, day_nr) < person_per_night:
            for person_ in team:
                if person_.is_day_free and not person_.month_is_full(number_of_working_days):
                    person_.take_one_day_work(day_nr, 'N')


def find_cnt_day_shifts(team, day_number):
    day_worked = 0
    for person_ in team:
        if person_.schedule[day_number] == 'D':
            day_worked += 1
    return day_worked


def find_cnt_night_shifts(team, day_number):
    night_worked = 0
    for person_ in team:
        if person_.schedule[day_number] == 'N':
            night_worked += 1
    return night_worked


if __name__ == "__main__":
    fill_team_schedules(crew_names, schedules, number_of_working_days, person_per_day, person_per_night)
