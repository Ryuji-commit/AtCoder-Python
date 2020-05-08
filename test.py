class Hello:
    def __init__(self):
        self.word = 'hello'

    def add(self):
        self.word += 'world'


if __name__ == '__main__':
    s = Hello()
    s.add()
    print(s.word)


