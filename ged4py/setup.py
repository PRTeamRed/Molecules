from setuptools import setup, find_packages

setup(
    name='ged4py',
    version='0.1dev',
    packages=find_packages(),
    author='Jacques Fize',
    license='MIT',
    install_requirements=['numpy==1.13.1', 'scipy==0.19.1', 'networkx>=1.11,~2'],
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        ]
)
