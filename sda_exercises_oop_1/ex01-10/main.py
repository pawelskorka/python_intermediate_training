from cat import Cat
from dog import Dog
from car import Car
from vet import Vet


def main():
    cat_object = Cat("Bonifacy")
    cat_object_2 = Cat("Doodley", "mrrr, mrrr")
    cat_object_3 = Cat("Mruczyslaw", "prr prr")
    cat_object_4 = Cat("Dandy")

    cats = [cat_object, cat_object_2, cat_object_3, cat_object_4]

    for cat in cats:
        cat_sound = cat.make_sound()
        print(cat_sound)

    cat_object.eat_mouse()
    cat_object.eat_mouse()
    cat_object.eat_mouse()
    cat_object_2.eat_mouse()
    cat_object_2.eat_mouse()

    print(f"{cat_object.name} ate {cat_object.eat_mouse()} mouses so far")
    print(f"{cat_object_2.name} ate {cat_object_2.eat_mouse()} mouses so far")

    dog_object = Dog("Jackie", "woof, woof")
    dog_object_2 = Dog("Thunder")
    dog_object_3 = Dog("Alonso")
    dog_object_4 = Dog("Morty", "ouuu, ouuu")

    dogs = [dog_object, dog_object_2, dog_object_3, dog_object_4]

    for dog in dogs:
        dog_sound = dog.make_sound()
        print(dog_sound)

    car = Car()
    print(car.move() + "\n")

    cat = Cat("New kitty appear")
    print(cat.move() + "\n")

    vet = Vet()
    print(vet.say_cat_hello(cat_object))
    print(vet.say_dog_hello(dog_object_3))
    print(Vet.say_hello(cat_object_2))


if __name__ == "__main__":
    main()
