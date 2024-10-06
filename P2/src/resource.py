# src/resource.py

class Resource:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.allocated = 0
    def allocate(self, amount):
        if self.allocated + amount <= self.capacity:
            self.allocated += amount
        else:
            raise ValueError(f"Cannot allocate {amount}. Exceeds capacity.")
    def release(self, amount):
        if self.allocated - amount >= 0:
            self.allocated -= amount
        else:
            raise ValueError(f"Cannot release {amount}. Below 0 allocation.")
    def __str__(self):
        return f"{self.name}: {self.allocated}/{self.capacity}"
class Node:
    def __init__(self, name):
        self.name = name
        self.resources = []
    def add_resource(self, resource):
        self.resources.append(resource)
    def allocate_resource(self, resource_name, amount):
        for res in self.resources:
            if res.name == resource_name:
                res.allocate(amount)
    def release_resource(self, resource_name, amount):
        for res in self.resources:
            if res.name == resource_name:
                res.release(amount)
    def __str__(self):
        return f"Node: {self.name}, Resources: {[str(res) for res in self.resources]}"


