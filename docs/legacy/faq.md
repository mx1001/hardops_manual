## FAQs / SFQs

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\c1.gif)

# How Do I Install Hard Ops / Boxcutter?

# [See Install](install)

# Why is the add-on checker not working?

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\start1\ad2.png)

The recommended addons will show checkboxes when the supported plugins are present.

This can have issues if the naming is different than what it is looking for.
BoxCutter for example requires the folder is named "BoxCutter"
The namings being searched for are as follows.

- "BoxCutter"
- "Auto Mirror"
- "Mira Tools"

This can be an issue to some however it is recommended to just check the folder naming. We are currently looking into improving it but it was intended to be a quick checklist to assist with troubleshooting.

To troubleshoot further you also can run the following command in the scripting area of the scripting tab.

**bpy.context.user_preferences.addons.keys()**

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\start1\checking addons.gif)

This will show a list of all the add ons present. This is how we troubleshoot this area when the plugin detection is not working.
___

# Why am I having issues when I boolean certain areas?



___

# What is Cstep / Sstep?

In short.

**Cstep** - bakes bevels to the mesh and hides it in edit mode for future booleans.

> Cstep is similar to Csharpen aside from the fact that it applies the bevels before re-adding it. This is where it differs from csharpen. The moment you cstep you will notice you no longer have the ability to adjust the bwidth. **This is because the bevel was applied and readded.**
This means that now you can boolean the object while being able to adjust the bevel for those singular areas.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\faq20.gif)

**SStep** - calculates sharpening from the mesh that is visible in edit mode. Compared to SSharpen which will unhide the mesh to calculate ssharps.

>SSharpen - unhides the mesh before ssharpening.
![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\faq18.gif)

>Sstep - only calculates ssharp from visible mesh in edit mode
![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\faq19.gif)
Sstep is basically the same as ssharpen except for unhiding the mesh. I also use this when I dont want to unhide my selection to calculate however the main purpose of this tool was for cstep workflows.

[See CStep](cstep)

___

# Why is my mesh hidden when I Cstep?

Cstep hides the mesh when used. See [How does Cstep work technically](How does Cstep work technically)

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\cstep\c5.gif)

> This example shows what happens when you cstep. After hitting the button in the Q menu the mesh type will say Cstep in the top left. Also the bwidth will no longer be fun. This is because it has been applied. When you go in edit mode it will be hidden.
  - press alt + h to unhide mesh
  - press h to hide mesh

In the example it shows me undo to get back to csharp state but understanding the states is essential to using the tools correctly and understanding the context.

# Can I get out of Cstep?

Absolutely. We added the ability to override states which can be useful to putting meshes back to the beginning for using alternate workflows. Here is an example.

> **q >> meshtools >> status reset** will reset any mesh back to a default state. Causing the Q menu dynamic options to also be default instead of cstep oriented.

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\cstep\c6.gif)

> In this example I use cstep to block it in sort of an bake a bevel while then using the Status reset located under **q >> meshtools >> status reset**. By resetting the sstatus I was able to use Tthick which is a basic option under meshes that have no sstatus. From there I went back through a csharp / rebool workflow and ended up back in a csharp workflow to finish off the shape with finer details and a bevel with 1 segment for the edges.

___

# Why is it called Sstep / Cstep / Ssharpen / Cssharpen?

The naming made sense at the time but the functions are best described like so. Someday the tools will be unified into something more logical however in the meantime we needed some sort of terminology for naming.

___

# Can I add my own inserts to Hard Ops?

No. However it is possible but not recommended since it's not user friendly.
For custom inserts I recommend the [Asset Management](https://gumroad.com/l/kANV/). This is a temporary solution but we do have plans to expand this down the road.

___

# What do the different inserts mean?

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\faq21.png) Orange Inserts are just basic inserts. These can be inserted in edit mode orented to faces.

> Orange inserts can be inserted on a series of faces and can be scaled immediately after selection via a modal operation. This allows for scaling to perfection. It even sets the pivot points to individual origins so they retain their position.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\faq24.gif)

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\faq22.png) Red Inserts are inserts made to be boolean cut into surfaces.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\faq23.png) Adjustable inserts are inserts that can be adjusted for additional length prior to being applied.

>Red inserts also do not get inserted on faces. They always are inserted at the 0,0,0 of the 3d view. This is because they dont behave well being placed automatically due to the hook modifiers that the adjustable ones have. These inserts also have an AP that allows for surface snapping while also seeing the outside perimeter. This allows for precise placement.

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\faq25.gif)

> Red inserts are built up out of these 3 pieces.
  - AP or alignment plane (used for aligning the whole insert)
  - BB of BoolBox (used for the boolean to make room for the OB)
  - OB or Object (the object being inserted)

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\faq26.png)

[Update Log Explaining Red Inserts ](https://masterxeon1001.com/2016/01/05/hops0065update/)

___

# Help! Why doesn't this add-on show activated in the add-on checker!

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\addon2.png)

By using this line in the scripting area of blender you can see all the add-ons  activated.

bpy.context.user_preferences.addons.keys()

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\addon1.gif)

The Boxcutter add-on folder requires the naming be "BoxCutter"

You can also find the foldername in the addon file area.
![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\faq28.png)

This is how it would be fixed in the add-ons directory.
![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\faq27.gif)

Now I can start boxcutter with Alt + W

![](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\faq29.gif)

Mira tools also is the same way.
![img](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\faq\f1.png)

In my add ons folder it is just called mira_tools. For this addon it can get complicated since the naming is rather specific.

I must add that the add on checker doesn't really matter. It was attempted to be a convenience thing. However some issues that users find with it is due to the naming.
