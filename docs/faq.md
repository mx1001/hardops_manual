## FAQs / SFQs

![](img\c1.gif)

# How do I get started with Hard Ops?

Let's start with a cube.
![](img\faq\faq1.png)

> In the top corner it specifies that this object is UNDEFINED. This ensures when I press Q the options are for meshes that are not considered beveled.

![](img\faq\faq2.gif)

When I first press Q these are the options I am presented.

  - SSharpen (soft sharpening without bevelling)
  - CSharpen (soft sharpening with bevel modifier added)
  - Tthick (add thickness to the volume via solifify)

I will start out Csharpening the object then use B-Width to adjust the bevel.

> Bwidth will show up on the main menu when an object is beveled via Csharpen

![](img\faq\faq3.gif)

From this point I will use booleans to make additional cuts into the object.

The hotkeys used are:
  - ctrl + numpad - (Subtractive Boolean)
  - ctrl + numpad / (Slice Boolean)

  - alt + shift + x (mirror mirror X axis)

![](img\faq\faq4.gif)

This can be alot to take in at once so I'll explain what I did here.

-  (shift + a) >> insert cube and used it with Slice Boolean to slice the center piece out.

- Added another cube and used Q >> operations >> b-width to put a simple bevel on the object without going into csharp.

> This was necessary because it is not recommended to use csharp objects to cut into csharp objects. This will result in bevel weight information being baked in that is not wanted. Here is an example.

![](img\faq\faq5.gif)

- (Ctrl + Numpad -) >> Subtractive Boolean then I used Csharp to apply the boolean to the object and calculate the sharpening.

- Deleted one side, selected the piece to mirror and then the body to mirror accross. (alt + shift + x)

> By mirroring it across the other side I am able to work on one side while the other is updated automatically. This allows me to cut more things out and the objects will retain their properties.

So continuing with these ideas in mind you can make something complex quickly even in just object mode.

![](img\faq\faq6.gif)

However the combination of both object mode and edit mode tools can allow for some interesting ideas. Especially when you focus on particular shapes and areas.

![](img\faq\faq7.gif)

> In this example I used a plane with knife project to force a plane in the ngon surface that resulted from the boolean operation.

Here is an example of me using edit mode to add some custom details.

![](img\faq\faq8.gif)

> In edit mode I have shift + ~ mapped to select boundary loop. This allows me to select a region then convert it to only the exterior loop. This isn't a hard Ops feature so you will have to map it manually.

![](img\faq\faq9.gif)

- Isolated the face with only 4 points with shift + h to hide alternate geometry
- W >> Subdivide (x2) / A >> select all >> shift + ~ >> select boundary.
- ctrl + shift + tab to switch to vert selection >> ctrl + I >> invert selection
> This step is useful because converting the exterior points to circles would not look as good. So I have become used to separating isolating the edge area for a buffer.
![](img\faq\faq10.gif)
- Q >> Meshtools >> Circle (Nth)
- E >> Extrude >> Alt + S >> Push on normal

While this sounds like a lot of buttons. I press these within a few seconds and can only say that it becomes easier as you get used to it.

![](img\faq\faq11.gif)

In this example I used demote to remove the modifier bevelling so that I could bevel it myself and give it a larger bevel. I also used another cube to cut more out of it.

Even this cube that I used to cut in the front section still has a use. I will simple scale it and then use it to slice out those pieces into manifold meshes of their own.

![](img\faq\faq12.gif)

> You might have noticed an error that happened after the initial cslice. Its important to note that sometimes if you cut close to edges you have to lower the bevel width to keep it working correctly.

After cutting you might have also noticed that I used alt + x to symmetrize the object (destructive symmetry) then used alt + shift + x to symmetrize the front cutout to the other side of the front base. The cutout received non destructive symmetry because the two piece do not touch. This keeps the bevel, mirror, and booleans behaving predictably.

![](img\faq\faq13.gif)

Using the basic tools a decent amount of detail is able to be accomplished in a short time.

This is just one way to use the tool but I hope this helps in getting started!
![](img\faq\faq14.jpg)

[More Getting Started](getstarted)
___

# Is there a hotkey guide?

# [Yes!](shortcuts)
___

# What is the difference between Ssharpen and Csharpen?

![](img\computer2.gif)

**SSharpen** is short for soft sharpen. We called it that because it does the following.

  - edit mode >> select sharps >> mark sharps, bevel weight, subdiv crease
  - sets mesh to smooth
  - enables autosmooth

To do it manually it looks like this.

![](img\faq\faq15.gif)

Alternatively Q >> Ssharpen does all of the steps for you.

![](img\faq\faq16.gif)

[See Csharpen](ssharpen)

