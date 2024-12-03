to_do_list=[]
def todo():
    user_input=int(input("Press 1 to add, 2 to view , 3 to remove the todo list and 4 to exit\n"))
    if(user_input==1):
        activity=input("Enter what you want to do?\n")
        to_do_list.append(activity)
        todo()
    elif(user_input==2):
        for key,plan in enumerate(to_do_list):
            print(f"{key+1}. {plan}")
        todo()
    elif(user_input==3):
        index=int(input("Enter the index of the activity you want to remove\n"))
        remove(index)
        todo()
    elif(user_input==4):
        exit
    else:
        print("Enter valid numbers\n")
        todo()


def remove(index):
    to_do_list.pop(index-1)

print("This is a To-do list app")
todo()

