# Actor cheats

With Patch 1.4.0, modders can now use actor cheats to create and manipulate actors on the fly while running a test map from the editor. This is useful for quickly testing ideas without having to set up data or execute triggers.

The cheats can also be used to modify and inspect almost any actor while a test map is running, which can be useful for debugging run time actor issues.

The cheats can be used to send several newly-enabled dump messages, such as AnimDumpDB, AttachDump, HostedPropDump, RefDump and TextureDump. These messages enable modders to inspect some internal aspects of certain actors while the game is running, which can be helpful as an additional debugging aid.

## Actor Cheat Concepts

### Ref Names

The term "Ref Name" is shorthand for "Actor Reference Name", which uniquely identifies a type of system variable known as an actor reference ("actor ref" or just "ref" for short). An actor reference can be resolved into a given actor, depending on 1) the meaning of the ref name and 2) the context in which it is used. Ref names can be used in many of the cheats, where specified. Their availability may vary, depending upon the context in which they are used:

- D - from within Actor(D)ata
- T - from within actor-related functions in (t)riggers
- C - via actor (c)heats

The currently available ref names are:

| **::HoverTarget**       | C    | The actor under the mouse cursor.                            |
| ----------------------- | ---- | ------------------------------------------------------------ |
| **::LastCreated**       | DTC  | From triggers, this resolves to the last actor successfully created directly via a trigger function (but not through any of the other means, such as via message in data as a result of a trigger call). From everywhere else, it also includes actors created explicitly via the Create message (i.e. Create SomeActor). This is intended to maximize consistency across the different variations of the LastCreated() mechanism in the triggers while still attempting to adhere to the rule of least surprise everywhere else. |
| **::LastCreatedActual** | DTC  | The last actor successfully created by the user through whatever means. Includes actors created by the Create message, actor request creates, or actors created internally by the system (such as when CActorAction creates squibs). |
| **::Main**              | DTC  | The "main" actor of the ::User scope                         |
| Doodad                  |      | The CActorDoodad.                                            |
| Unit                    |      | The CActorUnit.                                              |
| The rest                |      | The first actor created in the scope.                        |
| **::PortraitGame**      | DTC  | The main actor for the game portrait window, right now, regardless of what is selected. |
| **::PortraitGameSelf**  | DTC  | The portrait for the main actor in this actor's scope. Useful for sending messages from any actor in a unit's scope to its portrait actor. Returns nothing if the portrait is for a unit other than the current one. |
| **::Self**              | D    | The actor receiving an event.                                |
| **::User**              | TC   | Contains the results from the most recent ActorFrom cheat.   |
| **::global.<RefName>**  | DTC  | An actor ref from the global reference table.                |
| **::scope.<RefName>**   | DTC  | An actor ref from the containing scope reference table.      |
| **::actor.<RefName>**   | DTC  | An actor ref from the containing actor reference table.      |
| **TargetKey**           | TC   | The actor represented by the key from the ::User scope. Only returns the first one when there are multiple hits in the result set. |

### Branch Ref Names

|                  |      |                                                              |
| ---------------- | ---- | ------------------------------------------------------------ |
| **::Creator**    | DTC  | The creator of the ::User actor                              |
| Hosts            |      | A host actor is one that an actor inherits data from, such as bearings, hosted props, etc. |
| **::Host**       | DTC  | The main host. Used for bearings and hosted props.           |
| **::HostImpact** | DTC  | Used to position the impact point of a beam.                 |
| **::HostLaunch** | DTC  | Used to position the launch point of a beam.                 |
| **::HostReturn** | DTC  | The host a tentacle uses as the target for its return trip.  |
| **::Supporter**  | DTC  | Used to link the lifetime of an actor to a "supporting" actor (typically to set up events that tell an actor to die when its supporting actor has died). |


### Scope Ref Names

