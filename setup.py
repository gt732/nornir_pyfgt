import setuptools


setuptools.setup(name='nornir_pyfgt',
                 packages=setuptools.find_packages(),
                 entry_points={
                     'nornir.plugins.connections': "pyfgt = nornir_pyfgt.plugins.connections:Pyez"
                 },
                 zip_safe=False)