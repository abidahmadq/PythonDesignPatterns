### Builder Pattern
- Some objects are simple and can be created in a single initializer call
- Other objects require a lot of ceremony to create
- Having an object with 10 initializer arguments is not productive
- Instead, opt for piecewise construction
- When piecewise object constructtion is complicated. We provide an API to do it simply.
- Summary
  - A builder is a seperate component for building an object
  - Can either give a builder an initializer or return it via a static function
  - Make a fluent builder, return self.
  - Different facets of an object can built with different builders working in tandem with a base class.

### Factories
- Object creation logic becomes too convoluted
- Initializer is not descriptive
  - Name is always __init__
  - Cannot overload with same sets of arguments with different names
  - Can turn into optional parameter hell
- Wholesale object creation(not piecewise, unlike builder) can be outsourced to
  - A seperate method(Factory Method)
  - That may exist in a seperate class(Factory)
  - Can create hierarchy of factories with Abstract Factory
- Factory -> A componenet resposible solely for the wholesale(not piece wise) creation of object.


### Prototype
- Complicated Objects (e.g cars) aren't designed from scratch 
  - They reiterate existing designs 
- An existing design is a prototype
- We make a copy (clone) the prototype and customize it.
  - Requires a deep copy support.
- We make the cloning convenient.
- Desc: A partially or fully intialized copy or a clone.


### Singleton
- According to authors this pattern maybe sign of a design smell.
- For components it only makes sense to have one in the system.
  - Database Repository
  - Object Factory
- Eg -> The initializer call is expensive.
- Want to prevent anyone from creating additional copies.
- Need to take care of lazy instantiation.
- A component which is instantiated only once.
- Testing Singleton is difficult
