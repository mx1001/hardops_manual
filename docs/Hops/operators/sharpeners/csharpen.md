## CSharpen

Csharp also known as ComplexSharpen is similar to ssharpen but also very different.

To say it simply...

Ssharpen will mark sharps and set smoothing.
Csharpen will do that while also adding a bevel modifier and collapsing modifiers that are selected via the F6 menu.

Csharpen will also put the mesh in the Sstatus of Csharp.

### cSharpen use cases

Csharpen will put a bevel modifier on the mesh while also collapsing modifiers not specified via the F6 menu. This also changes the menu to allow for adjusting the bevel among other options.

![](img\ns7.gif)

Csharpen is mainly used for applying boolean modifers and making calculating the sharp information.

![](img\ns9.gif)

While this sounds strange. This is the main reason hard ops was made. Sharpening and applying modifiers. Certain modifiers.

![](img\ns10.gif)

In this example I put a lattice on the mesh and performed a subsequent boolean action. When Csharpened the boolean didnt work because the lattice is not listed and therefore ignored.

Any modifier not listed is ignored.

This allows for more experimental workflows and helps keep the controls set by the user via modifiers in creation intact.

![](img\ns11.gif)

This also helps with things like radial arrays and curve modelling workflows.

![](img\ns12.gif)

In this example I used the twist360 for a circular array, xsymmetrized to put a center loop at the origin point and booled a cube into the mesh while keeping the modifiers intact.

### cSharpen F6 options

Csharpen also has an F6 menu.

![](img\ns8.png)

The F6 menu is worth understanding since the modifiers not highlighted will be applied. The reason for the configuration seen is as follows.

- boolean (has to be applied for ssharps to be calculated)
- mirror (not applied / users prefer this. We respect the mirror even if booleans don't)
- bevel (this is not applied because doing so would make the mesh quite dense)
- solidify (applied. If you use csharpen on an object with thickness via modifier. Applied)
- array (this wouldn't be a good idea to apply. So we definetely respect it.)

General Parameters. (These options are never adjusted unless needed)
The general parameters are rather volataile. As in it is easier to not touch them. Just my experiences.

Autosmooth Angle - important option for hard surface set to an adequate and unobtrusive 60
Segments - bevel defaults at 3 for our standard csharpen. Use bwidth to adjust interactively
Bevel Width Amount - this is also best handled by the bwidth located in the Q menu after using this operation

Additive Mode - this was made to solve the need to clear ssharps and recalculate them to clean up messed up ssharps via modelling. This is also best activated in csharpen.

To sum it up... The top options matter. The old ones still remain due to usefulness however the workflow of Hard Ops is speed so the idea has expanded to the same ssharp panel.

![ss2](img/ns5.gif)

The helper ssharp panel is connected to all the sharpening tools. This is Csharp / Ssharp / Step.
