---
title: Game Variants
author: jrepp
category: 01_Introduction

---
GAME VARIANTS
=============

Setting Game Variants allows a developer to specify the options
available to players in a map's Battle.net lobbies. Together with Game
Attributes, game variants control the distinctions for the different
modes in which your project may be presented. These variants can only be
set in a map document, not in a mod file. They are configured by
navigating to Map -\> Game Variants from anywhere in the Editor. You can
see the location in the image below.

![Image](./012_Game_Variants/image1.png)

Navigating to Game Variants

Once you've selected Game Variants, you will be presented with the
following window.

![Image](./012_Game_Variants/image2.png)

Game Variants Window

Note the leftmost sidebar, titled 'Variants'. This list details all of
the modes available for the game and will remain active through any of
the tabbed views you select. You can create a new variant by
right-clicking in this side bar and selecting 'Add' or 'Add Standard.'

If you are working on a new project, before you can start editing
variants you'll need to opt out of the default settings by unchecking
the Use Default Variants option at the bottom-left corner of the
variants window. Highlighting a variant from the sidebar will allow you
to change its settings in the three tabs: Game Type, Game Attributes,
and Player Attributes. The settings in these tabs are detailed later in
this article.

VARIANTS - LOBBY VIEW
---------------------

Game variants are used to define the options available to the host of an
Arcade lobby. These options are accessible through the 'Settings' panel
of a typical lobby, as shown in the image below.

![Image](./012_Game_Variants/image3.png)

Default Lobby

GAME TYPE
---------

![Image](./012_Game_Variants/image4.png)

Game Type Tab

The basic settings of a variant are established in the Game Type tab.
The Mode defines what is generally thought of as the variant, while the
Category offers a sorting option. These will be reflected later in the
'Category' and 'Mode' fields that players see in the game lobby. The
Genre setting for a game, which is found on a dropdown at the top of the
variants window, defines the main search category under which the map
will be sorted on the Arcade.

GAME ATTRIBUTES
---------------

![Image](./012_Game_Variants/image5.png)

Game Attributes Tab

The Game Attributes tab determines most of the configurable values found
in the 'Settings' section of a typical lobby. Each of the five
attributes here may be set to a default value. In some cases, they can
have values removed from the list possible selections using the Removed
Values option. The details of each attribute are broken down in the
following table.

  ------------------------------------------------------------------------------
  Attribute   Details
  ----------- ------------------------------------------------------------------
  Game        The duration of time after which the game is concluded. Typically,
  Duration    this is set to Infinite and a game will have its own methodology
              for determining when play has ended.

  Game        Determines match history and build order visibility options. This
  Privacy     is primarily used to support high-level competitive play, where
              players may wish to keep certain game information private. The
              standard setting, Normal, sets both match history and build orders
              to visible after a game.

  Game Speed  Determines the specific game speed at which the engine will run.
              The standard is Faster.

  Lobby Delay Sets a countdown timer which will play after the game is launched
              from the lobby. The standard is 10 seconds.

  Locked      Sets the alliance lock status. Unlocked alliances will allow
  Alliances   players to negotiate who their allies and enemies are within the
              game. By default this is displayed, but Locked. It may also be
              Hidden, which locks alliances but will not show what those
              alliances are.
  ------------------------------------------------------------------------------

In order to understand how these attributes are set within a lobby, it
is important understand the concept of Access. Every attribute has a
specific Access that determines whether or not it can be changed in the
game lobby. If an attribute is set to Unlocked, it may be altered in the
lobby. A Locked attribute can be seen in the lobby, but cannot be
changed. A Hidden attribute can neither be seen nor changed. Any
attribute that is configurable in the lobby can only be set by the lobby
host.

PLAYER ATTRIBUTES
-----------------

![Image](./012_Game_Variants/image6.png)

Player Attributes Tab

The Player Attributes tab is a more in-depth version of Player
Properties. Here you can set attributes for each individual player,
including Race, Color, Handicap, and other standard melee options.

Much like the Game Attributes tab, the Access for every attribute can be
set here, but here it is handled on a per-player basis.
