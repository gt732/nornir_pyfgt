pyfgt_service_category
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_service_category


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_service_category
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_service_category)

    print_result(results)

Output::
    
   [ { 'comment': 'General services.',
    'fabric-object': 'disable',
    'name': 'General',
    'q_origin_key': 'General'},
  { 'comment': 'Web access.',
    'fabric-object': 'disable',
    'name': 'Web Access',
    'q_origin_key': 'Web Access'},
  { 'comment': 'File access.',
    'fabric-object': 'disable',
    'name': 'File Access',
    'q_origin_key': 'File Access'},
  { 'comment': 'Email services.',
    'fabric-object': 'disable',
    'name': 'Email',
    'q_origin_key': 'Email'},
  { 'comment': 'Network services.',
    'fabric-object': 'disable',
    'name': 'Network Services',
    'q_origin_key': 'Network Services'},
  { 'comment': 'Authentication service.',
    'fabric-object': 'disable',
    'name': 'Authentication',
    'q_origin_key': 'Authentication'},
  { 'comment': 'Remote access.',
    'fabric-object': 'disable',
    'name': 'Remote Access',
    'q_origin_key': 'Remote Access'},
  { 'comment': 'Tunneling service.',
    'fabric-object': 'disable',
    'name': 'Tunneling',
    'q_origin_key': 'Tunneling'},
  { 'comment': 'VoIP, messaging, and other applications.',
    'fabric-object': 'disable',
    'name': 'VoIP, Messaging & Other Applications',
    'q_origin_key': 'VoIP, Messaging & Other Applications'},
  { 'comment': 'Explicit web proxy.',
    'fabric-object': 'disable',
    'name': 'Web Proxy',
    'q_origin_key': 'Web Proxy'}]
    ...