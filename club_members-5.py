# === Stage 5: Связанная сущность ===
# Project: ClubMembers
from datetime import date


class Contribution:
    def __init__(self, amount, currency="RUB", date=None):
        self.amount = amount
        self.currency = currency
        self.date = date or date.today()

    def __repr__(self):
        return f"Contribution({self.amount}, {self.currency}, {self.date})"


class ClubMemberRepository:
    def __init__(self):
        self.members = {}
        self.contributions = []

    def add_member(self, name, role="participant", join_date=None, status="active"):
        member_id = len(self.members) + 1
        self.members[member_id] = {
            "id": member_id,
            "name": name,
            "role": role,
            "join_date": join_date or date.today(),
            "status": status,
        }
        return member_id

    def add_contribution(self, member_id, amount, currency="RUB", date=None):
        if member_id not in self.members:
            raise ValueError(f"Участник с id {member_id} не найден")
        contribution = Contribution(amount, currency, date)
        self.contributions.append(
            {
                "id": len(self.contributions) + 1,
                "member_id": member_id,
                "amount": contribution.amount,
                "currency": contribution.currency,
                "date": contribution.date,
            }
        )
        return contribution
