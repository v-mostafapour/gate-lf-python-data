class FeatureNgram(object):

    def __init__(self, datatype, attrinfo, featurestats):
        """Create the instance from the given meta info of an input feature"""


    def __call__(self):
        """Convert a value of the expected type for this feature to a value that can be
        fed into the corresponding input unit of the network"""
        pass

    def __str__(self):
        # TODO: add more info
        return "FeatureNgram(name="+self.fname+")"
