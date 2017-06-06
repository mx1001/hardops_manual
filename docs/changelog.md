![header](img/banner.gif)

changelog

## 0.0.9.2
- bump to ver 0092
- link update (docs / vids)
- slash to hotkey numpad slash for irony

### 0.0.9

- hoteys can be set in options hotkey tab
- scale option for modal operators was added
- booleans solver is global now can be set helper
- ssharp, cstep, csharp work on multi objects now (old multi operators removed)
- bool options added to menu/panel
- added 'reset axis' operator
- version bump.
- all operators support step workflow fromn ow on
- s/cstep operators removed and replaced by step
- wire options added to HOPS Helper
- sharpness angle for sharp operator is now global (acces via Tpanel/helper/F6)
- mesh display toggle added to edtimode >> meshtools
- pro mode switches clean ssharp with demote for reason....
- machin3 decal support added

### 0.0.8.7

- Multiple object support for B-Width
- New operator 'bevel multiplier' added
- Hud indicator moved from text to logo by default
	1. logo in corner added
	2. text status disabled by default
	3. added preferences to enable/disable logo/statustext (logo under extra / pro mode)
	4. preferences to change logo color/placement
- new operator - sharp manager was added
- csharpen uses global sharps now
- ssharpen uses global sharps now
- set sharp uses global sharps now
- added new global way to define what sharp edges to use (T-panel/ helper-misc)
- SUB-d status removed from all operators (use global statuses now)
- bweight can now select all other bweight edges in object while in modal state by presing A
- BOOLSHAPE objects are hiden to renderer now (outliner icon)
- slash assigns boolshape status for cutters now
- panels/menus/pie updated with correct operators
- added option for slash to refresh origin of cutters (in F6)
- Slice and rebbol operators replaces with slash
- fixes for material cutting
- renderset C created (speed preset)
- fix for register bug (hotkeys duplication)
- pie menu and menu uses same hotkey now (Q) it can be chosen in preferences

---

