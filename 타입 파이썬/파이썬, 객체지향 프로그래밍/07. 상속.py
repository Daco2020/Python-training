'''
상속 (inheritance)
부모 Class의 속성값과 행위(methods)을 그대로 상속 받고 행위(methods)의 일부분을 수정해야 할 경우
상속받은 자식 Class에서 해당 행위(methods)만 다시 수정하여 사용할 수 있도록 한다. 
또한 자식 Class에서 추가적으로 속성값이나 행위(methods)를 정의할 수 있게 한다.

1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.

2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.

3. 메서드 오버라이딩

4. Super( )

5. Python의 모든 클래스는 object 클래스를 상속한다. : 모든 것은 객체이다.

6, mro( ) : 상속 관계를 보여준다.

'''

class Parent:
    def __init__(self, name):
        self.name = name
    
    def say_name(self):
        return f"Hello, My name is {self.name}."
    

class Child(Parent):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name) 
        # super().__init__()은 Child의 __init__이 재정이되기 전의 __init__을 의미한다.
        # super()는 부모의 메서드를 호출하는데에도 사용가능하다.
        # super()의 핵심은 현재 클래스의 재정의 여부와 상관없이 재정의 전의 메서드를 호출한다는 점이다.
        
    def say_age(self):
        return f"I'm {self.age} years old"
    

child = Child('김자식', 15)

print(child.say_name())
print(child.say_age())


