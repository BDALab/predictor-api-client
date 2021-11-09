import numpy
from pprint import pprint
from http import HTTPStatus
from predictor_api_client.client import PredictorApiClient


def predict():
    """Example code: calls .predict(...) on a predictor"""

    # Prepare the predictor API client settings
    #
    # --------------------------------------------- #
    # Must be same as for the running Predictor API #
    # --------------------------------------------- #
    #
    # 1. host (IP address)
    # 2. port (port number)
    # 3. request verification
    # 4. request timeout in seconds
    host = "http://127.0.0.1"
    port = 5000
    verify = True
    timeout = 2

    # Instantiate the predictor API client
    client = PredictorApiClient(host=host, port=port, verify=verify, timeout=timeout)

    # TODO: prepare data for request authorization (access token and refresh token)
    access_token = "<TODO: FILL-IN>"
    refresh_token = "<TODO: FILL-IN>"

    # TODO: prepare model identifier
    #
    # Example:
    # model_identifier = "dummy_predictor"
    model_identifier = "<TODO: FILL-IN>"

    # TODO: prepare predictor data (feature values/labels)
    #
    # ---------------------------------------------------- #
    # Must meet the data requirements of the Predictor API #
    # ---------------------------------------------------- #
    #
    # Example (10 subjects, each having 100 1-D features):
    # feature_values = numpy.random.rand(10, 1, 100)
    # feature_labels = None
    feature_values = "<TODO: FILL-IN>"
    feature_labels = None

    print("\n-- [04] example --")
    print(f"Calling .predict(...) on a predictor identified with: {model_identifier}\n")

    # Call .predict(...) on a predictor
    response, status_code = client.predict(
        access_token=access_token,
        refresh_token=refresh_token,
        model_identifier=model_identifier,
        feature_values=feature_values,
        feature_labels=feature_labels)

    # Check the output
    if status_code == HTTPStatus.OK:
        print("Successfully called .predict(...)")
    else:
        print(f"The request was unsuccessful ({status_code}): {response}")

    print("Response:")
    pprint(response)


if __name__ == "__main__":
    predict()
