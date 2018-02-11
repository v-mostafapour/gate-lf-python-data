from collections import Counter
from . vocab import Vocab


class TargetNominal(object):

    def __init__(self, meta):
        self.meta = meta
        self.isSequence = meta["isSequence"]
        if self.isSequence:
            self.seq_max = meta["sequLengths.max"]
            self.seq_avg = meta["sequLengths.mean"]
        targetStats = meta["targetStats"]
        self.stringCounts = targetStats["stringCounts"]
        self.nrTargets = len(self.stringCounts)
        self.freqs = Counter(self.stringCounts)
        self.vocab = Vocab(self.freqs, emb_id="<<TARGET>>", no_pad=True)
        self.vocab.finish()
        # influences if the conversion will return the index or
        # the onehot vector
        self.as_onehot = False

    def set_as_onehot(self, flag=False):
        """Influence hot the original class label is converted. If
        the flag is False, then the string is converted to the corresponding
        string index, otherwise, to the corresponding onehot vector."""
        self.as_onehot = flag

    def __call__(self, value, as_onehot=False):
        as_onehot = self.as_onehot or as_onehot
        if self.isSequence:
            if as_onehot:
                ret = [self.vocab.string2onehot(v) for v in value]
            else:
                ret = [self.vocab.string2idx(v) for v in value]
            return ret
        else:
            if as_onehot:
                return self.vocab.string2onehot(value)
            else:
                return self.vocab.string2idx(value)

    def __str__(self):
        return "TargetNominal()"

    def __repr__(self):
        return "TargetNominal()"
