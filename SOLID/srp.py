class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # A second responsibility -> Not good -> Move to a seperate class
    '''
    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()
    '''

class PersistenceManager:

    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()
    
j = Journal()
j.add_entry('I cried today')
j.add_entry('I ate a bug')
print(j)


file = 'journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())