class Mydict(dict):
    def dict_sort(self):
        t = list()
        for key, val in self.items():
            t.append((val, key))
        t.sort()
        q = list()
        for count, name in t:
            q.append((name, count))
        return q
            