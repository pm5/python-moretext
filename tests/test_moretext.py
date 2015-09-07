
import unittest
import moretext

class TestMoreText(unittest.TestCase):

    def testSentences(self):
        sentences = moretext.sentences()
        self.assertIsNotNone(sentences['sentences'])

if __name__ == '__main__':
    unittest.main()
