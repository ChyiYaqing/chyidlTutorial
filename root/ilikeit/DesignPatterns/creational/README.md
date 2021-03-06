Creational design patterns
==========================
In plain words:
    Creational patterns are focused towards how to instantiate an object or group of related objects.
    

1. Simple Factory
-------------------
An abstract factory provides an interface for creating families of related objects without specifying their concrete classes.
Abstract Factory is a very central design pattern for **Dependency Injection(DI)**

[Python]()


2. Factory Method 
-------------------
Creates an instance of several derivel classes 


3. Abstract Factory
---------------------


4. Builder 
-----------
Separates object construction from its representation 


5. Prototype 
-------------
A fully initialized instance to be copied or cloned 


6. Singleton Pattern
----------------------
* Motivation
    - Sometimes it's important to have only one instance for a class. Using singletons are used for centralized management of internal or external resources and they provide a global point of access to themselves.
    - The singleton pattern is one of the simplest design patterns: it involves only one class which is responsible to instantiate itself, to make sure it creates not more than one instance; in the same time it provides a global point of access to that instance.

* Intent
    - Ensure that only one instance of a class is created 
    - Provide a global point of access to the object.

* Implementation
    -[C++](/root/ilikeit/DesignPatterns/creational/Singleton/implement.cpp)
    -[Python](/root/ilikeit/DesignPatterns/creational/Singleton/implement.py)

* Applicability & Examples
    - Example 1 - Logger Classes 
        * The Singleton pattern is used in the design of logger classes. This classes are usually implemented as a singleton, and provides a global logging access point in all the application components without being necessary to create an object each time a logging operations is performed.
        * [C++]()
        * [Python](/root/ilikeit/DesignPatterns/creational/Singleton/ex1_logger.py)
    - Example 2 - Configuration Classes 
        * The Singleton pattern is used to design the classes which provides the configuration settings for an application. By implementing configuration classes as Singleton not only that we provide a global access point, but we also keep the instance we use as a cache object. When the class
        is instantiated(or when a value is read) the singleton will keep the values in its internal structure. If the values are read from the database or from files this avoids the reloading the values each time the configuration parameters are used.
        * [Python]()
    - Example 3 - Accessing resources in shared mode 
        * In this case a singleton with synchronized methods could be used to manage all the operations on the serial port.
        * [Python]()
    - Example 4 - Factories implemented as Singleton 
        * Let's assume that we design an application with a factory to generate new object(Account, Customer, Site, Address objects) with their ids, in an multithreading environment. If the factory is instantiated twice in a 2 different threads then is possible to have a overlapping ids for 2 
        different objects. If we implement the Factory as a singleton we avoid this problem. Combining Abstract Factory or Factory Method and Singleton design patterns is a common practice.