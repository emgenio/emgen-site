from setuptools import setup, find_packages


setup(
    name='emgen',
    version='0.0.1a0',
    url='https://bitbucket.org/CentricWebEstate/emgen.git',
    author='Centic Web Estate',
    author_email='cso@cwe.space',
    license='Commercial',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: Non-Standard :: Commercial License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='host manager',
    install_requires=[
        'bottle',
        'simplejson',
        'pymongo',
        'mandrill',
        'IMAPClient'
    ],
    extras_require={
        'dev': [],
        'test': []
    },
    entry_points={
        'console_scripts':[
            'run=emgen:main',
            'cron=emgen:cron'
        ]
    }
)
