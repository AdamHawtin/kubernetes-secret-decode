import json

import base64
import yaml


def decode_secret(secret, secret_format='yaml'):
    secret_decoders = {'json': json_decode_data_fields,
                       'yaml': yaml_decode_data_fields,
                       'yml': yaml_decode_data_fields}
    return secret_decoders[secret_format.lower()](secret)


def guess_secret_format(secret):
    if secret.startswith('{'):
        return 'json'
    elif secret.startswith('apiVersion: '):
        return 'yaml'


def json_decode_data_fields(secret_json):
    return json.dumps(decode_data_fields(json.loads(secret_json)), indent=2)


def yaml_decode_data_fields(secret_yaml):
    return yaml.safe_dump(decode_data_fields(yaml.safe_load(secret_yaml)), indent=2)


def decode_data_fields(secret):
    decoded_data = {}
    for k, v in secret['data'].items():
        decoded_data[k] = base64.b64decode(v).decode()
    secret['data'] = decoded_data
    return secret
