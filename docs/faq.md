![header](img/banner.gif)

### FAQs / SFQs

# What happened to the topbar!?

Right click object mode and enable it.

![mir](img/faq/how3.gif)

___

# What kind of geo can I expect from booleans?

Something like this. Booleans solve as they will and with the most minimal of edges.

![mir](img/faq/how1.gif)

All hardOps does is help user make these mistakes quicker so they can be corrected and controlled even faster.

___

# How do you make a hardOps mesh work with subdivision?

Below is my classic video for converting from boolean / bevel to subdivison geometry. As you can see it is a process unto itself. This video is a classic from 2.79 so it is still applicable even in the 2.8 era.

<iframe width="560" height="315" src="https://www.youtube.com/embed/f7dvODWS4e4" frameborder="0" allowfullscreen></iframe>

When it comes to more complex assets sometimes I will convert an unbevelled version to the final model as shown here:

<iframe width="560" height="315" src="https://www.youtube.com/embed/UYMrkAOTV9E" frameborder="0" allowfullscreen></iframe>

I don't normally break down game models to all quads since tris also play a role in simplification but the process differs from subdivison conversion. Working smart and using guidance edges can go a long ways in keeping the work ahead minimal.

When I talk about guidance edges I mean this.

![mir](img/faq/faq41.gif)

> Booleans by default in blender will solve using any edge it can connect to it. And more often than not this is not the desired way to solve a boolean. In the above gif you can see the geometrical hit lessen as go to the edge while face cuts will solve to the nearest corner. Something as simple as adding an edge counteracted this. This edge has only the purpose of guiding the boolean. Therefore it is a guidance edge. That is the only purpose for adding it.

Having less booleans solve with the corners the less stress the bevel modifier will get which reduces the amount of streaking artifacts while working.

With the new miter options on bevel a user could easily build the block in cage from a boolean mesh. And from there make everything quads and be good to go. The bevel mod creates the guidance edges to prevent subdivison from shrinking everything.

![mir](img/faq/faq37.gif)

a few things to note note:

- bevel was set to profile with 1 by pressing P during bwidth to adjust the profile.
- boxcutter has sorting for bevel on so the bevel is kept on top of the boolean modifiers
- miter spaces out the top of a cut instead of converging them making the subdivision process easier than ever

![mir](img/faq/faq38.gif)

Also if subdivison is on an object. All is quad. Automatically. So just using subdivision makes and object all quads.

Using triangulate and bevel intelligently can be the difference between adequate shading with subdivison and artifacts due to ngon to subdivision  issues. Even now this object is still able to be modified thanks to [sorting.](sorting.md)

![mir](img/faq/faq40.gif)

about the above gif:

- bevel is still live but rounded by subdivision.
- triagulate mod via hops will only triangulate ngons which is thanks to enahncements to the modifier itself.
- everything is dynamic but also fully quad once subdivision is brought into play
- during bevel Z turns on wire. This is the object wire. Not to be confused with the viewport wireframe option that had to be toggled in this example

> The flow will not be what you like but it will be all quads.

![mir](img/faq/faq39.gif)

So the subdivision conversion process can be quite easy depending on geometry and that is built into blender. So exporting to Zbrush and 3dcoat is an option this way as well.

> While working sometimes I will duplicate a portion before progressing forward in order to keep a state I can revert to if I need to add more geometry to the initial mesh or make a large form change. So part of getting the most out of hops is working smart and using the tools Blender has in addition to the tools added with hardOps.

Alternatively users could apply the bevel and clean up the mesh by manually adding loops and that is the most direct way to get a perfect result. However make sure to bevel with a profile of one to create additional edges for managing surfaces. This can come in handy for modelling as well.

![](img/bool/b5.gif)

In the above example I beveled in edit mode with a profile of 1 to 100% keep the profile but add a spacer loop with low segments. This spacing workflow is essential for maintaining for and controlling flow to master shading with minimal geometry.

___

# [How did you do the curved wall demo from the 00983 trailer?](https://youtu.be/0qx_hOrW1C8)