| **::Actor**        | TC   | The scope of the ::User actor.                               |
| ------------------ | ---- | ------------------------------------------------------------ |
| **::LastCreated**  | TC   | The last scope successfully created by the user via cheat or client code. Irrelevant from within data, since data doesn't create scopes. |
| **::PortraitGame** | TC   | The scope of the game portrait window.                       |
| **::Selection**    | C    | The scope of the selected unit. Returns a single scope even if multiple units are selected. |
| **::User**         | TC   | Contains the result from the most recent ActorScopeFrom cheat. Automatically gets set to the value ::LastCreated when that ref is populated with a new valid actor scope. |

### Content Keys

Create messages can take between 1 and 3 content keys. These enable triggers and cheats to more easily create a variety of actor instances using the same data entry, but with different "content" parameters. For instance:

`ActorCreateAt Model Hydralisk `

`ActorCreateAt Model Marine`

Both cheats create a CActorModel called "Model". The first one creates it with the "Hydralisk" asset and the second one creates it with the "Marine" asset. The various types of actors support different creation parameter styles on a case-by-case basis. What follows is a list of actors that support content parameters, and the order in which they are specified.

#### CActorBeam ModelLink RefLaunch RefImpact

* **ModelLink** - the name of the modelData entry used for the beam.
* **RefLaunch** - the ref name used to populate the beam's ::HostLaunch.
* **RefImpact** - the ref name used to populate the beam's ::HostImpact.

#### CActorList RefName

* **RefName** - source ref name from which to populate the list.

#### CActorModel

* **ModelLink** - the name of the modelData entry to be used for the model.
* **Variation** - the specific variation number for the model, if desired (otherwise it picks randomly).

#### CActorSound

* **SoundLink** - the name of the sound to be used.

#### CActorSplat

* **ModelLink** - the name of the modelData entry to be used for the splat.



## Actor Cheat Usage

The user can enter actor cheats into the chat line when running his map from the editor.

Output goes into the Alert.txt log, which can be found in the user's "StarCraft II/GameLogs" directory. The Alert.txt log has a date and time stamp prepended to its file name, so a real world example actually has a name like: "2011-08-08 10.30.05 Alerts.txt".

Shortcuts are not currently supported, but may be added at a later time.



### Actor Cheat List

In the given syntax for each command, a parameter surrounded by curly brackets {} denotes an optional parameter. On successful execution of some of these cheats, two global variables, "::User actor" and "::User scope" values are set, which other cheats can act upon. Cheats that kill actors and scopes exclude those actors and scopes that would break currently active units and effects.

#### ActorCreateAt

Creates an actor at the specified location. Sets the ::User actor to this actor and the ::User scope to its scope.

This cheat is useful for directly creating an actor on a test map, in order to observe its properties and interact with it, without waiting for the map to encounter a situation that would create the actor normally. The coordinates enable the user to position actors precisely for combat tests and the like.

##### Syntax

```ActorCreateAt x,y actorName {contentName} {content2Name} {content3Name}```

##### Examples

```ActorCreateAt 50,50 Model Drone ```<br/>
```ActorCreateAt 50,50 NexusSplat```

#### ActorCreateAtCursor

Creates an actor (and an actor scope to contain it) at the mouse cursor. Sets the ::User actor to this actor and the ::User scope to its scope.

This cheat is useful for directly creating an actor on a test map, in order to observe its properties and interact with it, without waiting for the map to encounter a situation that would create the actor normally. It places the actor at the cursor location, so the user doesn't have to worry about getting specific coordinates to position the actor in a readily visible location.

##### Syntax

```ActorCreateAtCursor actorName {contentName} {content2Name} {content3Name}```

##### Examples

```ActorCreateAtCursor Model Drone ```<br/>
```ActorCreateAtCursor NexusSplat```

#### ActorDumpAutoCreates

Dumps a list of all actors that are created as the result of data like this:

```xml
<On Terms="UnitBirth.Marine" Send="Create"/>
```

This type of actor creation pattern is called autocreation, since the actor automatically creates itself in response to a message. This is different than a creation pattern like this:

```xml
<On Terms="ActorCreation" Send="Create SomeActor"/>
```

Because here the Create message is explicitly specifying an actor to create.

ActorDumpAutoCreates can be used to track down whether actors are unintentionally being created by certain events.

##### Syntax

```ActorDumpAutoCreates```

#### ActorDumpEvents

