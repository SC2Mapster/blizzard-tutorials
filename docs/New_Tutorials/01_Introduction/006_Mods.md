# Mods

Mods separate the assets of a game from a map file. As a result, they can never be launched within StarCraft itself, only handled in the Editor. Mods are eventually made usable by being placed within a map file. The map's requirement of these mod files is known as a dependency. The advantage of this arrangement is easy to explain; separating game data from map terrain allows a mod to be hosted within various different maps. This means that a custom game mode can be ported to many differently designed locations, whether for aesthetic or gameplay reasons.

## Mod Types

Mod type is largely dictated by where the mods are being applied. There are two groups. The more typical Dependent mods contain triggers, data, and any type of non-terrain editor information. You can upload these mods to Battle.net using the Editor. However, to make a full game, they will eventually need to be added as a dependency to an active map within the Editor. This design makes them a basic organization and utility construct, ready for use in any map which would use custom data.

Extension mods similarly contain all types of game changing data and are built within the Editor, but in contrast they are applied within the 'Custom Games' interface on Battle.net by selecting a base map, then an extension mod. This allows a division of map and mod design. In this way, mod makers can use maps in various capacities without the need for explicit collaboration. Extension mods can also contain Dependent mod dependencies, and as such can be thought of as an application of the basic dependant mods.

Observer Interfaces are a special subclass of extension mods. These mods can only make alterations to the UI segments of the Editor. This has special applications in customizing the competitive spectating experience of StarCraft matches. These interfaces can also be activated for use in replay viewing.

## Mod Usages

Mods are useful for avoiding redundancy. Imagine you had designed a custom campaign that carried special rules, characters, and player decisions through a series of ten maps. Without the use of a mod, you would have to replicate these custom rules for every single episode of the campaign. By moving elements of the game into a data construct, a mod, you eliminate the need to repeatedly rebuild maps.

The use of mods becomes even more crucial when you consider the possibility of continued updates to your custom campaign. Without a standard mod dependency, each update cycle will result in you needing to make alterations to every single map. You might copy and paste data from map to map for each update, but without the ability to control any of these versions, the possibility of catastrophic failure looms large. Mods will organize these changes and propagate them out to every single map utilizing the mod, saving you significant effort.

Beyond this, mods make it possible for you to separate work on a project by partitioning large portions of a game's design into individual mods. This allows multiple developers to collaborate on a single project, with each working on different aspects of the project, such as cutscenes, data, and terrain.

Mods are often used to bundle a lot of assets in order to streamline play on Battle.net and the Arcade. Remember that in StarCraft files are stored on the Battle.net servers, then downloaded and accessed locally. If the mod portion of a project remains unchanged between versions of a game, despite alterations to the rest of the game, players won't need to download those mods again. If used well, this can ease both the development process and sharing games online. Supporting this, mod files can reach a maximum of 100 MB, while maps have a maximum size of 20 MB. This encourages smart data use and increases a map's ability to use custom assets.
