from setuptools import setup, find_packages

setup(
    name="NetCloudAPI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests"],
    test_suite="tests",
    version="0.1.0",
    author="Anthony Martinez",
    author_email="anthony.martinez@gmail.com",
    url="https://collab.ajmartinez.com/amartinez/NetCloudAPI-py3",
    description="Python Interface for the Cradlepoint NetCloud API V2",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities"
    ]
)
