try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_requires = []

with open('README') as f:
    readme = f.read()

setup(
    name='cs170-project',
    version='1.0.0',
    packages=['solver'],
    description='Algorithms Final Project',
    long_description=readme,
    author='Alex Francis',
    author_email='afrancis@berkeley.com',
    install_requires=install_requires,
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ]
)
