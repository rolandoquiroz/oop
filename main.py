#!/usr/bin/env python3
Autobot = __import__('transformer').Autobot
Maximal = __import__('transformer').Maximal
Terrorcon = __import__('transformer').Terrorcon

mirage = Autobot("Mirage", "car")
mirage.transform()
mirage.attack()

print("--")

optimus_primal = Maximal("Optimus Primal", "gorilla")
optimus_primal.maximize()
optimus_primal.attack()
print(optimus_primal.faction)

print("--")

scourge = Terrorcon("Scourge", "logging truck")
scourge.terrorize()
scourge.attack()
