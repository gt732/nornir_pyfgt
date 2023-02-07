pyfgt_ip_pool
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_ip_pool


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_ip_pool
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_ip_pool)

    print_result(results)

Output::
   [ { 'add-nat64-route': 'enable',
    'arp-intf': '',
    'arp-reply': 'enable',
    'associated-interface': '',
    'block-size': 128,
    'comments': '',
    'endip': '20.20.20.20',
    'endport': 65533,
    'name': 'test',
    'nat64': 'disable',
    'num-blocks-per-user': 8,
    'pba-timeout': 30,
    'permit-any-host': 'disable',
    'port-per-user': 0,
    'q_origin_key': 'test',
    'source-endip': '0.0.0.0',
    'source-startip': '0.0.0.0',
    'startip': '10.10.10.10',
    'startport': 5117,
    'subnet-broadcast-in-ippool': 'enable',
    'type': 'overload'}]
    ...