Dumps a list of all actors events seen by the ::User actor, excluding autocreation events.

This cheat can be used to perform various text searches on all the actor events in a map, like if one wants to see all the actors that respond to a given Signal event, regardless of which dependency they are in.

##### Syntax

```ActorDumpEvents```

#### ActorDumpLeakRisks

Dumps a list of actors older than a particular age that have the possibility of leaking. The user can check if a muzzle flash model is over a minute old, for instance, since muzzle flashes never typically last that long. Some kinds of actors never show up the list of leak risks, since they are automatically cleaned up by the system and therefore cannot typically be leaked by bad data.

If a map gets progressively slower as time passes, this cheat can determine if leaking actors is the cause.

##### Syntax

```ActorDumpLeakRisks age```



#### ActorDumpLive

Dumps a list of living actors on the entire map, sorted by containing scope.

This cheat is helpful for determining if actors exist, despite them not appearing where they are expected to be in the game world. An actor that mistakenly appears at 0,0 will still show up in the list of live actors.

##### Syntax

```ActorDumpLive```



#### ActorFrom

Sets a new ::User actor from a live actor, given a ref name.

This cheat is crucial for setting various actors in the game world into the ::User ref, so that the user can send cheat commands to them.

##### Syntax

```ActorFrom RefName```

##### Examples

```ActorFrom ::HoverTarget```<br/>
```ActorFrom ::Selection```

#### ActorFromActor

Sets the ::User actor to an actor referenced via another actor and a branch ref name.

This cheat is useful for setting various parent and child actors in the game world into the ::User ref, so that the user can send cheat commands to them. It is commonly used to perform operations on the ::Host ref of an actor.

##### Syntax 

```ActorFromActor refName```

##### Examples

```ActorFromActor ::Host```

Sets the ::User actor to the actor that it was hosting from.

```ActorFromActor ::Creator```

Sets the ::User actor to the actor that created it.

#### ActorKillAll

Kills all actors, except those that are part of live units and effect trees.

Useful for clearing a test map of actors so that individual actors can subsequently be tested in isolation.

#### Syntax: 

```ActorKillAll```

#### ActorKillClass

Kills all actors of a specified class within a given radius from the cursor. If the radius is not specified, it is infinite.

Can be used to clear an area (or the whole map) of a given type of actor, if they are making it hard to focus on a problem that the user is investigating. For instance, it might make sense to kill all doodad actors to confirm whether they are the cause of a performance problem.

#### Syntax: 

```ActorKillClass class {range}```


Examples:

```ActorKillClass Model 15 ActorKillClass Sound```

#### ActorKillLink 

Kills all actors with a specified actor link within a given radius from the cursor. If the radius is not specified, it is infinite.

Can be used to clear an area (or the whole map) of all instances of a specific actor entry, if they are making it hard to focus on a problem that the user is investigating. For instance, it might make sense to kill all the models of a particular name in an area of effect (AoE) attack, if too many are being created and obscuring some other part of the graphical FX for an attack that the user is debugging. Or, the user might kill all sounds with a given name to see if he can hear other sounds also associated with an effect.

#### Syntax: 

```ActorKillLink link {range}```



##### ActorSend

Sends a valid user message to the currently active ::User actor.

By far the most used actor cheat, and the main way in which developers (internal or external) interact with actors via cheats.


#### Syntax: 

```ActorSend message```


#### Examples:

```ActorSend Destroy ActorSend SetTintColor {255,255,0}```

#### ActorSendTo

Sends a message to a system actor reference, using the ::User actor to help resolve the system actor reference. In other words, this routine sends messages to branch ref names (though it also works on the ::Main ref name).

This cheat can be a shorthand way of sending messages to branch actors; the user does not need to first use the ActorFromActor cheat to set them into the ::User ref.


Syntax: 
ActorSendTo refName message


Examples:

ActorSendTo ::Host SetOpacity 0.5 ActorSendTo ::Main SetTintColor {255,0,0}

#### ActorScopeDumpLive

Dumps a list of living scopes on the entire map.

This cheat can be useful for looking for actors scopes that are needlessly consuming resources, but no longer have any (useful) actors in them.


