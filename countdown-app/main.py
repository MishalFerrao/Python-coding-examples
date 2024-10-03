import datetime


goal_and_deadline = " "
while goal_and_deadline != 'exit':
    try:
        goal_and_deadline = input("User enter the goal and its respective deadline in DD/MM/YYYY format separated by colon\n")
        goal = goal_and_deadline.split(':')[0]
        deadline = goal_and_deadline.split(':')[1]

        deadline_date = datetime.datetime.strptime(deadline,"%d/%m/%Y")
        current_date = datetime.datetime.now()
        remaining_time = deadline_date - current_date
        if remaining_time.days > 0:
            print(f"Hello User! To finsih your goal: {goal} you have {remaining_time.days} days remaining\n")
        elif remaining_time.days < 0:
            print(f"Hello User! You are {remaining_time.days*-1} days behind to achieve your goal: {goal} ")
        else:
            pass
    except:
        print("Hello User! Check your input")