# coding: utf-8
from csv import DictReader
from io import BytesIO, StringIO
from zipfile import ZipFile

from pip.utils import cached_property

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

    @cached_property
    def download_link(self):
        return self._manager.get_download_link(log_filename=self.filename)

    @cached_property
    def content(self):
        """
        Returns raw CSV content of the log file.
        """
        raw_content = self._manager.api.session.get(self.download_link).content
        data = BytesIO(raw_content)
        archive = ZipFile(data)
        filename = archive.filelist[0]  # Always 1 file in the archive
        return archive.read(filename)

    @cached_property
    def records(self):
        data = StringIO(self.content.decode())
        return [LogRecord(manager=self._manager, **kwargs) for kwargs in DictReader(data)]


class LogRecord(LogItem):
    """
    Log record with all data about clicks / conversions / impressions.
    """

    def __str__(self):
        return '%s: %s (%s)' % (self.__class__.__name__, self.offer_id, self.transaction_id)


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

    def find_all(self, date):
        return sum([log_file.records for log_file in self.list_logs(date)], [])


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
