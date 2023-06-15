# Object Oriented Programming basics: Transformers: Rise of the Beasts

![Transformers: Rise of the Beasts](images/poster.jpg)

This module explains the basics of Object-Oriented Programming using characters from the "Transformers: Rise of the Beasts" movie.

## Classes

### Transformer

A base class representing a Transformer character from "Transformers: Rise of the Beasts"

#### Attributes

- `name`: The name of the Transformer.

#### Methods

- `attack()`: Performs an attack action.
- `defend()`: Performs a defense action.

### Autobot

A subclass representing an Autobot character from "Transformers: Rise of the Beasts".

#### Attributes

- `vehicle_mode`: The vehicle mode of the Autobot.

#### Methods

- `transform()`: Transforms the Autobot into vehicle mode.

### Maximal

A subclass representing a Maximal character from "Transformers: Rise of the Beasts".

#### Attributes

- `beast_mode`: The beast mode of the Maximal.
- `faction`: The faction of the Maximal (set to "Maximals").

#### Methods

- `maximize()`: Transforms the Maximal into beast mode.

### Terrorcon

A subclass representing a Terrorcon character from "Transformers: Rise of the Beasts".

#### Attributes

- `vehicle_mode`: The vehicle mode of the Terrorcon.
- `faction`: The faction of the Terrorcon (set to "Terrorcons").
- `leader`: The leader of the Terrorcons (initially set to None).

#### Methods

- `terrorize()`: Transforms the Terrorcon into vehicle mode.

#### Class Methods

- `announce_leader()`: Announces the leader of the Terrorcons.

---

Feel free to explore and use these classes to create your own Transformer characters and simulate their actions in the "Transformers: Rise of the Beasts" universe!



## Installation

```
$ git clone git@github.com:rolandoquiroz/oop.git
$ cd oop
3 pip install -r requirements.txt
```

```python
# Example Usage

# Create Autobot instance
optimus_prime = Autobot("Optimus Prime", "truck")

# Transform Autobot into vehicle mode
optimus_prime.transform()

# Output: "Optimus Prime is transforming into Truck!"

# Create Maximal instance
optimus_primal = Maximal("Optimus Primal", "gorilla")

# Maximize Maximal into beast mode
optimus_primal.maximize()

# Output: "Optimus Primal is maximizing into Gorilla!"

# Create Terrorcon instance
scourge = Terrorcon("Scourge", "logging truck")

# Terrorize as a Terrorcon
scourge.terrorize()

# Output: "Scourge is terrorizing by transforming into Jet!"

# Announce leader of the Terrorcons
Terrorcon.announce_leader()

# Output: "The leader of the Terrorcons has not been established."


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

MIT