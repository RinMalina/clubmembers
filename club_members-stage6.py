# === Stage 6: Генерация идентификаторов ===
# Project: ClubMembers
import string
import uuid


PROJECT_PREFIX = "clubmem"
_counter = 0


def _next_alphanumeric() -> str:
    global _counter
    chars = string.ascii_letters + string.digits
    while True:
        token = "".join(chars[(uuid.getrandom_bytes(4)).hex()])
        candidate = f"{PROJECT_PREFIX}-{token}"
        if candidate not in _taken:
            _counter += 1
            _taken.add(candidate)
            return candidate


def generate_member_id() -> str:
    """Генерация уникального идентификатора участника с префиксом проекта."""
    return _next_alphanumeric()


def generate_dues_id() -> str:
    """Генерация уникального идентификатора взноса с префиксом проекта."""
    return _next_alphanumeric()


_taken = set()


if __name__ == "__main__":
    first = generate_member_id()
    second = generate_member_id()
    third = generate_member_id()
    print(f"member_1={first}")
    print(f"member_2={second}")
    print(f"member_3={third}")
    if first in (second, third) or second == third:
        raise RuntimeError("Обнаружена коллизия идентификаторов")
    print("Коллизии отсутствуют, все идентификаторы уникальны")
