from main.Table import Table


class Main:
    def __init__(self):
        self.tables = []
        self.file = None

    def load(self, filePath):
        self.file = open(filePath, "r")

    def process(self):
        l = self.file.readlines()
        tableCount = 0
        for i_index in range(len(l)):
            line = l[i_index]
            if line.splitlines() == ["START_TABLE"]:
                # New Table
                previousLine = l[i_index - 1].splitlines()[0]
                self.tables.append(Table(previousLine))
                # Add the lines to the table
                for j_index in range(i_index, len(l)):
                    if l[j_index] == "\n":
                        break

                    self.tables[tableCount].append(l[j_index].split("\n")[0])
                    if l[j_index].splitlines() == ["END_TABLE"]:
                        break
                # Prepare the Next Table
                tableCount += 1
        self.file.close()

    def exportText(self, title):
        self.process()
        outputFile = open("../output/output.csv", "w")
        for table in self.tables:
            if title == table.content[0]:
                for line in table.content:
                    outputFile.write(line)
                    outputFile.write("\n")
