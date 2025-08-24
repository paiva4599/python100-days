import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_friend = random.randint(0, (len(friends) - 1))
print(f"The one paying the bill is {friends[random_friend]}")

print(random.choice(friends))