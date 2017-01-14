## How to get started with Hard Ops

![url](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\computer.gif)

Hard Ops can seem daunting however all the commands do basic things. So I recommend learning the ropes on basic objects to practice just to get used to the menus. In the next few examples I'll be going over how I use Hard Ops in my day to day work.

# Example #1
# Ssharp / Csharp Workflow

Try out modelling basic shapes and using the sharpeners. I usually do a small
trial run to warm up with the tools.

> In this example I right clicked my x-symmetrize and remapped it to
alt + x in object mode. This is part of my default scene but we allowed some options
to be able to be right clicked and allowed hotkeys.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\xsymset.gif)

> Here you see me using basic shapes and the Q menu to get started.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\p1.gif)

Its just a matter of my making mesh changes and adjusting the bwidth. Usually as
the model gets more detailed the bevel size gets shrunk. There is another
 workflow involving cstep however this is a bit more advanced. For now we will focus
 on the csharp / ssharp boolean workflow.

Many of the tools perform ssharp or csharp after the fact in order to do a post
operation surfacing of sorts.

One example would be the cslice. Cslice was made by AR as an alternative to my
rebool. Both of them have their cases and can be used interchagably depending
on the situation.

- rebool requires a pending boolean. Meaning you must set up a boolean with ctrl + (numpad +/-)
- cslice is the process. select two meshes and it will cut. That is all.

> In some cases it's easier to cslice however in the example you can see it did not
 work out so quickly so therefore setting it up was necessary. It's not a matter
 of one over the other but using whichever works best for your needs.

 ![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\rb-cs.gif)

So continuing on. As we make more cuts and the details become closer. Its
important to lower the bevel width distance to keep the mesh looking good.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\p2.gif)

___

# Example #2

Let's start with a cube.
![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq1.png)

> In the top corner it specifies that this object is UNDEFINED. This ensures when I press Q the options are for meshes that are not considered beveled.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq2.gif)

When I first press Q these are the options I am presented.

  - SSharpen (soft sharpening without bevelling)
  - CSharpen (soft sharpening with bevel modifier added)
  - Tthick (add thickness to the volume via solifify)

I will start out Csharpening the object then use B-Width to adjust the bevel.

> Bwidth will show up on the main menu when an object is beveled via Csharpen

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq3.gif)

From this point I will use booleans to make additional cuts into the object.

The hotkeys used are:
  - ctrl + numpad - (Subtractive Boolean)
  - ctrl + numpad / (Slice Boolean)

  - alt + shift + x (mirror mirror X axis)

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq4.gif)

This can be alot to take in at once so I'll explain what I did here.

-  (shift + a) >> insert cube and used it with Slice Boolean to slice the center piece out.

- Added another cube and used Q >> operations >> b-width to put a simple bevel on the object without going into csharp.

> This was necessary because it is not recommended to use csharp objects to cut into csharp objects. This will result in bevel weight information being baked in that is not wanted. Here is an example.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq5.gif)

- (Ctrl + Numpad -) >> Subtractive Boolean then I used Csharp to apply the boolean to the object and calculate the sharpening.

- Deleted one side, selected the piece to mirror and then the body to mirror accross. (alt + shift + x)

> By mirroring it across the other side I am able to work on one side while the other is updated automatically. This allows me to cut more things out and the objects will retain their properties.

So continuing with these ideas in mind you can make something complex quickly even in just object mode.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq6.gif)

However the combination of both object mode and edit mode tools can allow for some interesting ideas. Especially when you focus on particular shapes and areas.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq7.gif)

> In this example I used a plane with knife project to force a plane in the ngon surface that resulted from the boolean operation.

Here is an example of me using edit mode to add some custom details.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq8.gif)

> In edit mode I have shift + ~ mapped to select boundary loop. This allows me to select a region then convert it to only the exterior loop. This isn't a hard Ops feature so you will have to map it manually.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq9.gif)

- Isolated the face with only 4 points with shift + h to hide alternate geometry
- W >> Subdivide (x2) / A >> select all >> shift + ~ >> select boundary.
- ctrl + shift + tab to switch to vert selection >> ctrl + I >> invert selection
> This step is useful because converting the exterior points to circles would not look as good. So I have become used to separating isolating the edge area for a buffer.
![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq10.gif)
- Q >> Meshtools >> Circle (Nth)
- E >> Extrude >> Alt + S >> Push on normal

While this sounds like a lot of buttons. I press these within a few seconds and can only say that it becomes easier as you get used to it.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq11.gif)

In this example I used demote to remove the modifier bevelling so that I could bevel it myself and give it a larger bevel. I also used another cube to cut more out of it.

Even this cube that I used to cut in the front section still has a use. I will simple scale it and then use it to slice out those pieces into manifold meshes of their own.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq12.gif)

> You might have noticed an error that happened after the initial cslice. Its important to note that sometimes if you cut close to edges you have to lower the bevel width to keep it working correctly.

After cutting you might have also noticed that I used alt + x to symmetrize the object (destructive symmetry) then used alt + shift + x to symmetrize the front cutout to the other side of the front base. The cutout received non destructive symmetry because the two piece do not touch. This keeps the bevel, mirror, and booleans behaving predictably.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq13.gif)

Using the basic tools a decent amount of detail is able to be accomplished in a short time.

This is just one way to use the tool but I hope this helps in getting started!
![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq14.jpg)

[More Getting Started](getstarted)
___

# Is there a hotkey guide?

# [Yes!](shortcuts)
___

# What is the difference between Ssharpen and Csharpen?

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\computer2.gif)

**SSharpen** is short for soft sharpen. We called it that because it does the following.

  - edit mode >> select sharps >> mark sharps, bevel weight, subdiv crease
  - sets mesh to smooth
  - enables autosmooth

To do it manually it looks like this.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq15.gif)

Alternatively Q >> Ssharpen does all of the steps for you.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq16.gif)

[See Csharpen](ssharpen)

**CSharpen** is short for complex sharpen. Complex sharpen does all that Ssharpen does and more.

  What else does it do?

  - applies modifiers that are not excluded from the list
  - adds a bevel modifier to the object
  - changes the mesh state to Csharp which changes the options in the Q menu.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\faq\faq17.gif)

> The initial options are based on the most likely options for basic meshes. When the mesh is in Csharp state you have a higher likelyhood of wanting to see options for adjusting the bevel alternatively if you added a solifidy after bevelling it via csharp it would fold in on itself.

All I can recommend for now is also reading the additional chapters on Csharpen and Ssharpen and play with them yourself to best understand them.

[See Csharpen](csharpen)

___



![img](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\getusedtoit.gif)
