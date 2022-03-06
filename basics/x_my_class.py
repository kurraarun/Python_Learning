

class myclass():
    def method1(self):
        print('My class method1 ')
    def method2(self,someString):
        print('My class method2 ' +someString)

def main():
    c= myclass()
    c.method1()
    c.method2("This is string boss")

if __name__ == "__main__":
    main()