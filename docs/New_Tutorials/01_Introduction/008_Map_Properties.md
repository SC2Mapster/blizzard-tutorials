---
title: Map Properties
author: jrepp
category: 01_Introduction

---
MAP PROPERTIES
==============

Map Properties affect a wide range of settings, determining everything
from how your game lobby is handled on Battle.net to how the 'Fog of
War' behaves. You can navigate to the collected map properties via Map
-\> Map Info, from any of the Editor modules.

![Image](./008_Map_Properties/image1.png)

Map Tab

Note that 'Map Properties' actually refers to a grouping of eight tabs
of options that govern high-level map decisions. Accessing any of the
eight headings under the Map tab will direct you to the same 'Map
Properties' window. These tabs are broken down in the following
sections.

| 
| MAP INFO \-\-\-\-\-\-\--

The Map Info properties determine logistical details about a map.

![Image](./008_Map_Properties/image2.png)

Info Tab

+------+---------------------------------------------------------------+
| Prop | Details                                                       |
| e    |                                                               |
| rty  |                                                               |
+======+===============================================================+
| Name | The map name, displayed to locations such as Battle.net, the  |
|      | Arcade, and the publishing screens.                           |
+------+---------------------------------------------------------------+
| Sugg | An internal note for how many players the map could require.  |
| e    | This is unrelated to the Suggested Players value found in     |
| sted | 'Game Info' and 'Map Info' screens in the custom games        |
| Play | section and the Arcade respectively. That value is            |
| e    | automatically generated from lobby info.                      |
| rs   |                                                               |
+------+---------------------------------------------------------------+
| Desc | An area for describing the map's contents. This section is    |
| r    | also often used for author credits or any other type of       |
| ipti | general message that could be of interest to an audience.     |
| o    |                                                               |
| n    |                                                               |
+------+---------------------------------------------------------------+
| Prev | This image is displayed in several contexts.                  |
| i    |                                                               |
| ew   |                                                               |
| Imag |                                                               |
| e    |                                                               |
+------+---------------------------------------------------------------+
|      | -   As the main thumbnail on the Arcade's 'Browse' screen.    |
|      | -   When highlighting a game within the 'Custom Games'        |
|      |     section of Battle.net.                                    |
|      | -   Within the publish screen.                                |
|      | -   As the map preview screen under default map settings.     |
|      | -   In the 'Game Info' screen of the Arcade, if no            |
|      |     screenshots are selected.                                 |
+------+---------------------------------------------------------------+
|      | It may be set as a Map Image, Custom Image, or Hidden. The    |
|      | last option results in no image appearing in any of the       |
|      | contexts listed above.                                        |
+------+---------------------------------------------------------------+
| Game | Determines what image the minimap will use. Options include a |
| Mini | Map Image, or a Custom Image. Traditionally a Map Image is    |
| m    | expected, but the option is provided for non-traditional      |
| ap   | games.                                                        |
| Imag |                                                               |
| e    |                                                               |
+------+---------------------------------------------------------------+
| Mini | Determines minimap quality level as follows: Normal: 256 x    |
| m    | 248, High: 512 x 496, Ultra: 1024 x 992.                      |
| ap   |                                                               |
| Reso |                                                               |
| l    |                                                               |
| utio |                                                               |
| n    |                                                               |
+------+---------------------------------------------------------------+
| Loca | Selects the locale version for the inputted information. You  |
| l    | will also notice a 'Copy to All Locales' button, which will   |
| e    | move the information from the current view to all other       |
|      | existing locales.                                             |
+------+---------------------------------------------------------------+

MAP OPTIONS
-----------

The Map Options are a collection of gameplay and visual oriented options
for altering the game. There are also some logistical options here that
can affect decisions made during map creation.

![Image](./008_Map_Properties/image3.png)

