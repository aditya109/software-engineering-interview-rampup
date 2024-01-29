# GRASP (object-oriented design)

General Responsibility Assignment Software Patterns (or Principles) is a set of 9 fundamental principles in object design and responsibility assignment.

1. Information expert: 
   *Problem:* What is a basic principle by which one would assign responsibilities to objects?
   *Solution:* Assign responsibility to the class that has the most information needed to fulfil it.

2. Creator: *Low Coupling, Factory Pattern*

   *Problem:* Who creates object `A` ?
   *Solution:* Assign class `B` the responsibility to create object `A` if:

   - Instances of `B` contain or compositely aggregate instances of `A`
   - Instances of `B` record instance of `A`
   - Instances of `B` closely use instances of `A`
   - Instances of `B`  have the initialization for instances of `A` and pass it on to the creation.

3. Controller: *Command, Facade, Layers, Pure Fabrication*

   *Problem:* Who should be responsible for handling an input system event?
   *Solution:* A *use case controller* should be used to deal with all system events of a use case, and may be used for more than one use case.

4. Low coupling: Coupling is a measure of how strongly one element is connected to, knows of, or relies on other elements. 
   Low coupling indicates:

   - lower dependency between the classes;
   - change in one class having a lower impact on other classes,
   - higher reuse potential.

5. High cohesion: Cohesion is a measure of the strength of the relationship between the class's methods and the data themselves.
   High cohesion indicates:

   - elements are strongly related
   - elements are highly focused on a rather specific topic.

6. Indirection:
   *Problem*: Where to assign responsibility, to avoid direct coupling between two or more things? How to decouple objects so that low coupling is supported and reuse potential remains higher?
   *Solution:* Assign the responsibility to an intermediate object to mediate between other components or services so that they are not directly coupled, the intermediary creates an indirection between the other components.

7. Polymorphism: 

   *Problem*: How to handle alternatives based on type? How to create pluggable software components? 
   *Solution:* When related alternatives or behaviours vary by type, assign responsibility for the behaviour - using polymorphic relations - to the types for which the behaviour varies.

8. Protected variations:

   *Problem*: How to design objects, subsystems, and systems so that the variations or instability in these elements do not have an undesirable impact on other elements?

   *Solution:* Identify points of predicated variation or instability; assign responsibilities to create a stable interface around them.

9. Pure fabrication:
   A pure fabrication is a class that does not represent a concept in the problem domain, specially made up to achieve low coupling, high cohesion and the reuse potential thereof derived, often called a service in DDD terms.