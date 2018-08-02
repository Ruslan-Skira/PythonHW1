class Colors:
    def __init__(self, colors):
        self.colors = colors

    def __iter__(self):
        i = 0
        while True:
            yield self.colors(i)
            i += 1
            if i == len(self.colors):
                i = 0