Syntax: 
ActorScopeDumpLive






**ActorScopeFrom**

This cheat is crucial for setting various scopes in the game world into the ::User scope ref, so that the user can easily find and send messages to any of the actors in that scope.


Syntax: 
ActorScopeFrom scopeName


Examples:

ActorScopeFrom ::PortraitGame ActorScopeFrom ::Selection

Kills the currently set ::User actor and ::User scope. This command cannot kill scopes for live units or effects to prevent unexpected results.

This cheat is an effective way to kill one or more actors that the user has been experimenting with, by just killing their containing scope (since this kills all actors inside the scope).


Syntax: 
ActorScopeKill




**ActorScopeOrphan**

This cheat can be used to test the effects of the ActorOrphan message on actors inside the ::User scope.


Syntax: 
ActorScopeOrphan






**ActorScopeSend**

Useful in the rare cases where the user wants to send a message to all actors in a scope.

(As an aside, while it might seem like this cheat is a good way to tint all models in an actor scope red [for instance], it is typically better to have child actors host off of the ::Main actor and inherit the tintColor property. Then the user merely sends the SetTintColor messages to the scope's ::Main actor, and relies on hostedProp inheritance to percolate the color change. This latter method is typically superior when a scope can have actors that shouldn't be tinted red (such as enemy impact squibs) along with the actors that are intended to be red. Broadcasting the tintColor message turns all models in the scope red, regardless.)


Syntax: 
ActorScopeSend message


Examples:

ActorScopeSend Destroy




**ActorUsersDump**

This is useful if the user forgets what these refs are currently set to.


Syntax: 
ActorUsersDump




**ActorUsersFromHoverTarget**

Very useful for being able to inspect and operate upon any actor in the game world that does not belong to an object that can be selected.


Syntax: 
ActorUsersFromHoverTarget




**ActorUsersFromPortraitGame**

Useful for being able to inspect and operate upon the actors contained by the portrait window.


Syntax: 
ActorUsersFromPortraitGame




**ActorUsersFromSelection**

Very useful for being able to inspect and operate upon any actor in the game world that belongs to an object that can be selected.


Syntax: 
ActorUsersFromSelection




**ActorWorldParticleFXDestroy**

Can be used to immediately clear the world of obscuring particle and ribbon FX (typically while the game is paused), in order to closely inspect models or some other part of some visual FX.


Syntax: 
ActorWorldParticleFXDestroy

## 





Actor Dump Messages



The user can send actor dump messages to actors to get useful debugging-related information from them.




**AliasDump**

Prints out all the actor aliases currently associated with the actor.




**AnimDumpDB**

Prints out all the animations available to the model associated with the actor. Prints the duration for each animation, along with whether it is a looping animation.




**AttachDump**

Prints out all the attach points that exist on the model associated with the actor. Also prints the user-specified attach keys and target attach volumes associated with each attach point.




**HostedPropDump**

Prints out all the information associated with the specified hostedProp if it exists on the actor. If the IncludeChildren parameter is 1, it prints out the information for that prop for the target actor along with all of its children.

Examples:

HostedPropDump 0 TintColor HostedPropDump 1 TeamColor

Syntax: 
HostedPropDumpAll IncludeChildren

Prints out all the information associated with all the hosted props that exist on the actor. If the IncludeChildren parameter is 1, it does the same for all of the target actor's children as well.




**RefDump**

Prints out debugging information on the actor specified by the refName. Currently, this only works for actor refs in system ref tables, which means refs of the format ::actor.someUserRef, ::scope.someUserRef and ::global.someUserRef.


Examples:

RefDump ::actor.someUserRef




**RefTableDump**

Prints out debugging information on all the actor refs in a given ref table. The RefTableType parameter is case sensitive, and expects the tokens Actor, Scope or Global.


Examples:

RefDumpAll Actor




**TextureDump**

Prints out all the textures currently being used by the model associated with the target actor. Indicates which ones are associated with texture slots and whether they have been swapped out and replaced by other dynamic textures.




**TextureDumpDB**

Prints out all the textures available for dynamic texture swapping on the model associated with the target actor.
