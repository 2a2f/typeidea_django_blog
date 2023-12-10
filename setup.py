from setuptools import setup, find_packages


setup(
    name='typeidea',
    version='0.1',
    description='Blog system base on Django',
    author='gu',
    author_email='guzx5xyz@163.com',
    url='http://8.130.46.229',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    package_data={'': [
        'themes/*/*/*/*',
    ]},
    # include_package_data=True,
    install_requires=[
        'django==4.2.4',
        'django-ckeditor==6.7.0',
        # 'django-debug-toolbar==4.2.0',
        # 'django-debug-toolbar-line-profiler==0.6.1',
        'django-js-asset==2.1.0',
        'django-silk==5.0.3',
        'djangorestframework==3.14.0',
        'djdt-flamegraph==0.2.13',
        'Jinja2==3.1.2',
        'mistune==3.0.1',
        'mysql-client==0.0.1',
        'mysqlclient==2.2.0',
        'Pillow==9.5.0',
        'requests==2.31.0',
        'setuptools==33.1.1',
        'six==1.16.0',
        'wheel==0.41.2',
        'gunicorn==21.2.0'
    ],
    extras_require={
        'ipython': ['ipython==6.2.1']
    },
    scripts=[
        'typeidea/manage.py',
    ],
    entry_points={
        'console_scripts': [
            'typeidea_manage = manage:main',
        ]
    },
    # classifiers=[
    #
    # ]
)
