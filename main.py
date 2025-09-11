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
    elif order=="I":
        print("학생 성적을 입력합니다.")
    elif order=="M":
        print("학생 성적을 수정합니다.")
    elif order=="Q":
        print("작업을 종료합니다.")
        break