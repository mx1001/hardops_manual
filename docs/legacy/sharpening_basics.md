## Understanding C/Sharpen
_____
# How does Sharpening work?

> Ssharpen is just an automated process that marks sharp edges for hard surface.
While also setting up Autosmooth with an angle of default 60.

# SSharpen

Initially whenever a mesh was set to smooth the surfaces would look quite bad.

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\basics1\bas_1.gif)

This was improved with auto-smooth being added later. However it still needed a
 little more attention. You can see it looks better this way but not perfect.

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\basics1\bas_2.gif)

 This can be good enough for most cases however autosmooth on lower numbers might
 get undesired results. It can be easier to mark certain edges sharp using
 **ctrl + e >> mark sharps** than to lower the autosmooth threshold.

 ![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\basics1\bas_3.gif)

Sometimes when you are working you want a little finer control and would then benefit
from being able to select sharp edges and mark them manually in order to control what
is being smoothed exactly. Luckily there are controls for that. **select >> sharp edges**.
The select menu has an assortment of options worth looking into.

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\basics1\bas_4.gif)

Ssharpen will do the function of all the above gifs in one step. And thats it.

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\basics1\bas_5.gif)

____

# Csharpen

> So to recap Ssharpen is a "sharpener" it doesn't affect modifiers. It simply
"sharpens" the mesh. Ssharpen is a function in the background of many of the functions
in Hard Ops. It's important to know how it works manually to best understand it.

Even this can be a but of work especially when you bring bevelling into the mix.
For this reason Csharpen was created. This particular function is much different
than Ssharpen but it's best to explain it manually.

This shape as you can see has many live booltools still active.

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\basics1\bas_6.gif)

I can press **ctrl + ~** for the modifier manager and apply them manually but
that is more clicks than I would like to do. This is an example of what the csharpen
process will look like manually.

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\basics1\bas_7.gif)

After applying modifiers and calculating ssharps is the next part of Csharpen.
Putting a bevel modifier that is set to bevel only marked bevel weight edges.
This will give the mesh a nice bevel on sharp edges and make the model look better.
Before Hard Ops this was quite a process and was tedious.

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\basics1\bas_8.gif)

So now to demonstrate I will take this mesh with still live booleans and use Csharpen.
Afterwards I can use B-width to adjust the now ssharp object.

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\basics1\bas_9.gif)

These two cylinders are examples of the difference between the two operators.

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\basics1\bas_10.gif)

![image](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/img\basics1\bas_11.png)

Hopefully this recap on the underlying functions assists in helping make better cubes! 
