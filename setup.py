from setuptools import setup

setup(name='lykkex',
      version='0.1',
      description='Wrapper for the Lykke Exchange API',
      url='',
      author='Paul Pfeiffer',
      author_email='pfeifferpaul90@gmail.com',
      license='MIT',
      packages=['lykkex'],
      install_requires=['requests', ],
      setup_requires=['pytest-runner'],
      tests_require=['pytest', 'vcrpy'],
      zip_safe=False)
