def get_first_element(fst):
    print(fst[0])

user_list = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    user_list.append(input("Enter the element: "))

get_first_element(user_list)

