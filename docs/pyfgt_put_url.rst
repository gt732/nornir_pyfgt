pyfgt_put_url
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_put_url


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_put_url
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    data = {'passwd': 'test123'}

    results = nr.run(task=pyfgt_put_url, url="/api/v2/cmdb/user/local/test", data=data)

    print_result(results)

Output::
    pyfgt_put_url******************************************************************
    * FW-01 ** changed : False *****************************************************
    vvvv pyfgt_put_url ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
    <Response [200]>
    ^^^^ END pyfgt_put_url ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^