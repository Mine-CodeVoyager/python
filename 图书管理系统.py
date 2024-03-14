#定义书的相关信息#
class Book():
    def __init__(self,name,author,status,book_index):
        self.name=name
        self.author=author
        self.status=status
        self.book_index=book_index

    def __str__(self):
        if self.status==1:
            self.status='未借出'
        elif self.status==0:
            self.status='已借出'
        else:
            self.status='状态异常'
        return f"书名：《{self.name}》，作者:{self.author}，状态<{self.status}>,位置:{self.book_index}"

#定义图书管理系统#
class BookManage():
    books=[]
    def start(self):
        self.books.append(Book('平凡的世界','路遥',1,'IS001'))
        self.books.append(Book('风声', '麦家', 0, 'IS002'))
        self.books.append(Book('朝花夕拾', '鲁迅', 1, 'IS003'))

    def Menu(self):    #定义菜单#
        self.start()
        while True:
            print("""
            --------------------图书管理系统--------------------
            1.查询图书
            2.增加图书
            3.借阅图书
            4.归还图书
            5.退出系统
            """)
            choice=input("请选择：")
            if choice=='1':
                self.show()
            elif choice=='2':
                self.add()
            elif choice=='3':
                self.borrow()
            elif choice=='4':
                self.return_book()
            elif choice=='5':
                print('欢迎下次使用.')
                break
            else:
                print('输入错误')
    def show(self):
        for book in self.books:
            print(book)
    def add(self):
        name=input('书名:')
        author=input('作者：')
        book_index=input('位置：')
        self.books.append(Book(name,author,1,book_index))
        print(f'图书《{name}》增加成功')
    def check(self,name):
        for book in self.books:
            if book.name==name:
                return book
        return None
    def borrow(self):
        name=input('借阅图书名字：')
        ret=self.check(name)
        if ret:
            if ret.status==0:
                print(f'书籍《{name}》已借出')
            else:
                print(f"书籍《{name}》借阅成功")
                ret.status=0
        else:
            print(f"书籍《{name}》不存在")
    def return_book(self):
        name=input("归还图书名字：")
        ret= self.check(name)
        if ret:
            if ret.status==0:
                print(f'书籍《{name}》归还成功')
                ret.status=1
            else:
                print(f'书籍《{name}》未借出')
        else:
            print(f"书籍《{name}》不存在")

if __name__ == '__main__':
    manager=BookManage()
    manager.Menu()
