import datetime

class Inventory:
    def __init__(self, name, category, quantity, created_at=None, updated_at=None, id=None):
        self.name = name
        self.category = category
        self.created_at = created_at if created_at is not None else datetime.datetime.now().isoformat()
        self.updated_at = updated_at if updated_at is not None else datetime.datetime.now().isoformat()
        self.quantity = quantity
        self.id = id if id is not None else None