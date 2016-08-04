## Hard Ops Boolean system
___

![](img\smack.gif)

# Boolean Basics

> With the Hard Ops 8 update. Booltool is no longer a required dependency. In fact it is recommended to use the new system instead since it's more catered to our own tools.

**If Booltool is present it will respect it and not assign our hotkeys.**

The hotkeys are as follows
  - ctrl + numpad + / performs union
  - ctrl + numpad - / performs subtraction
  - ctrl + numpad * / peforms slicing

There is also a display for the operator to let you know details about the operation.

![img](.\img\bool\b1.gif)

As of now the boolean tool has 3 alternate solutions.
 - CarveMod (most stable, worst topo)
 - Carve (same as Carvemod except it applies it immediately)
 - B-Mesh (least stable, best topo result)

CarveMod is the default and will operate similar to the booltool itself.
Carve is the same thing as carve mod except it applies it and doesn't keep the boolean live. Below is an example of CarveMod versus Carve.

![img](.\img\bool\b2.gif)

Bmesh will require there to be guidance edges in order to ensure a successful cut. This is something thats best practiced on a simple object to best practice. Not having guidance edges with bmesh will result in cuts not working properly.

___

# Booleans And Curvature

Curvature can be a tricky thing to use with booleans and to be honest there is no shortcut to efficient geometry however there are some understandings that can make it easier.

> Using a boolean on a cylinder is the same in Hard Ops as it would be with just booleans alone.

![](img\bool\b3.gif)

As you can see the geometric result was quite bad. This is due to the surfacing / curves ngons and the bevel on top. There are a couple of ways to fix this.

  -adding geometry around the area to isolate the normal shading

  -removing doubles for double vertices in the same areas while merging near miss vertices

  This can require a small amout of work however we are always looking into ways to improve this.

  The difference between them can be quite immense.

  ![](img\bool\b4.png)

This is how it was cleaned up.

![](img\bool\b5.gif)



This video was a study of sort of curved surfaces and how it works with inserts and slicing.

https://youtu.be/B8X7BDMCJ40


___

# Pokeball example

A nice demonstration of the inadequacies of booleans for hard surfaces can be shown in making a pokeball. I did a small study about how it can be done quickly with booleans versus efficiently with a cast modifier and subdivision blocking.

> Booleans
![](img\bool\b6.gif)

![](img\bool\b7.png)
You can see with the surfaces that there is still a little touchup work to be done. However I must say that Hard Ops is not just for booleans it also is a tool for helping get a "finished" result. So now lets try using a cast modifier with subdivision to get the shape more sharper.

>Cast Modifier With Subdivision Blocking
![](img\bool\b8.gif)

![](img\bool\b9.png)
In this example the finishing was done via the Csharpen while the initial shape is blocked in using modifiers efficiently and the cast modifier. While this can't work in all cases. It just serves as an example of an alternative way to approach such a shape.
