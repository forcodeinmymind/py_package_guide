"""test mypackage
```powershell
PYTHONPATH=. pytest tests/
```
`pytest` python module for software testing
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mypackage
