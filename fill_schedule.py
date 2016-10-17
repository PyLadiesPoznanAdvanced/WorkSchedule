

from person import Person


def fill_the_team_schedules(crew, schedules, no_of_working_days, person_per_day, person_per_night):
    """
    Funkcja wypełnia automatycznie grafik pracy dla teamu zożonego z instancji Person,
    na podstawie ustawionych parametrów.

    crew - załoga
    schedules - lista grafików pracy dla poszczególnych osób z crew
    no_of_working_days - max liczba dyżurów (dni pracujących dla jednej osoby)
    person_per_day - liczba osób pracujących w dzień
    person_per_night - liczba osób pracujących w nocy
    """

    # tworzenie załogi złożonej z instancji Person
    team = [Person(name, schedule) for name, schedule in zip(crew, schedules)]

    # reszta należy do Ciebie. ;-)





if __name__ == '__main__':

    work = ('D', 'N', 'U', '.')     # 'D' - dyżur dzienny, 'N' - dyżur nocny, 'U' - urlop, '.' - dzień wolny

    person_per_day = 3              # liczba osób na dyżurze dziennym
    person_per_night = 2            # liczba osób na dyżurze nocnym
    number_of_working_days = 12     # liczba dyżurów w ciągu miesiąca

    crew = [
        'A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O'
    ]

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
        '..............D.N..............'
    ]