At this moment in the trailer I showed a curved wall.

<iframe width="560" height="315" src="https://www.youtube.com/embed/0qx_hOrW1C8?start=36" frameborder="0" allowfullscreen></iframe>

This utilizes spin with curve deformation. It was a happy little accident.

To showcase setting it up in action:

![mir](img/faq/faq35.gif)

- moved the plane held ctrl for increment snap
- ctrl + A applied location
- deleted one point to make it an edge
- duplicated and separated one vert with P for making the object w/ same origin / rotation
- converted main shape to curve after bevelling
- extrude (spin) the vert shape then ctrl + P (curve deform) to the curve

> Curve deform rarely works out the box so some adjustment may be needed.

This can result in an interesting setup for completion of the asset.

To extend on the previous example:

![mir](img/faq/faq36.gif)

___

# Why does it crash when using the operator properties?

Blender 2.8 has been having issues with the undo / redo portion that is connected to the properties panel. When changing parameters theres a chance Blender could crash and take you to the desktop.

![mir](img/faq/faq30.gif)

In the above example I attempted to use csharp and adjust the F6 to trigger an issue. But it didn't come up. But this is a common issue.

Another example is in boxcutter. Notice how changing the apply modifier area can cause a crash.

![mir](img/faq/faq31.gif)

 > At the top of boxcutter is a button that applies booleans. If tampered with it can quickly take you to the desktop. I'm my general use I dont mess with the F6 of this property because the purpose is only applying booleans.

![mir](img/faq/faq32.png)

![mir](img/faq/faq32.gif)

