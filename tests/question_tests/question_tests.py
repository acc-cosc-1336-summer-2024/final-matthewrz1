#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_c.question_c import lowest_num
from src.question_c.question_c import highest_num
from src.question_c.question_c import total
from src.question_c.question_c import average

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())
    
    def test_question_c_config(self):
        a = [5,10,15,-10,1]
        self.assertEqual(-10, lowest_num(a))
        self.assertEqual(15,highest_num(a))
        self.assertEqual(21,total(a))
        self.assertEqual(4.2,average(a))



