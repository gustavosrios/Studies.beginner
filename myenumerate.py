lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]
def my_enumerate(iterable, start=0):
    i = 0
    while i < 5: #star 0
        
        yield i
        i += 1
    return i
for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))