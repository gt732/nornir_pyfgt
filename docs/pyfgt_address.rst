pyfgt_address
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_address


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_address
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_address)

    print_result(results)

Output::

    { 'allow-routing': 'disable',
    'associated-interface': '',
    'cache-ttl': 0,
    'clearpass-spt': 'unknown',
    'color': 0,
    'comment': '',
    'country': '',
    'dirty': 'dirty',
    'fabric-object': 'disable',
    'filter': '',
    'fsso-group': [],
    'interface': '',
    'list': [],
    'macaddr': [],
    'name': 'ADDRESS',
    'node-ip-only': 'disable',
    'obj-id': '',
    'obj-type': 'ip',
    'q_origin_key': 'ADDRESS',
    'sdn': '',
    'sdn-addr-type': 'private',
    'sub-type': 'sdn',
    'subnet': '127.0.0.100 255.255.255.252',
    'tag-detection-level': '',
    'tag-type': '',
    'tagging': [],
    'type': 'ipmask',
    'uuid': '0cdb9216-a648-51ed-b43f-238c3b127bc2'}