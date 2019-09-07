![header](img/banner.gif)

### Meshtools Submenu (Object Mode)

## What are Meshtools?

![mt](img/meshtools/mt1.png)

Meshtools are tools that perform quick operations that I use quite often in my workflow. There are also options for materials and a shortcut to the [HOPS Helper](helper.md). These options are just random tools and experiments that are useful in the hard ops workflow at certain points.

<iframe width="560" height="315" src="https://www.youtube.com/embed/iSQjRdiomlw" frameborder="0" allowfullscreen></iframe>

---

## Plugin

Extendable submenu for 3rd party tools that HOPS connects with.

Currently extends to the following
- meshmachine
- bezier mesh shaper
- mira tools

A video about this topic is also available.

<iframe width="560" height="315" src="https://www.youtube.com/embed/l4IlEZZPpG4" frameborder="0" allowfullscreen></iframe>

---

## Reset Axis

In object mode Reset Axis will allow you to reset an object on the Xyz on global space.

![mt](img/meshtools/mt15.gif)

When 2 objects are selected it will allow the axis to be reset in accordance with the primary object.

![mt](img/meshtools/mt16.gif)

---

## Material List (Alt + M)

see [materials](tips_material_menu.md).

Pressing alt + M will list all the materials in your scene. If you have no materials this list will be blank.

***HARD OPS provides no materials besides the placeholders for inserts that are simple shaders and not recommended for rendering***

The material list has proven to be quite useful to assigning materials to assets. Just selecting things and pressing alt + m.

![mt](img/meshtools/mt8.gif)

---

## Symmetry (only here for legacy reasons)

see [mirror](mirror_symmetry.md)

This workflow can get complicated due to there being 3 systems we support but in short:

  - symmetrize is make symmetrical and be done. No modifiers are used.
  - auto mirror is self symmetry and involved bisection and uses the mirror modifier.
  - mirror mirror is primarily used to mirror objects across other objects.

For more information see [mirror](mirror_symmetry.md).

If you are still reading this, here is a demo of all 3 in action.

![mt](img/meshtools/mt17.gif)

---

## HOPS Reset

Sometimes in the Hard Ops workflow you can go off the rails and apply modifiers or decide to escape the auto hiding behavior of [cstep](step.md) sstates.

While this sounds odd its worth thinking that from an undefined mesh you can :

  - go into csharp sstate with just a simple [csharpen](csharpen.md)
  - go from csharp to cstep with just a simple [step](step.md)

Sometimes backing out of the workflow and going back in without modifying the object can open the door for some interesting workflows. Not to mention resetting boolshapes to also deviate in their workflows as well and do shaping before committing booleans.

![mt](img/meshtools/mt3.gif)

In this example you can see the boolshape at the beginning because of the green icon in the corner. After resetting the sstate I was able to treat the undefined but still live mesh as a neutral mesh using options from the [operations](operations.md).

> This option is all that remains from sstatus override introduced in HOPS 007.

---

## Circular Array

see [circulars](circular.md)

![mt](img/meshtools/mt18.gif)

---

## Twist 360

This adds an array modifier and a simple deform modifier. This also sets up the parameters according to my defaults. This is quite basic and is a less interactive version of Radial 360 however this doesn't diminish it's use, in fact it makes it more valuable.

![mt](img/meshtools/mt4.gif)

In this example I put the twist360 on the mesh and showcased the F6 menu. In order to make this primarily ngon mesh deform properly I had to use the knife and make some cuts before symmetrizing which got a more acceptable surface rendering.

---

# Apply 360

![mt](img/meshtools/mt6.gif)

Since Twist 360 is intended to keep the object non destructive apply 360 remains in order to do the following
- apply all modifiers
- remove doubles
- recenter origin

This can be done manually as well but this is in order to automate that part of the process.

---

## Auto Unwrap

When it comes to UVs I personally use the following tools to perfect UVs.

[UV Shotpacker](https://gum.co/UVShotPacker) | [Smart UV](https://gum.co/Smart_uv) | [UV Squares](https://blendermarket.com/products/uv-squares/)

That aside. X-Unwrap was a quick UV unwrapper we came up with for Hard Ops assets. It was formerly capable of displaying the UVs in the 3d view saving the need to have a UV editor and I hope to add it back. I personally love this tool and can see some potential in advancing its workflow and features.

**It is just a quick and dirty UV unwrapper for quickly going to substance / unity / unreal / quixel.**

- If one object is selected, it will UV it to an entire sheet.
- If multiple objects are selected they will be atlas'ed on one UV setup.

![mt](img/meshtools/mt12.gif)

---

## [Modifier Helper](helper.md) (CTRL + ~)

see [Modifier Helper](helper.md)

Pressing CTRL + ~ will open the HOPS helper. This tool is now capable of more than dealing with just modifiers.

![mt](img/meshtools/mt7.gif)

The HOPS helper is worth a look to see if the tool can fit in your workflow. The helper is indespensible for full screen working and has supercharged my personal workflow.

---
