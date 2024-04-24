import json
import logging

from wiremock.server import WireMockServer

from config.config import abs_path
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class WiremockStub:

    def __init__(self):
        self.wiremock = WireMockServer()
        self.wiremock.start()

    def create_stub(self, endpoint, file_name):

        # with WireMockServer() as wiremock:
        url_mapping_server = f"http://localhost:{self.wiremock.port}/__admin/mappings"
        LOGGER.debug("URL Wiremock Server: %s", url_mapping_server)
        validate = ValidateResponse()
        rest_client = RestClient(headers={})
        json_data = validate.read_input_data_json(f"{abs_path}/todo_api/input_data/{endpoint}/{file_name}.json")
        response = rest_client.request("post", url_mapping_server, body=json.dumps(json_data))

        LOGGER.debug("Response Body: %s", response["body"])
        LOGGER.debug("Response Headers: %s", response["headers"])
        LOGGER.debug("Response Status Code: %s", response["status_code"])

        return response, self.wiremock

    def stop(self):
        LOGGER.debug("Stopping wiremock server")
        self.wiremock.stop()


if __name__ == '__main__':
    mock = WiremockStub()
    mock.create_stub()
