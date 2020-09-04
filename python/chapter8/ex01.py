def swap(x, y):
    temp = y
    y = x           # 스택 프레임 안에 있음
    x = temp

    print("x", x)
    print("y", y)   # 스와프 안에 프린트 함수 호출, 스와프 스택 프레임 위에 프린트 스택프레임 생성


a = 10       # 데이터 파트 중 전역 영역에 있음, 함수 영향 안 받음
b = 20
swap(a, b)   # 위로 갔다가 돌아왔을 때, 위의 a=10, b=20은 그대로 있어야 한다, 데이터
             # 데이터 유지해야 한다


print("a", a)
print("b", b)     # 이번 경우에는 함수 내 조작이 원본에 영향을 미치지 않는다
                  # 왜 각각의 함수에서 동일한 변수의 이름을 사용했는데 왜 다 다르냐
                  # 함수처리를 시스템이 어떻게 관리함? 데이터 파트, 코드 파트
                  # 다른 곳에 데이터 있음, 그걸 가져와서 사용
                  # 코드는 실행하게 되면 수정 불가
                  # 데이터는 동적
                  # 함수 관리를 스택으로 한다
                  # 함수가 끝났을 때 어디로 돌아갈 것인가 기억하고 있어야 한다 (전 것 기억)
