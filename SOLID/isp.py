
### DONT DO THIS
class Machine:
    def print(self, document): #Create Seperate Interfaces for each of them
        raise NotImplementedError
    
    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):

    def print(self, document):
        print("Do Something!")
    
    def fax(self, document):
        print("Do Something!")

    def scan(self, document):
        print("Do Something!")
    
class OldFashionPrinter(Machine):

    def print(self, document):
        print("Do Something!")
    
    def fax(self, document):
        ''' Not Supported'''
        raise NotImplementedError('Printer cannong fax!')

    def scan(self, document):
        ''' Not Supported '''
        raise NotImplementedError('Printer cannong scan!')

### DO THE ABOVE THIS WAY
def Printer:
    @abstractmethod
    def print(self, document):
        pass

def Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class PhotoCopier(Printer, Scanner):
    def print(self, document):
        print(document)
    
    def scan(self, document)
        pass

class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner)
        self.printer = printer
        self.scanner = scanner
    
    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.printer.scan(document)