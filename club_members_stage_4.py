# === Stage 4: Удаление и восстановление ===
# Project: ClubMembers
from datetime import datetime


class ClubMember:
    """Участник клуба с поддержкой мягкого удаления."""

    def __init__(self, name, role, join_date, status="active"):
        self.id = None
        self.name = name
        self.role = role
        self.join_date = join_date
        self.status = status
        self.deleted = False
        self.deleted_at = None

    def soft_delete(self):
        if self.status != "active":
            raise ValueError("Нельзя удалить участника со статусом, отличным от active")
        self.deleted = True
        self.status = "deleted"
        self.deleted_at = datetime.now()

    def restore(self):
        if not self.deleted:
            raise ValueError("Участник не был удалён")
        self.deleted = False
        self.status = "active"
        self.deleted_at = None

    @property
    def is_deleted(self):
        return self.deleted

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "join_date": self.join_date,
            "status": self.status,
            "deleted": self.deleted,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
        }


class MemberRepository:
    """Хранилище участников с поддержкой мягкого удаления."""

    def __init__(self):
        self._members = {}

    def add(self, member):
        member.id = len(self._members) + 1
        self._members[member.id] = member
        return member

    def get(self, member_id):
        return self._members.get(member_id)

    def active_members(self):
        return [m for m in self._members.values() if not m.is_deleted]

    def soft_delete(self, member_id):
        member = self.get(member_id)
        if member is None:
            raise KeyError(member_id)
        member.soft_delete()
        return member

    def restore(self, member_id):
        member = self.get(member_id)
        if member is None:
            raise KeyError(member_id)
        member.restore()
        return member

    def __len__(self):
        return len(self._members)
