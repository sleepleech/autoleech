TEAM_FILE = "bot/data/team.txt"

def is_team_member(user_id: int) -> bool:
    try:
        with open(TEAM_FILE, "r") as file:
            ids = file.read().splitlines()
        return str(user_id) in ids
    except Exception:
        return False
