# Домашнее задание по теме "Логирование"

from rt_with_exceptions import Runner
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log", encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('Аполлинарий', speed=-5)
            [runner.walk() for i in range(10)]
            self.assertEqual(runner.distance,  50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(33, speed=10)
            [runner.run() for i in range(10)]
            self.assertEqual(runner.distance,  100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")


if __name__ == '__main__':
    unittest.main()
