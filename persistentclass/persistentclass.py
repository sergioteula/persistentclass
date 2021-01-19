# -*- coding: utf-8 -*-
import pickle
import os


#TODO Add documentation
#TODO Add exception handling
#TODO Try adding autosave to any method


class Persistent:
    """This class makes data permanent using object storage with pickle"""
    def __init__(self, data_id='', folder='', autosave=True, use_dill=False):
        self.data_id = data_id
        self.autosave = autosave
        self.use_dill = use_dill

        # Create forlders structure
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
        self.folder = folder

        # Create file name
        self.filename = self.__class__.__name__ + str(self.data_id) + '.pickle'
        self.path = self.folder + self.filename

        # Initialize data if not loaded
        if not self.load():
            self.init()
            self.save()

    def load(self):
        """Loads the data."""
        if os.path.isfile(self.path):
            with open(self.path, 'rb') as f:
                if self.use_dill:
                    import dill
                    data = dill.load(f)
                else:
                    data = pickle.load(f)
                self.__dict__.update(data.__dict__)
            return True
        else:
            with open(self.path, 'xb'):
                pass
            return False

    def save(self):
        """Saves the data."""
        try:
            if self.use_dill:
                import dill
                data = dill.dumps(self)
            else:
                data = pickle.dumps(self)

            with open(self.path, 'wb') as f:
                f.write(data)

        except Exception as e:
            raise PersistentError('Error saving data for ' + self.filename + ': ' + str(e))

    def asave(self):
        """Saves the data if autosave is True."""
        if self.autosave:
            self.save()

    def init(self):
        """Initializes the object. Replace this on your class with custom method."""
        pass


class PersistentError(BaseException):
    pass
