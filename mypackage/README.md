# Make your own package

Option 1, old: `python setup.py bdist_wheel` && pip install ...`
Option 2, modern: `python -m build` && `python -m installer ...`


1. Make package structure

```
mypackage/
├── mypackage/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── README.md
├── MANIFEST.in
├── pyproject.toml
└── setup.py
```

2. create setup.py

```powershell
   pip install setuptools
```

```python
   from setuptools import find_packages, setup
   setup(
       name='my_package',
       version='0.1',
       packages=find_packages(),
       install_requires=[
           # List your dependencies here "pygame"
           ],
       include_package_data=True,
       description='A simple example package',
       author='Your Name',
       author_email='your.email@example.com',
       url='https://github.com/yourusername/my_package',
       classifiers=[
           'Programming Language :: Python :: 3',
           'License :: OSI Approved :: MIT License',
           'Operating System :: OS Independent',
       ],
       python_requires='>=3.6',
    )
```

3. pack

```powershell
mypackage\python setup.py bdist_wheel | sdist
```
bdist_wheel -> .whl
sdist -> .tar.gz

creates directories:
- \build
- \dist
- \my_package.egg-info


Recomended: use `build`

- include `pyproject.toml`  
  my_package/
  └── pyproject.toml

```pyproject.toml (file)
[build-system]  
requires = ["setuptools>=42", "wheel"]  
build-backend = "setuptools.build_meta"
```

```powershell
`pip install build`
`powershell pip install build`
`python -m build`; instead of old `python setup.py`


4. install local

- `pip install .` | `pip install *.whl` | `*.tar.gz`

- Recomended: using `installer`
  ```powershell
  pip install installer`
  python -m installer dist/my_package-0.1-py3-none-any.whl
  ```

5. ignore certain folders

- ```setup.py
     setup(
         include_package_data=True,
     )
  ```

- ```MANIFEST.in
     prune `to_ignore_directory`
     p.e.: `prune tests`
  ```


