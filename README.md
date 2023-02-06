# Fortigate-Api for Nornir

## Plugins

Connections - fortigate-api

## Description

"This plugin integrates the fortigate-api library with the Nornir framework to simplify and automate configuration tasks on Fortigate devices. Using this plugin, you can easily create, delete, get, and update objects in the Fortigate using REST API and SSH. With commonly used objects already implemented, this plugin provides a powerful solution for managing your Fortigate network."

## Installation

```
pip install nornir-pyfgt
```

## Read the Documentation

link goes here

## Usages

pyfgt get firewall addresses

```python
from nornir import InitNornir
from nornir_pyfgt.plugins.tasks import pyfgt_address
from nornir_utils.plugins.functions import print_result

nr = InitNornir(
    config_file="your/config/path"
)


results = nr.run(task=pyfgt_address)

print_result(results)

```

results

```
vvvv pyfgt_address ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
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
    'name': 'DEMO',
    'node-ip-only': 'disable',
    'obj-id': '',
    'obj-type': 'ip',
    'q_origin_key': 'ADDRESS',
    'sdn': '',
    'sdn-addr-type': 'private',
    'sub-type': 'sdn',
    'subnet': '10.10.10.10 255.255.255.0',
    'tag-detection-level': '',
    'tag-type': '',
    'tagging': [],
    'type': 'ipmask',
    'uuid': '0cdb9216-a648-51ed-b43f-238c3b127bc2'},
    ...
^^^^ END pyfgt_address ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

pyfgt get custom URL - Check Fortigate API Documentation for API endpoints

```python
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_pyfgt.plugins.tasks import pyfgt_get_url


nr = InitNornir(
    config_file="your/config/path"
)


results = nr.run(task=pyfgt_get_url, url="/api/v2/cmdb/user/local")

print_result(results)

```

results

```
vvvv pyfgt_get_url ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
[ { 'auth-concurrent-override': 'disable',
    'auth-concurrent-value': 0,
    'authtimeout': 0,
    'email-to': '',
    'fortitoken': '',
    'id': 16777217,
    'ldap-server': '',
    'name': 'guest',
    'passwd': 'ENC XXXX',
    'passwd-policy': '',
    'passwd-time': '0000-00-00 00:00:00',
    'ppk-identity': '',
    'ppk-secret': '',
    'q_origin_key': 'guest',
    'radius-server': '',
    'sms-custom-server': '',
    'sms-phone': '',
    'sms-server': 'fortiguard',
    'status': 'enable',
    'tacacs+-server': '',
    'two-factor': 'disable',
    'two-factor-authentication': '',
    'two-factor-notification': '',
    'type': 'password',
    'username-sensitivity': 'enable',
    'workstation': ''}]
^^^^ END pyfgt_get_url^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

pyfgt send SSH command

```python
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_pyfgt.plugins.tasks import pyfgt_send_command


nr = InitNornir(
    config_file="your/config/path"
)


results = nr.run(task=pyfgt_send_command, command="get system interface")

print_result(results)

```

results

```
vvvv pyfgt_send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
== [ port1 ]
name: port1   mode: dhcp    ip: 192.168.0.158 255.255.255.0   status: up    netbios-forward: disable    type: physical   ring-rx: 0   ring-tx: 0   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable    mtu-override: disable    wccp: disable    drop-overlapped-fragment: disable    drop-fragment: disable
== [ port2 ]
name: port2   mode: static    ip: 0.0.0.0 0.0.0.0   status: up    netbios-forward: disable    type: physical   ring-rx: 0   ring-tx: 0   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable    mtu-override: disable    wccp: disable    drop-overlapped-fragment: disable    drop-fragment: disable
...
^^^^ END pyfgt_send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```
