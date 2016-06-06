from setuptools import setup

setup(
    name='bdub',
    version='0.1',
    py_modules=['bdub'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        bdub=bdub:cli
    ''',
)
