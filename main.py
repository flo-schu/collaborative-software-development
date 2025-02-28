from csd.student import Student
from csd.team import Team

def main():
    # Create a new team
    team = Team()

    # Hard-coded relationships
    flo = Student("Flo")
    waldo = Student("Waldo")
    marie = Student("Marie")

    amelie = Student("Amelie")

    # Establish relationships
    amelie.add_neighbor(flo)

    # Add students to the team
    team.add_student(amelie)

    leo = Student("Leo")
    markus = Student("Markus")
    holzmichel = Student("Holzmichel")

    # Establish relationships
    flo.add_neighbor(waldo)
    markus.add_neighbor(flo)
    markus.add_neighbor(holzmichel)

    # Add students to the team
    team.add_student(flo)
    team.add_student(marie)
    team.add_student(leo)

    leo.add_neighbor(flo)
    leo.add_neighbor(waldo)
    team.add_student(markus)
    team.add_student(holzmichel)

    vinc = Student("Vincent")
    vinc.add_acquaintance(flo)
    team.add_student(vinc)

    markus.add_neighbor(waldo)
    markus.add_neighbor(leo)
    markus.add_neighbor(marie)
    markus.add_neighbor(amelie)
    markus.add_neighbor(vinc)

    # Draw the graph of connections based on neighbors
    team.draw_graph(connection_type='neighbors')  # Change to 'acquaintances' to visualize acquaintances

if __name__ == "__main__":
    main()