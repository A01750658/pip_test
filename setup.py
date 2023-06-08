from setuptools import setup, find_packages


setup(
    name='zoren_pip_test',
    version='0.1',
    license='MIT',
    author="Zoren",
    author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'pandas',
          'tkinter',
          'Editor',
          'matplotlib',
          'IPython',
          'Editor'

      ],

)