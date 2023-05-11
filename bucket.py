# Бакет для хранения файлов (в том числе и html файлов/страниц)

class Bucket:
    '''Объектное хранилище для статического вебсайта (иммитация)'''
    
    def __init__(self, tutorial):
        if tutorial is not None:
            self.content.append(tutorial)
        self.content = []
    
    def __str__(self) -> str:
        return 'Содержимое:' + ', '.join(self.content)
    
    def __bool__(self):
        return self.content != []
    
    
    def add_file(self, file):
        print('Добавлен', file)
        self.content.append(file)

    def inspect(self):
        print('Текущее состояние бакета:')
        for i in self.content:
            print('  ', i)


website = Bucket('README.md')
website.add_file('index.html')
print(website.content)
website.inspect()
print(website)

# new_bucket = Bucket()
# print(bool(new_bucket))
print()




