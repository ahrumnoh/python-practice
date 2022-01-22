class bostonPackage:
    def detail(self):
        print("[보스톤 패키지 5반 6일] 보스톤, 하버드대학교 투어 200만원")


if __name__ == "__main__":

    print("Boston.py 모듈을 직접실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행되어짐")
    trip_to = bostonPackage()
    trip_to.detail()

else:
    print("boston.py 외부에서 모듈 호출")
