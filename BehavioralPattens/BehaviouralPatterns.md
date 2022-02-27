### Mediator
- Facilates communication between componenets.
- Components may go in and out of a system at any time.
  - Chat rooms 
  - Players in a MMORPG
- It makes no sense for them to have direct references to one another
  - As these references may go dead at any time
- Solution: Have them all refer to some central component that facilitates communication.
- A component that facilitates communication between other components without them necessarily being aware of each other or having direct access to each other.


### Memento
- Keep a memento of an objects state to return to that state
- An object or system goes through changes
- There are different ways of navigating those changes.
- One way is to record every change(Command) and teach a command to undo itself.
- Another is to simple save the snapshots of the System. (Memento).
- A Token/Handle representing the system state. Let us rollback to the state when the tocken was generated. May or may not directly expose state information.

### Statergy
- System behavior partially specified at runtime.
- Many Algorithms can be decomposed into higher and lower level parts.
- Making tea can be decomposed into 
  - The process of making a hot beverage( boil water, pour into cup); and
  - Tea-specific things (put teabag into water)
- The high level algorithm can then be resused for making coffee or hot chocolate
  - Supported by beverage-specific strategies.
- Enables the exact behavior of a system to be selected run-time.

### Template
- A high level blueprint for an algorithm to be completed by inheritors
- Algorithms can be decomposed into common parts + specifics
- Strategy patter does this through composition
  - High level algorithm expects strategies to conform to an interface.
  - Concrete implementations implement the interface.
- Template Method does the same thing through inheritance
  - Overall Algorithm definded in base class.
  - Inheritors override the abstract method.
  - Template method invoked to get work done.
- Allows us to define the skeleton of the algorithm, with concrete implementation in sub class.