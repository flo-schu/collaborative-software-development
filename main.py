from csd.student import Student
from csd.team import Team

def main():
    # Create a new team
    team = Team()

    # Hard-coded relationships
    flo = Student("Flo")
    waldo = Student("Waldo")

    # Establish relationships
    flo.add_neighbor(waldo)

    # Add students to the team
    team.add_student(flo)

    vinc = Student("Vincent")
    vinc.add_acquaintance(flo)
    team.add_student(Student("Vincent"))
    

    # Draw the graph of connections based on neighbors
    team.draw_graph(connection_type='neighbors')  # Change to 'acquaintances' to visualize acquaintances

if __name__ == "__main__":
    main()