# coding: utf-8
from pyoffers.models.raw_log import DateDir, LogFile


CASSETTE_NAME = 'raw_log'


def test_list_date_dirs(date_dirs):
    assert len(date_dirs) == 3
    assert all(isinstance(item, DateDir) for item in date_dirs)
    assert str(date_dirs[0]) == 'DateDir: Sep 9, 2016 (20160909)'


def assert_log_files(log_files):
    assert len(log_files) == 3
    assert all(isinstance(item, LogFile) for item in log_files)
    assert str(log_files[0]) == 'LogFile: Sep 9, 2016 - 09:00 am (20160909/clicks-1473411600-SlY9UO.zip)'


def test_manager_list_logs(api):
    result = api.raw_logs.clicks.list_logs('20160909')
    assert_log_files(result)


def test_model_list_logs(date_dirs):
    date_dir = date_dirs[0]
    result = date_dir.list_logs()
    assert_log_files(result)


def test_download_link(log_file):
    assert log_file.download_link == 'https://s3.amazonaws.com/ho-adserverlogs-prod/qproc/raw-logs/clicks/blabla'


def test_equality(date_dirs):
    assert date_dirs[0] != date_dirs[1]
    assert date_dirs[0] == date_dirs[0]
