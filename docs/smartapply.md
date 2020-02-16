![header](img/banner.gif)

____

# Smart Apply

Smart apply is intended to be our all in one apply / conversion system.

![smartapply](img/smartapply/sa12.png)

By default it is intended to apply all modifiers except the following:

  - last bevel
  - weighted normal
  - last mirror if more than 1 mirror mod is present

This is an expansion on the [csharpen](csharpen.md) workflow and its separation from sharpen.

____

# Locating Smart Apply

Smart apply can be found in both [meshtools](meshtools.md) and [operations](operations.md).

![smartapply](img/smartapply/sa1.png)

![smartapply](img/smartapply/sa2.png)

_____

# Smart Apply in action

In the below example I use hopstool w/ smart box to add a dynamic box containing many modifiers.

![smartapply](img/smartapply/sa3.gif)

To apply this using ctrl + A >> Visual Geometry to mesh would apply more modifiers than desired.

>> As in creating custom normals that will reflect on the next cut.

Also ctrl + clicking Sharpen (csharp) will not apply the mods necessary to result in a usable object since it is optimized for boolean application primarily.

![smartapply](img/smartapply/sa4.gif)

Smart apply is capable of giving us the result we want.

![smartapply](img/smartapply/sa5.gif)

> last bevel and weighted normal left upapplied making it optimal for more boolean work.

____

# Smart Apply Ctrl + click

Ctrl + click smart apply will convert to curve.

![smartapply](img/smartapply/sa11.gif)

____  

# Smart Apply Advanced

![smartapply](img/smartapply/sa6.png)

- LMB - General Smart Apply

![smartapply](img/smartapply/sa7.gif)

- CTRL - Convert to curve and expand (2d meshes only)

![smartapply](img/smartapply/sa8.gif)

- SHIFT - Smart apply (remove leftover mods after apply)
  - useful for face extractions
  - removes the leftover mods that are left behind

![smartapply](img/smartapply/sa9.gif)

- ALT - [classic step](step.md)
  - WEIGHT Workflow
    - applies current bevel
    - unmarks bevel weighted edges
    - adds new bevel at half without marking
  - ANGLE Workflow
    - adds new bevel at half of previous bevel
    - applies nothing
    - only adds new bevel

![smartapply](img/smartapply/sa10.gif)

![smartapply](img/smartapply/banner2.gif)
