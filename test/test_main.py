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
        self.assertEqual(len(main.tables[0].content), 5)
        self.assertEqual(len(main.tables[1].content), 10)
        self.assertEqual(len(main.tables[2].content), 4)

    def test_createOutputFileWithTablesWithSpecificTitle(self):
        # given
        main = Main()
        main.file = open("result.csv")
        # when
        main.exportText("TableB")
        # then
        f = open("../output/output.csv")
        self.assertEqual(len(f.readlines()), 10)




if __name__ == '__main__':
    unittest.main()
