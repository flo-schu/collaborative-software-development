import networkx as nx
import matplotlib.pyplot as plt
from csd.student import Student

class Team:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        """Add a student to the team."""
        self.students.append(student)

    def draw_graph(self, connection_type: str = 'neighbors'):
        """Draw a graph representation of the students and their connections."""
        G = nx.Graph()
        
        # Add nodes and edges to the graph based on connection type
        for student in self.students:
            G.add_node(student.name)
            if connection_type == 'neighbors':
                for neighbor in student.neighbors:
                    G.add_edge(student.name, neighbor.name)
            elif connection_type == 'acquaintances':
                for acquaintance in student.acquaintances:
                    G.add_edge(student.name, acquaintance.name)
            else:
                raise ValueError("Connection type must be either 'neighbors' or 'acquaintances'.")

        # Draw the graph
        plt.figure(figsize=(8, 6))
        nx.draw(G, with_labels=True, node_color='lightblue', font_size=10, node_size=2000)
        plt.title(f"Student Connections based on {connection_type.capitalize()}")
        plt.show()