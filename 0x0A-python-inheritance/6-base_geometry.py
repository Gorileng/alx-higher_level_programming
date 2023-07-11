#!/usr/bin/python3
"""Defines the base of geometry class BaseGeometry."""


class BaseGeometry:
    """Represents the base geometry."""

    def area(self):
        """Never implemented."""
        raise Exception("area() is not implemented")
