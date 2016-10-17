

class Person:
    """Klasa Person"""

    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule

    def __str__(self):
        return 'Person {}'.format(self.name)

    def wheather_day_is_free(self, number):
        """
        Metoda zwraca True jeśli osoba może przyjąć dyżur, False jeśli nie może przyjąć dyżuru IMPORTANT.
        """
        pass

    def take_work(self, day_number, work):
        """
        Metoda wprowadza zmiany w grafiku dla danego dnia i rodzaju dyżuru IMPORTANT.
        """
        pass

    def get_number_of_nights(self):
        """
        Metoda zwraca liczbę dyżurów nocnych w ciągu miesiąca IMPORTANT.
        """
        pass

    def get_number_of_days(self):
        """
        Funkcja zwraca liczbę dyżurów dziennych w ciągu miesiąca IMPORTANT.
        """
        pass

    def get_working_days_number_person(self):
        """
        Metoda zwraca sumę dyżurów dziennych i nocnych w ciągu miesiąca IMPORTANT.
        """
        pass

    #####################
    # Advanced Part below
    #####################

    def filtre_work_days_in_month(self, no_of_working_days):
        """
        Metoda zwraca True jeśli osoba ma mniej lub równą liczbę dyżurów
        w miesiącu do no_of_working_days, inaczej False.
        """
        pass

    def filtre_double_work(self, day_number, work):
        """
        Metoda zwraca False jeśli dodanie dyżuru D lub N spowoduje powstanie dyżuru 24h 'ND', inaczej True
        """
        pass

    def filtre_work_days_in_week(self, no_of_working_days, day_number):
        """
        Metoda zwraca True
        - jeśli wstawiając dyżur w dzień day_number liczba dni roboczych w tygodniu nie przekracza no_of_working_days,
        - inaczej False.
        """
        pass


