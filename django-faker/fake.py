from faker import Faker

myfake = Faker()

# seed 파일: 코드를 실행할 때마다 같은 data가 도출 되기를 원할 때
# seed 번호: 각각의 각자 data의 데이터 번호
Faker.seed(1)

# Faker의 메소드를 통해 어떤 종류의 가짜 data를 뽑아낼지 결정 가능
print(myfake.name())
print(myfake.address())
print(myfake.text())
print(myfake.state())       # 미국 state 이름
print(myfake.sentence())
print(myfake.random_number())


# 한국어로 사용하고 싶은 경우
myfake2 = Faker('ko_KR')

print(myfake2.name())
print(myfake2.address())
# print(myfake.text())      한국어는 사용에 제한이 있음
# print(myfake.state())
# print(myfake.sentence())
print(myfake2.random_number())