t_questions = int(input("How many questions are made? : "))
list_questions = []
answer = []

x = 1
while x <= t_questions:
    questions = input("Question no {} : ".format(x))
    list_questions.append(questions)
    x+=1

print("============================")

# make variable questions again
for q in list_questions:
    questions = input(q + " : ")
    answer.append(questions)

print("============================")

print("Answer : ")
for a in answer:
    print(a)
