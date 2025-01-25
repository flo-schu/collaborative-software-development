class Student:
    def __init__(self, name: str):
        self.name = name
        self.neighbors = []       # List to store neighboring students
        self.acquaintances = []   # List to store acquaintances

    def add_neighbor(self, neighbor: 'Student'):
        """Add a neighbor to this student."""
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
            neighbor.add_neighbor(self)  # Add self to neighbor's neighbors

    def add_acquaintance(self, acquaintance: 'Student'):
        """Add an acquaintance to this student."""
        if acquaintance not in self.acquaintances:
            self.acquaintances.append(acquaintance)
            acquaintance.add_acquaintance(self)  # Add self to acquaintance's acquaintances

    def describe(self):
        """Provide a description of the student."""
        return (f"{self.name}, "
                f"Neighbors: {[n.name for n in self.neighbors]}, "
                f"Acquaintances: {[a.name for a in self.acquaintances]}")