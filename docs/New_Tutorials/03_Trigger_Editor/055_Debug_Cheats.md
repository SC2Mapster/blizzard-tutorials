# Debug Cheats

Cheat codes were originally intended as testing elements for developers. When games began to be ship with these codes still included, they became a favorite for players to experiment with and use as shortcuts past irksome obstacles. Although player-side cheats like GreedIsGood and Black Sheep Wall still exist in StarCraft II, there are many more cheats that you can enable to ease development and testing of your projects. Below you'll find a list of these debug cheats for easy reference.

## Test Document Cheats

When testing a document from the editor, the Test Document Cheats are available. These are special chat commands that allow for game-time actions like creating units and modifying resources. They save developers from having to hand design special triggers for commonly performed testing tasks. **See complete [list of debug cheats in StarCraft II](https://sc2mapster.wiki.gg/wiki/Debug_Commands)**.

An example trial of some of these test document cheats is shown below.

[![Test Document Cheats](./resources/055_Debug_Cheats1.png)](./resources/055_Debug_Cheats1.png)
*Test Document Cheats*

It should be noted that there is no way to enable these cheats for multiplayer tests. Should you require something similar, you'll need to devise a custom solution. If some mixture between private and public testing is desired, it is recommended to limit access to cheats to yourself as the developer and trusted parties only. This can be done with secrecy, but a better method is to use player handles and make a check of them upon either entering the game or within the conditions of each cheat trigger. Doing so will ensure that only a hardcoded list of players has access to your equivalent of test document cheats in multiplayer trials. You can see one example a system like this below.

[![Multiplayer Test Document Cheats](./resources/055_Debug_Cheats2.png)](./resources/055_Debug_Cheats2.png)
*Multiplayer Test Document Cheats*

## Actor Cheats

When testing a document from the editor, Actor Cheats are also available. These cheats provide a number of ways to create and control Actors without needing to create custom testing provisions. It should be noted that

actor cheats are the only way to debug actors, as the Trigger Debugger does not contain any information about them due to their asynchronous nature. Actor cheats are similar to test document cheats in that they are activated by entering text into the in-game chat.

A particularly useful actor cheat command is `actorinfodisplay`. This command will display an in-game overlay showing how many actors and actor scopes are currently active, along with other useful information. The following images show the actor stats before and after a stress test trial.

![](./resources/055_Debug_Cheats3.png)
*Before Actor Stress Test -- After Actor Stress Test*
