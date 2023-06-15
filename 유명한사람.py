def knows(a, b):
    # 사람 a가 사람 b를 알고 있는지 여부를 반환하는 가상의 함수
    # 실제 구현은 문제의 조건에 맞게 구현되어야 합니다.
    pass

def find_famous_person(n):
    famous_person = 0

    # 유명한 사람을 찾기 위해 모든 사람을 확인합니다.
    for i in range(1, n):
        # 유명한 사람이 다른 사람을 알고 있으면 다음 사람으로 넘어갑니다.
        if knows(famous_person, i):
            continue
        # 유명한 사람이 i를 모르는 경우, i를 유명한 사람으로 설정합니다.
        famous_person = i

    # 유명한 사람을 모르는지 확인합니다.
    for i in range(n):
        # 유명한 사람을 제외한 다른 사람이 유명한 사람을 알고 있는 경우,
        # 유명한 사람이 아니므로 -1을 반환합니다.
        if i != famous_person and (not knows(i, famous_person) or knows(famous_person, i)):
            return -1

    # 유명한 사람을 반환합니다.
    return famous_person
