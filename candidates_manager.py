import json


class CandidatesManager:

    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return f"CandidatesManager ({self.path})"

    def load(self):
        """Возвращает список записей из файла"""
        with open(self.path, encoding="UTF-8") as file:
            data = json.load(file)
        return data

    def get_all(self):
        """Получает всех кандидатов"""
        candidates = self.load()
        return candidates

    def get_one(self, cid):
        """Получает кандидата по номеру (id)"""
        candidates = self.get_all()
        for candidate in candidates:
            if cid == candidate["id"]:
                return candidate

    def by_name(self, name):
        """Получает список кандидатов по имени (name)"""
        candidates = self.load()
        name = name.lower()
        matching_candidates = [candidate for candidate in candidates if name in candidate["name"].lower()]
        return matching_candidates

    def by_skill(self, skill):
        """Получает список кандидатов по навыку (skill)"""
        candidates = self.load()
        skill = skill.lower()
        matching_candidates = [candidate for candidate in candidates if skill in candidate["skills"].lower().split(", ")]
        return matching_candidates