> This was the log on the first version of Hard Ops. I saw it and had to put it back in the docs. It was such a mess back then. Now things are more calculated and planned. Less random. At the beginning I was struggling with so much however as I worked with more people my knowledge and understanding expanded. I wasn't even using git at this time. So I had to learn how to even work with people to get the help I was asking for in the first place.
To anyone starting out coding I must recommend [stackexchange](https://blender.stackexchange.com/users/18988/masterxeon1001). I also recommend reading code and other scripts to understand how problems are solved by others. I must also thank [AR](https://www.artstation.com/artwork/ww4yX) who has helped me in the shadows with my stubbornness and repetetive mistakes haha. I cannot recommend [stackexchange](https://blender.stackexchange.com/users/18988/masterxeon1001) enough however. Ask the right questions and you'll be amazed with the answers.

### 0.0.0.1 to 0.0.4.0

So as I said I am not a coder. So expect some breakage. In fact I started with a template! Try it out! I used the [macro recorder](http://blenderartists.org/forum/showthread.php?254117-Macros-recorder) for Blender. From that it wasn't a whole lot to make it customizable and part of what you
see here. On that note excuse issues and be patient while I work on this to make it awesome! Thank all who purchased this tool and I hope to make it worth your investment. If you got if for free... well congrats. ***Hahaha get to work anyways***. I also gotta add. If you expect Nth circles to result in clean geo you'd be a madman. You should know by now I don't care about topology anymore. Only when it matters.

fixes -     

- 9/22 UnkTime - fixed errors / added experimental (E) /
- 9/22 8:22 - fixed nth circle / adjusted the circle selection command
- 9/22 9:11 - spent alot of time angry with the circle operators and they isolate themselves 			geometrically while you fix it later but at least still have flows
    - changed names more and added in some cleaner operations.
    - realized that the circles have vert / face combos so mode is important
- 9/22 10:00 -broke more stuff than I fixed. Im a Winner!
    - added a modal test. I'll get that figured out.... after some metal gear
    - added option to recenter/remove doubles/recalc orgin. works great
- 9/23 7AM - adjusted the SCleanCenter to convert to mesh first
    - began adding end-time parameter control
    - began adding clean UI module. needs toggle.
    - began adding red UI module. needs toggle also.
        - currently the clean UI gets out the red. Or just disable matcap haha.
    - added skinHose Operator turns lines of verts into a hose with mods
        updated to (0, 0, 3, 8)
- 9/24 4AM -visited with AR and made changes
    - worked with ClearSharps and added crease weight affecting
    - fixed up C/S/Sharpen operators as fought with bugs.
    - found demons in the Cicle tool with 3 edges / ew.
    - 4PM - fixed Ssharpen now it clears and readds it on reapplication / fixed ssharpen edit operation also
        - sharpen appears to behave properly.
- 9/25 5AM - fixed the csharp to make not apply bevel before adding bevel. Now it removes solidify and bevel.
    - updated to version 0.0.4.1
    - added edit mode symmetrizer that unselects then symmetrizes it.
    - more fixes to cSharpen / damn that cSharpen will drive me insane before its perfect.
- 9/28 5PM - made fixes to n-th circle.
    - made fixes to circle vert to make it usable.
    - hid the face circle operator. dated.
- 9-29 - SSharpen should add to the sharps
    - CSharpen should use the existing while clearing previous entries and adding onto it.
    - Began checking into adding dDo color palette.
- 10-10 -began making changes based off of test instances
    - created CircleSetup allows for the creation of a circle that you can scale at least
    - redesigned sharpen operator workflow.
    - Ssharp - sharpens however now it add the crease to the crease set not redo it
    - Csharp - sharpens but adds crease
    - ReSharp - recalculates sharps and ignores modifiers
    changed behaviors to all sharpens - tsharp no longer applies bevels. Nothing applies bevels. Or Should.
- 10-13 - FaceGrate now has setup behaviors instead of the initial operation
    - Nth Circle now does setup behavior instead.
    - Version Number don't mean #(@* to me so now it's version 0.0.4.3
    - check into using If loops to keep parameters on modifiers its removing and re-added.
- 10-14 -Made a psychological improvement to Cshapen. Now it reduces keystrokes by 2.
    - put version 0.0.4.3 on gumroad.
    - attempted a quick render settings button reduces settings of rendering by 18 clicks.
    - changed the psychological behavior of all sharpeners again
    - grid setup psychology changes.
    - tested a knurl operator with setup
- 10-19 Added some F6 support. Now sharpeners have F6 operator capabilities.
    - bump up to verion 0.0.4.4.... yay
    - more changes are needed to fix the global bevel and sharp parameters
    - more operator fixes. Changed the angle of the sharpeners to 60 to test out.
    - more psychology adjustments. Fuuuuuuuu!
        - todo - copy bevel information from selected.
        - todo - there should be a /2 button that divides the bevel parameter by half.
    - now x-slap reveals the mesh before x slapping it.
- 10-21 - made fixes to bevel param of resharpen. It doesn't need it. Kinda bad behavior.
- 10-22 - bbox off now makes things unrenderable too
- 10-24 - Hoooooooooly Shiiiiiiit Massive Upgrades - All Sharpen Rewrites
    - ssharpen now has 2 behaviors. Additivie / Subtractive behavior -
    - clear S/C Sharps now has an option to downgrade to Bevel >> angle or to not remove modifiers
    - Csharp has died temporarily.
    - Resharp is dead
    - Menus are grouped
    - Still need popup menu thats automatic.
    - rethought CSharpen
- 10-25 - Got the bevel width working. Effing awesome!
    - Still needs to have....
    - worked with RF - substancial changes.
    - bpy.ops.mesh.select_interior_faces() removes interior faces. add this to the atwist 360
    - csharp is working , ssharp is working, testsharp is gone. I think this is gonna work.
- 10-29 todo - the csharp should have an angle for shapening for one and an option to no sharpen at all as a checkbox added.  (DONE)
    - todo - invert final boolean option. Just to make it easier.
    - todo - fix the resetting issue with recursive parameter changes for csharpen.
    - now version 0.0.4.8 just to be confusing.
- 11-9 Discussed naming convetions.
    - added draw all edges to show wire. AR request.
    - AR suggested keep mirror on csharpen.       
    - discussed icons           
- 11-10 Created y-slap (merge with x slap along with opposite behavior)
    - began framework for interactive array
    - stole Paweł Łyczkowski's script for making UVs on hard surface. I asked for permission though.
- 11-12 TODO -at suggestion of Vitalii add shortcut capabilities
    -began testing version 0048 for issues to add todo.
- 11-13 - began adding icons. Fuuuu Icons are kinda hard haha.
    - icons are now showing.... like 5 hours later haha. Time for some COD!
    - actually no cod yet. more testing. Now the script doesnt load icons by default. Fuuuu.
