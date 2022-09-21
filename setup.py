from setuptools import setup, find_packages
import os

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='maoproxy',
    packages=find_packages(),
    include_package_data=True,
    version="0.0.1",
    description='Free proxy list for python!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='mao2116',
    author_email='mao2116@yandex.com',
    install_requires=['requests'],
    
    
    keywords=["mao2116","mao-hacking","mao-community","proxy list","free proxy","termux - command","termux","android hacking","mao tool","mao","pip proxy","python proxy","proxy list with python"],
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Environment :: Console',
    ],
    
    license='MIT',
    python_requires='>=3.9.5'
)
