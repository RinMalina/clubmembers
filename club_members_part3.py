# === Stage 3: Хранилище в памяти ===
# Project: ClubMembers
from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List, Optional


@dataclass
class Member:
    name: str
    role: str = "member"
    join_date: Optional[date] = None
    status: str = "active"

    def __post_init__(self):
        if self.name and self.name[0].islower():
            self.name = self.name.capitalize()


class MemberStore:
    def __init__(self):
        self._members: Dict[str, Member] = {}

    def add(self, member: Member) -> Member:
        if not member.name:
            raise ValueError("Имя участника не может быть пустым")
        key = str(member.name).lower()
        if key in self._members:
            raise ValueError(f"Участник с именем {member.name!r} уже существует")
        self._members[key] = member
        return member

    def get(self, name: str) -> Optional[Member]:
        if not name:
            return None
        return self._members.get(str(name).lower())

    def list_all(self) -> List[Member]:
        return list(self._members.values())

    def __len__(self) -> int:
        return len(self._members)

    def __contains__(self, name: str) -> bool:
        return self.get(name) is not None

    def __repr__(self) -> str:
        return f"MemberStore(count={len(self._members)})"


if __name__ == "__main__":
    store = MemberStore()

    alice = Member(name="анна", role="moderator", join_date=date(2024, 1, 15), status="active")
    bob = Member(name="Боб", role="member", join_date=date(2024, 3, 2), status="active")
    charlie = Member(name="Кэл", role="member", status="inactive")

    store.add(alice)
    store.add(bob)
    store.add(charlie)

    print(store)
    print(store.list_all())
    print(store.get("Анна"))
    print("Анна" in store)
    print(store.get("Джон"))

    try:
        store.add(Member(name="Анна", role="member"))
    except ValueError as exc:
        print(exc)

    print(len(store))
