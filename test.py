# 별그리기

#----------------------------------------

# import turtle as t
# n = 5
# for i in range(n):
#   t.forward(100)
#   t.right((360/n)*2)
#   t.forward(100)
#   t.left(360/n)

# 별 출력

# ---------------------------------------

# for i in range(5):
#     for j in range(5):         
#         if(i>j):
#            print(" ",end="")
#         else:
#             print("*",end="")
#     print()       

# 끝자리 3 출력

# ---------------------------------------

# i = 0
# while True:
#     if(not(i%10==3)):
#         i += 1
#         continue
#     if(i>74):
#         break
#     print(i, end=" ")
#     i += 1

# 과반수 득표

# ---------------------------------------

def solution(n,votes):
    answer = 0
    votes_len = len(votes)
    candidate = votes[0]
    count = 1

