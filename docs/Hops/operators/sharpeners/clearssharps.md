## Clear S/C/Sharps

Clear SCSharps is used for removing Hard Ops from a mesh and changing it back into a neutral state. It does this via the following.

- remove ssharp information
- reset sstatus to undefined
- remove bevel / solidify modifier


### Clear S/C/Sharps use cases

Returning a mesh back into a neutral state

![](img\cm1.gif)


### Clear S/C/SharpsF6 options

![ss2](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/operators/sharpeners/img/clear2.png)

1. remove modifiers
   * removes all bevel/solidify modifiers from selected mesh

2. clear sharps
   * remove all sharp edges

3. clear bevels
   * clears all bevel weights from edges

4. clear creases
   * remove creases from edges

### Alternative Uses

Clearing the sstate and resetting the mesh can be useful in situations where the user also wants to reset the Q menu behavior. This serves as a quick way to restart the process or refine without behavior adjustments as occurs later in operations.
