"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class CreatePhoneNumberRequestBodyTypedDict(TypedDict):
    user_id: str
    r"""The ID representing the user"""
    phone_number: str
    r"""The new phone number. Must adhere to the E.164 standard for phone number format."""
    verified: NotRequired[Nullable[bool]]
    r"""When created, the phone number will be marked as verified."""
    primary: NotRequired[Nullable[bool]]
    r"""Create this phone number as the primary phone number for the user. Default: false, unless it is the first phone number."""
    reserved_for_second_factor: NotRequired[Nullable[bool]]
    r"""Create this phone number as reserved for multi-factor authentication. The phone number must also be verified.
    If there are no other reserved second factors, the phone number will be set as the default second factor.
    """


class CreatePhoneNumberRequestBody(BaseModel):
    user_id: str
    r"""The ID representing the user"""

    phone_number: str
    r"""The new phone number. Must adhere to the E.164 standard for phone number format."""

    verified: OptionalNullable[bool] = UNSET
    r"""When created, the phone number will be marked as verified."""

    primary: OptionalNullable[bool] = UNSET
    r"""Create this phone number as the primary phone number for the user. Default: false, unless it is the first phone number."""

    reserved_for_second_factor: OptionalNullable[bool] = UNSET
    r"""Create this phone number as reserved for multi-factor authentication. The phone number must also be verified.
    If there are no other reserved second factors, the phone number will be set as the default second factor.
    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["verified", "primary", "reserved_for_second_factor"]
        nullable_fields = ["verified", "primary", "reserved_for_second_factor"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
