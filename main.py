stdlist=[
    {'id': '202501', 'name': 'kim', 'korean': 95, 'english': 80, 'math': 85},
    {'id': '202502', 'name': 'park', 'korean': 75, 'english':89 , 'math': 20},
    {'id': '202503', 'name': 'lee', 'korean': 100, 'english': 60, 'math': 40},
    {'id': '202504', 'name': 'hong', 'korean': 55, 'english': 63, 'math': 92},
    {'id': '202505', 'name': 'jo', 'korean': 99, 'english': 98, 'math': 100},
    {'id': '202506', 'name': 'jeong', 'korean': 21, 'english': 34, 'math': 11},
    {'id': '202507', 'name': 'choi', 'korean': 43, 'english': 56, 'math': 39}
]
accumulatedID=3
page=-1
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
while True:
    if order=="C":
        print("학생을 생성합니다.")
    elif order=="D":
        print("학생을 삭제합니다.")
    elif order=="V":
        print("학생을 조회합니다.")
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