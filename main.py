students=[
    {"id":0,"name":"영희","korean":100,"english":50,"math":0},
    {"id":1,"name":"철수","korean":0,"english":50,"math":100},
    {"id":2,"name":"맹구","korean":80,"english":80,"math":80}
]
accumulatedID=3
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
    elif order=="Q":
        print("작업을 종료합니다.")
        break