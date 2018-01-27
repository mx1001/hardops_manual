![header](img/banner.gif)

### Mirroring Options

> Mirroring is important  when it comes to keeping a mesh symmetrical however in
Boolean workflows having active mirror modifiers isn't always ideal. So we attempted to
provide many options for how to best approach symmetry.

___
As of 0094 the mirroring system received a major rewrite. No external addons are required for mirroring or symmetry and all the methods discussed on this page are now built in.

 > The tools depend on the case however they all provide unique solutions for
 particular issues pertaining to mirroring.
 ___

## Symmetrize -

 > Symmetrize was one of the first tools made for HOPS and symmetry. The purpose is to mirror and be done. It's also important to note that Blender has a built in symmetrize under the W >> symmetrize menu.

 ![mirror](img\mirror\mm1.gif)

 Q >> Meshtools >> Symmetry options

This tool is also available in edit mode.

 ![mirror](img\mirror\mm2.gif)

 There are hotkeys I personally use with this such as

 Alt + X in object mode

 Alt + Y in object mode

 > It is worth noting to set these you must right click the operator and choose to set a hotkey. This is outside of the default keymaps since it may interfere with other tools. So it is personal to my workflow.

 ![mirror](img\mirror\mm3.gif)

I definitely recommend the hotkeys for it however the next mirroring is built in with hotkeys and is a more complete expansion.

___

## Mirror Mirror Final -

> Mirrormirror was one of the first tools I ever got involved with before Hard Ops. I am happy to say it is not only built in but expanded in a way I couldn't have ever dreamed. This tool has it's own panel and multiple options for behavior.

# Hotkeys
Alt + shift + X / Y / Z is the hotkey for mirror mirror.
Ctrl + ~ is the hotkey for the modifier / material / misc helper of Hard Ops.

Before usage it is worth exploring the options in the mirror panel of the modifier helper.

![mirror](img\mirror\mm4.gif)

The purpose of the panel being here is to allow the user to adjust the behavior of the mirror before activating the hotkey.

So with that aside let's review the mirroring types.

# Mod

This one simply adds a mirror modifier on the axis selected. This does no bisection. Just adds a mirror modifier.

![mirror](img\mirror\mm5.gif)

Notice that I had to delete half in order for the mirror to work properly. This is the classic mirror mirror behavior.

If you select 2 objects and use the mirror mirror hotkey, the primary object will be mirrored across the secondary object.

Also this is a persistent 2 object behavior among all mirroring types. Even relink.

![mirror](img\mirror\mm6.gif)

___

# Bisect

Bisect is similar to mod except it removes half destructively and uses the mirror modifier. This is some of my most used behavior when mirroring since it splits the model down the local axis for splitting.

![mirror](img\mirror\mm7.gif)

___

# Symmetry

This one is similar to symmetrize however it is using the alt + shift + x/y or z hotkey from the mirror mirror system. This one was added for completion but isn't needed since there are dedicated symmetrizing destructive behaviors.

The minus and plus on the helper will reverse the axis which does make this more versatile than the previous ways with the preferences toggle.

![mirror](img\mirror\mm8.gif)

___

# Relink

> Relink is a different form of mirroring altogether. This was once a seperate thought however it found a nice place in HOPS.

Relink is non destructive and mirrors using group instancing so there's no mirror modifier required and requires a small bit of explanation.

![mirror](img\mirror\mm9.gif)

When used the result was a group instance based off of an empty called relink_x. This was something I used alot for space vehicles and things using absolute mirror.

You are also able to select the other half to hide in object mode which can be useful for certain processes.

![mirror](img\mirror\mm10.gif)

Also to remove an object from this relink mirroring the process invoves going into the object panel and removing the object from the relink group.

Here is an example.

![mirror](img\mirror\mm11.gif)

___

I hope users are able to find ways to implement each of these in their workflow however through experimentation it will become obvious quickly.
