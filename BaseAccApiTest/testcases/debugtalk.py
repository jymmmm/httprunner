def setup_hook_request(request):
    exposed_ids= request.get("params", {}).get("exposed_ids")
    print(exposed_ids)

def teardown_hook_response(response):
    print(response.status_code)
    print(response.text)