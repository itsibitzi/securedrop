import setuptools

long_description = "The SecureDrop whistleblower platform."

setuptools.setup(
    name="securedrop-app-code",
<<<<<<< HEAD
<<<<<<< HEAD
    version="1.2.2",
=======
    version="1.3.0~rc1",
>>>>>>> Backporting 1.2.0 changelog and updating version to 1.3.0~rc1
=======
    version="1.3.0~rc2",
>>>>>>> SecureDrop 1.3.0-rc2
    author="Freedom of the Press Foundation",
    author_email="securedrop@freedom.press",
    description="SecureDrop Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3+",
    python_requires=">=3.5",
    url="https://github.com/freedomofpress/securedrop",
    classifiers=(
        "Development Status :: 5 - Stable",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ),
)
