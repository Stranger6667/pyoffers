# coding: utf-8
from pyoffers.models.raw_log import DateDir, LogFile, LogRecord


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


def test_content(log_file):
    assert log_file.content == b'transaction_id,affiliate_id,affiliate_manager_id,advertiser_id,advertiser_manager_id,' \
                               b'offer_id,creative_url_id,affiliate_source,affiliate_sub1,affiliate_sub2,' \
                               b'affiliate_sub3,affiliate_sub4,affiliate_sub5,datetime,revenue_cents,payout_cents,' \
                               b'refer,url,pixel_refer,ip,user_agent,country_code,browser_id,is_click_unique,' \
                               b'ad_campaign_id,ad_campaign_creative_id,offer_file_id,status,offer_file_size,' \
                               b'currency,payout_type,revenue_type,device_brand,device_model,device_os,' \
                               b'device_os_version,device_id,device_id_md5,device_id_sha1,android_id,' \
                               b'android_id_md5,android_id_sha1,mac_address,mac_address_md5,mac_address_sha1,' \
                               b'odin,open_udid,ios_ifa,ios_ifa_md5,ios_ifa_sha1,ios_ifv,user_id,unknown_id,' \
                               b'payout_group_id,revenue_group_id,req_connection_speed,google_aid\n' \
                               b'"1020f1afc9b6af45c4efe622938512",3,12,44,12,13,"","NEX","UNUSE","PD","",' \
                               b'"d3ba452c-6abb-487f-a9f7-10a513765f36","","2016-09-09 14:00:28","","","",' \
                               b'"http://example.com/aff_c?offer_id=13&aff_id=3&source=NEX&aff_sub=UNUSE&aff_sub2=' \
                               b'PD&aff_sub4=d3ba452c-6abb-487f-a9f7-10a513765f36","","127.0.0.1",' \
                               b'"Mozilla/5.0 (Linux; Android 4.1.2; GT-S6310N Build/JZO54K) AppleWebKit/537.36 ' \
                               b'(KHTML, Like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36","CZ",8,0,"","","","",' \
                               b'"","CZK","cpa_flat","cpa_flat","Samsung","GT-S6310N","Android","4.1","","","","","",' \
                               b'"","","","","","","","","","","","",0,0,"mobile",""\n' \
                               b'"102f149014c5fae4576c577c26347c",10,4,18,4,84,"","NEX","THM","AD","",' \
                               b'"94be64d8-5c3e-4bad-8d6a-ad4e9a9a01cb","","2016-09-09 14:00:44","250","","",' \
                               b'"http://example.com/aff_c?offer_id=84&aff_id=10&source=NEX&aff_sub=THM&aff_sub2=AD' \
                               b'&aff_sub4=94be64d8-5c3e-4bad-8d6a-ad4e9a9a01cb","","127.0.0.1","Mozilla/5.0 ' \
                               b'(Windows NT 10.0) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/46.0.2486.0 ' \
                               b'Safari/537.36 Edge/13.10586","ES",6,0,"","","","","","EUR","cpa_flat","cpc",' \
                               b'"Microsoft","Edge","Desktop","","","","","","","","","","","","","","","","","",' \
                               b'"",0,0,"broadband",""\n'


def test_log_records(log_file):
    records = log_file.records
    assert len(records) == 2
    assert all(isinstance(item, LogRecord) for item in records)
    assert str(records[0]) == 'LogRecord: 13 (1020f1afc9b6af45c4efe622938512)'
