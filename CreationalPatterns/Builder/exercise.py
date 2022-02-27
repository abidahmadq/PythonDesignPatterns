class Field:

    def __init__(self, name='', value=''):
        self.variable_name = name
        self.variable_value = value

    def __str__(self):
        return 'self.%s = %s' % (self.variable_name, self.variable_value)    

class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []
    
    def __str__(self):
        lines = ['class %s:' % self.name]
        if not self.fields:
            lines.append('  pass')
        else:
            lines.append('  def __init__(self):')
            for field in self.fields:
                lines.append('    %s' % field)
        return "\n".join(lines)


class CodeBuilder:
    def __init__(self, root_name):
        self.__root = Class(root_name)

    def add_field(self, name, value):
        self.__root.fields.append(Field(name, value))
        return self

    def __str__(self):
        return self.__root.__str__()


cb = CodeBuilder('Person').add_field('name', "").add_field('age', '0')

print(cb)