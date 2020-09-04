# myapp.py  ----> myapp.py가 여기에 복붙되어서 모듈로 실행되는 것이라 생각!!!!!!!!!
# 만일 myapp.py에 __name__이 있다면
#import sys


class MenuItem:  # 범용적 -> 재사용 가능함, 코드 재사용이 함수 때보다 더 좋아짐
    def __init__(self, title, action=None):  # 타이틀은 필수(문자열), 선택됐을 때 취할 행돟ㅇ,기능(함수)은 액션->디폴트넌
        self.title = title
        self.action = action  # self가 누군지 알고 싶으면 호출하는 곳으로 가야함
        # 위의 action은 지역변수, 다른 곳에서도 쓰고 싶음.. 그래서 인스턴스 변수로 저장해두는 것

    def __str__(self):  # 현재 내부 정보 리턴
        return f"<MenuItem {self.title}>"

    def __repr__(self):  # 컬렉션에 담겨있는 걸 호출할 때는 이 함수가 호출된다
        return f"<MenuItem {self.title}>"

    def run(self):  # 이 메뉴가 선택됐을 때 내가 하기로 했던 일을 수행해주는 메소드
        self.action()  # 전달받은 행동 실행, 함수 호출

    # item = MenuItem("열기", lambda : print("열기 실행"))  #lamda의 매개변수 없는 함수


class Menu:  # MenuItem을 Menu로 통합해서 관리... /  범용적
    def __init__(self):
        self.menus = []  # 메뉴 아이템 관리할 리스트

    def add(self, menu_item):  # self.menus(목록)에 메뉴아이템 넣는 함수
        self.menus.append(menu_item)

    def print(self):  # 목록의 메뉴아이템 출력
        print(f"[메뉴] ", end='')
        for no, menu in enumerate(self.menus):
            print(f"{no}:{menu.title} ", end='')  # menu.title -> menu의 타이틀
        print()

    def run(self, select):  # select -> index, 선택된 메뉴 아이템 실행
        if select >= len(self.menus):
            print('잘못된 메뉴 선택입니다')
            return

        menu_item = self.menus[select]
        menu_item.run()
    # self.menus[select].run()


class Application:  # 범용 클래스
    def __init__(self):
        self.menu = Menu()  # 어플리케이션이 메뉴를 하나 가진다, 공통특징
        self.create_menu(self.menu)

    def create_menu(self, menu):
        pass

    def run(self):  # 어플리케이션 바뀌더라도 안 바뀜.. / 공통 메소드
        while True:
            self.menu.print()  # 메뉴 보여주고
            sel = int(input("메뉴의 번호를 입력하세요 : "))  # 메뉴 선택하고
            self.menu.run(sel)  # 메뉴 실행하고


if __name__ == "__main__":
    pass