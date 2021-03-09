import setuptools


with open("README.md", "r") as setup:
    long_description = setup.read()

setuptools.setup(
    name="mygtu",
    version="0.1.0",
    author="Dhruv Maaniya (@midnightmadwalk)",
    author_email="midnightmadwalk@gmail.com",
    description="pyhton interaction with gtu website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mygtu/mygtu",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['datetime', 'pytz', 'ujson', 'aiofiles', 'aiohttp'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
