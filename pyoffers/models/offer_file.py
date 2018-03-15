import os

from .core import Model, ModelManager


class OfferFile(Model):
    generic_methods = ('update', 'delete')


class OfferFileManager(ModelManager):
    model = OfferFile
    name = 'offer_files'
    generic_methods = (
        'find_by_id',
        'find_all',
        'find_all_ids',
        'delete',
        'update',
    )

    def create(self, path, **kwargs):
        with open(path, 'rb') as fd:
            if 'filename' not in kwargs:
                kwargs['filename'] = os.path.basename(path)
            return self._call('create', data=kwargs, files={kwargs['filename']: fd})
