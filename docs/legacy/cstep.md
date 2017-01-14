## Cstep (Basics)
___

# What is Cstep?
___

Cstep is basically a workflow involving baking bevels destructively and working forward with subsequently smaller bevels.

> The workflow of cstep was developed primarily by [AR](https://www.artstation.com/artist/adrianrutkowski) and is highly destructive however can get rather unique results. I still consider this workflow experimental but I also highly recommend trying it out.

# How does Cstep work technically?
___

Let's say you csharp and object and adjust the bwidth.

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img/cstep/c1.gif)

From this point all I can do is adjust the bwidth at this level. Even when I do subsequent cuts they will be at this bevel level. Even further cuts that are csharpened will be at this bevel level. In order to maintain. I will have to lower the bwidth to accomodate.

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img/cstep/c2.gif)

This is generally not the best choice since I am having to adjust in order to compensate. So now lets see how cstep helps with this situation. By making the bevels I can get more and more micro.

![image](../../docs/img/cstep/c3.gif)

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

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img/cstep/c4.gif)

___

# Alternate Use Of Cstep / Sstep

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img/cstep/ca1.png)

In this example I start out with the Csharpen then use B-width to increase the segments to 12. I then cstepped it in order to bake the bevels.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img/cstep/ca2.gif)
