from nornir_pyfgt.plugins.tasks import pyfgt_address_grp



def test_pyfgt_address_grp(nr):
    result = nr.run(task=pyfgt_address_grp)
    device_result = result['FW-01'][0].result
    assert result['FW-01'].failed is False
    assert device_result[0]['name'] == 'G Suite'