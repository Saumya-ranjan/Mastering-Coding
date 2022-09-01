# queue = 'FIFO'
# elem = ''
# stack1 = []
# stack2 = []
# for i in queue:
#     stack1.append(i)
# print(stack1)
# for j in range(len(stack1)):
#     stack2.append(stack1[-1])
#     stack1.pop(-1)
# for i in range(len(stack2)):
#     elem+=stack2[-1]
#     stack2.pop(-1)
# print(elem)
   
    
# Implementing stack using Queues:

# stack = 'FIFO'
# container = ''
# queue1 = []
# queue2 = []
# for i in stack:
#     queue1.append(i)

# while len(queue1)!=0:
#     for i in range(len(queue1)):
#         if len(queue1) != 1:
#             queue2.append(queue1[0])
#             queue1.pop(0)
#         else:
#             container+=queue1[0]
#             queue1.pop()
#     queue1 ,queue2 = queue2 , queue1
# print(container)

    




        
        