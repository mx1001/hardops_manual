Ssharpen / Csharpen
*******************

Ssharpen is the base of the sharpening system and is a foundational element of Hard Ops. The idea of Ssharpen came through the collaborations of myself and AR which also was the base of Csharpen as well.

People always ask what is the difference between the two.

Ssharpen is a calculator. It also sets the mesh up for hard surface modelling.
In short. Ssharpen

    -goes into edit mode unhides the mesh and deselects all.
          selects sharps edges via select >> sharp edges.
    -edges are marked with bevel,sharp,crease
    -autosmooth is activated at a 60 degree angle

So this merely sets up a mesh for hard surface rendering and helps it look better in the 3d view and rendering. This is a rather non-destructive operation and doesn't affect the mesh negatively. To best understand Ssharpen try doing it manually. Here is an example of the process.
![](http://i.imgur.com/XMBcamx.gif)

Alternatively. Here is ssharpen in action.
![](http://i.imgur.com/SEYSWBg.gif)

Csharpen is a more destructive sort of operator in the fact that in addition to sharpening it also does beveling and applies certain modifiers. This is to allow for modifier based modelling and rapid concepting with minimal worry about the rendering process of the hard surface form.

Csharpen is an applier / sharpener. This can also be used to set up the mesh however it is also built to be an applier of modifiers in order to allow forward working.
