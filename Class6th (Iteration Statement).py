#region 반복문
# 프로그램 내에서 특정한 작업을 반복적으로 수행하는 명령문입니다.

#region for문
# 반복 가능한 객체를 순회하면서 각 요소에 대해 코드를 반복 실행하는 반복문이다.

# for i in range(5):
    # print("execute")

# 반복문의 범위는 일정한 규칙에 따라 숫자를 차례대로 만들어주는 기능입니다.
#endregion

#region while문
# 특정 조건을 만족할 때까지 계속해서 주어진 명령문을 실행하는 반복문입니다.

# count = 1

# while count <= 5 :
   # print("count : ", count)

   # count = count + 1


# 반복문은 순차적으로 실행하면서 조건 분기(Branch)를 만나게 되면, 어느 쪽으로
# 실행 흐름이 갈지 미리 예측(branch prediction)합니다.
#endregion

#region continue문
# 현재 반복을 수행하지 않고 다음 반복을 수행하는 제어문입니다.

# for i in range(10) :
   # if i % 2 == 1 :
      # print(i) 

#endregion

#region break문
# 반복문의 실행을 바로 종료하는 제어문입니다.
# list = ["exception", "system", "exit"]

# for message in list:

    # if message == "system" :
        # break

    # print(message)

#endregion

#endregion