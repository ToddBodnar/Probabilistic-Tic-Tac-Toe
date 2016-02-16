from unittest import TestCase
import src.game.game_evaluator as evaluator
import src.game.Move as move


class TestTestFixed(TestCase):
    def test_empty(self):
        scores = evaluator.testFixed(dict())
        self.assertEqual(scores,-1)

    def test_draw(self):
        placements = dict()
        placements[(0,0)] = 1
        placements[(0,1)] = 2
        placements[(0,2)] = 1

        placements[(1,0)] = 1
        placements[(1,1)] = 2
        placements[(1,2)] = 1

        placements[(2,0)] = 2
        placements[(2,1)] = 1
        placements[(2,2)] = 2

        self.assertEqual(evaluator.testFixed(placements),-1)


    def test_horizontal(self):
        placements = dict()
        placements[(1,0)] = 1
        placements[(0,0)] = 1
        placements[(2,0)] = 1
        self.assertEqual(evaluator.testFixed(placements),1)
        placements = dict()
        placements[(1,2)] = 2
        placements[(0,2)] = 2
        placements[(2,2)] = 2
        self.assertEqual(evaluator.testFixed(placements),2)

    def test_vertical(self):
        placements = dict()
        placements[(0,1)] = 1
        placements[(0,0)] = 1
        placements[(0,2)] = 1
        self.assertEqual(evaluator.testFixed(placements),1)
        placements = dict()
        placements[(2,1)] = 2
        placements[(2,0)] = 2
        placements[(2,2)] = 2
        self.assertEqual(evaluator.testFixed(placements),2)

    def test_diagonal(self):
        placements = dict()
        placements[(0,0)] = 1
        placements[(1,1)] = 1
        placements[(2,2)] = 1
        self.assertEqual(evaluator.testFixed(placements),1)
        placements = dict()
        placements[(0,2)] = 2
        placements[(1,1)] = 2
        placements[(2,0)] = 2
        self.assertEqual(evaluator.testFixed(placements),2)

class TestEvaluator(TestCase):
    def testNoMoves(self):
        points = evaluator.evaluate()
        self.assertEqual(points[-1],1)
        self.assertEqual(points[1],0)
        self.assertEqual(points[2],0)

    def testDeterministicGameWin(self):
        moves = []
        moves += [(move.Move(1))]
        moves += [(move.Move(2))]
        moves += [(move.Move(1))]
        moves += [(move.Move(2))]
        moves += [(move.Move(1))]

        moves[0].setMove(0,0,1)
        moves[1].setMove(1,0,1)
        moves[2].setMove(0,1,1)
        moves[3].setMove(1,1,1)
        moves[4].setMove(0,2,1)

        for m in moves:
            m.normalize()

        points = evaluator.evaluate(moves)

        self.assertEqual(points[-1],0)
        self.assertEqual(points[1],1)
        self.assertEqual(points[2],0)

    def testDeterministicNoComplete(self):
        moves = []
        moves += [(move.Move(1))]
        moves += [(move.Move(2))]
        moves += [(move.Move(1))]
        moves += [(move.Move(2))]

        moves[0].setMove(0,0,1)
        moves[1].setMove(1,0,1)
        moves[2].setMove(0,1,1)
        moves[3].setMove(1,1,1)

        for m in moves:
            m.normalize()

        points = evaluator.evaluate(moves)

        self.assertEqual(points[-1],1)
        self.assertEqual(points[1],0)
        self.assertEqual(points[2],0)

    def testDeterministicTie(self):
        moves = []
        moves += [(move.Move(1))]
        moves += [(move.Move(2))]
        moves += [(move.Move(1))]
        moves += [(move.Move(2))]
        moves += [(move.Move(1))]
        moves += [(move.Move(2))]
        moves += [(move.Move(1))]
        moves += [(move.Move(2))]
        moves += [(move.Move(1))]

        moves[0].setMove(0,0,1)
        moves[1].setMove(1,0,1)
        moves[2].setMove(2,0,1)
        moves[0].setMove(0,1,1)
        moves[1].setMove(1,1,1)
        moves[2].setMove(2,1,1)
        moves[0].setMove(0,2,1)
        moves[1].setMove(1,2,1)
        moves[2].setMove(2,2,1)

        for m in moves:
            m.normalize()

        points = evaluator.evaluate(moves)

        self.assertEqual(points[-1],1)
        self.assertEqual(points[1],0)
        self.assertEqual(points[2],0)

    def testNondeterministicStraightGameWin(self):
        self.fail()

    def testNondeterministicNoCompletions(self):
        self.fail()

    def testNondeterministicParitalWin(self):
        self.fail()
