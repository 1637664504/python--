
def fun_a():
    assert 1==2, "1不等于2" 
    print('aaa')

def fun_b():
    fun_a()
    print('bbb')

def fun_c():
    fun_b()
    print('ccc')

fun_c()

''' 
Traceback (most recent call last):
  File "./1_assert_断言测试.py", line 14, in <module>
    fun_c()
  File "./1_assert_断言测试.py", line 11, in fun_c
    fun_b()
  File "./1_assert_断言测试.py", line 7, in fun_b
    fun_a()
  File "./1_assert_断言测试.py", line 3, in fun_a
    assert 1==2, "1不等于2" 
AssertionError: 1不等于2 
'''

''' 
结论
异常追踪是 下源
'''