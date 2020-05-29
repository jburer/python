#val = 100

#print(val)
#print(val.__hash__())
#print("falcon".__hash__())
#print((1,).__hash__())


class User:

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def __eq__(self, other):
        return self.name == other.name and self.occupation == other.occupation

    def __hash__(self):
        return hash((self.name, self.occupation))

    def __str__(self):
        return f'{self.name} {self.occupation}'


u1 = User('John Doe', 'gardener')
u2 = User('John Doe', 'gardener')

users = {u1, u2}

print(len(users))

print('hash of user 1')
print(hash(u1))

print('hash of user 2')
print(hash(u2))

if (u1 == u2):
    print('same user')
    print(f'{u1} == {u2}')
else:
    print('different users')
    print(f'{u1} != {u2}')

# users = {u1, u2}
# print(len(users))

print('------------------------------------')

u1.occupation = 'programmer'

users = {u1, u2}

print(len(users))

if (u1 == u2):
    print('same user')
    print(f'{u1} == {u2}')
else:
    print('different users')