## CSharpen

Complex sharpener, is the 2nd sharpening option in hops. It not only creates sharp edges but also apply bevel to it.

Csharpen puts selected object in new CSHARP state, that indicates the mesh is beveled

![ss1](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/operators/sharpeners/img/cs1.png)

### cSharpen F6 options

![ss1](https://raw.githubusercontent.com/mx1001/hardops_manual/master/docs/Hops/operators/sharpeners/img/cs2.png)


1. modifiers ignored by Csharpen

   * this is the list of modifiers that can work with Csharp 
   * -by default only booleans and solidify are applied whenever the csharpen is used

2. general parameters

   1. sharpness
      * edge angle to witch sharpening is applied - default 30 

   2. auto smooth angle
      * value for autosmoouth angle for selected object - default 60

   3. segments
      * number of segments of bevel modifiers

   4. bevel width amount
      * bevel size
3. sharpening parameters

   3. additive mode
      * ON - apply defined sharpness and keeps other created sharp edges
      * OFF - clears all sharp edges befor applying its own sharpness

   4. sub-D mode
      * ON - do not apply sharp edges and creases making it easier to work with subd after
