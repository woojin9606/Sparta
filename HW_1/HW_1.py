#1.args, kwargs를 사용하는 예제 코드 짜보기
def hw1(*args, **kwargs):
    print(args)
    print(kwargs)
    return

a = [1, 2, 3, 4, 5]
b = {'test1' : 1, 'test2' : 2, 'test3' : 3, 'test4' : 4}
hw1(*a,**b)

#2. mutable과 immutable은 어떤 특성이있고, 어떤 자료형이 어디에 해당하는지 서술하기
# mutable 은 주소값을 넘겨주고 immutale은 값을 넘겨줌
# 주소값이 아닌 값을 넘겨주려면 deepcopy() 나 [:]를 사용
immutable = "String is immutalbe!!"
mutable = ["list is mutable!!"]
string = immutable
list_ = mutable
string += " immutable string!!"
list_.append("mutable list!!")
print(immutable)
print(mutable)
print(string)
print(list_)

#3.DB Field에서 사용되는 Key 종류와 특징 서술하기
# pk , fk, uk 등이 있음
# pk = Primary Key 즉 기본키로 후보키 중 하나를 선정하여 대표로 삼는 키
# fk = Foreign Key 즉 외래키로 다른 테이블의 기본키를 참조하는 속성
# uk = Unique Key 각 필드의 값이 테이블 내에서 유일한 값을 가지는 필드로 만듬

#4. django에서 queryset과 object는 어떻게 다른지 서술하기
# qeuryset은 객체들을 담고있는 목록 object는 객체