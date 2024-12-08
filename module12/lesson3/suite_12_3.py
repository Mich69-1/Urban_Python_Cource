#  Домашнее задание по теме "Систематизация и пропуск тестов".

import unittest
import module_12_3

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.TournamentTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerST)
