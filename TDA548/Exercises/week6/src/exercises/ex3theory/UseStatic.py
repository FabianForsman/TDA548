# package exercises.ex3theory

# If you uncomment lines below, what errors will you get? Explain, in depth!
class UseStatic:
    i = 0

    def __init__(self):
        self.j = 0

    def do_it(self):
        print(self.j)
        # print(self.i)
        # self.do_other()

    @staticmethod
    def do_other():
        print(UseStatic.i)
        # print(UseStatic.j)
        # UseStatic.do_it()


if __name__ == "__main__":
    # UseStatic.do_it()
    UseStatic.do_other()
