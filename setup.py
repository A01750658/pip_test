from setuptools import setup, find_packages


setup(
    name='zoren_pip_test',
    version='0.2',
    license='MIT',
    author="Zoren",
    author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/A01750658/pip_test',
    keywords='example project',
    install_requires=[
          'pandas',
          'tk',
          'Editor',
          'matplotlib',
          'IPython',
          'Editor'

      ],

)