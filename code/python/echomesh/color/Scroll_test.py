from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.color.Scroll import scroll

from echomesh.util.TestCase import TestCase

class ScrollTest(TestCase):
  def setUp(self):
    self.data = ['red', 'green', 'blue', 'yellow', 'beige', 'khaki',
                 'olive', 'tan', 'plum', 'teal', 'wheat', 'orchid', ]

  def doTest(self, dx, dy, expected):
    self.assertEquals(scroll(self.data, dx, dy, 4, empty='black'), expected)

  def test_empty(self):
    self.doTest(0, 0, self.data)

  def test_one_right(self):
    self.doTest(1, 0, ['black', 'red', 'green', 'blue', 'black', 'beige',
                       'khaki', 'olive', 'black', 'plum', 'teal', 'wheat', ])

  def test_three_right(self):
    self.doTest(3, 0, ['black', 'black', 'black', 'red', 'black', 'black',
                       'black', 'beige', 'black', 'black', 'black', 'plum', ])

  def test_four_right(self):
    self.doTest(4, 0, ['black', 'black', 'black', 'black', 'black', 'black',
                       'black', 'black', 'black', 'black', 'black', 'black', ])

  def test_five_right(self):
    self.doTest(5, 0, ['black', 'black', 'black', 'black', 'black', 'black',
                       'black', 'black', 'black', 'black', 'black', 'black', ])

  def test_one_left(self):
    self.doTest(-1, 0, ['green', 'blue', 'yellow', 'black', 'khaki', 'olive',
                        'tan', 'black', 'teal', 'wheat', 'orchid', 'black', ])

  def test_three_left(self):
    self.doTest(-3, 0, ['yellow', 'black', 'black', 'black', 'tan', 'black',
                        'black', 'black', 'orchid', 'black', 'black', 'black', ])

  def test_four_left(self):
    self.doTest(-4, 0, ['black', 'black', 'black', 'black', 'black', 'black',
                        'black', 'black', 'black', 'black', 'black', 'black', ])

  def test_five_left(self):
    self.doTest(-5, 0, ['black', 'black', 'black', 'black', 'black', 'black',
                        'black', 'black', 'black', 'black', 'black', 'black', ])

  def test_one_down(self):
    self.doTest(0, 1, ['black', 'black', 'black', 'black', 'red', 'green',
                       'blue', 'yellow', 'beige', 'khaki', 'olive', 'tan', ])

  def test_two_down(self):
    self.doTest(0, 2, ['black', 'black', 'black', 'black', 'black', 'black',
                       'black', 'black', 'red', 'green', 'blue', 'yellow', ])

  def test_three_down(self):
    self.doTest(0, 3, ['black', 'black', 'black', 'black', 'black', 'black',
                       'black', 'black', 'black', 'black', 'black', 'black', ])

  def test_four_down(self):
    self.doTest(0, 4, ['black', 'black', 'black', 'black', 'black', 'black',
                       'black', 'black', 'black', 'black', 'black', 'black', ])

  def test_one_up(self):
    self.doTest(0, -1, ['beige', 'khaki', 'olive', 'tan', 'plum', 'teal',
                        'wheat', 'orchid', 'black', 'black', 'black', 'black', ])

  def test_two_up(self):
    self.doTest(0, -2, ['plum', 'teal', 'wheat', 'orchid', 'black', 'black',
                        'black', 'black', 'black', 'black', 'black', 'black', ])

  def test_three_up(self):
    self.doTest(0, -3, ['black', 'black', 'black', 'black', 'black', 'black',
                        'black', 'black', 'black', 'black', 'black', 'black', ])

  def test_four_up(self):
    self.doTest(0, -4, ['black', 'black', 'black', 'black', 'black', 'black',
                        'black', 'black', 'black', 'black', 'black', 'black', ])

  def test_down_right(self):
    self.doTest(1, 1, ['black', 'black', 'black', 'black', 'black', 'red',
                       'green', 'blue', 'black', 'beige', 'khaki', 'olive', ])

  def test_up_left(self):
    self.doTest(-1, -1, ['khaki', 'olive', 'tan', 'black', 'teal', 'wheat',
                         'orchid', 'black', 'black', 'black', 'black', 'black', ])

