pyfgt_service
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_service


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_service
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_service)

    print_result(results)

Output::
   { 'app-category': [],
    'app-service-type': 'disable',
    'application': [],
    'category': 'VoIP, Messaging & Other Applications',
    'check-reset-range': 'default',
    'color': 0,
    'comment': '',
    'fabric-object': 'disable',
    'fqdn': '',
    'helper': 'auto',
    'iprange': '0.0.0.0',
    'name': 'MS-SQL',
    'protocol': 'TCP/UDP/SCTP',
    'proxy': 'disable',
    'q_origin_key': 'MS-SQL',
    'sctp-portrange': '',
    'session-ttl': '0',
    'tcp-halfclose-timer': 0,
    'tcp-halfopen-timer': 0,
    'tcp-portrange': '1433 1434',
    'tcp-rst-timer': 0,
    'tcp-timewait-timer': 0,
    'udp-idle-timer': 0,
    'udp-portrange': ''},
  { 'app-category': [],
    'app-service-type': 'disable',
    'application': [],
    'category': 'VoIP, Messaging & Other Applications',
    'check-reset-range': 'default',
    'color': 0,
    'comment': '',
    'fabric-object': 'disable',
    'fqdn': '',
    'helper': 'auto',
    'iprange': '0.0.0.0',
    'name': 'MYSQL',
    'protocol': 'TCP/UDP/SCTP',
    'proxy': 'disable',
    'q_origin_key': 'MYSQL',
    'sctp-portrange': '',
    'session-ttl': '0',
    'tcp-halfclose-timer': 0,
    'tcp-halfopen-timer': 0,
    'tcp-portrange': '3306',
    'tcp-rst-timer': 0,
    'tcp-timewait-timer': 0,
    'udp-idle-timer': 0,
    'udp-portrange': ''},
    ...