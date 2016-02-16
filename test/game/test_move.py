from unittest import TestCase
import src.game.Move as gameEval

class TestMove(TestCase):
    def test_moveCreate(self):
        move = gameEval.Move(1)
        self.assertEqual(str(move), "Player 1 makes moves:")

    def test_addMovePoint(self):
        move = gameEval.Move(1)
        move.setMove(1,2,.5)
        ##print(move)
        self.assertEqual(move.distribution[(1,2)],.5)

    def test_normalizeMoves(self):
        move = gameEval.Move(1)
        move.setMove(1,2,.5)
        move.setMove(2,2,1)
        move.normalize()
        print(move)
        self.assertAlmostEqual(move.distribution[(1,2)],.333333,delta=4)
        self.assertAlmostEqual(move.distribution[(2,2)],.666667,delta=4)
        self.assertAlmostEqual(move.distribution[(0,0)],0)

    def test_normalizedEmpty(self):
        move = gameEval.Move(1)
        move.normalize()
        self.assertEqual(move.distribution[(2,0)],0)
