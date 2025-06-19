class DefaultList(list):
    def __init__(self,*items,default):
        super().__init__(*items)
        self.default = default
    def __getitem__(self,index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.default
        


class NewList(list):
    def range(self):
        return max(self) - min(self)


class NewDefaultList(NewList,DefaultList):
    pass


