pyfgt_post_url
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_post_url


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_post_url
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    data = {'name': 'test',
            'passwd': 'test123'}

    results = nr.run(task=pyfgt_post_url, url="/api/v2/cmdb/user/local", data=data)

    print_result(results)

Output::
    
    pyfgt_post_url******************************************************************
    * FW-01 ** changed : False *****************************************************
    vvvv pyfgt_post_url ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
    <Response [200]>
    ^^^^ END pyfgt_post_url ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^