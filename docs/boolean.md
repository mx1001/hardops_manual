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

___

# More On Booleans And Curvature

Let's start by convering a cube to a sphere.

![](img\bool\c1.gif)

And then slicing it.

![](img\bool\c2.gif)

All the cross edges that are present will make the csharpen not operate correctly without some cleanup. This is due to the fact that the geometry solved the bevel modifier so if the edge flow is less than optimal so will the behavior of the bevel modifier.

![](img\bool\c3.gif)

Using the CleanMesh(E) function can help in this situation however for the exterior piece we see that cleanup will be needed. So lets clean it up.

![](img\bool\c4.gif)

I used symmetrize y and then z to put a symmetry division loop that allowed me to rip the geometry with V and then mirror it using mirror mirror which is alt + shift + y then opened up the modifier helper with ctrl + ~ and added the z axis as well.

From there is was a matter of cleanup and merging verts.
Alt + M >> Merges points. (its important to merge them in a way that doesnt affect silouette.)
GG >> Edge slide. (when dealing with form you want to move points without interupting the form. GG >> Edge slide is my favorite change to Blender)

As the geometry gets finer you can have a large bevel width because you are working in finer and finer detail. So lower the bwidth as you work lower and lower. That is why it is part of the main Q menu when the bevel modifier is present.

Let's add an additional cylindrical cutout in the front.

![](img\bool\c5.gif)

A few things to note in this example.

- when you add a subdivision to a cylinder it turns to something not nice.
Just ssharpen it. And then it will hold its form. That is due to the creasing.
- I use ssharpen on spherical shapes to smooth them. I know they have no hard edges and therefore will get smoothed only. If subdivision is there the underlying mesh will be creased so keep that in mind.
- I used the boolean hotkey of ctrl + numpad minus to subtract it then used Csharpen to apply the boolean and make the geo real. This is one of the main behaviors of csharpen.

I can clean it up much easier if I use the same symmetry tricks. However I can also use the auto-mirror to quickly mirror as well and just add the Z axis as well so lets do that.

![](img\bool\c6.gif)

After the mesh cleaning we got rid of some planar elements at the base but for the most part the bevel still looks bad. So once again its time to fix that geometry.

![](img\bool\c7.gif)

Merge here, merge there. As you do it more and more it gets easier however this is the foundation of using booleans, and bevels with curved surfaces.

![](img\bool\c8.gif)

I took the original cylinder used for the bevel and made it real again.
First I made it solid in the Settings menu. Then I reset the sstatus which made it a regular shape in the eyes of Hard Ops. From here I was able to do the following.

- apply subdivision using the modifier helper
- csharpen to add a bevel and set the mesh to a csharp form
- clean mesh(E) to dissolve planar verts like the junction on the flat faces

![](img\bool\c9.gif)

First I will add a cube and rotate it 45 to make a cut. Then use cslice in the Q menu. As you can see the geo is pretty bad. Lets finish cleaning that up.

![](img\bool\c10.gif)

The main functions used here were the following.

- ctrl + X >> dissolve geometry
- G + G >> edge slide
- alt + m >> merge

And in less than a minute the area was looking much better. All thats left is the sliced piece.
