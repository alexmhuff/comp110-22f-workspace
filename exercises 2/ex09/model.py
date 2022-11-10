"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730484416"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other_point: Point) -> float:
        """Calculating the distance between two cells."""
        return sqrt(((self.x - other_point.x) ** 2) + ((self.y - other_point.y) ** 2))


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        result: str = ""
        if self.is_vulnerable():
            result = "gray"
        if self.is_infected():
            result = "pink"
        if self.is_immune():
            result = "green"
        return result
    
    def contract_disease(self) -> None:
        """"Making a cell contract a disease."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Affirming a cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Affirming if a cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def contact_with(self, another_cell_object: Cell) -> None:
        """Cells infecting other cells of they're in contact."""
        if self.is_infected() and another_cell_object.is_vulnerable():
            another_cell_object.contract_disease()
        if another_cell_object.is_infected() and self.is_vulnerable():
            self.contract_disease()

    def immunize(self) -> None:
        """Immunizing a cell."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Affirming a cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False



class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):  # given number of cells and speed we want them moving around at
        """Initialize the cells with random locations and directions."""
        self.population = []  # initialized to be an empty list; construct cells number of new cells and set them up so that they have random locations and random speeds
        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        # ADD A LOOP (for in range)
        for i in range(infected_cells):
            self.population[i].contract_disease()
        i: int = infected_cells
        while i < infected_cells + immune_cells:
            self.population[i].immunize()
            i += 1
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checking if cells are in contact with each other."""
        i: int = 0
        j: int = 0
        while i < len(self.population):
            j = i + 1
            while j < len(self.population):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
                j += 1
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        i : int = 0
        while i < len(self.population):
            if self.population[i].is_infected():
                return False
            i += 1
        return True