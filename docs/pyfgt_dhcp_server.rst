pyfgt_dhcp_server
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_dhcp_server


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_dhcp_server
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_dhcp_server)

    print_result(results)

Output::
    
    [ { 'auto-configuration': 'enable',
    'auto-managed-status': 'enable',
    'conflicted-ip-timeout': 1800,
    'ddns-auth': 'disable',
    'ddns-key': 'ENC -13+0ogUQdtlo7HUQ8EQGYP3qCBek=',
    'ddns-keyname': '',
    'ddns-server-ip': '0.0.0.0',
    'ddns-ttl': 300,
    'ddns-update': 'disable',
    'ddns-update-override': 'disable',
    'ddns-zone': '',
    'default-gateway': '10.255.1.1',
    'dhcp-settings-from-fortiipam': 'disable',
    'dns-server1': '0.0.0.0',
    'dns-server2': '0.0.0.0',
    'dns-server3': '0.0.0.0',
    'dns-server4': '0.0.0.0',
    'dns-service': 'specify',
    'domain': '',
    'exclude-range': [],
    'filename': '',
    'forticlient-on-net-status': 'enable',
    'id': 1,
    'interface': 'fortilink',
    'ip-mode': 'range',
    'ip-range': [ { 'end-ip': '10.255.1.254',
                    'id': 1,
                    'lease-time': 0,
                    'q_origin_key': 1,
                    'start-ip': '10.255.1.2',
                    'uci-match': 'disable',
                    'uci-string': [],
                    'vci-match': 'disable',
                    'vci-string': []}],
    'ipsec-lease-hold': 60,
    'lease-time': 604800,
    'mac-acl-default-action': 'assign',
    'netmask': '255.255.255.0',
    'next-server': '0.0.0.0',
    'ntp-server1': '0.0.0.0',
    'ntp-server2': '0.0.0.0',
    'ntp-server3': '0.0.0.0',
    'ntp-service': 'local',
    'options': [],
    'q_origin_key': 1,
    'reserved-address': [],
    'server-type': 'regular',
    'status': 'enable',
    'tftp-server': [],
    'timezone': '00',
    'timezone-option': 'disable',
    'vci-match': 'enable',
    'vci-string': [ { 'q_origin_key': 'FortiSwitch',
                      'vci-string': 'FortiSwitch'},
                    { 'q_origin_key': 'FortiExtender',
                      'vci-string': 'FortiExtender'}],
    'wifi-ac-service': 'specify',
    'wifi-ac1': '0.0.0.0',
    'wifi-ac2': '0.0.0.0',
    'wifi-ac3': '0.0.0.0',
    'wins-server1': '0.0.0.0',
    'wins-server2': '0.0.0.0'}]
    ...