from setuptools import setup

setup(
    name='Arduino RC Car with GUI',
    version='0.1.0',
    author='Jugal Bilimoria and Henry Gu',
    description="An arduino 4 motor RC car with a python GUI control interface.",
    url='https://github.com/JugalBili/Arduino-RC-Car-With-GUI',
    license='license.txt',
    long_description=open('README.md').read(),
    install_requires=[
        "pyserial==3.5"
    ],
    python_requires='>=3.6',
)