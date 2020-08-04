import requests
import json


def pretty_print_request(request):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body)
    )


def pretty_print_response(response):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text)
    )


def test_post_header_body_json():
    # url = "https://issuer-id.slock.it/api/daf/server-identity"
    url = 'http://127.0.0.1:3000/json'

    # Additional header
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'connect.sid=s%3Am2e0uJVUe6EmggDh_s0pr4xgLM1YahGg.DiX0ugy97NWajtwSimPn2XKHaFJLpt25xiMgcIrXeGE'
    }
    # Body
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    # resp_body = response.json()
    # print(response.text)
        # print full request and response
    pretty_print_request(response.request)
    pretty_print_response(response)
    # assert resp_body['url'] == url

    # print(response.text.encode('utf8'))


if __name__ == '__main__':
    test_post_header_body_json()

