import unittest
import cap
class test(unittest.TestCase):
    def test_one_word(self):
        text='python'
        result=cap.cap_txt(text)
        self.assertEqual(result, 'Python')
    def test_multi_word(self):
        text='monty python'
        result=cap.cap_txt(text)
        self.assertEqual(result, 'Monty Python')

if __name__=='__main__':
    unittest.main()