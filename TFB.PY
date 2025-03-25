class Fish:
    def __init__(self, velocity):
        self.vel = velocity

def align(fish, neighbors):
    if not neighbors:
        return  # No change if no neighbors
    avg_velocity = sum(n.vel for n in neighbors) / len(neighbors)
    fish.vel += (avg_velocity - fish.vel) * 0.1  # Adjust velocity

# Test alignment
fish1 = Fish(5)
neighbor_fish = [Fish(7), Fish(9), Fish(6)]  # Other fish with different velocities

print("Before alignment, velocity:", fish1.vel)
align(fish1, neighbor_fish)
print("After alignment, velocity:", fish1.vel)
