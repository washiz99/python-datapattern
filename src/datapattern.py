from functools import reduce


class DataPattern(object):

    def __init__(self, factor):
        self.factor = factor

    def _product(self, *args):
        pools = [pool for pool in args]
        result = [[]]
        for pool in pools:
            result = [x+[y] for x in result for y in pool]
        return result

    def get_pattern_size(self):
        return reduce(lambda x, y: x * y, [len(x) for f in self.factor for x in f])

    def generate(self):
        pattern_product = [x for y in self.factor for x in [self._product(*y)]]

        max_size = self.get_pattern_size()
        cur_size = max_size

        result = []
        for pattern in pattern_product:
            row = []
            cur_size //= len(pattern)
            for i in range(max_size // (cur_size * len(pattern))):
                for p in pattern:
                    row.extend([p] * cur_size)
            result.append(row)

        return result
