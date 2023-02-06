import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

with open("requirements.txt", "r") as f:
    INSTALL_REQUIRES = f.read().splitlines()

setuptools.setup(name='nornir_pyfgt',
                 version='1.0.0',
                 description='Fortigate-Api library and plugins for Nornir',
                 url='https://github.com/gt732/nornir_pyfgt',
                 packages=setuptools.find_packages(),
                 author='Geury Torres',
                 author_email='geuryt@yahoo.com',
                 license='MIT',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 install_requires=INSTALL_REQUIRES,
                 entry_points={
                     'nornir.plugins.connections': "pyfgt = nornir_pyfgt.plugins.connections:Pyfgt"
                 },
                 zip_safe=False)