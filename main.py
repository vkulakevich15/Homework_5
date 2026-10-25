from warriors import Warrior, Orc, fight


print("\n first_warrior")
w = Warrior()
print(w)
print("Жив:", w.is_alive)


print("\n Арифметика ")
w + 5
print("После +5:", w)
w * 2
print("После *2:", w)


print("\n second_warrior ")
second_warrior = Orc()
print(second_warrior)
print("Урон 1-го удара:", second_warrior.get_damage())
print("Урон 2-го удара:", second_warrior.get_damage())
print("Урон 3-го удара с яростью:", second_warrior.get_damage())


print("\n Бой ")
boris = Warrior()
emelya = Orc()
print("До боя:")
print(" ", boris)
print(" ", emelya)

result = fight(boris, emelya)
print("Победил первый воин", result)

print("Результаты боя и количество атак:")
print(" ", boris)
print(" ", emelya)