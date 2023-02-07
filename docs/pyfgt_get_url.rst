pyfgt_get_url
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_get_url


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_get_url
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_get_url, url="/api/v2/cmdb/firewall/address/test")

    print_result(results)

Output::
   [ { 'allow-routing': 'disable',
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
    'name': 'test',
    'node-ip-only': 'disable',
    'obj-id': '',
    'obj-type': 'ip',
    'q_origin_key': 'test',
    'sdn': '',
    'sdn-addr-type': 'private',
    'sub-type': 'sdn',
    'subnet': '10.25.25.25 255.255.255.255',
    'tag-detection-level': '',
    'tag-type': '',
    'tagging': [],
    'type': 'ipmask',
    'uuid': '1bdab84c-a6a1-51ed-c732-7d0b7daedca4'}]
    ...