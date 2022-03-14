import base64
import copy
import json

import yaml

import decode_kubernetes_secret


def test_decode_data_fields():
    # Given
    secret, expected_decoded_secret = get_example_secret()

    # When
    actual_decoded_secret = decode_kubernetes_secret.decode_data_fields(secret)

    # Then
    assert actual_decoded_secret == expected_decoded_secret


def test_deduce_secret_format_json():
    # Given
    secret = '{"thisLooksLike": "JSON"}'

    # When
    secret_format = decode_kubernetes_secret.deduce_secret_format(secret)

    # Then
    assert secret_format == 'json'


def test_deduce_secret_format_yaml():
    # Given
    secret = ('apiVersion: v1 \n'
              'thisLooksLike: YAML')

    # When
    secret_format = decode_kubernetes_secret.deduce_secret_format(secret)

    # Then
    assert secret_format == 'yaml'


def test_json_decode_data_fields():
    # Given
    secret, expected_decoded_secret = get_example_secret()

    # When
    actual_decoded_secret_json = decode_kubernetes_secret.json_decode_data_fields(json.dumps(secret))
    actual_decoded_secret = json.loads(actual_decoded_secret_json)

    # Then
    assert actual_decoded_secret == expected_decoded_secret


def test_decode_data_fields_handles_no_data_gracefully():
    # Given
    secret_with_no_data = {'foo': 'bar'}

    # When
    actual_decoded_secret = decode_kubernetes_secret.decode_data_fields(secret_with_no_data)

    # Then
    assert actual_decoded_secret == secret_with_no_data


def test_yaml_decode_data_fields():
    # Given
    secret, expected_decoded_secret = get_example_secret()

    # When
    actual_decoded_secret_json = decode_kubernetes_secret.yaml_decode_data_fields(yaml.safe_dump(secret))
    actual_decoded_secret = yaml.safe_load(actual_decoded_secret_json)

    # Then
    assert actual_decoded_secret == expected_decoded_secret


def test_json_data_values_are_prettified():
    # Given
    json_value = b'{"testKey": "testValue"}'

    # When
    actual_decoded_value = decode_kubernetes_secret.decode_data_value(base64.b64encode(json_value))

    # Then
    assert actual_decoded_value == json.loads(json_value)


def get_example_secret():
    decoded_secret = {
        'data': {
            'key1': 'value1',
            'key2': 'value2',
        },
        'metadata': 'stuff'
    }
    secret = copy.deepcopy(decoded_secret)
    secret['data']['key1'] = base64.b64encode(secret['data']['key1'].encode()).decode()
    secret['data']['key2'] = base64.b64encode(secret['data']['key2'].encode()).decode()
    return secret, decoded_secret
