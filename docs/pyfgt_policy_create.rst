pyfgt_policy_create
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_policy_create


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_policy_create
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    data = dict(
    name="POLICY",
    status="enable",
    action="accept",
    srcintf=[{"name": "any"}],
    dstintf=[{"name": "any"}],
    srcaddr=[{"name": "all"}],
    dstaddr=[{"name": "all"}],
    service=[{"name": "ALL"}],
    schedule="always",)

    results = nr.run(task=pyfgt_policy_create, data=data)

    print_result(results)

Output::
    
    pyfgt_policy_create******************************************************************
    * FW-01 ** changed : False *****************************************************
    vvvv pyfgt_policy_create ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
    <Response [200]>
    ^^^^ END pyfgt_policy_create ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^