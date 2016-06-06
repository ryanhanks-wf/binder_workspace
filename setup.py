from setuptools import setup

setup(
    name='binders_workspace',
    version='0.0.1',
    py_modules=['bdub'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        bdub=bdub:cli
    ''',
)
