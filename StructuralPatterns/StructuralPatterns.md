### Adapter 
- Example -> Electrical devices have different power requirements.
- Thus we use a special device ( and adapter) to give us the interface we require from the interface we have
- A construct which adapts and existing interface X to conform to the required interface Y.

### Bridge
- Connecting components together through abstractions.
- Can be premptive or cooperative
- Can run on Windows or Unix
- End up with a 2x2 scenario
- A mechanism that decouples an interface - (hierarchy) from an implementation. 

### Composite
- Treating individual and aggregate objects uniformly
- Objects use other objects properties/members through inheritance and composition
- Composition lets us make compound objects
  - A mathematical expression composed of simple expressions
  - A grouping of shapes that consists of several shape.
- Composite design pattern is used to treat both sinlge and composite objects uniformly
  - Foo & Sequence have common API's.

### Facade
- Exposing Several components through a single interface.
- Balance complexity and presentaion/usability
- Typical home
  - Many subsystem(electrical, sanitation)
  - Complex internal structure
  - End user is not exposed to internals.
- Same with software
  - Many systems working to provide flexibility
  - API consumers want it to just work.
- Provides a simple, easy to understand user interface over a large sophisticated body of code.

### Proxy 
- An interface for accessing a particular resource
- You are calling foo.Bar()
- This assumes that foo is in the same process as Bar()
- What if, later on, you want to put all Foo related operations into a seperate process.
  - Can we avoid changing the code?
- Proxy can be used here.
  - Same interface, entirely different behaviour.
- This is called a communication proxy.
  - Other Types: Logging, Virtual, Guarding etc.
- A class that functions as an interface to particular resource. That resource may be remote, expensive to construct, or may require logging or some other added functionality.
- Two Types -> Protection & Virtual
- Proxy vs Decorator
  - Proxy provides an identical interface --------------- decorator provides and enchanced interface.
  - Proxy doesn't do thios --------------- Decorator Typically aggragates what it is decorating.
  - Proxy might not even be working with a materialized object.