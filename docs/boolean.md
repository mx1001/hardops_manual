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

# Booleans In Action
