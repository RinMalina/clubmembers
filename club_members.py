# === Stage 1: Каркас модуля ===
# Project: ClubMembers
from dataclasses import dataclass
from datetime import date


@dataclass
class Participant:
    name: str
    role: str
    join_date: date
    status: str


def sample_participants() -> list[Participant]:
    return [
        Participant("Анна", "администратор", date(2024, 1, 15), "активный"),
        Participant("Борис", "участник", date(2024, 3, 22), "активный"),
        Participant("Виктор", "участник", date(2023, 11, 5), "пассивный"),
    ]


def main() -> None:
    for p in sample_participants():
        print(f"{p.name} | {p.role} | {p.join_date} | {p.status}")


if __name__ == "__main__":
    main()
