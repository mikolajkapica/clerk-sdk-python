"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .organization import Organization, OrganizationTypedDict
from clerk_backend_api.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class OrganizationsTypedDict(TypedDict):
    r"""A list of organizations"""

    data: List[OrganizationTypedDict]
    total_count: int
    r"""Total number of organizations

    """


class Organizations(BaseModel):
    r"""A list of organizations"""

    data: List[Organization]

    total_count: int
    r"""Total number of organizations

    """
