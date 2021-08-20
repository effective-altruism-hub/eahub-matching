from typing import List

from django.http import HttpRequest
from ninja import NinjaAPI
from ninja import Schema


api = NinjaAPI(
    docs_url="docs/",
    csrf=True,
    urls_namespace="api",
)


class ProfileFields(Schema):
    profile_id: int
    fields: list[str]


@api.patch("/profiles/patch/{profile_id}", response=ProfileFields)
def get_rule_schedule(request: HttpRequest, profile_id: int) -> ProfileFields:
    return ProfileFields(profile_id=35, fields=["tags_common"])
