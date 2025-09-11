# ===== 샘플 학생 7명 =====
stdlist = [
    {'id': '202501', 'name': 'kim',   'korean': 95, 'english': 80, 'math': 85},
    {'id': '202502', 'name': 'park',  'korean': 75, 'english': 89, 'math': 20},
    {'id': '202503', 'name': 'lee',   'korean': 100, 'english': 60, 'math': 40},
    {'id': '202504', 'name': 'hong',  'korean': 55, 'english': 63, 'math': 92},
    {'id': '202505', 'name': 'jo',    'korean': 99, 'english': 98, 'math': 100},
    {'id': '202506', 'name': 'jeong', 'korean': 21, 'english': 34, 'math': 11},
    {'id': '202507', 'name': 'choi',  'korean': 43, 'english': 56, 'math': 39}
]

# 현재 학생 위치 (아직 조회 전이라 -1)
PAGE = -1

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

        for i, stu in enumerate(students):
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
            stu = students[PAGE]
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
        elif PAGE < len(students) - 1:
            PAGE += 1
            stu = students[PAGE]
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
            stu = students[PAGE]
            print("[현재 학생]")
            print("이름:", stu["name"],
                  "국어:", stu["korean"],
                  "영어:", stu["english"],
                  "수학:", stu["math"])