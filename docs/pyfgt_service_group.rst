pyfgt_service_group
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_service_group


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_service_group
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_service_group)

    print_result(results)

Output::
    
   [ { 'color': 0,
    'comment': '',
    'fabric-object': 'disable',
    'member': [ {'name': 'DNS', 'q_origin_key': 'DNS'},
                {'name': 'IMAP', 'q_origin_key': 'IMAP'},
                {'name': 'IMAPS', 'q_origin_key': 'IMAPS'},
                {'name': 'POP3', 'q_origin_key': 'POP3'},
                {'name': 'POP3S', 'q_origin_key': 'POP3S'},
                {'name': 'SMTP', 'q_origin_key': 'SMTP'},
                {'name': 'SMTPS', 'q_origin_key': 'SMTPS'}],
    'name': 'Email Access',
    'proxy': 'disable',
    'q_origin_key': 'Email Access'},
  { 'color': 0,
    'comment': '',
    'fabric-object': 'disable',
    'member': [ {'name': 'DCE-RPC', 'q_origin_key': 'DCE-RPC'},
                {'name': 'DNS', 'q_origin_key': 'DNS'},
                {'name': 'HTTPS', 'q_origin_key': 'HTTPS'}],
    'name': 'Exchange Server',
    'proxy': 'disable',
    'q_origin_key': 'Exchange Server'},
  { 'color': 0,
    'comment': '',
    'fabric-object': 'disable',
    'member': [ {'name': 'DNS', 'q_origin_key': 'DNS'},
                {'name': 'HTTP', 'q_origin_key': 'HTTP'},
                {'name': 'HTTPS', 'q_origin_key': 'HTTPS'}],
    'name': 'Web Access',
    'proxy': 'disable',
    'q_origin_key': 'Web Access'},
  { 'color': 0,
    'comment': '',
    'fabric-object': 'disable',
    'member': [ {'name': 'DCE-RPC', 'q_origin_key': 'DCE-RPC'},
                {'name': 'DNS', 'q_origin_key': 'DNS'},
                {'name': 'KERBEROS', 'q_origin_key': 'KERBEROS'},
                {'name': 'LDAP', 'q_origin_key': 'LDAP'},
                {'name': 'LDAP_UDP', 'q_origin_key': 'LDAP_UDP'},
                {'name': 'SAMBA', 'q_origin_key': 'SAMBA'},
                {'name': 'SMB', 'q_origin_key': 'SMB'}],
    'name': 'Windows AD',
    'proxy': 'disable',
    'q_origin_key': 'Windows AD'}]
    ...