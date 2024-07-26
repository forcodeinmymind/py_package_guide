from setuptools import find_packages, setup


# ChatGPT

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        # "pygame"
    ],
    include_package_data=True,
    description="A simple example package",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/my_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

"""
entry_points={
        "console_scripts": [
            "mypackage-main = mypackage.main:main",
        ],
"""

"""
ArjanCodes
setup(
	name="mymodule",
	version = "0.0.10",
	description="...",
	package_dir={"": "app"},
	packages=find_packages(where="app"),
	long_description="...",
	long_description_content_type="text/markdown"
	url="https://git..."
	author_email = ""
	license="MIT"
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3.10",
		"Operating System :: OS Independent"]
	install_requires=["bson >= 0.5.10"]
	extras_require={
		"dev": ["pytest>=7.0", "twine>=4.0.2"]
	}
	python_requires=">=3.10"
)
"""

"""
# from ?

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add your dependencies here
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "my_package=my_package.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
"""
