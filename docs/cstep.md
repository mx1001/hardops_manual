## Cstep (Basics)
___

# What is Cstep?
___

Cstep is basically a workflow involving baking bevels destructively and working forward with subsequently smaller bevels.

> The workflow of cstep was developed primarily by [AR](https://www.artstation.com/artist/adrianrutkowski) and is highly destructive however can get rather unique results. I still consider this workflow experimental but I also highly recommend trying it out.

# How does Cstep work technically?
___

Let's say you csharp and object and adjust the bwidth.

![image](img\cstep\c1.gif)

From this point all I can do is adjust the bwidth at this level. Even when I do subsequent cuts they will be at this bevel level. Even further cuts that are csharpened will be at this bevel level. In order to maintain. I will have to lower the bwidth to accomodate.

![image](img\cstep\c2.gif)

This is generally not the best choice since I am having to adjust in order to compensate. So now lets see how cstep helps with this situation. By making the bevels I can get more and more micro.

![image](img\cstep\c3.gif)

In this example you can see I used ctrl + numpad minus to cut the cube into the main shape after activating cstep on it. This technically
  - applied the bevel modifier
  - added a new bevel modifier set to weight
  - hid the mesh in edit mode and removed marked bevel weights

   This is how we "bake the bevels". So Cstep in a way is "Bake Bevels"

> This is why when you cstep you no long have access to bevel width. You are baking the bevel then re-adding it while removing previous bevel information.

In the above example you also see me use Sstep. Sstep is the process of calucalating the bevels based off either modifiers or the mesh that is visible in edit mode. Unlike csharp cstep focuses on the mesh that is visible and does not unhide unless it is being baked and cleaned (bevel weight removed).

In this example take note of the following.

  - Cstep is how I bake each level before going further
  - Sstep is how I calculate the sharps after setting up the booleans for that level
  - Sstep has an F6 menu for which modifiers it can ignore but really it doesn't need to be messed with unless you are focusing on the sharpening amount which generally is also left at default.

![image](img\cstep\c4.gif)

## Faqs On Cstep

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

# Why is it called Sstep / Cstep / Ssharpen / Cssharpen?

The naming made sense at the time but the functions are best described like so. Someday the tools will be unified into something more logical however in the meantime we needed some sort of terminology for naming.
