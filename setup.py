try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name' : 'Atomic Hub Bot',
    'description' : 'AtomicHub Bot',
    'author' : 'Zachary Thomas',
    'download_url' : 'Where to download it.',
    'author_email' : 'zackthomas13@gmail.com',
    'url' : 'https://github.com/zackthomas1',
    'version' : '0.1',
    'install_requires' : ['logging', 'datetime', 'os', 'time'],
    'packages' : ['AtomicHubMonitor'],
    'scripts' : ['Main'],
}

setup(**config)
