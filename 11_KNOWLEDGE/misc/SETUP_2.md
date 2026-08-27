---
tags: [misc]
---
"""
Build an example package using the limited Python C API.
"""

import os

import numpy as np
from setuptools import Extension, setup

macros = [("NPY_NO_DEPRECATED_API", 0), ("Py_LIMITED_API", "0x03060000")]

limited_api = Extension(
    "limited_api",
    sources=[os.path.join('.', "limited_api.c")],
    include_dirs=[np.get_include()],
    define_macros=macros,
)

extensions = [limited_api]

setup(
    ext_modules=extensions
)

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
