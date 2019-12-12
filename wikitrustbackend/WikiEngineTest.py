import unittest
from WikiEngine import WikiEngine

class testWikiEngine(unittest.TestCase):
    
    def test_revisions_ids(self):
        w = WikiEngine()
        test_output = w.get_revision_ids("Stomach", 2)
        self.assertEquals(len(test_output), 2, "It should output 2 revisions")
        self.assertEquals(len(set(test_output)), 2, "It should be two different ids")

        test_output = w.get_revision_ids("Stomach", 4)
        self.assertEquals(len(test_output), 4, "It should output 4 revisions")
    
    def test_get_revision_text(self):
        w = WikiEngine()
        self.assertGreater(len(w.get_revision_text(927069159)), 1, "It should ouput text from Revision")
        



if __name__ == '__main__':
    unittest.main()