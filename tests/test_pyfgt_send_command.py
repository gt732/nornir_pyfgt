from nornir_pyfgt.plugins.tasks import pyfgt_send_command



def test_pyfgt_send_command(nr):
    result = nr.run(task=pyfgt_send_command, command='get system interface')
    device_result = result['FW-01'][0].result
    assert result['FW-01'].failed is False, str(device_result)