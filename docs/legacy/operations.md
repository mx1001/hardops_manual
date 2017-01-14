## Operations Menu

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\phone.gif)

The operations contain all the options that can sometimes show up in the dynamic Q menu.

![Op](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op2.png)

These are the default options that show up under the q menu. There are also additional options that will show up due to multiple meshes being selected or other context based reasons. For example when a bevel modifier is present like in csharp, segments will show at the top of this menu.

![Op](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op1_1.png)
____

## Operations options

# UV Preview
UV preview will display the uvs of the mesh in the 3d view.
> *This option will only show if UVs are present on the mesh.* The quickest way to get some quick uvs is **Q >> Meshtools >> X-Unwrap**. Otherwise you will need uvs to be present in order for this to work.

![Op](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op11.gif)

Here is an example of using X-Unwrap to get some quick UVs.

![Op](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op12.gif)

> The idea behind this tool was to make UV previewing easier for working with only the 3d view. Previously I was using the UV image editor frequently for this purpose but with this I am now able to focus on just modeling for elements that don't specifically need attention.

# Segments
This allows for you to adjust the bevel segments on the object. This option is older and not needed since Bwidth also handles the bevel segments amount via mouse roll.
> This will only be shown if a bevel modifier is present on the object.

![img](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op3.gif)

# Bwidth
Bwidth allows you to dynamically adjust the bevel if one is present.
  - if a bevel modifier is not present it will add one however using settings that are different than the one added by csharpen.
  ![Op](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op4.png)   ![Op](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op5.png)
  - if a bevel modifier is present it allows the modal operation of adjusting the bevel width and segment amount
  - it's important to note that the Q menu doesn't show this until a bevel modifier is in place for the initial 3 options. As of now this happens in the csharp / cstep sstate.

![op](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op6.gif)

# QArray
Qarray is a modal operator for adding array modifiers dynamically without the modifier panel. This is capable of arraying in multiple matrixes via the Q >> axis modifier.

Here is an example of this in action.
![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op7.gif)

You can also use it with multiple axis as previously mentioned.
![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op8.gif)

# Tthick
Tthick adds a solidify modifier self destructively.

> This option shows up in the main menu if the mesh status is undefined. Otherwise it is located in the Operations >> Tthick.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op13.gif)

This option comes in handy in situations where you just need spacing or thickness quickly that can be adjusted on the fly.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op14.gif)

> In this example I used (ctrl + numpad -) to cut a cube from another cube. While the boolean was like I used Q >> Thick on the bool shape and used it to make a paneling cut instead of a simple subtractive cut.

# Ssharpen
  See [Ssharpen](ssharpen)

# Csharpen
  See [Csharpen](csharpen)

# Cstep / Sstep
  See [Cstep](cstep)

# Clear Ssharps
This option clears all ssharp information and resets the mesh back to default.

When ran Clear S/C/Sharps does the following,
  - removes modifiers from the mesh
  - clears all bevel weight / bevel weight / sharp marked edges
  - removes auto smooth
  - sets mesh shading back to flat
  - sets sstatus to undefined / resets sstatus

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op10.gif)

# Clean Mesh (E)

This option performs a limited disolve with 0.5 degress and a remove double with a threshold of .02.

This is a new feature added in Hard Ops 8 and is just an experimental way of optimizing planar meshes for continuous boolean.

In some instances. I set the hotkey to alt + ctrl + X.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op15.gif)

After using Cslice to make the separation you can see a series of skewed edges.

These can be dissolved manually.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op16.gif)

I used C for circle select and then pressed ctrl + x to dissolve. Alternatively you can select all and do a limited dissolve through the X menu.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op17.gif)

So now let's see the Clean Mesh in action.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op18.gif)

> There's still additional things I want to add to this such as temporarily showing the wire of the model during the F6 operation. This may be expanded in further releases.

I must also add that while it dissolves edges to simplify surfaces. This is not always ideal since it goes against the idea of using guidance edges to control shading. So use at your own risk and always check the mesh after the operation. This was only intended to make it easier to do subsequent booleans without mesh error.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/menus/img\operations\op19.gif)
