#!/usr/bin/env python3
"""
This module explains basics Object Oriented Programming
using characters from "Transformers: Rise of the Beasts" movie
"""


class Transformer:
    """
    A base class representing a Transformer character from
    "Transformers: Rise of the Beasts"

    Attributes
    ----------
    name : str
        The name of the Transformer.

    Methods
    -------
    attack()
        Performs an attack action.
    defend()
        Performs a defense action.
    """
    def __init__(self, name):
        self.name = name

    def attack(self):
        """Performs an attack action."""
        print(f"{self.name} is attacking!")

    def defend(self):
        """Performs a defense action."""
        print(f"{self.name} is defending!")


class Autobot(Transformer):
    """
    A subclass representing an Autobot character
    from "Transformers: Rise of the Beasts".

    Attributes
    ----------
    vehicle_mode : str
        The vehicle mode of the Autobot.

    Methods
    -------
    transform()
        Transforms the Autobot into vehicle mode.
    """
    def __init__(self, name, vehicle_mode):
        super().__init__(name)
        self.vehicle_mode = vehicle_mode

    def transform(self):
        """Transforms the Autobot into vehicle mode."""
        print(f"{self.name} is transforming into {self.vehicle_mode}!")

    @property
    def vehicle_mode(self) -> str:
        """Returns the vehicle mode of the Autobot."""
        return self._vehicle_mode

    @vehicle_mode.setter
    def vehicle_mode(self, vehicle_mode: str):
        """Sets the vehicle mode of the Autobot"""
        self._vehicle_mode = vehicle_mode.title()


class Maximal(Transformer):
    """
    A subclass representing a Maximal character from
    "Transformers: Rise of the Beasts".

    Attributes
    ----------
    beast_mode : str
        The beast mode of the Maximal.

    Methods
    -------
    maximize()
        Transforms the Maximal into beast mode.
    """
    faction = "Maximals"

    def __init__(self, name, beast_mode):
        super().__init__(name)
        self.beast_mode = beast_mode

    def maximize(self):
        """Transforms the Maximal into beast mode."""
        print(f"{self.name} is maximizing into {self.beast_mode}!")


class Terrorcon(Transformer):
    """
    A subclass representing a Terrorcon character from
    "Transformers: Rise of the Beasts".

    Attributes
    ----------
    vehicle_mode : str
        The vehicle mode of the Terrorcon.

    Methods
    -------
    terrorize()
        Transforms the Terrorcon into vehicle mode.

    """
    leader = None

    def __init__(self, name, vehicle_mode):
        super().__init__(name)
        self.vehicle_mode = vehicle_mode

    def terrorize(self):
        """Transforms the Terrorcon into vehicle mode."""
        print(f"{self.name} is terrorizing as {self.vehicle_mode}!")

    @classmethod
    def announce_leader(cls):
        """Announces Scourge as the leader of the Terrorcons."""
        if cls.leader is not None:
            print(f"The leader of the Terrorcons is {cls.leader}.")
        else:
            print("The leader of the Terrorcons has not been established.")


