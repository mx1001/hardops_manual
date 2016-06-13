## CSharpen

>Csharpen is the first tool based on the sharpening system and is a a crucial tool
in Hard Ops. The idea of Csharpen came about through a need to quickly apply booleans
and then sharpen the mesh to keep working forwards.

*We could have called it apply and move on but Csharpen sounds better*
___
# What does Csharp do that Ssharp doesn't?
  - apply modifiers that are not listed otherwise as exceptions in the F6 menu
  - set up a bevel modifier on the mesh with a specific profile and segment count
  - also it ssharpens the mesh after applying the correct modifiers / basically updating the mesh with accurate bevels via weights

# Why does Csharp apply all my modifiers?
It only applies certain modifiers. By pressing F6 you have options on what is being applied when Csharpen is ran.

![image](img/csharp1/F6menu.png)

If the modifier is not highlighted in this list it will be applied.
It's as simple as that.

<iframe width="240" height="180" src="https://www.youtube.com/embed/rXRZeuQpvsg?list=PL0RqAjByAphGEVeGn9QdPdjk3BLJXu0ho" frameborder="0" allowfullscreen></iframe>

Luckily I also discussed Csharpen in action in the same video as the one where I discussed Csharpen.

# F6 Menu
The F6 Menus is also worth explaining in depth since this is the beauty of this tool.

![image](img/csharp1/F6menu.png)

*Modifiers Ignored By Csharp*

> This area lists all the modifiers that are currently ignored by the Csharp operation. By default it ignores the following modifiers.

- array
- bevel
- boolean
- mirror
- solidify
- subdivision

> Shift + clicking additional options will add additional modifiers to the list. This may be expanded in the future to be a user preset list with allowable toggles.

# *General Parameters*

Sharpeness - specifies what angles receives sharp, bevel weight(1), crease(1) for the SSharp process.

Autosmooth Angle - specifies what angle the autosmooth receives in the Object Data tab.

Segments - specifies amount of segments the bevel modifier that is added will receive.

Bevel Width Amount - specifies the bevel width of the bevel modifier


# *Sharpening Parameters*

Additive Mode - this is an important option. This is also the main reason I use the F6 panel.

- unchecked: this option with recalculate ssharp information every time Csharp is ran. This will remove your previous sharpening and recalulate it. This is used when its easier to recalulate the sharps than it is to correct.

![img](img/csharp1/cs2.gif)

> in this example you can see that since I bevelled in edit mode the bevel weight marked edges of offset into flat surfaces. These surfaces don't benefit from bevelling because they are flat. Since the form is simple additive mode cleans it up easily.

- checked: this option will add new ssharp information and leave and previous information Sharp / Crease / Bevel information that existed before. This is the default behavior.

It is generally preferable to not have your sharpening overwritten. That is why it is checked by default. I recommend this as well however experimentation will make it apparent which tool will work for you.

___

To better understand there is some additional reading.

- [Csharpen Advanced](csharp_adv1)
- [Ssharpen](ssharpen)
- [Sharpening Basics](sharpening_basics)