Options Tab

  -----------------------------------------------------------------------
  Prop   Details
  erty   
  ------ ----------------------------------------------------------------
  Unex   Sets the type of the 'Fog of War' used by the map. Options
  plor   include Grey Mask, Black Mask, and Black Mask (Reduced Radius).
  ed     Additionally, the 'Modify' tab directs you to the Data Module,
  Area s for a higher degree of customization.

  Mini   Sets the minimum height flying units will descend to.
  mum    
  Flye r 
  Heig   
  ht     

  Stat   Sets the opacity for static mapped shadows, a provision for low
  ic     graphics.
  Shad   
  ow     
  Inte   
  nsit y 

  'Gam e Disable Observers: Prevents observers within online matches.
  Opti   
  ons'   
  Flag s 

         Disable Replay Recording: Turns off replay archiving within map
         sessions.

         Disable Trigger Preloading: Any data referenced explicitly
         within triggers is eligible for preloading, cutting initial load
         time at the expense of trigger load time.

         Hide Errors During Online Games: Prevents any map debug or error
         messages from being displayed on Battle.net.

         Hide Errors During Test Document: Prevents any map debug or
         error messages from being displayed during use of the 'Test
         Document' function.

         Show Game Start Countdown: Enables an animated countdown after
         the map loads.

         Stagger Periodic Trigger Events: Automatically spaces out
         periodic triggers in an effort to optimize performance and avoid
         trigger queueing.

         Use Horizontal Field of View: Changes the game from its default
         vertical field of view. Useful for custom projects such as third
         or first person shooters.

  Publ   Sets the map category to Melee/Custom Map or Arcade Map. This
  ishi   distinction determines whether the map is available in the
  ng     'Custom Games' or Arcade sections of Battle.net. Automatically
  Opti   Add Multiplayer Data allows the Melee/Custom Map to add the
  ons    needed multiplayer dependencies at game launch. Hide Battle.net
         Lobby will allow Arcade Map users to minimize the lobby while
         waiting for a game to start.
  -----------------------------------------------------------------------

MAP BOUNDS
----------

The Map Bounds allow for dynamic alteration of the size limitation of
both the playable area and the camera area within the map. The arrow
buttons found on each side of the map allow for resizing along their
specific axes.

![Image](./008_Map_Properties/image4.png)

Bounds Tab

  -----------------------------------------------------------------------
  Property       Details
  -------------- --------------------------------------------------------
  Modify Camera  Locks or unlocks the effect of resizing on the camera
  Bounds         area.

  Modify Map     Locks or unlocks the effect of resizing on the playable
  Bounds         map area.

  Reset to       Alters all configured bounds to their default settings.
  Defaults       

  (Map Size)     A basic generated description of map sizes. Options
  Description    include: Tiny, Small, Medium, Huge, and Epic.

  Playable (Map  The current map's dimensions, minus the required buffer
  Size)          of unplayable area around the map.

  Full (Map      The current map's dimensions, including buffer area.
  Size)          
  -----------------------------------------------------------------------

MAP SYMMETRY
------------

.![image0](./008_Map_Properties/image5.png)

Symmetry Tab

Map Symmetry is used to set the symmetry controls within the map. This
is useful in terrain generation for melee maps, where symmetry is often
a necessary feature for competitive play.

MAP TEXTURES
------------

![Image](./008_Map_Properties/image6.png)

Textures Tab

Each map uses a specific Texture Set type, which is a palette of eight
textures used to paint the ground on the map. You can select these
palettes for use in the Map Textures tab. Note that cliff styles are
also a part of this palette and may be configured here.

MAP TAGS
--------

Map Tags are used to create Difficulty Tags for organizing terrain
objects, such as Units, Doodads, Regions and Points, allowing you to
filter them for later viewing.

![Image](./008_Map_Properties/image7.png)

Tags Tab

MAP LOADING SCREEN
------------------

The Map Loading Screen tab allows you to configure the introductory
screen shown to players while the map is loading.

![Image](./008_Map_Properties/image8.png)

Load Screen Tab
