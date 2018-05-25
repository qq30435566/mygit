content = """

Structure of Code is Key

Thanks to the way imports and modules are handled in Python, it is relatively easy to structure a Python project. Easy, here, means that you do not have many constraints and that the module importing model is easy to grasp. Therefore, you are left with the pure architectural task of crafting the different parts of your project and their interactions.

Easy structuring of a project means it is also easy to do it poorly. Some signs of a poorly structured project include:

    Multiple and messy circular dependencies: if your classes Table and Chair in furn.py need to import Carpenter from workers.py to answer a question such as table.isdoneby(), and if conversely the class Carpenter needs to import Table and Chair, to answer the question carpenter.whatdo(), then you have a circular dependency. In this case you will have to resort to fragile hacks such as using import statements inside methods or functions.
    Hidden coupling: each and every change in Table’s implementation breaks 20 tests in unrelated test cases because it breaks Carpenter’s code, which requires very careful surgery to adapt the change. This means you have too many assumptions about Table in Carpenter’s code or the reverse.
    Heavy usage of global state or context: instead of explicitly passing (height, width, type, wood) to each other, Table and Carpenter rely on global variables that can be modified and are modified on the fly by different agents. You need to scrutinize all access to these global variables to understand why a rectangular table became a square, and discover that remote template code is also modifying this context, messing with table dimensions.
    Spaghetti code: multiple pages of nested if clauses and for loops with a lot of copy-pasted procedural code and no proper segmentation are known as spaghetti code. Python’s meaningful indentation (one of its most controversial features) make it very hard to maintain this kind of code. So the good news is that you might not see too much of it.
    Ravioli code is more likely in Python: it consists of hundreds of similar little pieces of logic, often classes or objects, without proper structure. If you never can remember if you have to use FurnitureTable, AssetTable or Table, or even TableNew for your task at hand, you might be swimming in ravioli code.

"""

lines = content.splitlines()

new_content = ''
width = 90
for line in lines:
    if line:    # 去掉空白行
        while len(line) > width:
            print(line[:width], end='')
            line = line[width:]

            while line[0] != " ":
                # 避免换行是拆开单词, 找到空格位置换行
                print(line[0], end='')
                line = line[1:]

            line = line[1:]     # 去掉行首空格
            print()

        print(line)

