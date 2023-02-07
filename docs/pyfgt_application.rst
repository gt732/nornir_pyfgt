pyfgt_application
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_application


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_application
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_application)

    print_result(results)

Output::
    [ { 'app-replacemsg': 'enable',
    'comment': '',
    'control-default-network-services': 'disable',
    'deep-app-inspection': 'enable',
    'default-network-services': [],
    'enforce-default-app-port': 'disable',
    'entries': [ { 'action': 'block',
                   'application': [],
                   'behavior': 'all',
                   'category': [ {'id': 2, 'q_origin_key': 2},
                                 {'id': 6, 'q_origin_key': 6}],
                   'exclusion': [],
                   'id': 1,
                   'log': 'enable',
                   'log-packet': 'disable',
                   'parameters': [],
                   'per-ip-shaper': '',
                   'popularity': '1 2 3 4 5',
                   'protocols': 'all',
                   'q_origin_key': 1,
                   'quarantine': 'none',
                   'quarantine-expiry': '5m',
                   'quarantine-log': 'enable',
                   'rate-count': 0,
                   'rate-duration': 60,
                   'rate-mode': 'continuous',
                   'rate-track': 'none',
                   'risk': [],
                   'session-ttl': 0,
                   'shaper': '',
                   'shaper-reverse': '',
                   'technology': 'all',
                   'vendor': 'all'},
                 { 'action': 'pass',
                   'application': [],
                   'behavior': 'all',
                   'category': [],
                   'exclusion': [],
                   'id': 2,
                   'log': 'enable',
                   'log-packet': 'disable',
                   'parameters': [],
                   'per-ip-shaper': '',
                   'popularity': '1 2 3 4 5',
                   'protocols': 'all',
                   'q_origin_key': 2,
                   'quarantine': 'none',
                   'quarantine-expiry': '5m',
                   'quarantine-log': 'enable',
                   'rate-count': 0,
                   'rate-duration': 60,
                   'rate-mode': 'continuous',
                   'rate-track': 'none',
                   'risk': [],
                   'session-ttl': 0,
                   'shaper': '',
                   'shaper-reverse': '',
                   'technology': 'all',
                   'vendor': 'all'}],
    'extended-log': 'disable',
    ...