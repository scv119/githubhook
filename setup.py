##############################################################################
#
# Copyright (c) 2011 Zhihu.
# All Rights Reserved.
#
##############################################################################

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

install_requires = [
                    'tornado',
                    'redis',
                   ]

setup(name='zhihu.githubhook',
      version='0.1',
      description='Zhihu github hook Tools',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        ],
      keywords='zhihu github hook tool',
      author="scv@zhihu.com",
      author_email="cvzhihu.com",
      url="http://www.zhihu.com",
      license="",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['zhihu'],
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      [console_scripts]
      web = zhihu.hook.main:main
      """,
      )

