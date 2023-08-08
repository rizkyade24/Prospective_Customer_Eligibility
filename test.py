a = list(map(int, input().split()))
b = [ ]
while i < len(a):
     if a[i] == 2 or a[i] == 3:
          b.append(a[i])
          a[i] = 0 
    else: 
     i += 1
print("A =", a)
print(len(b))

def make_list(number):
     names = []
     for item in number: 
          names.append(input("Enter your name with a capital letter"))
    print(names)

number = int(input("How many names need to be entered"))
names = make_list(number)
for name in names:
     if name [1] == "A":
          print("Name ", name, " starts with A")

class Character(BaseSprite):
class BaseSprite(pygame.sprite.Sprite):
class Enemy1(Enemy):
class Actor(Character):
class Enemy(Actor):