**CSharpen** is short for complex sharpen. Complex sharpen does all that Ssharpen does and more.

  What else does it do?

  - applies modifiers that are not excluded from the list
  - adds a bevel modifier to the object
  - changes the mesh state to Csharp which changes the options in the Q menu.

![](img\faq\faq17.gif)

> The initial options are based on the most likely options for basic meshes. When the mesh is in Csharp state you have a higher likelyhood of wanting to see options for adjusting the bevel alternatively if you added a solifidy after bevelling it via csharp it would fold in on itself.

All I can recommend for now is also reading the additional chapters on Csharpen and Ssharpen and play with them yourself to best understand them.

[See Csharpen](csharpen)

___

# What is Cstep / Sstep?

In short.

**Cstep** - bakes bevels to the mesh and hides it in edit mode for future booleans.

> Cstep is similar to Csharpen aside from the fact that it applies the bevels before re-adding it. This is where it differs from csharpen. The moment you cstep you will notice you no longer have the ability to adjust the bwidth. **This is because the bevel was applied and readded.**
This means that now you can boolean the object while being able to adjust the bevel for those singular areas.

![](img\faq\faq20.gif)

**SStep** - calculates sharpening from the mesh that is visible in edit mode. Compared to SSharpen which will unhide the mesh to calculate ssharps.

>SSharpen - unhides the mesh before ssharpening.
![](img\faq\faq18.gif)

>Sstep - only calculates ssharp from visible mesh in edit mode
![](img\faq\faq19.gif)
Sstep is basically the same as ssharpen except for unhiding the mesh. I also use this when I dont want to unhide my selection to calculate however the main purpose of this tool was for cstep workflows.

[See CStep](cstep)

___

# Why is my mesh hidden when I Cstep?

Cstep hides the mesh when used. See [How does Cstep work technically](How does Cstep work technically)

![](img\cstep\c5.gif)

> This example shows what happens when you cstep. After hitting the button in the Q menu the mesh type will say Cstep in the top left. Also the bwidth will no longer be fun. This is because it has been applied. When you go in edit mode it will be hidden.
  - press alt + h to unhide mesh
  - press h to hide mesh

In the example it shows me undo to get back to csharp state but understanding the states is essential to using the tools correctly and understanding the context.

# Can I get out of Cstep?

Absolutely. We added the ability to override states which can be useful to putting meshes back to the beginning for using alternate workflows. Here is an example.

> **q >> meshtools >> status reset** will reset any mesh back to a default state. Causing the Q menu dynamic options to also be default instead of cstep oriented.

![image](img\cstep\c6.gif)

> In this example I use cstep to block it in sort of an bake a bevel while then using the Status reset located under **q >> meshtools >> status reset**. By resetting the sstatus I was able to use Tthick which is a basic option under meshes that have no sstatus. From there I went back through a csharp / rebool workflow and ended up back in a csharp workflow to finish off the shape with finer details and a bevel with 1 segment for the edges.

___

# Why is it called Sstep / Cstep / Ssharpen / Cssharpen?

The naming made sense at the time but the functions are best described like so. Someday the tools will be unified into something more logical however in the meantime we needed some sort of terminology for naming.

___

# Can I add my own inserts to Hard Ops?

No. However it is possible but not recommended since it's not user friendly.
For custom inserts I recommend the [Asset Management](https://gumroad.com/l/kANV/). This is a temporary solution but we do have plans to expand this down the road.

___

# What do the different inserts mean?

![](img\faq\faq21.png) Orange Inserts are just basic inserts. These can be inserted in edit mode orented to faces.

> Orange inserts can be inserted on a series of faces and can be scaled immediately after selection via a modal operation. This allows for scaling to perfection. It even sets the pivot points to individual origins so they retain their position.

![](img\faq\faq24.gif)

![](img\faq\faq22.png) Red Inserts are inserts made to be boolean cut into surfaces.

![](img\faq\faq23.png) Adjustable inserts are inserts that can be adjusted for additional length prior to being applied.

>Red inserts also do not get inserted on faces. They always are inserted at the 0,0,0 of the 3d view. This is because they dont behave well being placed automatically due to the hook modifiers that the adjustable ones have. These inserts also have an AP that allows for surface snapping while also seeing the outside perimeter. This allows for precise placement.

![](img\faq\faq25.gif)

> Red inserts are built up out of these 3 pieces.
  - AP or alignment plane (used for aligning the whole insert)
  - BB of BoolBox (used for the boolean to make room for the OB)
  - OB or Object (the object being inserted)

![](img\faq\faq26.png)

[Update Log Explaining Red Inserts ](https://masterxeon1001.com/2016/01/05/hops0065update/)

___
