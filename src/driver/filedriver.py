"""f = open("pe.txt", "r")
for i in f:
    print("{}".format(i.replace(",", ".")[0:-1]), end=",")"""


class FileDriver:
    def reform_line(self, line: str, before=",", after="."):
        return line.replace(before, after).replace("\n", "")

    def read(self, location: str):
        f = open(location, "r")
        lines = f.readlines()
        f.close()
        for index, value in enumerate(lines):
            lines[index] = self.reform_line(value)
        return lines

    def write(self, location, value_list: list):
        value_list = [str(value) for value in value_list]
        f = open(location, "w")
        for line in value_list:
            f.write(self.reform_line(line=line, before=".", after=",")+"\n")
        f.close()


def main():
    a = FileDriver()
    l = a.read("src/data/pe.txt")
    for i in l:
        print(i, end="")


if __name__ == "__main__":
    main()
