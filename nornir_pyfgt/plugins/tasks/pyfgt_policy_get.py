from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyfgt.plugins.connections import CONNECTION_NAME


def pyfgt_policy_get(
    task: Task,
    **kwargs
) -> Result:
    """
    Retrieve policy configuration from a Fortinet device using the api path "api/v2/cmdb/firewall/policy/"

    Arguments:
        task (Task): Nornir task object
        **kwargs: **kwargs
        Need to use only one of params
        :param int uid: Filters fortigate-object by identifier. Used to get a single object
        :param list filter: Filters fortigate-objects by one or multiple conditions: equals "==",
            not equals "!=", contains "=@". Used to get multiple objects
        :param str efilter: Extended filter: "srcaddr", "dstaddr" by condition: equals "==",
            not equals "!=",  supernets ">=", subnets "<="
        :return: *List[dict_]* List of the fortigate-objects
    Returns:
        Result: Result object containing the result of the operation, with the policy information.
    """

    fgt_conn = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    
    result = fgt_conn.policy.get(**kwargs)
    
    return Result(host=task.host, result=result)