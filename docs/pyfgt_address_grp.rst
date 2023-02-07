pyfgt_address_grp
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_address_grp


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_address_grp
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_address_grp)

    print_result(results)

Output::
    
   [ { 'allow-routing': 'disable',
    'category': 'default',
    'color': 0,
    'comment': '',
    'exclude': 'disable',
    'exclude-member': [],
    'fabric-object': 'disable',
    'member': [ {'name': 'gmail.com', 'q_origin_key': 'gmail.com'},
                { 'name': 'wildcard.google.com',
                  'q_origin_key': 'wildcard.google.com'}],
    'name': 'G Suite',
    'q_origin_key': 'G Suite',
    'tagging': [],
    'type': 'default',
    'uuid': 'fe3f8dc6-a4ac-51ed-f0e2-e11854189b4e'},
  { 'allow-routing': 'disable',
    'category': 'default',
    'color': 0,
    'comment': '',
    'exclude': 'disable',
    'exclude-member': [],
    'fabric-object': 'disable',
    'member': [ { 'name': 'login.microsoftonline.com',
                  'q_origin_key': 'login.microsoftonline.com'},
                { 'name': 'login.microsoft.com',
                  'q_origin_key': 'login.microsoft.com'},
                { 'name': 'login.windows.net',
                  'q_origin_key': 'login.windows.net'}],
    'name': 'Microsoft Office 365',
    'q_origin_key': 'Microsoft Office 365',
    'tagging': [],
    'type': 'default',
    'uuid': 'fe3f90aa-a4ac-51ed-6202-6c97e89d3206'}]
    ...