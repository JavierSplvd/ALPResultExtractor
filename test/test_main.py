import unittest

from main.Main import Main


class TestMain(unittest.TestCase):
    def test_loadFile(self):
        # given
        filePath = "result.csv"
        # when
        main = Main()
        main.load(filePath)
        # then
        self.assertNotEqual(main.file, None)

    def test_createTableObjects(self):
        # given
        main = Main()
        main.file = open("result.csv")
        # when
        main.process()
        # then
        self.assertNotEqual(main.tables, None)
        self.assertEqual(len(main.tables), 3)
        self.assertEqual(len(main.tables[0].content), 4)
        self.assertEqual(len(main.tables[1].content), 9)
        self.assertEqual(len(main.tables[2].content), 3)

    def test_createOutputFileWithTables(self):
        pass


if __name__ == '__main__':
    unittest.main()
