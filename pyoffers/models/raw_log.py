# coding: utf-8
from .core import Model, ModelManager


class LogItem(Model):
    """
    Log entities have no id field, because they should be compared in a different way.
    """

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self._data == other._data


class DateDir(LogItem):
    """
    Directory with log files.
    """

    def __str__(self):
        return '%s: %s (%s)' % (self.__class__.__name__, self.displayName, self.dirName)

    def list_logs(self):
        return self._manager.list_logs(dir_name=self.dirName)


class LogFile(LogItem):
    """
    Log file.
    """

    def __str__(self):
        return '%s: %s (%s)' % (self.__class__.__name__, self.displayName, self.filename)

    @property
    def download_link(self):
        return self._manager.get_download_link(log_filename=self.filename)


class LogItemManager(ModelManager):
    """
    Works with exact type of log.
    """

    def __init__(self, *args, log_type, **kwargs):
        self.log_type = log_type
        super().__init__(*args, **kwargs)

    def _call(self, method, **kwargs):
        return self.api._call('RawLog', method, log_type=self.log_type, **kwargs)

    def list_date_dirs(self):
        response = self._call('listDateDirs', raw=True)
        return [DateDir(manager=self, **kwargs) for kwargs in response['dateDirs']]

    def list_logs(self, dir_name):
        response = self._call('listLogs', date_dir=dir_name, raw=True)
        return [LogFile(manager=self, **kwargs) for kwargs in response['logFiles']]

    def get_download_link(self, log_filename):
        return self._call('getDownloadLink', log_filename=log_filename, raw=True)['link']


class RawLogManager(ModelManager):
    """
    Works as proxy for other managers.
    """
    name = 'raw_logs'
    log_types = (
        'clicks',
        'conversions',
        'impressions',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_managers()

    def setup_managers(self):
        for log_type in self.log_types:
            setattr(self, log_type, LogItemManager(api=self.api, log_type=log_type))
