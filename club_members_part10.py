# === Stage 10: Поиск по нескольким словам ===
# Project: ClubMembers
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Member:
    name: str
    role: str = "member"
    join_date: Optional[str] = None
    status: str = "active"

    def __str__(self) -> str:
        return f"{self.name} ({self.role}, {self.status})"


def _split_query(query: str) -> List[str]:
    tokens = []
    for token in query.replace("-", " - ").split():
        token = token.strip("-")
        if not token:
            continue
        tokens.append(token)
    return tokens


def _token_matches(token: str, member: Member, exclude: bool) -> bool:
    if exclude and token in member.__dict__:
        return False
    for value in member.__dict__.values():
        if isinstance(value, str) and token in value:
            return True
    return False


def search_members(members: List[Member], query: str) -> List[Member]:
    tokens = _split_query(query)
    if not tokens:
        return list(members)
    result = []
    for member in members:
        if all(_token_matches(token, member, not token.startswith("-")) for token in tokens):
            result.append(member)
    return result
