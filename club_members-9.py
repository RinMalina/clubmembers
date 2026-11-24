# === Stage 9: Текстовый поиск ===
# Project: ClubMembers
clubmembers_search.py

from typing import List, Dict, Any, Callable


def normalize_text(text: Any) -> str:
    if text is None:
        return ""
    return str(text).strip().lower()


def build_search_fields(member: Dict[str, Any]) -> Dict[str, str]:
    fields: Dict[str, str] = {}
    for key in ("name", "role", "join_date", "status"):
        if key in member:
            fields[key] = normalize_text(member[key])
    return fields


def find_matches(fields: Dict[str, str], query: Any) -> List[int]:
    query_norm = normalize_text(query).strip()
    if not query_norm:
        return []
    matches: List[int] = []
    for index, value in fields.items():
        if query_norm in value:
            matches.append(index)
    return matches


def build_highlighter(fields: Dict[str, str], query: Any) -> Callable[[str], str]:
    query_norm = normalize_text(query).strip()
    if not query_norm:
        return lambda text: text
    tokens = set()
    for key in ("name", "role", "join_date", "status"):
        if key in fields:
            for token in query_norm.split():
                if token and token in fields[key]:
                    tokens.add(token)
    if not tokens:
        return lambda text: text

    def highlight(text: Any) -> str:
        if text is None:
            return ""
        result = str(text)
        for token in sorted(tokens, key=len, reverse=True):
            pattern = " " + token + " "
            if pattern in result:
                result = result.replace(pattern, " " + token + " ", case_insensitive=False)
        return result

    return highlight


def format_search_result(member: Dict[str, str], query: Any) -> str:
    fields = build_search_fields(member)
    matched_keys = find_matches(fields, query)
    if not matched_keys:
        return ""
    lines: List[str] = [f"Имя: {member.get('name') or ''}"]
    for key in ("role", "join_date", "status"):
        if key in member:
            lines.append(f"{key}: {member[key]}")
    for key in ("name", "role", "join_date", "status"):
        if key in member and key in matched_keys:
            lines[-1] = f"{key}: {build_highlighter(fields, query)(member[key])}"
    return "\n".join(lines)
