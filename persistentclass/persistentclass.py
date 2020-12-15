# -*- coding: utf-8 -*-
import dill
import os


class Persistent:
    """This class makes data permanent using object storage with dill"""
    def __init__(self, data_id, autosave=True, folder=None):
        self.data_id = data_id
        if not folder:
            folder = './'
        elif not os.path.exists(folder):
            os.makedirs(folder)
        self.file_name = folder + '/' + self.__class__.__name__ + str(self.data_id) + '.dpo'
        self.autosave = autosave
        if not self._load():
            self._init()
            self.save()

    def _load(self):
        """Loads the data."""
        if os.path.isfile(self.file_name):
            with open(self.file_name, 'rb') as f:
                data = dill.load(f)
                self.__dict__.update(data.__dict__)
            return True
        else:
            f = open(self.file_name, 'xb')
            f.close()
            return False

    def save(self):
        """Saves the data."""
        with open(self.file_name, 'wb') as f:
            dill.dump(self, f)

    def save_check(self):
        """Saves the data if autosave is True."""
        if self.autosave:
            self.save()

    def _init(self):
        """Initializes the object. Replace this on your class with custom method."""
        pass
