from abc import ABCMeta, abstractmethod

class FileBase(metaclass=ABCMeta):
    def __init__(self, file_name):
        self._data = []
        # process file here ...

    @abstractmethod
    def to_csv(self):
        print("hello from to_csv()")

    @abstractmethod
    def plot(self):
        pass

class SpamFile(FileBase):
    def to_csv(self):
        super().to_csv()
        print("hello from SpamFile.to_csv()")

    def plot(self):
        pass

sf = SpamFile("weasels.txt")
sf.to_csv()
sf.plot()

class HamFile(FileBase):
    pass

class ToastFile(FileBase):
    pass

