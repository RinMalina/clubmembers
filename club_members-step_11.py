# === Stage 11: Теги ===
# Project: ClubMembers
class Tag:
    def __init__(self, name):
        self.name = name
        self.members = []

    def __repr__(self):
        return f"Tag({self.name!r})"


class Member:
    def __init__(self, name, role="member", join_date=None, status="active"):
        self.name = name
        self.role = role
        self.join_date = join_date
        self.status = status
        self.tags = set()

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.add(tag)

    def remove_tag(self, tag):
        self.tags.discard(tag)

    def find_tag(self, tag):
        return tag in self.tags


TAGS = {}


def add_tag_to_member(member, tag_name):
    if tag_name not in TAGS:
        TAGS[tag_name] = Tag(tag_name)
    member.add_tag(TAGS[tag_name])


def remove_tag_from_member(member, tag_name):
    if tag_name in member.tags:
        member.remove_tag(TAGS[tag_name])
        del TAGS[tag_name]


def find_members_by_tag(tag_name):
    return [m for m in TAGS[tag_name].members]


def add_member_with_tag(member, tag_name):
    add_tag_to_member(member, tag_name)
    TAGS[tag_name].members.append(member)


def remove_member_from_tag(member, tag_name):
    if member in TAGS[tag_name].members:
        TAGS[tag_name].members.remove(member)
        member.remove_tag(TAGS[tag_name])
        if not TAGS[tag_name].members:
            del TAGS[tag_name]


def search_members_by_tag(tag_name):
    return [m for m in TAGS[tag_name].members if m.find_tag(TAGS[tag_name])]
