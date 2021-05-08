import setuptools

setuptools.setup(
    name = "binance-bot",
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)