THIS DOC NEEDS TO BE DELETED AT THE END OF VERSION 8

## Version 8 Completion Goals
___

The main goal of version 8 is to make Hard Ops more standalone and powerful by absorbing dependencies that are critical to the main functions of Hard Ops. As a result as of version 8 Booltool is no longer needed.

> The booltool was a complex tool containing many features that were not used at all due to the shortcut system. We simply just made a shortcut system doing the same thing so if you still have Booltool our plugin will allow it to override our system.

___

Merge options - this was started by AR with the ver 7 rewrite.

![a1](8final\a1.png)

- cmerge would be csharp merge or Hard merge
- smerge would be soft merge or "stepped merge" this allows users to set up the boolean but still adjust and preview before committing via csharpen
- material helper only shows one mat. That has to be fixed.
- qarray should be able to be initialized with an empty selected as well.
  - this would set the empty to the selection field of the array modifier. 
