# Домашнее задание по теме "Простые Юнит-Тесты"

from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner('Вася')
        [runner.walk() for i in range(10)]
        self.assertEqual(runner.distance,  50)

    def test_run(self):
        runner = Runner('Петя')
        [runner.run() for i in range(10)]
        self.assertEqual(runner.distance,  100)

    def test_challenge(self):
        runner = Runner('Саша')
        runner1 = Runner('Петя')
        [(runner.run(), runner1.walk()) for i in range(10)]
        self.assertNotEqual(runner.distance, runner1.distance)


if __name__ == '__main__':
    unittest.main()
