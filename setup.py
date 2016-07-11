from setuptools import setup

setup(
    name='binder_workspace',
    version='0.0.1',
    py_modules=['bw'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        bw=bw:cli
    ''',
)
