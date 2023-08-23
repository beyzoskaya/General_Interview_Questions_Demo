from collections import deque

class AnimalShelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.timestamp = 0
    def enqueue(self, animal_type):
        self.timestamp += 1
        animal = {'type' : animal_type, 'timestamp' : self.timestamp}
        if animal_type == 'dog':
            self.dogs.append(animal)
        elif animal_type == 'cat':
            self.cats.append(animal)
        else:
            raise ValueError("Invalid animal type.")
    def dequeueAny(self):
        if len(self.dogs) == 0:
            return self.dequeueCat()
        elif len(self.cats) == 0:
            return self.dequeueDog()
        else:
            if self.dogs[0]['timestamp'] < self.cats[0]['timestamp']:
                return self.dequeueDog()
            else:
                return self.dequeueCat()
    
    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        return self.dogs.popleft()
    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        return self.cats.popleft()
    
shelter = AnimalShelter()
shelter.enqueue('dog')
shelter.enqueue('cat')
shelter.enqueue('dog')
shelter.enqueue('cat')

print(shelter.dequeueAny())  # Output: {'type': 'dog', 'timestamp': 1}
print(shelter.dequeueCat())  # Output: {'type': 'cat', 'timestamp': 2}
print(shelter.dequeueDog())  # Output: {'type': 'dog', 'timestamp': 3}