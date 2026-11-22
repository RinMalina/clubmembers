# === Stage 8: Сортировка записей ===
# Project: ClubMembers
import datetime


def sort_members_by_name(members, descending=False):
    reverse = descending
    return sorted(members, key=lambda m: m["name"], reverse=reverse)


def sort_members_by_created(members, descending=False):
    reverse = descending
    return sorted(
        members,
        key=lambda m: m.get("created_at") or datetime.datetime.min,
        reverse=reverse,
    )


def sort_members(members, field="name", descending=False):
    if field == "created_at":
        return sort_members_by_created(members, descending=descending)
    return sort_members_by_name(members, descending=descending)
