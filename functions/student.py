def mk_student(accumulatedID,page):
    student={"korean":None,"math":None,"english":None}
    # 100명 이내라 가정
    s_id="2025"+"0"*(2-len(str(accumulatedID)))+str(accumulatedID)
    s_name=input("학생 이름을 입력해주세요: ")
    student["id"]=s_id
    student["name"]=s_name
    accumulatedID+=1
    if page==-1:
        page=0
    return accumulatedID,page,student