pyfgt_delete
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_delete


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_delete
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_delete, url='/api/v2/cmdb/firewall/address/blahblah')

    print_result(results)

Output::
    
    pyfgt_delete********************************************************************
    * FW-01 ** changed : False *****************************************************
    vvvv pyfgt_delete ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
    <Response [200]>
    ^^^^ END pyfgt_delete ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^