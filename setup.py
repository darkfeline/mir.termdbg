# Copyright (C) 2016 Allen Li
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(
    name='mir.termdbg',
    version='2.1.0',
    description='Terminal debugging tools',
    long_description='',
    keywords='',
    url='https://github.com/darkfeline/mir.termdbg',
    author='Allen Li',
    author_email='darkfeline@felesatra.moe',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],

    packages=['mir.termdbg'],
    package_data={
        'mir.termdbg': ['*.csv'],
    },
    install_requires=[],
)
