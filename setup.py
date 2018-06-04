from setuptools import setup, find_packages

setup(
    name="netcloudapi",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests"],
    version="0.3-b.1",
    author="Anthony Martinez",
    author_email="anthony.martinez@gmail.com",
    url="https://github.com/anthonyjmartinez/netcloudapi",
    description="Python Interface for the Cradlepoint NetCloud API V2",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
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
