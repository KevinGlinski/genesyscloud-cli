from setuptools import setup

setup(
    name='genesyscloudcli',
    version='0.1',
    py_modules=['genesyscloudcli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        # each line identifies one console script. 
        # The first part before the equals sign (=) is the name of the script that should be generated,
        # the second part is the import path followed by a colon (:) with the Click command.
        gcli=clidriver:cli
    ''',
)