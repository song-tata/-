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

# candidate[n]에 득표수 저장 += count 해서 비교하기


def solution(n,votes):
    answer = 0
    votes_len = len(votes)
    candidate = votes[0]
    count = 1
    for j in range(votes_len):
      # 후보자 수 만큼 반복, votes[j]번째와 같다면, candidate[j]번째를 증가시키고,
      # 다음 반복문 실행 
      for i in range(1,n):
        if(i==votes[j]):
          candidate[j] += count
          break
    # 제일 많이 받은 후보 찾아내는 방법
    
    
    
    
    return answer
 

n = 3
votes = [1,2,3,2,1,3,2,1,3]  
candidate = votes[0]
print(range(len(votes)))

for i in range(n):
   candidate[i] = 0
for j in range(len(votes)):
      # 후보자 수 만큼 반복, votes[j]번째와 같다면, candidate[j]번째를 증가시키고,
      # 다음 반복문 실행 
      for i in range(n):
        if(i+1==votes[j]):
          candidate[i] += 1

print(candidate)
# for i in votes:
#   print(i)
# list 순서 뒤집기

#-----------------------------

# def solution(arr):
#     left = 0
#     right = len(arr)-1
#     # for i in range(len(arr)):
#     #     idx = arr[left]
#     #     arr[left] = arr[right]
#     #     arr[right] = idx
#     #     left += 1
#     #     right -= 1
#     #     if(left>right):
#     #         break 
#     while(left<right):
#         tmp = arr[left]
#         arr[left] = arr[right]
#         arr[right] = tmp
#         left += 1
#         right -= 1 
#     return arr

# arr1 = [1,2,3,4]
# arr2 = [3,5,7,8,2,1]

# print(solution(arr1))
# print(solution(arr2))

# 징검다리 건너기

# ------------------------

# stones = [1,1,3,2,4,2,1,3,1,2]

# cnt = 0
# n = len(stones)
# frog_rocation = 0
# while(n>frog_rocation):
#     cnt += 1
#     frog_rocation += stones[frog_rocation]
# print(stones)
# print(str(cnt)+"번 뜀")


# import random
# a = random.randint(1,6)

# arr = [1,2,3,4]
# arr.pop()
