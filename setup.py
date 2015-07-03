from setuptools import setup


setup(
    name='gzip-reader',
    version='0.1',
    author='Alexander Schepanovski',
    author_email='suor.web@gmail.com',

    description='Decompress gzipped streams on the fly',
    long_description=open('README.rst').read(),
    url='http://github.com/Suor/gzip-reader',
    license='BSD',

    py_modules=['gzip_reader'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ]
)
