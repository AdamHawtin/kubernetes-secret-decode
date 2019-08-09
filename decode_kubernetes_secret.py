import json

import base64
import yaml


def decode_secret(secret: str, secret_format: str = 'yaml') -> str:
    secret_decoders = {'json': decode_secret_json,
                       'yaml': decode_secret_yaml,
                       'yml': decode_secret_yaml}
    return secret_decoders[secret_format](secret)


def guess_secret_format(secret: str) -> str:
    if secret[0] == '{':
        return 'json'
    elif secret.startswith('apiVersion: '):
        return 'yaml'


def decode_secret_json(secret_json: str) -> str:
    return json.dumps(decode_data_fields(json.loads(secret_json)), indent=2)


def decode_secret_yaml(secret_yaml: str) -> str:
    return yaml.safe_dump(decode_data_fields(yaml.safe_load(secret_yaml)), indent=2)


def decode_data_fields(secret: dict) -> dict:
    decoded_data = {}
    for k, v in secret['data'].items():
        decoded_data[k] = base64.b64decode(v).decode()
    secret['data'] = decoded_data
    return secret
