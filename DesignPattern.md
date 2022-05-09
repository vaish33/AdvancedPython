python-patterns
===============

A collection of design patterns and idioms in Python.

Current Patterns
----------------

__Creational Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [abstract_factory](AbstractFactoryMethod.py)| use a generic function with specific factories |
| [borg]| a singleton with shared-state among instances |
| [builder](BuilderPattern.py)| instead of using multiple constructors, builder object receives parameters and returns constructed objects |
| [factory](Factory.py) | delegate a specialized function/method to create instances |
| [lazy_evaluation]| lazily-evaluated property pattern in Python |
| [pool] | preinstantiate and maintain a group of instances of the same type |
| [prototype] | use a factory and clones of a prototype for new instances (if instantiation is expensive) |

__Structural Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [3-tier]| data<->business logic<->presentation separation (strict relationships) |
| [adapter] | adapt one interface to another using a white-list |
| [bridge]| a client-provider middleman to soften interface changes |
| [composite] | lets clients treat individual objects and compositions uniformly |
| [decorator] | wrap functionality with other functionality in order to affect outputs |
| [facade] | use one class as an API to a number of others |
| [flyweight] | transparently reuse existing instances of objects with similar/identical state |
| [front_controller] | single handler requests coming to the application |
| [mvc]| model<->view<->controller (non-strict relationships) |
| [proxy] | an object funnels operations to something else |

__Behavioral Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [chain_of_responsibility] | apply a chain of successive handlers to try and process the data |
| [catalog] | general methods will call different specialized methods based on construction parameter |
| [chaining_method] | continue callback next object method |
| [command]| bundle a command and arguments to call later |
| [iterator] | traverse a container and access the container's elements |
| [iterator] (alt. impl.)| traverse a container and access the container's elements |
| [mediator] | an object that knows how to connect other objects and act as a proxy |
| [memento] | generate an opaque token that can be used to go back to a previous state |
| [observer] | provide a callback for notification of events/changes to data |
| [publish_subscribe]| a source syndicates events/data to 0+ registered listeners |
| [registry]| keep track of all subclasses of a given class |
| [specification] |  business rules can be recombined by chaining the business rules together using boolean logic |
| [state] | logic is organized into a discrete number of potential states and the next state that can be transitioned to |
| [strategy] | selectable operations over the same data |
| [template] | an object imposes a structure but takes pluggable components |
| [visitor] | invoke a callback for all items of a collection |

__Design for Testability Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [dependency_injection] | 3 variants of dependency injection |

__Fundamental Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [delegation_pattern] | an object handles a request by delegating to a second object (the delegate) |

__Others__:

| Pattern | Description |
|:-------:| ----------- |
| [blackboard]| architectural model, assemble different sub-system knowledge to build a solution, AI approach - non gang of four pattern |
| [graph_search]| graphing algorithms - non gang of four pattern |
| [hsm]| hierarchical state machine - non gang of four pattern |