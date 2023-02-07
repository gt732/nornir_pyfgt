pyfgt_zone
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_zone


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_zone
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_zone)

    print_result(results)

Output::
   [ { 'description': '',
    'interface': [{'interface-name': 'port3', 'q_origin_key': 'port3'}],
    'intrazone': 'deny',
    'name': 'test',
    'q_origin_key': 'test',
    'tagging': []}]
    ...