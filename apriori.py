import re


class Apriori(dict):
    def __init__(self, sequence, support=34):
        super(Apriori, self).__init__()
        self.threshold = (support * len(sequence)) / 100.
        self._data = [re.sub(r'(,)([0-9])', r', \2', s) for s in sequence]
        self.primitives = {event for seq in self._data for event in seq.split(', ')}
        self.__apriori()
        del self._data

    def __apriori(self):
        candidates = self.__update_candidates(self.primitives)
        while len(candidates) > 0:
            result = self.__patterns(candidates)
            candidates = self.__update_candidates(result.keys())
            self.update(result)

    def __update_candidates(self, old_candidates):
        candidates = set()
        for seq in self._data:
            for can in old_candidates:
                for subs in re.findall(can + r'. [0-9]+', seq):
                    candidates.add(subs)
        return candidates

    def __patterns(self, candidates):
        from collections import defaultdict
        result = defaultdict(int)
        for seq in self._data:
            for c in candidates:
                if c in seq:
                    result[c] += 1
        return {k: v for k, v in result.items() if v > self.threshold}
