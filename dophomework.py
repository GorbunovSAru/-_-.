grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Джонни', 'Бильбо', 'Стив', 'Хендрик', 'Аарон'}
students = sorted(students) # Сортировка по алфавиту
a = (sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]),
     sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])) # определение среднего балла
klass = {students[0]: a[0], students[1]: a[1], students[2]: a[2],
         students[3]: a[3], students[4]: a[4]} # Словарь класса с оценкой каждого ученика

print(klass)
