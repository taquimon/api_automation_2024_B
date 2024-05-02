from __future__ import annotations

import hvac


def get_token():
    client = hvac.Client(
        url="http://127.0.0.1:8200",
        token="dev-only-token",
    )

    read_response = client.secrets.kv.read_secret_version(path="token_todo")

    token = read_response["data"]["data"]["token"]
    print(token)
    return token


get_token()
