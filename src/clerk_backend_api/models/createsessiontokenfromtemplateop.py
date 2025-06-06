"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from enum import Enum
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateSessionTokenFromTemplateRequestBodyTypedDict(TypedDict):
    expires_in_seconds: NotRequired[Nullable[int]]
    r"""Use this parameter to override the JWT token lifetime."""


class CreateSessionTokenFromTemplateRequestBody(BaseModel):
    expires_in_seconds: OptionalNullable[int] = UNSET
    r"""Use this parameter to override the JWT token lifetime."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["expires_in_seconds"]
        nullable_fields = ["expires_in_seconds"]
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


class CreateSessionTokenFromTemplateRequestTypedDict(TypedDict):
    session_id: str
    r"""The ID of the session"""
    template_name: str
    r"""The name of the JWT Template defined in your instance (e.g. `custom_hasura`)."""
    request_body: NotRequired[CreateSessionTokenFromTemplateRequestBodyTypedDict]


class CreateSessionTokenFromTemplateRequest(BaseModel):
    session_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the session"""

    template_name: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The name of the JWT Template defined in your instance (e.g. `custom_hasura`)."""

    request_body: Annotated[
        Optional[CreateSessionTokenFromTemplateRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class CreateSessionTokenFromTemplateObject(str, Enum):
    TOKEN = "token"


class CreateSessionTokenFromTemplateResponseBodyTypedDict(TypedDict):
    r"""OK"""

    object: NotRequired[CreateSessionTokenFromTemplateObject]
    jwt: NotRequired[str]


class CreateSessionTokenFromTemplateResponseBody(BaseModel):
    r"""OK"""

    object: Optional[CreateSessionTokenFromTemplateObject] = None

    jwt: Optional[str] = None
