from dataclasses import dataclass,field
from typing import List

@dataclass
class C:
    mylist: List[int] = field(default_factory=list)
    explain: List[str] = field(default_factory=list)
    author: List[str] = field(default_factory=list)

c = C()
c.mylist += [1, 2, 3]
c.explain += ['这是一个','测试功能']
c.author += ['Aimar','lili']
print(c.mylist,c.explain,c.author)
