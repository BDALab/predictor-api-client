from pprint import pprint
from http import HTTPStatus
from predictor_api_client.client import PredictorApiClient


def example_log_in_user():
    """Example code: log-in an existing user"""

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

    # TODO: prepare data for an existing user (data from: ./01_sign_up_user.py)
    #
    # 1. username
    # 2. password
    username = "<TODO: FILL-IN>"
    password = "<TODO: FILL-IN>"

    print("\n-- [02] example --")
    print(f"Logging-in an existing user with username: {username} and password: {password}\n")

    # Log-in an existing user
    response, status_code = client.log_in(username, password)

    # Check the output
    if status_code == HTTPStatus.OK:
        print("Successfully logged-in an existing user")
    else:
        print(f"The request was unsuccessful ({status_code}): {response}")

    print("Response:")
    pprint(response)


if __name__ == "__main__":
    example_log_in_user()
