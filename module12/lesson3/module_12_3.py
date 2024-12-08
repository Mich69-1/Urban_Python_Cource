# Домашнее задание по теме "Методы Юнит-тестирования"

from runner_and_tournament import Runner
from runner_and_tournament import Tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frosen = False

    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Вася')
        [runner.walk() for i in range(10)]
        self.assertEqual(runner.distance,  50)

    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Петя')
        [runner.run() for i in range(10)]
        self.assertEqual(runner.distance,  100)

    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner = Runner('Саша')
        runner1 = Runner('Петя')
        [(runner.run(), runner1.walk()) for i in range(10)]
        self.assertNotEqual(runner.distance, runner1.distance)


class TournamentTest(unittest.TestCase):
    is_frosen = True

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def test_first(self):
        tour1 = Tournament(90, self.runner1, self.runner3)
        TournamentTest.all_results.append({k: v.name for k, v in tour1.start().items()})
        self.assertTrue(TournamentTest.all_results[-1][2] == 'Ник')
        print('test_first')

    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def test_second(self):
        tour2 = Tournament(90, self.runner2, self.runner3)
        TournamentTest.all_results.append({k: v.name for k, v in tour2.start().items()})
        self.assertTrue(TournamentTest.all_results[-1][2] == 'Ник')
        print('test_second')

    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def test_third(self):
        tour3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        TournamentTest.all_results.append({k: v.name for k, v in tour3.start().items()})
        self.assertTrue(TournamentTest.all_results[-1][3] == 'Ник')
        print('test_third')

    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def test_fourth(self):
        tour4 = Tournament(90, self.runner2, self.runner1, self.runner3)
        TournamentTest.all_results.append({k: v.name for k, v in tour4.start().items()})
        self.assertTrue(TournamentTest.all_results[-1][3] == 'Ник')
        self.assertTrue(TournamentTest.all_results[-1][1] == 'Усэйн')
        print('test_fourth')

    @classmethod
    def tearDownClass(cls):
        for i in TournamentTest.all_results:
            print(i)


if __name__ == '__main__':
    unittest.main()
