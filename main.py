stdlist=[
    {'id': '202501', 'name': 'kim', 'korean': 95, 'english': 80, 'math': 85},
    {'id': '202502', 'name': 'park', 'korean': 75, 'english':89 , 'math': 20},
    {'id': '202503', 'name': 'lee', 'korean': 100, 'english': 60, 'math': 40},
    {'id': '202504', 'name': 'hong', 'korean': 55, 'english': 63, 'math': 92},
    {'id': '202505', 'name': 'jo', 'korean': 99, 'english': 98, 'math': 100},
    {'id': '202506', 'name': 'jeong', 'korean': 21, 'english': 34, 'math': 11},
    {'id': '202507', 'name': 'choi', 'korean': 43, 'english': 56, 'math': 39}
]
accumulatedID=8
page=-1

while True:
    order=input(
    """
    C: 학생 추가,
    D: 학생 삭제,
    V: 학생 조회,
    I: 성적 입력,
    M: 성적 수정,
    Q: 작업 종료
    """
    ).upper()
    if order=="C":
        print("학생을 생성합니다.")
        student={"korean":None,"math":None,"english":None}
        # 100명 이내라 가정
        s_id="2025"+"0"*(2-len(str(accumulatedID)))+str(accumulatedID)
        s_name=input("학생 이름을 입력해주세요: ")
        student["id"]=s_id
        student["name"]=s_name
        accumulatedID+=1
        if page==-1:
            page=0
        stdlist.append(student)
        print(stdlist)
    elif order=="D":
        print("학생을 삭제합니다.")
    elif order=="V":
        print("학생을 조회합니다.")


        # ===== 조회 기능 루프 (절차적) =====
        while True:
            print("\n[학생 조회 기능]")
            print("1) ID로 조회   2) 이전 학생   3) 다음 학생   4) 현재 학생 보기   0) 종료")

            cmd = input("메뉴 선택: ")

            if cmd == "0":  # 종료
                print("조회 기능을 종료합니다.")
                break

            elif cmd == "1":  # ID로 조회
                sid = input("조회할 학생 ID 입력: ")

                if not sid.isdigit():
                    print("[안내] ID는 숫자여야 합니다.")
                    continue

                sid = int(sid)
                found = False

                for i, stu in enumerate(stdlist):
                    if stu["id"] == sid:
                        PAGE = i
                        print("[조회 결과]")
                        print("이름:", stu["name"],
                            "국어:", stu["korean"],
                            "영어:", stu["english"],
                            "수학:", stu["math"])
                        found = True
                        break

                if not found:
                    print(f"[안내] ID {sid} 학생을 찾을 수 없습니다.")

            elif cmd == "2":  # 이전 학생
                if PAGE == -1:
                    print("[안내] 아직 조회된 학생이 없습니다. 먼저 ID로 조회하세요.")
                elif PAGE > 0:
                    PAGE -= 1
                    stu = stdlist[PAGE]
                    print("[이전 학생]")
                    print("이름:", stu["name"],
                        "국어:", stu["korean"],
                        "영어:", stu["english"],
                        "수학:", stu["math"])
                else:
                    print("[안내] 이미 첫 번째 학생입니다.")

            elif cmd == "3":  # 다음 학생
                if PAGE == -1:
                    print("[안내] 아직 조회된 학생이 없습니다. 먼저 ID로 조회하세요.")
                elif PAGE < len(stdlist) - 1:
                    PAGE += 1
                    stu = stdlist[PAGE]
                    print("[다음 학생]")
                    print("이름:", stu["name"],
                        "국어:", stu["korean"],
                        "영어:", stu["english"],
                        "수학:", stu["math"])
                else:
                    print("[안내] 이미 마지막 학생입니다.")

            elif cmd == "4":  # 현재 학생
                if PAGE == -1:
                    print("[안내] 아직 조회된 학생이 없습니다. 먼저 ID로 조회하세요.")
                else:
                    stu = stdlist[PAGE]
                    print("[현재 학생]")
                    print("이름:", stu["name"],
                        "국어:", stu["korean"],
                        "영어:", stu["english"],
                        "수학:", stu["math"])
            
    elif order=="I":
        print("학생 성적을 입력합니다.")
    elif order=="M":
        print("학생 성적을 수정합니다.")
        while True:
            choice1=input('수정하시려는 학생의 ID를 입력하세요 : ') # ID 존재 여부 체크 필요
            idx=-1
            for i in range(0,len(stdlist)):
                if stdlist[i]['id'] == choice1:
                    idx=i
            if idx==-1:
                print('등록되지 않은 학생의 ID입니다.')       
                break
                        
            choice2=input('''
            다음 중 수정하실 정보를 골라주세요 .
                    name, korean, english, math
            (수정할 정보가 없으면 'exit' 입력)
            ''')
            if choice2 in ('name','korean','english','math'):
                stdlist[idx][choice2]=input('수정할 {}을 입력하세요 :'.format(choice2))
                break
            elif choice2 =='exit':
                break
            else:
                print('존재하지 않는 정보입니다.')
                break

    elif order=="Q":
        print("작업을 종료합니다.")
        break