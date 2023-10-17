queue = []
stack = []

print("You need to enter Client's name, Paid or End!")

while True:
    command = input()

    #проверява ако потребителя е въвел End 
    if command.lower() == "end":
        #Оставащите хора са равни на колкото object-a има в опашката
        remaining_people = len(queue)
        #Докато има нещо в листа 'stack'
        while stack:
            #Придава стойноста на customer от първия елемент на List-a 'stack' и я премахва от него
            customer = stack.pop(0)
            print(customer)
        print(f"{remaining_people} people remaining.")
        break
    #проверява ако потребителя е въвел Paid
    if command.lower() == "paid":
        #Докато има нещо в листа 'queue'
        while queue:
            #Придава стойноста на customer от първия елемент на List-a 'queue' и я премахва от него
            customer = queue.pop(0)
            stack.append(customer)
    #Ако не е въведено Paid или End 
    else:
        #Добавя въведеното от потребителя в List-a 'queue'
        queue.append(command)
