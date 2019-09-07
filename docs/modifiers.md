![header](img/banner.gif)

### HOPS Modifiers

With the introduction of Hard Ops 0098 a modifier system was added. This allows for procedural creation using hardOps. It was expanded further with the [hopsTool](hopsTool.md)

![tthick](img/modifiers/m1.png)

Currently the list has the following:

  - Bevel
  - Solidify
  - Array
  - Mirror
  - Screw
  - Simple Deform
  - Displace
  - Simple Deform
  - Cast
  - Decimate
  - Weighted Normal
  - Subdivision
  - Triangulate
  - Lattice
  - Shrinkwrap
  - Wireframe
  - Skin

  And then the custom versions of modals modified for hops:

  - 2d Bevelling
    > bevel w/ vertices set (useful for planes)

  - Spherecast
    > subdivision x 3 + cast mod set to sphere and 1

  - Circular Array
    > displace + array + driver for radial array w/ live update

Then apply modifiers. Which does just that. Applies modifiers.

## Modifiers

# [Bevel](bwidth.md)

See [Bevel](bwidth.md)

Bevel needs no introduction but in case you need one it adds a bevel mod to the mesh which and give a nice rounding or filleting.

![mod](img/modifiers/m1.gif)

During the modal H shows help options.

![tthick](img/modifiers/m2.png)

The bwidth page goes more in depth on the topic.

___

# [Solidify](tthick.md)

See [Solidify](tthick.md)

Solidify also called tThick sometimes for menu reasons will add thickness to the model. It is useful for adding thickness to boolshapes.

![mod](img/modifiers/m3.gif)

There is also a help panel.

![tthick](img/modifiers/m3.png)

[Solidify / Tthick is also useful](tthick.md) for boolean operations.

![mod](img/modifiers/m4.gif)

___

# [Mirror](mirror_symmetry.md)

Mirror brings up the interactive mirror gizmo that offers 3 different ways to mirror.
For more information see [Mirror](mirror_symmetry.md).

![mirror](img/mirror/mmm1.gif)

[This also has the hotkey alt+X.](hotkeys.md)

Mirror has 3 different options.

- modifier (new to 2.8)
  - mirrors the mesh on the modifier level using bisect
- bisect (classic)
- symmetrize (symmetrize and be done) doesn't leave a modifier behind nor use one

![mirror](img/mirror/m1.gif)

___

# Array

Array will allow users to add or modify an array modifier on an object.

![mod](img/modifiers/m5.gif)

Array also works on multiple objects.

Of course press H for help.

![tthick](img/modifiers/m6.png)

Pressing 2 during the modal will add a 2nd modifier.

![mod](img/modifiers/m7.gif)

___

# Screw

Screw will allow users to add or modify a spin modifier. The spin modifier is interesting because it can be used for a variety of things outside of lathe. By setting the angle to 0 this will behave like an extrude leading to some interesting results in non destructive asset creation.

This is how I use it on planes to make cylinoids.

![mod](img/modifiers/m8.gif)

It can also be used in conjuction with displace to create quick springs on the fly.

![mod](img/modifiers/m9.gif)

Screw is also a major component in [hopsTool.](hopsTool.md).

![hotkey](img/hopstool/h6.gif)

Press H for help during the screw modal.

![tthick](img/modifiers/m10.png)

___

# Displace

Adds a displace modifiers on the model. We use in to move geometry while preserving the initial origin point.

It has special uses in conjunction with screw.

![tthick](img/modifiers/m10.png)

It is also a part of the [circular array](circular.md).

![mod](img/modifiers/m11.gif)

Press H to help.

![tthick](img/modifiers/m12.png)

___

# Simple Deform

Adds a simple deform that can be toggled between twist, taper, and deform.

![mod](img/modifiers/m13.gif)

Press H for help.

![tthick](img/modifiers/m14.png)

It makes more sense in [hopsTool.](hopsTool.md).

![mod](img/modifiers/m15.gif)

___

# Cast

Adds or modifies a cast modifier set to sphere, cube or cylinder. Typically I use this on sphere for spherecast.
Users can scroll the wheel to change the result.
![mod](img/modifiers/m15.gif)

Press H for help.

![tthick](img/modifiers/m16.png)

___

# Decimate

Adds a decimate modifier to the mesh. We set this to 5 degrees which results in a non destructive form of clean mesh.

The gif below shows the difference on planar surface. It can be tricky in action and is [recommended to sort wisely.](sorting.md)

![mod](img/modifiers/m18.gif)

Ctrl + click to add an additional one in the modifier stack.

___

# Weighted Normal

Adds a weighted normal modifier to the selected object(s).

In blender shading is always a struggle especially with edgeflows going wild from modifier and boolean based modelling. Weighted normal is generally put at the end of the stack and can be useful for improving shading.

It's subtle in most cases but can be a lifesaver on more complex models.

![mod](img/modifiers/m19.gif)

Ctrl + click to add an additional one in the modifier stack.

___

# Subdivision

Adds a subdivision modifier to the selected object(s).

This is similar to ctrl + 1 to add a subdivision modifier.

Ctrl + click to add an additional one in the modifier stack.

___

# Triangulate

Adds a triangulate modifier to the selected object(s).

___

# Lattice

Adds a lattice modifier and lattice to the selected object(s).

This is intended to fit to the bounds of the object so it is unparented in the event adjustments must be made.

![mod](img/modifiers/m20.gif)

Ctrl + click to add an additional one in the modifier stack.

___

# Shrinkwrap

Adds a shrinkwrap modifier to the main object while shrinkwrapping it to the secondary object.

![mod](img/modifiers/m21.gif)

___

# Wireframe

Adds a wireframe modifier to the selected object(s).

![mod](img/modifiers/m22.gif)

___

# Skin

Adds a skin modifier to the selected object(s).

![mod](img/modifiers/m23.gif)

___

## Custom Modifiers

___

# [2d Bevel](2dbevel.md)

[2d Bevel](2dbevel.md) adds a bevel modifier (verts) to the selected object.

This isn't intended for non-2d shapes. See the [2d Bevel](2dbevel.md) page for more info.

![bevel](img/2dbevel/bv1.gif)

It also has a use and button in hopsTool.

![mod](img/modifiers/m24.png)

![bevel](img/2dbevel/bvl9.gif)

___

# Spherecast

Spherecast was made to turn cubes into sphere. When used spherecast does the following things.

- adds a subdivision modifier level 3
- adds a cast modifier(sphere) factor 1

That's all it takes to turn a cube into a sphere.

![mod](img/modifiers/m25.gif)

___

# [Circular Array](circular.md)

[Circular Array](circular.md) does the following.

- empty with a driver based off of Array
- displace modifier to push the object outside for radius
- array with offset based off of initial empty

![mod](img/modifiers/m26.gif)

for more details see [Circular Array](circular.md).

Hovering over the option shows alternate creation types.

![mod](img/modifiers/m27.png)

___

# Modifier modelling

The video below showcases modelling using modifiers manually. This was before hops Modifier support was added.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ivmVWILUzZU" frameborder="0" allowfullscreen></iframe>
