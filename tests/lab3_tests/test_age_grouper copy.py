import unittest
from age_grouper import AgeGrouper

class TestAgeGrouper(unittest.TestCase):
    def test_group_basic(self):
        bounds = [18, 25, 35, 45, 60, 80, 100]
        grouper = AgeGrouper(bounds)
        people = [
            ("Кошельков Захар Брониславович", 105),
            ("Дьячков Нисон Иринеевич", 88),
            ("Иванов Варлам Якунович", 88),
            ("Старостин Ростислав Ермолаевич", 50),
            ("Ярилова Розалия Трофимовна", 29),
            ("Соколов Андрей Сергеевич", 15),
            ("Егоров Алан Петрович", 7),
        ]
        grouped = grouper.group(people)
        expected = [
            ("101+", [("Кошельков Захар Брониславович", 105)]),
            ("81-100", [("Дьячков Нисон Иринеевич", 88), ("Иванов Варлам Якунович", 88)]),
            ("46-60", [("Старостин Ростислав Ермолаевич", 50)]),
            ("26-35", [("Ярилова Розалия Трофимовна", 29)]),
            ("0-18", [("Соколов Андрей Сергеевич", 15), ("Егоров Алан Петрович", 7)]),
        ]
        self.assertEqual(len(grouped), len(expected))
        for i, (label, members) in enumerate(grouped):
            self.assertEqual(label, expected[i][0])
            self.assertEqual(members, expected[i][1])

    def test_empty_people(self):
        bounds = [18, 25]
        grouper = AgeGrouper(bounds)
        grouped = grouper.group([])
        self.assertEqual(grouped, [])

    def test_all_in_one_group(self):
        bounds = [100]
        grouper = AgeGrouper(bounds)
        people = [("A", 20), ("B", 30)]
        grouped = grouper.group(people)
        self.assertEqual(len(grouped), 2)
        self.assertEqual(grouped[0][0], "0-100")
        self.assertEqual(grouped[0][1], [("B", 30), ("A", 20)])
        self.assertEqual(grouped[1][0], "101+")
        self.assertEqual(grouped[1][1], [])

    def test_sorting_by_age_desc_and_name_asc(self):
        bounds = [50]
        grouper = AgeGrouper(bounds)
        people = [("Ivanov", 30), ("Petrov", 30), ("Sidorov", 25)]
        grouped = grouper.group(people)
        self.assertEqual(grouped[0][1], [("Ivanov", 30), ("Petrov", 30), ("Sidorov", 25)])