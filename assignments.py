class MaxSizeList(object):
    def __init__(self, max):
        self.max_size = max
        self.innerlist = []

    def push(self, obj):
        self.innerlist.append(obj)
        if len(self.innerlist) > self.max_size:
            self.innerlist.pop()

    def get_list(self):
        return self.innerlist
