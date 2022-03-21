from shareData import GlobalRequest
import json
import server_test

test_test = {
    "name1": 'name1',
    'name2': 'name2'
}
server_test.app.run(host='127.0.0.1', port=8808, debug=False)