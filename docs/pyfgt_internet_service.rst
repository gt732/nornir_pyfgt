pyfgt_internet_service
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_internet_service


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_internet_service
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_internet_service)

    print_result(results)

Output::
    
    { 'city': [],
    'city6': [],
    'country': [],
    'country6': [],
    'database': 'isdb',
    'direction': 'both',
    'extra-ip-range-number': 0,
    'extra-ip6-range-number': 0,
    'icon-id': 203,
    'id': 13304053,
    'ip-number': 0,
    'ip-range-number': 0,
    'ip6-range-number': 0,
    'name': 'Azion-Azion.Platform',
    'obsolete': 0,
    'q_origin_key': 13304053,
    'region': [],
    'region6': [],
    'singularity': 0},
  { 'city': [],
    'city6': [],
    'country': [],
    'country6': [],
    'database': 'isdb',
    'direction': 'both',
    'extra-ip-range-number': 0,
    'extra-ip6-range-number': 0,
    'icon-id': 204,
    'id': 13369590,
    'ip-number': 0,
    'ip-range-number': 0,
    'ip6-range-number': 0,
    'name': 'Hurricane.Electric-Hurricane.Electric.Internet.Services',
    'obsolete': 0,
    'q_origin_key': 13369590,
    'region': [],
    'region6': [],
    'singularity': 0},
  { 'city': [],
    'city6': [],
    'country': [],
    'country6': [],
    'database': 'isdb',
    'direction': 'both',
    'extra-ip-range-number': 0,
    'extra-ip6-range-number': 0,
    'icon-id': 205,
    'id': 13435127,
    'ip-number': 0,
    'ip-range-number': 0,
    'ip6-range-number': 0,
    'name': 'NodePing-NodePing.Probe',
    'obsolete': 0,
    'q_origin_key': 13435127,
    'region': [],
    'region6': [],
    'singularity': 0},
  { 'city': [],
    'city6': [],
    'country': [],
    'country6': [],
    'database': 'isdb',
    'direction': 'dst',
    'extra-ip-range-number': 0,
    'extra-ip6-range-number': 0,
    'icon-id': 206,
    'id': 13500665,
    'ip-number': 0,
    'ip-range-number': 0,
    'ip6-range-number': 0,
    'name': 'Frontline-Frontline',
    'obsolete': 0,
    'q_origin_key': 13500665,
    'region': [],
    'region6': [],
    'singularity': 0},
  { 'city': [],
    'city6': [],
    'country': [],
    'country6': [],
    'database': 'isdb',
    'direction': 'dst',
    'extra-ip-range-number': 0,
    'extra-ip6-range-number': 0,
    'icon-id': 207,
    'id': 13566202,
    'ip-number': 0,
    'ip-range-number': 0,
    'ip6-range-number': 0,
    'name': 'Tally-Tally.ERP',
    'obsolete': 0,
    'q_origin_key': 13566202,
    'region': [],
    'region6': [],