from setuptools import setup, find_packages

setup(
    name='picobackup',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/davidfialho14/picobackup',
    license='MIT License',
    author='David Fialho',
    author_email='fialho.david@gmail.com',
    description='',

    scripts=['bin/picobackup'],
    install_requires=['configparser', 'docopt', 'watchdog', ],
)
