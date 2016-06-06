## CSharpen

>Csharpen is the first tool based on the sharpening system and is a a crucial tool
in Hard Ops. The idea of Csharpen came about through a need to quickly apply booleans
and then sharpen the mesh to keep working forwards.

# What does Csharp do that Ssharp doesn't?
  - apply modifiers that are not listed otherwise
  - set up a bevel modifier on the mesh with a specific profile and segment count

  - also it ssharpens the mesh after applying the correct modifiers

# Why does Csharp apply all my modifiers?
This would be based off of the understanding of what you want the tool to do.
Initially after using it to set up the bevel you wouldn't use it again unless
you want to **apply modifiers** and then calculate the sharp angles.
The idea was that you would use the booltool workflow of cutting shapes and then
use csharp to apply the shape and therefor proceed forward.

This can be a bit to understand however Csharpen is used as a part of many of
the other tools we have been discussing.  

Csharpen is a more destructive sort of operator in the fact that in addition to
sharpening it also does beveling and applies certain modifiers. This is to allow
for modifier based modelling and rapid concepting with minimal worry about the
rendering process of the hard surface form.

<iframe width="240" height="180" src="https://www.youtube.com/embed/rXRZeuQpvsg?list=PL0RqAjByAphGEVeGn9QdPdjk3BLJXu0ho" frameborder="0" allowfullscreen></iframe>

Luckily I also discussed Csharpen in action in the same video as the one where I
discussed Csharpen.

To better understand ssharpen there is also a chapter on that. 
[Ssharpen](ssharpen.md)
