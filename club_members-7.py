# === Stage 7: Фильтрация записей ===
# Project: ClubMembers
from datetime import date


def filter_members_by_role(members, role):
    return [m for m in members if m.get("role") == role]


def filter_members_by_date_range(members, start=None, end=None):
    def in_range(member):
        join = member.get("join_date")
        if start and join < start:
            return False
        if end and join > end:
            return False
        return True
    return [m for m in members if in_range(m)]


def filter_members(members, role=None, start=None, end=None):
    result = members
    if role is not None:
        result = filter_members_by_role(result, role)
    if start is not None or end is not None:
        result = filter_members_by_date_range(result, start, end)
    return result
