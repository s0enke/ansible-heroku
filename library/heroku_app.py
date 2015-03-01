#!/usr/bin/python
import sys
import os
import time
import heroku3
import requests.exceptions

def main():
    module = AnsibleModule(
        argument_spec = dict(
            state     = dict(default='present', choices=['present', 'absent']),
            name      = dict(required=True),
        )
    )

    heroku_conn = heroku3.from_key(os.environ.get('HEROKU_API_KEY'))

    app_name = module.params['name']
    
    try:
        heroku_conn.app(module.params['name'])
    except requests.exceptions.HTTPError:
        heroku_conn.create_app(name=app_name)
        pass



    json_output = {}
    json_output['changed'] = True
    print json.dumps(json_output)
    sys.exit(0)

from ansible.module_utils.basic import *
main()
