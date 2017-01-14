## Sstatus System
___

> Sstatus is displayed in the left corner of the 3d view.

![](//img\phone.gif)

![sstatus](//img\sstatus\st_1.png)

Depending on the sstatus of the mesh the menus will be different. This is intended
to provide the most relevant options based off of the context.

____

## Sstatus Types

# Undefined
- this is the default state of meshes. All options are default and behaviors are also at default.

![sstatus](//img\sstatus\st_8.gif)
> In the above example you can see that ssharpen does not change the sstatus or options.

# Csharp
 - this is the live state for HardOps and means that the bevel modifier has been added.
This will cause tools to work with that in mind. This is the most used state and when active
changes the Q menu as well.

![sstatus](//img\sstatus\st_10.gif)
> You can see from the addition of the bevel and csharpening the options change to the more relevant ones.

- Ssharpen (now an updater for Csharpen and the sharp edges)
- B-Width (adjust the bevel interactively for the Csharpened mesh)
- Cstep (for baking the bevel into the mesh)

Cstep - this is for times when bevels are being baked while booleans are also being baked. This
is considered an advanced mode and was a tough call to even add to the main menu. To put it simply,
with this state the mesh is automatically hidden after operations like cstep / symmetrize / step / csharpen / ssharpen.

![sstatus](//img\sstatus\st_11.gif)
> In this example you can see how in edit mode the mesh is hidden after subsequent operators. This allows for the bevels to get isolated when booleans are applied. Its a bit of a hack but it works until certain features are added.

# Boolshape
 - this was added as a result of Boxcutter. This was done so that when
modshapes are made they also have a special q menu. Normally B-width is inaccessible
from the q menu unless you go under operations but in this case its best to bevel
it without sharpening in order to prevent from booling crease, bevel weight or
crease information that is added from Csharpening.

![sstatus](//img\sstatus\st_12.gif)
> Box cutter has the ability to make mod shapes which have a Q menu of the following options.
- tthick (solidify modifier)
- bwidth (bevel modifier)
- array (array modifier)

This will also be expanded on more in the future when the boolean workflow is expanded.
![sstatus](//img\sstatus\st_13.gif)

____

## Sstatus In Action


**Q >> Meshtools >> Sstatus Overide**

![sstatus](//img\sstatus\st_2.png)

Sstatus overide will allow you to set the mesh to another sstatus which will
change tool behavior and how operators behavor as well. Below is an example of two
objects.

  - the left cube is taken from undefined >> csharp >> cstep
  - the right cube was thickened using Tthick which is available in the undefined
  menu but not in csharp / cstep menus


![example](//img\sstatus\st_3.gif)

As you can see the context changes a bit. This was intended to prevent undesired behaviors.
For example if a cstepped mesh is csharpened it will cause issues with the mesh. This system
prevents it from occuring.

![example](//img\sstatus\st_4.gif)

In the Q menu you can see the context options changing as I am moving through the states.
Because Csharpen and Ssharpen involves unhiding the mesh it also causes issues with
the behavior of Cstep which requires the mesh be hidden to isolate booleans for Sstep
sharpening.

![example](//img\sstatus\st_5.gif)

So now that the left cube is in Cstep mode the behavior for mirroring and the Q menu will be different.
In the below example I am using alt + x as my custom symmetrize x shortcut but whenever it is ran you
can see the mesh is rehidden in edit mode due to the cstep behavior. This advantage can allow you boolean
quickly and without having to tend to the mesh in edit mode.

![example](//img\sstatus\st_6.gif)

Even though the mesh is in cstep mode I can use the mesh overide to reset the mesh
back to default. For this example since the mesh's baked bevels are at 12 segments
initially. I know overiding to csharpen again won't cause any issues.

I am able to work in Csharp mode again with those options and I can even go back
into cstep if I wanted to bake the bevels and go in further.

![example](//img\sstatus\st_7.gif)

So with this I can use the tools with different behaviors and shift it around to my advantage.
I would recommend trying this system with simple shapes to grasp an understanding.
____

## Mesh Overide / Sstatus Reset

# Status Override
Mesh override is located in the q menu under mesh tools.

![](//img\sstatus\st_15.png)

Status override will provide a pop up window to allow you to change the state of the mesh.

![](//img\sstatus\st_14.png)

Below is an example of me using the mesh override in action.
![example](//img\sstatus\st_16.gif)

> Above the mesh was
- csharpened which added a bevel
- cstepped to bake the bevels
- mesh overide >> undefined to reset the mesh
- tthick which was available from the undefined main Q menu
- csharpened to bevel the newly solidified mesh

In action has allowed me another level of speed in creating basic hard surface
shapes and detailing.

# Status Reset

Status reset is located in the q menu under mesh tools and right below Mesh override

![](//img\sstatus\st_15.png)

This option simplifies the process of Status Override into being just a quick way to reset the mesh back to undefined.

> I use this option almost more than the status override

![example](//img\sstatus\st_17.gif)
___
