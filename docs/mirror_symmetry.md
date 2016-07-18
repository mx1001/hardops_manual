## Mirroring And Symmetry

![](img\songbread.gif)

> Mirroring is important  when it comes to keeping a mesh symmetrical however in
Boolean workflows having active mirror modifiers isn't always ideal. So we attempted to
provide many options for how to best approach symmetry.

___
When it comes to Hard Ops there are 3 ways mirroring is dealt with.
 - Mirror Mirror - (integrated) non destructively via modifiers. works based off of object selection
 - [AutoMirror](http://blenderaddonlist.blogspot.com/2014/07/addon-auto-mirror.html) -
(separate) this plugin is capable of bisecting a model and adding a mirror modifier
 - Symmetrize - these options use blender's own symmetrize for all axis and is built in. This is my default choice for symmetry

 > The tools depend on the case however they all provide unique solutions for
 particular issues pertaining to mirroring.
 ___

# Mirror Mirror

> This was one of the first plugins I ever was involved with. It was made by me
and Robert Fornoff who also was a part of the building of Hard Ops. Initially this
was a separate plugin but now it has been merged into Hard Ops to use the
drawing system and reduce outside dependencies.

Mirror Mirror has 3 hotkeys.
- alt + shift + x (X Symmetry)
- alt + shift + y (Y Symmetry)
- alt + shift + z (Z Symmetry)

The beauty of this tool is that the indended behavior was selecting two objects
and after pressing the before mentioned hotkeys would mirror the object across
another object's axis. You can also use the mirroring hotkeys on a single object
 and that  would give it a mirror on itself across an axis.

To demonstrate MirrorMirror in my workflow.  

![image](img\mirror\m1.gif)

After slicing off one half. I used my alt + x symmetrize shortcut to make the body
symmetrical. However for the piece I sliced off I was able to use **alt + shift + x (X Symmetry)
to mirror it across the body** and therefore only have to work on one half. This
is something I do quite a bit and also use MirrorMirror in blocking to quickly
have mirrored halves of a character that I can then later adjust easily and with
the original origin axis still kept.

In fact just to show how I go about character blocking using mirror mirror, I
provided an example.

![image](img\mirror\m2.gif)

> I personally can't work without this enabled so it was only natural to add it
into the core of Hard Ops 8. I would recommend getting used to it and spending
 some time with it in order to better understand how it works.

 ___

 #  [Automirror Addon](http://blenderaddonlist.blogspot.com/2014/07/addon-auto-mirror.html)

 > Automirror is a tool made by [Lampaigne](https://cgcookiemarkets.com/all-products/lapineiges-tool-add-ons-compilation/).
 This tool fullfills a rather unique need and does it so well I need not bother
 making a tool of my own. I cannot recommend this add on enough for mirroring.
 However this tool has a rather specific behavior that is worth going over in depth.

The support for automirror is in the pie/tpanel/qmenu.
  ![image](img\mirror\m4.png)

> In this menu you can either just click Auto-Mirror to mirror on the default X-axis
or choose and axis as well as set positive or negative and set up the mirroring type before
initializing. Generally it is set up to mirror x by default.

 ![image](img\mirror\m3.gif)

You can see now after setting up the Automirror after the block in that the
model was automatically mirrored for the following sectional cuts that were made.
Its also important to note that I was unable to cut across into mirrored territory.
This is something that can be fixed by just applying the mirror modifier but it's
important to note:

 - You cannot cut mirrored meshes using booleans if the mirror is not applied. This is because one half of the mesh is not real.
    - you can fix it by applying it
    - you can work around it by not cutting near the mirror point. This is where the fun begins. But if you do want to cut it globally just apply the mirror and automirror again if needed.

You can use the automirror with these rules in mind to pull off some awesome stuff.

For example, Here's a quick 2 minute example of me using this particular behavior with Hard Ops.

> In this example I set up both x and y symmetry which isn't always ideal.

![image](img\mirror\m5.gif)

So when utilized properly you can get some quick results rather fast.

> In this example I set up just x symmetry which is more ideal.

![image](img\mirror\m6.gif)

Within 2 minutes I can get pretty far with the basic operators. And this is due to the speed and time saved with the auto bisect behavior. I cannot recommend [AutoMirror](http://blenderaddonlist.blogspot.com/2014/07/addon-auto-mirror.html) enough.

___

# Symmetrize

> So last but definetely not least is blender's own symmetrize. This tool is fantastic. I am personally a big fan of how quick it is and how accessible it is. Basically our operator is just a frontend of the one that is located in the w menu by default.

Here is blender's own symmetrize. All we did was make it more accessible to our needs. The reason this is used often is because it is mirror and done. This prevents boolean errors and allows for more veratility. Even while being the most destructive.

![image](img\mirror\m7.gif)

I am still a big fan of this and even have it mapped to alt + shift + x in edit mode in my version of Blender. However now let's see symmetrize in action. Keep in mind I have mine mapped to alt + x via right clicking it in the q menu. There are some differences that I will go over more after this example. I also usually combo this with mirror mirror as well so look out for the shortcut (alt + shift + x)

![](img\mirror\m8.gif)

By working this way I can make vertical cuts without limit and less issues than with a dynamic modifier in place. So theres a time and place for all of them but to recap.

- mirror mirror - is used for separate objects that need to be mirrored across another object's x/y/z axis
- symmetrize - is used to mirror objects across themselves without regard for what is on the other side. I consider it mirror and be done.

So with that out the way the symmetrize we created is also able to behave slightly different due to mesh sstatus. One example is cstep meshes will be hidden automatically after being symmetrized. Keeping the user moving if aware of the situation and sstatus.

Here is an example of that.

![image](img\mirror\m9.gif)
