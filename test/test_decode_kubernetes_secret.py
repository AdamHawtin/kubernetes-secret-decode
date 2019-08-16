import base64
import copy
import json

import yaml

import decode_kubernetes_secret as under_test


def test_decode_data_fields():
    # Given
    expected_decoded_secret = {
        'data': {
            'key1': 'value1',
            'key2': 'value2',
        },
        'metadata': 'stuff'
    }
    secret = copy.deepcopy(expected_decoded_secret)
    secret['data']['key1'] = base64.b64encode(secret['data']['key1'].encode())
    secret['data']['key2'] = base64.b64encode(secret['data']['key2'].encode())

    # When
    actual_decoded_secret = under_test.decode_data_fields(secret)

    # Then
    assert expected_decoded_secret == actual_decoded_secret


def test_guess_secret_format_json():
    # Given
    secret = '{"thisLooksLike": "JSON"}'

    # When
    secret_format = under_test.guess_secret_format(secret)

    # Then
    assert 'json' == secret_format


def test_guess_secret_format_yaml():
    # Given
    secret = ('apiVersion: v1 \n'
              'thisLooksLike: YAML')

    # When
    secret_format = under_test.guess_secret_format(secret)

    # Then
    assert 'yaml' == secret_format


def test_json_decode_data_fields():
    # Given
    expected_decoded_secret = {
        'data': {
            'key1': 'value1',
            'key2': 'value2',
        },
        'metadata': 'stuff'
    }

    secret = copy.deepcopy(expected_decoded_secret)
    secret['data']['key1'] = base64.b64encode(secret['data']['key1'].encode()).decode()
    secret['data']['key2'] = base64.b64encode(secret['data']['key2'].encode()).decode()
    secret_json = json.dumps(secret)

    # When
    actual_decoded_secret_json = under_test.json_decode_data_fields(secret_json)
    actual_decoded_secret = json.loads(actual_decoded_secret_json)

    # Then
    assert expected_decoded_secret == actual_decoded_secret


def test_yaml_decode_data_fields():
    # Given
    expected_decoded_secret = {
        'data': {
            'key1': 'value1',
            'key2': 'value2',
        },
        'metadata': 'stuff'
    }

    secret = copy.deepcopy(expected_decoded_secret)
    secret['data']['key1'] = base64.b64encode(secret['data']['key1'].encode()).decode()
    secret['data']['key2'] = base64.b64encode(secret['data']['key2'].encode()).decode()
    secret_yaml = yaml.safe_dump(secret)

    # When
    actual_decoded_secret_json = under_test.yaml_decode_data_fields(secret_yaml)
    actual_decoded_secret = yaml.safe_load(actual_decoded_secret_json)

    # Then
    assert expected_decoded_secret == actual_decoded_secret
