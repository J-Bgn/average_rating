grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]#дано
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}#дано
#посчитаем финальную оценку(возможно, здесь можно сделать изящнее без внесения вручную):
final_score= sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])
students= sorted(students)#сортировка множества, так как грейды в алфавитном порядке, а студенты в разброс
average_rating = dict(zip(students, final_score))#создадим словарь
print(average_rating)#результат