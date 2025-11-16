from linked_list import LinkedList


my_list = LinkedList()

for i in range(4):
    my_list.add_to_tail(i)

print(my_list)
print(my_list[2])

empty_list = LinkedList()

print(empty_list)

print(my_list.find_by_value(10))

print(f"Размер списка - {my_list.size}")
del (my_list[2])
print(f"Размер списка - {my_list.size}")
print(my_list)
my_list.del_tail()
print(my_list)
my_list.del_head()
print(my_list)
my_list[0] = 10
print(my_list)
