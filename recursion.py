# count = 0
# # head recursion

# def func():
#     global count
#     if count == 4:
#         return
#     else:
#         print('shivansh')
#         count+=1
#         func()
        
        
# func()


# tail recursion
count1 = 0
def func1():
    global count1
    if count1==4:
        return
    count1+=1
    func1()
    print('shivansh')
    
    
func1()