>> [The hard ops thread can be a nice way to convey issues and find support when needed. ](https://blenderartists.org/t/hard-ops-thread/)

[When crashes occur it can be handy to capture it and convey them to us.](issues.md)

But F6 and undo / redo related issues are a known thing that is an issue all throughout 2.8 at this time.

[In 2.7x there was also an issue with undo / redo and as a result we used outside properties to manage ssharp / csharp / booleans / clean mesh and marking.](https://hardops-manual.readthedocs.io/en/latest/ssharpen/#inside-out-sharpening)

![mir](img/faq/faq34.png)

In the hops helper / mini helper or n panel we have the workflow area which has some of those outside exposed properties you would normally adjust on F6. Since we put them outside we never looked back. I recommend spending some time getting acquainted with it.

___


# I was not logged in when purchasing your product. How do I get the latest update?

## Blendermarket


[Purchase Retreival](https://support.blendermarket.com/article/16-how-to-retrieve-your-purchase)

The product should be listed under [orders](https://www.blendermarket.com/account/orders) on your Blendermarket account. Having the product on your account is essential for the updates that come frequently due to changes with Blender.

![mir](img/faq/f16.png)

For additional assistance blendermarket can be contacted at [support@blendermarket.com](support@blendermarket.com)

## Gumroad

When it comes to gumroad you can view products in [your library](https://gumroad.com/library).

If you are unable to login you will need to locate the purchase email and use that to connect the product to your account.

 ![mir](img/faq/f15.png)

 If you are logged into your gumroad account you should see view product or download on the sales pages for the purchase related to you. [Alternatively the library will show all your purchases.](https://gumroad.com/library)

[HardOps](https://gumroad.com/l/hardops)

[Boxcutter](https://gumroad.com/l/BoxCutter)

[hopsCutter](https://gumroad.com/l/hopscutter)

___

# How do I update Hard Ops / Boxcutter?

Q: I haven't used HardOps for a while and need to update. Where do I get the latest update?

Blendermarket: [log into your account and go under orders in the dropdown of the upper right list.](https://www.blendermarket.com/account/orders)

Gumroad: [log into your account then access the](https://gumroad.com/library) [HardOps](https://gumroad.com/l/hardops) or [Boxcutter](https://gumroad.com/l/BoxCutter) pages.

The top file is always the latest.

Q: How do I get up to speed with the tool?

A: In the N panel or HOPS button is an option called Hard Ops learning that is built to help users find the documentation or [tutorial](https://www.youtube.com/playlist?list=PL0RqAjByAphEUuI2JDxIjjCQtfTRQlRh0) content. Every major version I usually make a new course set of materials to show off the tools.

___

# How do you stack bevels non-destructively? My bevels keep bevelling each other.

First lets look at the bevel modifier as it is in the Add Modifier submenu.

![mir](img/faq/f12.png)

- LMB - adds 30 degree bevel if not present / adjusts if present
- ctrl + LMB - adds an additional bevel modifier at 30 degrees.
- shift + ctrl + LMB - adds an additional bevel modifier at 60 degrees.

The **shift + ctrl + LMB - adds a bevel at 60 degrees** is the key.

If you bevel 3 segments at 30 then bevel again more than likely you will double bevel.

![mir](img/faq/f13.gif)

Ideally you want the subsequent bevels at 60 so you dont catch the same edges. This is the easiest solution.

> Alternatively you could add more segments to the first level to round it out for the 2nd level to not get caught under the 30 degree threshold.

![mir](img/faq/f14.gif)

In hopsTool adding multiple bevels is slightly different but still the same.

- LMB adds bevel modifiers at 30 degrees
- ctrl + LMB adds bevel modifiers at 60 degrees

![mir](img/faq/f17.gif)

___

# How does reverse bevel work?

In edit mode with a face selected on a "boolshape" the face will be flipped resulting in a nice outwards bevel.

![mir](img/faq/rb1.gif)

Even if HN is on this feature should ignore that since harden normals would affect the shading. (we try to avoid cutting custom normals into other meshes).

![mir](img/faq/rb2.gif)

> Notice how harden normals is ignored on boolshapes.

This video goes more in depth on the topic.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6TdRQc1Grws" frameborder="0" allowfullscreen></iframe>

___

# How do you use sorting? The sort tickbox doesnt do anything.

The sort tickbox in hardOps and boxcutter is there for users to specify what modifiers are supposed to be where in the stack. Unchecked modifiers do nothing and remain where there are in the stack.

**clicking them does nothing until the next boolean operation**

![mir](img/faq/f2.png)

Sort can be turned off an on overall and the buttons next to it do the following:

- last bevel to bottom of stack (ahead of booleans)
- sort bevel modifiers - move bevel mods to bottom of stack
  - non vgroup / weight models
- sort array - ensures array is last so it shows booleans in all subparts
- sort mirror - using modifier mirror at the end of the stack will mirror all cuts
- sort solidify - keeps solidify later in the stack. Off by defaults. Only used in certain situations.
- sort weighted normal - keeps weighted normal at the end of the stack (maintains shading)
- sort simple deform - keeps simple deform at the end of the stack before the rest.
- sort triangulate - keeps triangulate after boolean to allow for iterative working on an exportable mesh
- sort decimate - moves decimate at the end of the stack (useful for rare situations)
  - recommended off for smart shapes and situations where the mod order is crucial.

To show sort bevel in action.

![mir](img/faq/f3.gif)

In this example I turned on only bevel sorting. Notice that when I used the boolean operation, the modifier for mirror was put last.

![mir](img/faq/f5.gif)

The down pointing arrow is for latest bevel sort. If you have more than one bevel more than likely you only want to deal with the highest level in order to cut with an independent bevel level.

## ctrl + ~ helper

![mir](img/faq/f4.png)

This is how I am able to cut on the final level of a bevel without affecting previous levels.
In this example the bevel angles are as follows.

- 30 degrees
- 60 degrees
- 60 degrees

If I use another 30 degree bevel it will detect the previous levels and cause mesh issues and possibly a crash. So this can be a delicate dance.

With mirror sorting the mirror will also be added to the end of the stack ensuring that the modifiers are always ordered in a way to keep working with booleans non destructively.

![mir](img/faq/f6.gif)

At the end of the last gif I added a Weighted normal modifier. This mod will always need to be at the end or else shading issues will occur. Turning it on will ensure the mod remains at the end when boolean operations are performed. It is best to turn that on when working with weighted normal.

![mir](img/faq/f7.gif)

> Multi- Bevel Sorting video

<iframe width="560" height="315"
src="https://www.youtube.com/watch?v=ZnyMUIilp6g"
frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>

## Sort Gotcha w/ hShapes

Some of the new smart shapes will require certain mods be off in order to maintain stack order.
Lets look at the current smart bbox and scroll through its mods to see how it is made.

![mir](img/faq/f8.gif)

The mods on this box are as follows.

![mir](img/faq/f9.png)

If we move / toggle the decimate mod this shape will be fundamentally changed. The decimate is needed for simplification and will cause issues.

To show that in action.

![mir](img/faq/f10.gif)

This is just to show that all situations can't be handled with sorting and at this time turning off sorting can also be of benefit to users.

Boxcutter also has a sort that must be taken into account. It can be found in either the topbar, n panel or D menu.

![mir](img/faq/f11.gif)

We aspire to expand sorting into something more expansive down the road but for now it will have to suffice for boolean operation.

___

# How do I apply a boolean I set up with Hard Ops?

Quickest answer. Apply the modifier. A boolean is just a modifier in your modifier stack. However this isn't the quickest or most recommended.

![mir](img/faq/faq1_3.png)

First lets set up a boolean and examine what is happening.

![mir](img/faq/faq1_1.gif)

By pressing (ctrl + ~) or using the N panel or HOPS mini helper I am able to see the modifiers on the object via the helper. This can be an easy way to quickly see whats happening with an object in the 3d view.

From the helper you can apply like and modifier or apply it using csharpen which is one of the primary purposes of the behavior.

![mir](img/faq/faq1_2.gif)

Csharpen is being used in the above example to apply the modifier as you work forward thus making the workflow faster and easier than going through panels and menus.


# How Do I Install Hard Ops / Boxcutter?

 [See Install](installation.md)


# Why is the add-on checker not working?

![](img/start1/ad2.png)

The recommended addons will show checkboxes when the supported plugins are present.

This can have issues if the naming is different than what it is looking for.
BoxCutter for example requires the folder is named "BoxCutter"

If the naming is not exact this will cause issues. Just rename the .py to resolve the issue.        

The naming is as follows.       

- [Boxcutter](https://gumroad.com/l/BoxCutter/)     
- [kitops](https://gumroad.com/l/kitops)     
- [mira_tools](http://blenderartists.org/forum/showthread.php?366107-MiraTools)     
- [meshmachine](https://www.blendermarket.com/products/MESHmachine)
- [Group Pro](https://gumroad.com/l/GroupPro/)
- [bms](https://gumroad.com/l/bezier_mesh_shaper)
- [power_snapping_pies](https://github.com/mx1001/power_snapping_pies)
- [DECALmachine](https://gumroad.com/l/DECALmachine/)       
- [Batch Operations](https://gumroad.com/l/batchops)        



This can be an issue to some however it is recommended to just check the folder naming. We are currently looking into improving it but it was intended to be a quick checklist to assist with troubleshooting.

To troubleshoot further you also can run the following command in the scripting area of the scripting tab.

**bpy.context.preferences.addons.keys()**

![install](img/install/ins3.gif)

This will show a list of all the add ons present. This is how we troubleshoot this area when the plugin detection is not working.

___

# Why am I having issues when I boolean certain areas?

see [boolean tips](tips_boolean.md)

___

# What is Cstep / step?

In short.

**Cstep** - cstep is an [sstatus](sstatus.md) for baking bevels while keeping a bevel modifier active for new intersectional bevelling.

**step** - bakes bevels while adding a bevel modifier back to the mesh for new bevelling.

[See Step](step.md)

___

# Why is my mesh hidden when I step?

Step hides the mesh when used. See [How does step work technically](step.md)

  - press alt + h to unhide mesh
  - press h to hide mesh


# Can I get out of Cstep?

Absolutely. Q >> meshtools >> sstatus reset

> **q >> meshtools >> status reset** will reset any mesh back to a default state. Causing the Q menu dynamic options to also be default instead of cstep oriented.

___

# Why is it called Step / Cstep / Ssharpen / Cssharpen?

The naming made sense at the time but the functions are best described like so. Someday the tools will be unified into something more logical however in the meantime we needed some sort of terminology for naming.

When I was originally writing a book about modelling I found myself saying repeatedly:
tab >> editmode >> select sharps >> mark sharp >> mark seam >> mark crease >> mark bevel weight

Over time I just simplified it into that for my own sake however after they became tools the names just stuck.
Since it's version 9, changing names might confuse actual users just to appease people who possibly are not even using the tool nor plan to.

___

# Help! Why doesn't this add-on show activated in the add-on checker!

![](img/faq/ad2.png)

By using this line in the scripting area of blender you can see all the add-ons  activated.

**bpy.context.preferences.addons.keys()**

![](img/faq/addon1.gif)

The Boxcutter add-on folder requires the naming be "BoxCutter"

You can also find the foldername in the addon file area.

![](img/faq/faq28.png)

This is how it would be fixed in the add-ons directory.

![](img/faq/faq27.gif)


Mira tools also is the same way.

![img](img/faq/f1.png)

In my add ons folder it is just called mira_tools. For this addon it can get complicated since the naming is rather specific.

I must add that the add on checker doesn't really matter. It was attempted to be a convenience thing. However some issues that users find with it is due to the naming.

___

## Mira Tools

# Why doesn't curveStretch show up in the Q menu?

![img](img/faq/faq2_1.png)

Check the add on preferences for Hard Ops under the add on tab. If Mira tools is not enabled you must download and install it.

[Mira Tools](https://github.com/mifth/mifthtools/archive/master.zip) /
[Thread](https://blenderartists.org/forum/showthread.php?366107-MiraTools)

If mira tools is not enabled the icon next to the button will show an error.

![img](img/faq/faq2_2.png)

The below example shows how installing it and enabling it allows HOPS to use it as well.

![](img/faq/faq2_3.gif)

___

# What is the difference between [Hard Ops](https://gumroad.com/l/hardops/) and [Boxcutter](https://gumroad.com/l/BoxCutter)?

Hard Ops is a toolkit containing many tools for various tasks ranging from viewport adjustment, rendering, helpers and symmetrization and not to mention sharpening.

Boxcutter is only a cutter. It only cuts. The purpose of boxcutter is to cut via drawing.

One can't replace the other. They are supplemental to each other. Boxcutter is a small subtool when compared to the entirety of the hops suite.

___

# What is the difference between [Hard Ops](https://gumroad.com/l/hardops/) and [KitOps](https://gumroad.com/l/kitopspro)?

Hard Ops is a toolkit containing many tools for assisting users with getting all the way from cube to final result. It's our swiss army knife of modelling. [However back in 2016 I did discuss the implementation and our plans with it.](https://masterxeon1001.com/2016/01/05/hops0065update/)

A few things to note.
  - I took the idea for Insert Merging from Chipp in Moi and I left a comment about it.
  - now he's using Blender years later and we collaborated to make his system from Moi a thing in Blender but faster
  - the initial insert system of HOPS was just a means to an end. It was limited due to its simplicity which limited our expansion on it. One mesh merged and one mesh left behind.

KitOps is focused primarily on insert management into packs called Kpacks and the workflows of aligning them on surfaces and smart behaviors. This takes the behavior system of subsets and removes several steps and makes it an artistic process compared to before.

# What can [KitOps](https://gumroad.com/l/kitopspro) do that [Hard Ops](https://gumroad.com/l/hardops/) doesn't?

- manage inserts / allows for user created inserts
- merge multiple levels of booleans in order
- connection / disconnection live via smart selector
- thumbnail rendering and creation
- duplication / shift + r redo capabilities
- support for HOPS tools like interactive mirror and Qarray
- smart hiding of modifiers for quick modifications
- insert hiding via quick selectors in T panel
- auto scale system
- custom scale system
- auto grouping for quick selection
- inserts dont appear until mouse is over surface during insertion

and much more.

KitOps was made from the ground up to offer a faster and more user friendly experience than our initial offering in Hard Ops. With an emphasis on expandability.

[There is a free version available.](https://gumroad.com/l/kitops) However there are some restrictions since it is a demo.

Try it for yourself. [KitOps Videos](https://www.youtube.com/playlist?list=PL0RqAjByAphG7h2dzNXdbao1tTNgQYNwb) / [HOPS Red Insert Demo](https://youtu.be/xURxPGdAbjg)

The videos themselves should show the differences.
___

# How about [Meshmachine](https://gumroad.com/l/MESHmachine/)? How about that?


[Meshmachine](https://gumroad.com/l/MESHmachine/) is a different system going for something different altogether. And that't what makes it awesome.

Meshmachine began as a series of tools to make Machin3's life easier in edit mode but has introduced "Plugs". I cannot recommend his tool enough. I imagine the final version being unlike any tool we have seen before.

KitOps currently does nothing beyond connecting meshes to other meshes with booleans and even simple placement. As you know this can be inefficient and messy when combined with curvature. So planar surfaces are optimal for this if you are not skilled with cleanup and efficient boolean modelling.

[Meshmachine](https://gumroad.com/l/MESHmachine/) takes this in a brilliant new direction. With his inserts you will be able to not only merge them with any surface efficiently, but the normals and shading will be resolved as well. This is alone worth my recommendation for this product. Fuse, Refuse, Unf*ck, UnChamfer, and Boolean Cleanup are tools that fill holes in the workflow of concept mesh creation.

 [Meshmachine](https://gumroad.com/l/MESHmachine/) is poised to do great things but this workflow does come with speed compromises due to complexity.
 This shouldn't affect your decision but this is where Plugs and Kpacks differ. They are 2 very different delivery systems for 2 different circumstances.

Kpacks are intended to just be used as inserts with users having to deal with consequences and ramifications of poor placement or hotlining. And not to mention doubles and shading issues with bad geo.

Plugs will conform with the surface and heal the shading. They both have their place. But in short there is no doubt that we will evolve to meet the standards that [Meshmachine](https://gumroad.com/l/MESHmachine/) will set.

I recommend to use [Meshmachine](https://gumroad.com/l/MESHmachine/) and bring it into your workflow. Our goal is never to compete. If someone can do a better job why not expand on that.

___

# Why did my shading get messed up starting the cylinoid video?

<iframe width="560" height="315" src="https://www.youtube.com/embed/szrnUx_2_uk" frameborder="0" allowfullscreen></iframe>

In 2.8 the parameter "Harden Normals" was added to the bevel modifier. While it's capable of being useful for shading later in the model this can have issues with the start of the cylinoid video.

![](img/faq/c1.png)

> The ctrl + ~ helper can allow users the change workflow or using the N panel.

This is what happens if the HN (harden normals) parameter is on.

The shading looks incorrect for the following reasons:

- harden normals is on making the normals look smoothing
- autosmooth is set to 60 and not 30.

Here is how I would fix it using the ctrl + ~ helper.
![](img/faq/c3.gif)


And here I am working on both the shading and the Harden Normal not being on.
![](img/faq/c2.gif)

This should not be an issue in the most recent update. 1 during bwidth will now fix the shading properly. We apologize for this being an entry level gotcha. Markets have been updated with this change. (9-6-19)

![](img/faq/c4.gif)

___

# How do I bake alpha maps / height maps from a Hard Ops model?

I assume you mean bake in substance painter or get normal / height maps.

Also I must add [DecalMachine has it's own system worth looking into for baking out decals to textures.](https://www.youtube.com/watch?v=YCUV8pS7MXQ)

If you wanted to be lazy you could make a version without bevelling and use x-unwrap on it to get some quick UVs.

Then export the bevelled as the high and the unbevelled triangulated as the low and with the correct settings you should be fine. However the best work is done by UVing and properly creating a low but workflows for hacking your way through exists.

![](img/faq/ff1.gif)

And then exported.

![](img/faq/ff2.gif)

Xunwrap provided some UVs however you can also preview them using operations << UV preview.

![](img/faq/ff3.gif)

Now in substance painter I bring up the mesh and do a quick bake.

![](img/faq/ff4.gif)

The UVs provided will do for such a boxy example however when inserts and material colors are present you will need to accomodate for baking ID maps and so on.

![](img/faq/ff5.gif)

In this bake I'll up the res and allow a little AA to get a nice result.

![](img/faq/ff6.gif)

As you can see from my IDs the material colors also baked into the low mesh.

![](img/faq/ff7.gif)

None of the inserts are present on the low. Its all just the bake. By removing the render and the filters and finally the layers you can see its the same low I used for the block in phase.

So the point of all this is to explain that a workflow exists however it is up to the preferences of you the user as to how you want to go about using the tools in your workflow.

The beauty of hard ops is you can use as much or as little of it as you need for your preferred workflow. But many of the tools are designed with particular workflows in mind.
___

# Obligatory Text

When it comes to having issues the first thing I'll recommend is updating. Theres a couple of ways to do that.

- [Buildbot](https://builder.blender.org/download)
- [Official](https://www.blender.org/download/)
- [Blender Update Utility](https://github.com/DotBow/Blender-Version-Manager/releases)
  - I like the update utility because it keeps Blender up to date and works well.
  - It's only for windows though.
  - [BlenderUpdater is also nice.](https://github.com/overmindstudios/BlenderUpdater/releases)

![mir](img/faq/ff2.png)

![mir](img/faq/ff1.png)

Anyways after having blender up to date comes ensuring you have the latest version.

Accessing previous orders.

- [Gumroad](https://gumroad.com/library)
- [Blendermarket](https://www.blendermarket.com/account/orders)
- [BM Support](https://gfycat.com/UnevenSmartGadwall)

When it comes to contacting us theres a couple of ways.

[Blendermarket](https://www.blendermarket.com/account/orders)

![mir](img/faq/ff3.png)
> Clicking that button will send us a message which can be easy.

[Gumroad](https://gumroad.com/library)

Responding to any email I send should come back to me. Believe me people use that alot.


>[Also I'm always on twitter so I can be messaged there as well. I probably post there the most. You can follow me for updates and occasional tips.](https://twitter.com/mxeon1001)


[Support Channels](https://thumbs.gfycat.com/FastInferiorGlowworm-mobile.mp4)

Boxcutter has a support button in the behavior panel. This will take you to our discord where we're haunted 24/7 with support issues.

![mir](https://i.imgur.com/axYJ8P7.png)

hardOps has multiple help areas.

![mir](img/faq/how2.gif)

![mir](https://i.imgur.com/W2XjC9R.gif)

Below are links to the direct sales pages which you can access the product via being logged in.

Gumroad
- [hopsCutter](https://gum.co/hopscutter)
- [boxcutter](https://gum.co/BoxCutter)
- [hardops](https://gum.co/hardops)

Blendermarket
- [hopsCutter](https://www.blendermarket.com/products/hard-ops--boxcutter-ultimate-bundle)
- [boxcutter](https://www.blendermarket.com/products/boxcutter)
- [hardops](https://www.blendermarket.com/products/hardopsofficial)

Artstation
- [hopsCutter](https://www.artstation.com/jerryperkins1447/store/D7aM/hard-ops-boxcutter-ultimate-bundle)

___

# Hello I am a student / child / woman / lover / hobbyist / beginner. Can I get a discount on the product?

No.

We keep our prices low to keep the entry low. The sales of our product go to paying programmers, paying for blender to keep improving and ensuring the tools evolving. We pride ourselves on our willingness to reinvest into the growth of Hard Ops / Boxcutter. This is 24/7 operation to us and we love working late nights, holidays, birthdays and family events on this tool to ensure you have the best experience in Blender for concept creation.

Please buy it.
