import unittest as ut
import captalize as cap
class TestCap(ut.TestCase):
    def test_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Monty Python')
if __name__ == '__main__':
    ut.main()