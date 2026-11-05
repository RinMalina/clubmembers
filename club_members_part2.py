# === Stage 2: Проверка полей ===
# Project: ClubMembers
"""club_members: нормализация и валидация сущности «участник».

Модуль полностью самодостаточен: использует только стандартную
библиотеку и не ссылается на другие файлы проекта.
"""

from datetime import datetime
from typing import Any, Dict, List

# Допустимые роли участника клуба.
VALID_ROLES: List[str] = ("участник", "организатор", "гость")

# Допустимые статусы участника клуба.
VALID_STATUSES: List[str] = ("активный", "приостановлен", "выбыл")

# Формат даты вступления, принимаемый реестром.
DATE_FORMAT: str = "%Y-%m-%d"


def normalize_name(value: Any) -> str:
    """Нормализовать имя участника.

    Обрезает пробелы по краям, заменяет внутренние множественные
    пробелы на одиночные и приводит к читаемому виду.
    """
    if value is None:
        return ""
    text = str(value).strip()
    return " ".join(text.split())


def normalize_role(value: Any) -> str:
    """Нормализовать роль участника.

    Приводит роль к нижнему регистру, убирает лишние пробелы и
    сопоставляет с допустимыми значениями по ключевым словам.
    """
    if value is None:
        return ""
    text = normalize_name(value).lower()
    for role in VALID_ROLES:
        if role and role in text:
            return role
    return ""


def normalize_status(value: Any) -> str:
    """Нормализовать статус участника.

    Приводит статус к нижнему регистру, убирает лишние пробелы и
    сопоставляет с допустимыми значениями по ключевым словам.
    """
    if value is None:
        return ""
    text = normalize_name(value).lower()
    for status in VALID_STATUSES:
        if status and status in text:
            return status
    return ""


def parse_join_date(value: Any) -> str:
    """Сформировать строку даты вступления в формате ДД.ММ.ГГГГ.

    Если значение не похоже на дату, возвращается пустая строка.
    """
    if value is None:
        return ""
    text = str(value).strip()
    if not text:
        return ""
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(text, fmt).strftime(DATE_FORMAT)
        except ValueError:
            continue
    return ""


def validate_participant(data: Dict[str, Any]) -> List[str]:
    """Проверить данные сущности «участник».

    Возвращает список сообщений об ошибках. Если список пуст, данные
    валидны.
    """
    errors: List[str] = []

    name = normalize_name(data.get("name"))
    if not name:
        errors.append("Имя участника обязательно.")

    role = normalize_role(data.get("role"))
    if not role:
        errors.append(
            "Роль должна быть одной из: " + ", ".join(VALID_ROLES) + "."
        )

    status = normalize_status(data.get("status"))
    if not status:
        errors.append(
            "Статус должен быть одним из: " + ", ".join(VALID_STATUSES) + "."
        )

    join_date = parse_join_date(data.get("join_date"))
    if not join_date:
        errors.append("Дата вступления должна быть в формате ДД.ММ.ГГГГ.")

    return errors


def normalize_participant(data: Dict[str, Any]) -> Dict[str, Any]:
    """Нормализовать данные сущности «участник».

    Применяет нормализацию ко всем полям и возвращает новый словарь
    с нормализованными значениями.
    """
    return {
        "name": normalize_name(data.get("name")),
        "role": normalize_role(data.get("role")),
        "join_date": parse_join_date(data.get("join_date")),
        "status": normalize_status(data.get("status")),
    }
