# coding: utf-8


CREATE_ADVERTISER_SUCCESS = {
    'request': {
        'Target': 'Advertiser',
        'NetworkToken': 'token',
        'Format': 'json',
        'Method': 'create',
        'NetworkId': 'id',
        'data': {
            'zipcode': '123456',
            'status': 'pending',
            'company': 'Test',
            'country': 'CZ'
            },
        'Version': '2',
        'Service': 'HasOffers'
        },
    'response': {
        'data': {
            'Advertiser': {
                'zipcode': '123456',
                'status': 'pending',
                'ref_id': None,
                'conversion_security_token': None,
                'SHARED_Accounts_id': None,
                'id': '72',
                'region': None,
                'account_manager_id': None,
                'tmp_token': None,
                'country': 'CZ',
                'phone': None,
                'SHARED_Network_Map_id': None,
                'fax': None,
                'other': None,
                'date_added': '2016-08-25 13:00:06',
                'address1': None,
                'company': 'Test',
                'website': None,
                'wants_alerts': '1',
                'address2': None,
                '_NETWORK_affiliate_status': None,
                '_NETWORK_brand_active': '1',
                'expose_subs': '0',
                'AFFILIATE_NETWORK_Brands_id': None,
                '_NETWORK_affiliate_id': None,
                'signup_ip': None,
                'city': None,
                'modified': -62169966000
                }
            },
        'status': 1,
        'errorMessage': None,
        'errors': [],
        'httpStatus': 200
        }
    }

UPDATE_ADVERTISER_SUCCESS = {
    'request': {
        'Target': 'Advertiser',
        'Method': 'update',
        'Format': 'json',
        'NetworkToken': 'token',
        'id': '72',
        'data': {
            'company': 'Another'
            },
        'NetworkId': 'id',
        'Version': '2',
        'Service': 'HasOffers'
        },
    'response': {
        'data': {
            'Advertiser': {
                'zipcode': '123456',
                'status': 'pending',
                'ref_id': None,
                'conversion_security_token': None,
                'SHARED_Accounts_id': None,
                'id': '1',
                'region': None,
                'account_manager_id': None,
                'tmp_token': None,
                'country': 'CZ',
                'phone': None,
                'SHARED_Network_Map_id': None,
                'fax': None,
                'other': None,
                'date_added': '2016-08-25 13:00:06',
                'address1': None,
                'company': 'Another',
                'website': None,
                'wants_alerts': '1',
                'address2': None,
                '_NETWORK_affiliate_status': None,
                '_NETWORK_brand_active': '1',
                'expose_subs': '0',
                'AFFILIATE_NETWORK_Brands_id': None,
                '_NETWORK_affiliate_id': None,
                'signup_ip': None,
                'city': None,
                'modified': 1472159845
                }
            },
        'status': 1,
        'errorMessage': None,
        'errors': [],
        'httpStatus': 200
        }
    }

UPDATE_ADVERTISER_FAIL = {
    'request': {
        'Method': 'update',
        'NetworkId': 'id',
        'Version': '2',
        'data': {
            'expose_subs': '0',
            'fax': 'None',
            'address2': 'None',
            'wants_alerts': '1',
            'SHARED_Accounts_id': 'None',
            'website': 'None',
            'ref_id': 'None',
            'city': 'None',
            'zipcode': '123456',
            'tmp_token': 'None',
            'conversion_security_token': 'None',
            'country': 'PL',
            'date_added': '2016-08-25 13:00:06',
            'address1': 'None',
            'status': 'blocked',
            'other': 'None',
            '_NETWORK_affiliate_id': 'None',
            'SHARED_Network_Map_id': 'None',
            '_NETWORK_affiliate_status': 'None',
            'id': '72',
            'company': 'Another',
            'region': 'None',
            '_NETWORK_brand_active': '1',
            'account_manager_id': 'None',
            'signup_ip': 'None',
            'modified': '1472161004',
            'phone': 'None',
            'AFFILIATE_NETWORK_Brands_id': 'None'
            },
        'Target': 'Advertiser',
        'Service': 'HasOffers',
        'id': '72',
        'Format': 'json',
        'NetworkToken': 'token'
        },
    'response': {
        'errorMessage': 'Could not update advertiser.',
        'status': -1,
        'httpStatus': 200,
        'data': '',
        'errors': [{
                       'publicMessage': 'Could not update advertiser.',
                       'err_msg': 'Account_manager_id is not valid.',
                       'attribute_name': 'account_manager_id',
                       'err_code': 3
                       }, {
                       'err_msg': 'Conversion_security_token should be between 32 and 32 characters.',
                       'attribute_name': 'conversion_security_token',
                       'err_code': 3
                       }]
        }
    }

FIND_BY_ID_ADVERTISER_SUCCESS = {
    'response': {
        'httpStatus': 200,
        'data': {
            'Advertiser': {
                'fax': None,
                'conversion_security_token': None,
                'AFFILIATE_NETWORK_Brands_id': None,
                'phone': None,
                'other': None,
                'account_manager_id': None,
                'signup_ip': None,
                '_NETWORK_affiliate_id': None,
                'date_added': '2016-08-25 13:00:06',
                'status': 'blocked',
                'ref_id': None,
                'zipcode': '123456',
                'website': None,
                '_NETWORK_brand_active': '1',
                'SHARED_Network_Map_id': None,
                'tmp_token': None,
                'company': 'Another',
                'address1': None,
                '_NETWORK_affiliate_status': None,
                'country': 'CZ',
                'wants_alerts': '1',
                'address2': None,
                'city': None,
                'region': None,
                'SHARED_Accounts_id': None,
                'modified': 1472211500,
                'expose_subs': '0',
                'id': '72'
                }
            },
        'status': 1,
        'errorMessage': None,
        'errors': []
        },
    'request': {
        'NetworkToken': 'token',
        'Target': 'Advertiser',
        'NetworkId': 'id',
        'id': '72',
        'Version': '2',
        'Format': 'json',
        'Service': 'HasOffers',
        'Method': 'findById'
        }
    }

FIND_BY_ID_ADVERTISER_FAIL = {
    'response': {
        'httpStatus': 200,
        'data': None,
        'status': 1,
        'errorMessage': None,
        'errors': []
        },
    'request': {
        'NetworkToken': 'token',
        'Target': 'Advertiser',
        'NetworkId': 'id',
        'id': '1000',
        'Version': '2',
        'Format': 'json',
        'Service': 'HasOffers',
        'Method': 'findById'
        }
    }

BLOCK_ADVERTISER_SUCCESS = {
    'request': {
        'NetworkToken': 'token',
        'reason': 'reason text',
        'NetworkId': 'id',
        'Service': 'HasOffers',
        'Format': 'json',
        'Target': 'Advertiser',
        'id': '72',
        'Method': 'block',
        'Version': '2'
        },
    'response': {
        'data': True,
        'errors': [],
        'httpStatus': 200,
        'errorMessage': None,
        'status': 1
        }
    }
