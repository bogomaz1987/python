class Diff(object):
    '''
    Class for diff two objects
    '''

    def diff_two_dict(self, data_before, data, res):
        '''
        Function for diff two dict
        '''
        if not isinstance(data_before or data, dict):
            raise TypeError('Expected dict')

        if len(data) != len(data_before):
            for x in set(data) - set(data_before):
                res[x] = data[x]

        for i, j in data_before.iteritems():
            if not (data.get(i) == data_before.get(i)):
                try:
                    if isinstance(data[i], dict) and isinstance(data_before[i], dict):
                        res[i] = {}
                        self.diff_two_dict(data_before[i], data[i], res[i])
                    else:
                        res[i] = data[i]
                except KeyError:
                    res[i] = data_before[i]
        return res
