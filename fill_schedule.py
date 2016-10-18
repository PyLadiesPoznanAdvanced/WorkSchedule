from person import Person


"""
Witamy ;-)

Przed Tobą zaawansowane zadanie PyLadies.
Masz do przygotowania skrypt umożliwiający automatyczne wypełnienie grafiku pracy zespołu wedłóg zadanych parametrów.

A teraz do rzeczy:
1)
Masz do dyspozycji drużynę pracowników zebranych w postaci listy crew (patrz poniżej).
Dla uproszczenia sytuacji 'pracownicy' to po prostu osoby oznaczone literami od 'A' do 'O'. W sumie 15 osób.

2)
Nasz zespół pracuje na dwie zmiany po 12h przez cały miesiąc. Weekendy też pracujące (sic!)

Możliwości zapisu dnia w grafiku:
'D' - dyżur w dzień
'N' - dyżur w nocy
'U' - dzień urlopowy
'.' - dzień wolny od pracy

Przed każdym miesiącem pracy, pracownicy mają możliwość zdecydowania w jakie dni biorą urlop ('U').
Dodatkowo każda osoba może mieć prośbę do osoby układającej grafik pracy,
że chciałaby mieć np: dyżur nocny ('N') np. 5 dnia miesiąca, a dyżur dzienny ('D') 14 dnia miesiąca itp.

Lista schedules zawiera grafiki pracy dla poszczególnych osób.
Grafiki te zawierają urlopy oraz prośby dyżurów w konkretne dni.

Pierwszej osobie z listy crew odpowiada pierwszy grafik z listy schedules itd.
Przykładowy grafik na 31 dni w miesiącu:
osoba A --> grafik 'D.........UUUUUU..............N',
osoba B --> grafik '.D...........................N.',

3)
Nadszedł czas na zadanie.

Skrypt, który trzeba napisać powinien samodzielnie wypełniać brakujące dyżury w grafiku pracy
wedłóg zadanych parametrów / wymagań, i to właśnie wymagania są kluczową sprawą !

Wymagania:
- każdego dnia powinny być 3 osoby na dyżurze dziennym i 2 osoby na dyżurze nocnym

- liczba dyżurów dla pojedynczej osoby w całym miesiącu --> maksymalnie 13

- liczba dyżurów dziennych i nocnych dla jednej osoby - bez znaczenia.
  Dopuszcza się sytuację w której jedna osoby ma tylko dyżuru dzienne, a inna tylko nocne.

    #####################
    # Advanced Part below
    #####################

- liczba dyżurów dla pojedynczej osoby w ciągu 7 dni pod rząd wynosi maksymalnie 4 dyżuru.

- jedna osoba nie może pełnić dyżuru przez 24 h pod rząd.
  W naszym grafiku oznacza to, że nie może wystąpić dyżur dzienny po nocnym.
  Zatem w grafiku dla pojedynczej osoby nie może wystąpić 'ND'.
  'DN' w grafiku jest dopuszczalne.

    #####################

Przykładowy grafik po wypełnieniu automatycznym z takimi wymaganiami:

osoba       grafik
A   D.D...N..NUUUUUUNNN.D..D..D.D.N
B   .DN..D..D..D..D..D.D..D..D..DN.
C   ..DN.D..D..N..N.D..D..D..D..N.D
D   ..DD.D..D..N.D..D..D.UUUUUUNNNN
E   ..N.DN.D..D..D..D..D.D...DN.D..
F   .D...DN.N.D..D..D.D..D..DN.D...
G   .D..D.DD..D.D..D..D.D...N.N.D..
H   .D..D..DN.N.D..D..D.D..N.D.D...
I   .N..D..DD.N.D..D.D..D.N.D..D...
J   UUUNNNUUUUUUUNNN.D..NN.DD..D..D
K   D...N..N.DD.N.D..D..N.D.D..N..D
L   NN.D...N.D.DN.UUUUUUUUNNNN...DD
M   D..D..D..D..DN.D..NN.D.D..D..D.
N   D..D..D..D.D.DD..N.N.DD...D..D.
O   N.D...D..N.D..DNN.D..N.D..D..D.

Powodzenia.
"""

crew = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O'
]

work = ('D', 'N', 'U', '.')  # 'D' - dyżur dzienny, 'N' - dyżur nocny, 'U' - urlop, '.' - dzień wolny

person_per_day = 3  # liczba osób na dyżurze dziennym
person_per_night = 2  # liczba osób na dyżurze nocnym
number_of_working_days = 13  # liczba dyżurów w ciągu miesiąca

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


def fill_the_team_schedules(crew, schedules, number_of_working_days, person_per_day, person_per_night):
    """
    Funkcja wypełnia automatycznie grafik pracy dla teamu zożonego z instancji Person,
    na podstawie ustawionych parametrów.

    crew - załoga
    schedules - lista grafików pracy dla poszczególnych osób z crew
    no_of_working_days - max liczba dyżurów (dni pracujących dla jednej osoby --> 13)
    person_per_day - liczba osób pracujących w dzień --> 3
    person_per_night - liczba osób pracujących w nocy --> 2
    """

    # tworzenie załogi złożonej z instancji Person
    team = [Person(name, schedule) for name, schedule in zip(crew, schedules)]

    # reszta należy do Ciebie. ;-)






