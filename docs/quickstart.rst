quickstart
==========

1) Install nornir_pyfgt::

    pip install nornir_pyfgt


2) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_address


3) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_address
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_address)

    print_result(results)