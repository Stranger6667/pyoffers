# coding: utf-8
import base64
import glob
import gzip
import json
import os


class Record:
    def __init__(self, data):
        self.data = data

    @property
    def is_gzip(self):
        return self.data["response"]["headers"].get("Content-Encoding") == ["gzip"]

    @property
    def body(self):
        value = base64.b64decode(self.data["response"]["body"]["base64_string"].encode())
        if self.is_gzip:
            value = gzip.decompress(value)
        return value

    @body.setter
    def body(self, value):
        if self.is_gzip:
            value = gzip.compress(value)
        self.data["response"]["body"]["base64_string"] = base64.b64encode(value).decode()

    @property
    def request_uri(self):
        return self.data["request"]["uri"].encode()

    @request_uri.setter
    def request_uri(self, value):
        self.data["request"]["uri"] = value.decode()

    @property
    def response_url(self):
        return self.data["response"]["url"].encode()

    @response_url.setter
    def response_url(self, value):
        self.data["response"]["url"] = value.decode()


class Cleaner:
    def __init__(self, path, old_token, new_token, old_id, new_id):
        self.path = path
        self.rewrite = False
        self.old_token = old_token.encode()
        self.new_token = new_token.encode()
        self.old_id = old_id.encode()
        self.new_id = new_id.encode()

    def clean_value(self, value):
        self.rewrite = True
        return value.replace(self.old_token, self.new_token).replace(self.old_id, self.new_id)

    def contains_real_credentials(self, value):
        return self.old_token in value or self.old_id in value

    def clean(self):
        with open(self.path) as fp:
            data = json.load(fp)
        for chunk in data["http_interactions"]:
            record = Record(chunk)
            for attribute in ("body", "request_uri", "response_url"):
                value = getattr(record, attribute)
                if self.contains_real_credentials(value):
                    setattr(record, attribute, self.clean_value(value))
        return data, self.rewrite

    def write(self, data):
        with open(self.path, "w") as fp:
            json.dump(data, fp, sort_keys=True, indent=2, separators=(",", ": "))


def replace_real_credentials(cassette_dir, old_token, new_token, old_id, new_id):
    cassettes = glob.glob(os.path.join(cassette_dir, "*.json"))
    for cassette_path in cassettes:
        cleaner = Cleaner(cassette_path, old_token, new_token, old_id, new_id)
        cleaned_data, rewrite_required = cleaner.clean()
        if rewrite_required:
            cleaner.write(cleaned_data)
