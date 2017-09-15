import  sys
from    setuptools import setup

# Make sure we are running python3.5+
if 10 * sys.version_info[0]  + sys.version_info[1] < 35:
    sys.exit("Sorry, only Python 3.5+ is supported.")


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
      name             =   'pfioh',
<<<<<<< HEAD
      version          =   '1.5.0',
=======
      version          =   '1.4.8',
>>>>>>> 176a56fde20c83d4fa510a974e7567855a6ca258
      description      =   'Path-and-File-IO-over-HTTP',
      long_description =   readme(),
      author           =   'Rudolph Pienaar',
      author_email     =   'rudolph.pienaar@gmail.com',
      url              =   'https://github.com/FNNDSC/pman',
      packages         =   ['pfioh'],
      install_requires =   ['pycurl', 'pyzmq', 'webob', 'pudb', 'psutil', 'keystoneauth1', 'python-swiftclient'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      scripts          =   ['bin/pfioh'],
      license          =   'MIT',
      zip_safe         =   False
     )