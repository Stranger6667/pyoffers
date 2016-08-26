# coding: utf-8
import base64
import glob
import gzip
import json
import os

from .conftest import CASSETTE_DIR, DEFAULT_NETWORK_ID, DEFAULT_NETWORK_TOKEN, NETWORK_ID, NETWORK_TOKEN


def replace_real_credentials(network_token=NETWORK_TOKEN, network_id=NETWORK_ID):
    """
    HasOffers response body contains NetworkId & NetworkToken and they should be replaced with test values.
    """
    cassettes = glob.glob(os.path.join(CASSETTE_DIR, '*.json'))
    for cassette_path in cassettes:
        with open(cassette_path) as fp:
            data = json.load(fp)
            for record in data['http_interactions']:
                body = record['response']['body']['base64_string'].encode()
                body = gzip.decompress(base64.b64decode(body))
                cleaned_body = body.replace(
                    network_token.encode(), DEFAULT_NETWORK_TOKEN.encode()
                ).replace(
                    network_id.encode(), DEFAULT_NETWORK_ID.encode()
                )
                record['response']['body']['base64_string'] = base64.b64encode(gzip.compress(cleaned_body)).decode()
        with open(cassette_path, 'w') as fp:
            json.dump(data, fp, sort_keys=True, indent=2, separators=(',', ': '))
