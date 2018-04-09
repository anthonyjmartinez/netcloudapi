from setuptools import setup, find_packages

setup(
    name="netcloudapi",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests"],
    version="0.1.2-a.2",
    author="Anthony Martinez",
    author_email="anthony.martinez@gmail.com",
    url="https://github.com/anthonyjmartinez/netcloudapi",
    description="Python Interface for the Cradlepoint NetCloud API V2",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
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
