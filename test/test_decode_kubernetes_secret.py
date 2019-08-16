import base64
import copy

from decode_kubernetes_secret import decode_data_fields, guess_secret_format


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
    actual_decoded_secret = decode_data_fields(secret)

    # Then
    assert expected_decoded_secret == actual_decoded_secret


def test_guess_secret_format_json():
    # Given
    secret = '{"thisLooksLike": "JSON"}'

    # When
    secret_format = guess_secret_format(secret)

    # Then
    assert 'json' == secret_format


def test_guess_secret_format_yaml():
    # Given
    secret = ('apiVersion: v1 \n'
              'thisLooksLike: YAML')

    # When
    secret_format = guess_secret_format(secret)

    # Then
    assert 'yaml' == secret_format
