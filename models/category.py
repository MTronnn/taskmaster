class Category:
    """Класс для представления финансовой категории."""
    
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.date = date
        self.type = type  
    
    def __repr__(self):
        return f"Transaction({self.amount}, {self.category}, {self.date})"
