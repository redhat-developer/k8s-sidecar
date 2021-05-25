import setuptools

setuptools.setup(
    name="k8s-sidecar",
    version="0.0.1",
    author="kiwigrid",
    url="https://github.com/redhat-developer/k8s-sidecar.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "sidecar"},
    packages="",
    python_requires=">=3.6",
)