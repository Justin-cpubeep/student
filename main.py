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
        target_id = input('삭제하려는 고객의 ID를 입력하세요 >>> ').strip()
        delok = 0
        for idx, student in enumerate(stdlist):
            if student['id'] == target_id:
                data = stdlist.pop(idx)
                print('{}님의 정보가 삭제되었습니다.'.format(data['id']))
                delok=1
                break
        if delok == 0:
            print('등록되지 않은 이메일입니다.')
        print(stdlist)
        page = len(stdlist)-1

    elif order=="V":
        print("학생을 조회합니다.")

    elif order=="I":
        print("학생 성적을 입력합니다.")
        target_id = input("성적을 입력할 학생 ID를 입력하세요 >>> ")
        found = False
        for student in stdlist:
            if student["id"] == target_id:
                found = True
                try:
                    student["korean"] = int(input("국어 성적 입력 >>> "))
                    student["english"] = int(input("영어 성적 입력 >>> "))
                    student["math"] = int(input("수학 성적 입력 >>> "))
                    print("성적 입력 완료:", student)
                except ValueError:
                    print("성적은 숫자로 입력해야 합니다.")
                break
        if not found:
            print("해당 ID의 학생을 찾을 수 없습니다.")
        print(student)
        stdlist.append(student)
        print(stdlist)
        page = len(stdlist)-1

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