from setuptools import setup, find_packages


setup(
    name='doctools',
    version='0.2',
    description='docblock manipulation utilities',
    long_description=open('README.rst').read(),
    py_modules=['doctools'],
    install_requires=['pytest', 'pytest-cov'],
    author = 'Adam Wagner',
    author_email = 'awagner83@gmail.com',
    url = 'https://github.com/awagner83/doctools',
    license = 'BSD3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ]
)

