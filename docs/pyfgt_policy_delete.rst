pyfgt_policy_delete
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_policy_delete


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_policy_delete
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")


    results = nr.run(task=pyfgt_policy_delete, filter="name==POLICY")

    print_result(results)

Output::
    pyfgt_policy_delete******************************************************************
    * FW-01 ** changed : False *****************************************************
    vvvv pyfgt_policy_delete ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
    <Response [200]>
    ^^^^ END pyfgt_policy_delete ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^