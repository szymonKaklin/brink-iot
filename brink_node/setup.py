from setuptools import setup, find_packages

setup(
    name="brink_node",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "paho-mqtt",
        "requests",
        "python-dotenv"
    ],
    entry_points={
        'console_scripts' : [
            'brink-node = brink_node.client:main',
        ],
    },
    tests_require=[
        'pytest',
    ],
    test_suite="tests",
)
