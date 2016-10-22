

class Person:
    """Klasa Person.
    Klasa służy do tworzenia instancji Person.
    Zawiera metody potrzebne do automatycznego wypełniania grafiku pracy (schedule).
    """

    def __init__(self, name, schedule):
        """Konstruktor klasy Person.

        :param name: nazwisko
        :param schedule: grafik pracy
        """
        self.name = name
        self.schedule = schedule

    def __str__(self):
        return 'Person {}'.format(self.name)

    def is_day_free(self, day_number):
        """Metoda zwraca True jeśli osoba w dniu day_number ma dzień wolny i może wziąć dyżur,
        False jeśli nie może przyjąć dyżuru.

        :param day_number: numer dnia w miesiącu
        :returns: True lub False
        """

    def take_one_day_work(self, day_number, work):
        """Metoda wprowadza zmiany w grafiku (schedule) dla danego dnia i rodzaju dyżuru.

        :param day_number: numer dnia w miesiącu
        :param work: rodzaj dyżuru, dyżur dzienny - "D", dyżur nocnny - "N"
        """

    def get_number_of_working_days(self):
        """Metoda zwraca sumę dyżurów dziennych i nocnych w ciągu miesiąca.

        :returns: return_type - liczba naturalna
        """

    def month_is_full(self, number_of_working_days):
        """Metoda zwraca True jeśli liczba dyżurów w miesiącu jest równa lub większa niż liczba number_of_working_days,
        inaczej zwraca False.

        :param number_of_working_days: maksymalna liczba dyżurów przypadająca na jedną osobę w miesiącu.
        :returns: True lub False
        """

    ####################
    # Zadania dodatkowe:
    ####################

    def if_double_work(self, day_number, work):
        """Metoda zwraca True jeśli dodanie dyżuru dziennego "D" lub nocnego "N"
        spowoduje powstanie dyżuru 24h "ND", inaczej False.

        :param day_number: numer dnia w miesiącu
        :param work: rodzaj dyżuru, dyżur dzienny - "D", dyżur nocnny - "N"
        :returns: True lub False
        """

    def if_week_is_full(self, day_number, no_of_working_days_in_week=4):
        """Metoda zwraca True jeśli po wstawieniu dyżuru w dzień day_number liczba dyżurów
        w ciągu 7 dni po rząd będzie większa niż no_of_working_days_in_week,
        inaczej zwraca False.

        :param day_number: numer dnia w miesiącu
        :param no_of_working_days_in_week: maksymalna liczba dyżurów w ciągu 7 dni pod rząd
        :returns: True lub False
        """
