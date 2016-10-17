
import unittest
from person import Person


class PersonTests(unittest.TestCase):
    """
    Test for methods of Person model.
    """
    def setUp(self):
        self.person = Person(name='name', schedule='...DDD...NNN...DDD...NNN...DDD')

    def test_get_working_days_number_person(self):
        """Test for method get_working_days_number_person for Person object."""

        self.assertEqual(self.person.get_working_days_number_person(), 15)

    def test_get_number_of_nights(self):
        """Test for method get_number_of_nights for Person object."""

        self.assertEqual(self.person.get_number_of_nights(), 6)

    def test_get_number_of_days(self):
        """Test for method get_number_of_days for Person object."""

        self.assertEqual(self.person.get_number_of_days(), 9)

    def test_wheather_day_is_free(self):
        """Test for method wheather_day_is_free for Person object."""

        self.assertEqual(self.person.wheather_day_is_free(2), True)
        self.assertEqual(self.person.wheather_day_is_free(3), False)

    def test_take_work(self):
        """Test for method take_work for Person object."""

        person = Person(name='name', schedule='...DDD...NNN...DDD...NNN...DDD')
        person.take_work(0, 'N')
        person.take_work(7, 'D')
        self.assertEqual(person.schedule, 'N..DDD.D.NNN...DDD...NNN...DDD')

    def test_filtre_work_days_in_month(self):
        """Test for method filtre_work_days_in_month for Person object."""

        self.assertEqual(self.person.filtre_work_days_in_month(15), True)
        self.assertEqual(self.person.filtre_work_days_in_month(14), False)

    def test_filtre_double_work(self):
        """Test for method filtre_double_work for Person object."""

        person = Person(name='name', schedule='.D............................')
        self.assertEqual(person.filtre_double_work(0, 'N'), False)
        self.assertEqual(person.filtre_double_work(0, 'D'), True)

        person = Person(name='name', schedule='.N............................')
        self.assertEqual(person.filtre_double_work(0, 'N'), True)
        self.assertEqual(person.filtre_double_work(0, 'D'), True)

        person = Person(name='name', schedule='D.............................')
        self.assertEqual(person.filtre_double_work(1, 'N'), True)
        self.assertEqual(person.filtre_double_work(1, 'D'), True)

        person = Person(name='name', schedule='N.............................')
        self.assertEqual(person.filtre_double_work(1, 'N'), True)
        self.assertEqual(person.filtre_double_work(1, 'D'), False)

        person = Person(name='name', schedule='............D.................')
        self.assertEqual(person.filtre_double_work(11, 'D'), True)
        self.assertEqual(person.filtre_double_work(11, 'N'), False)

        person = Person(name='name', schedule='............N.................')
        self.assertEqual(person.filtre_double_work(13, 'D'), False)
        self.assertEqual(person.filtre_double_work(13, 'N'), True)

    def test_filtre_work_days_in_week(self):
        """Test for method filtre_work_days_in_week for Person object."""

        self.assertEqual(self.person.filtre_work_days_in_week(4, 6), True)
        self.assertEqual(self.person.filtre_work_days_in_week(4, 9), True)

        person = Person(name='name', schedule='.N.DDD.D.NNN...DDD...NNN...DDD')
        self.assertEqual(person.filtre_work_days_in_week(4, 8), False)
        self.assertEqual(person.filtre_work_days_in_week(4, 10), False)


if __name__ == '__main__':
    unittest.main()



