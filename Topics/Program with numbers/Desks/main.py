first_math_group_students = int(input())
second_math_group_students = int(input())
third_math_group_students = int(input())

first_math_group_desks = first_math_group_students // 2 + first_math_group_students % 2
second_math_group_desks = second_math_group_students // 2 + second_math_group_students % 2
third_math_group_desks = third_math_group_students // 2 + third_math_group_students % 2

desks_needed = first_math_group_desks + second_math_group_desks + third_math_group_desks

print(desks_needed)
