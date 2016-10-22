import person


crew = [
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

person_per_day = 3           # liczba osób na dyżurze dziennym
person_per_night = 2         # liczba osób na dyżurze nocnym
number_of_working_days = 13  # liczba dyżurów w ciągu miesiąca


def fill_team_schedules(crew, schedules, number_of_working_days, person_per_day, person_per_night):
    """Funkcja służąca do automatycznego wypełniania grafuku pracy.

    Funkcja wypełnia automatycznie grafiki pracy (schedule) dla poszczególnych osób z załogi (crew)
    Wszystkie osoby (w postaci instancji Person) należy zebrać w listę (team).
    Wypełnianie grafiku pracy odbywa się na podstawie ustawionych parametrów.

    :param crew: załoga
    :param schedules: lista grafików pracy dla poszczególnych osób z crew

    :param number_of_working_days: maksymalna liczba dni pracujących w miesiącu dla jednej osoby
    :param person_per_day: - liczba osób pracujących w dzień
    :param person_per_night: - liczba osób pracujących w nocy
    """

    # tworzenie drużyny złożonej z instancji Person
    team = [person.Person(name, schedule) for name, schedule in zip(crew, schedules)]

    # TODO poniżej Twoje rozwiązanie




if __name__ == "__main__":
    fill_team_schedules(crew, schedules, number_of_working_days, person_per_day, person_per_night)
