# Map Types

The Editor breaks files down into two main types, each of which serves
different purposes. They are known as maps and mods.

Maps are likely the most intuitive type for those who are familiar with
Blizzard's editing tools. Maps organize a single game type into a single
file, combining terrain, code, and data. Whenever you play a game of
StarCraft, you're launching a map file.

All maps have at least some data running under the surface. Melee maps
have a very basic set of default game instructions contained in the
file. These spawn units and start any computer-controlled AIs, if
needed. Arcade maps can contain extensive custom data to articulate
entirely new types of gameplay. In both cases, the map's internal data
is directly connected to the top level terrain data in a single package,
the map.

This is not always the case. Sometimes it can be useful to create a
separation between the data and map terrain, which is the main purpose
of mods.

MAP TYPES
---------

As mentioned above, Melee maps require a default set of game
instructions. They are used to play the standard multiplayer StarCraft
games. Due to its nature as a premier competitive game, the melee mode
is kept to a specific Blizzard standard. Any changes to a map's data
will mark it as unfit for melee usage. As a result, melee maps only
describe components like terrain design and base layout. Designing these
elements alone is quite an extensive discipline.

Once an alteration has been made in the data of a game, changing it from
the melee map standards, it will be tagged as an Arcade map. These maps
can make full use of the Editor's capacity to shape new experiences with
StarCraft. Furthermore, Arcade maps are organized into a separate area
of StarCraft II's Battle.net, dubbed the Arcade. In the Arcade, special
organizational features allow creators to host, distribute, and
publicize their game in a much more powerful fashion than for melee
maps.

Other popular terms for maps include the titles 'Custom Maps' and 'Use
Map Settings.' These refer to maps with customized rulesets from
Warcraft III and StarCraft: Brood War respectively. Due to the cultural
momentum of those games, these terms are often used interchangeably with
the currently preferred term, Arcade Map.

It is worth noting that Custom Maps still exist in another context. The
term now refers to the use of a melee map with what is known as an
extension mod. The map design and mod data are slotted together within
Battle.net's 'Custom Games' interface, giving users more control for
collaboration and offering players more customization options.

Another topic of interest is campaign maps. These are maps which form a
unified campaign, made by linking overworld elements in a manner similar
to the singe player mode. Campaign maps make alterations to data. As a
result, if you were to upload any of the available Blizzard campaign
maps to Battle.net, they would be labelled as Arcade maps. You can
publish your own campaigns to the Arcade as a series of individual
Arcade maps. Usually, they are labelled similarly and contain various
pointers directing the player from one map to another. There are also
options in the Editor for those who would like to build offline
campaigns.
