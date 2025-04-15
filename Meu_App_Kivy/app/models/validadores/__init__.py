# -*- coding: utf-8 -*-

"""
    This module initializes and exposes validation
    functions for different platforms.

    Imports:
        - `validar_mac`: Validation function for MAC addresses.
        - `validar_posix`: Validation function for POSIX systems.
        - `validar_windows`: Validation function for Windows systems.

    Exports:
        - `validar_windows`: Validation function for Windows systems.
        - `validar_posix`: Validation function for POSIX systems.
        - `validar_mac`: Validation function for MAC addresses.
"""

from .tri_fasico import Identidade, ValidadorTriFasico

__all__ = [
    "Identidade",
    "ValidadorTriFasico",
]
