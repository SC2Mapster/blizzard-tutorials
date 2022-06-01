---
title: Basic spellswap system
authors:
    - duckies
---



# Basic spellswap system


## Preface


This tutorial attempts to be beginner friendly, however it is expected to have some minimal experience with both data and triggers as we will need to work with both of those modules. Trigger part will feature creation of action definitions, working with catalog triggers and data tables. All in all there will be a total of 5 triggers made, all of them being pretty small + there is an example map attached for reference.


## Introduction


Back in Patch 5.0 blizzard graced us with:


>**Dynamic Ability Support**
>
>    Modders can now use triggers to add or remove abilities from units.

We are going to take advantage of this feature to make something very cool.



Here are our objectives for this tutorial:



**Objective 1** – Check out how this feature works by giving unit an ability via trigger.

**Objective 2** – Create a simple ability equip/dequip system that is quick to setup and easy to work with.





## Objective 1 – ability addition test

**What we will do:**

Our goal is to successfully add ability to unit via triggers.

**Process**

Lets take a Zeratul and place him on the map. From now on I'll refer to this unit as "***hero***".


We want to see how the trigger works. Open up trigger module, remove default actions from map initialization trigger and create new action "**Add Ability**". Lets add ability called "***ArtanisVoidPsiStorm***" to our hero.

![](SpellSwapAssets/1_InitalAbilAdd.png)

If we launch map now we'll notice that nothing happened. Lets check description of that add ability action.

>Added ability may not be able to be cast without command buttons. You can set a ability to automatically create command button, by go to the ability's Command+ field, and assign default button for them. "Use Default Button" and "Create Default Button" flags needs to be check to allow the button to be auto created. The position of the auto-created button can be set in the Button data.



Lets' do just that. In ability which we will be assigning ("***ArtanisVoidPsiStorm***") go to "**Commands+**" field and as tooltip tells us, check "**Use Default Button**" and "**Create Default Button**" flags.

![](SpellSwapAssets/1_CommandExtraFlags.png)

After that go to button that is linked to execute command ("***Artanis - Psionic Super Storm***") and find field called "**Default Button Layout+**". Set "**CardID**" to "0001", "**Column**" to "1", "**Row**" to "1". Note that columns go from 0 to 4, rows go from 0 to 2. It should be easy to figure out what to put here to get desired button position.



Now, launch the map again. Everything should be working! Just in case if something went wrong, there is a map at the bottom of tutorial to serve as reference.

![](SpellSwapAssets/1_AbilityAddedIngameScreen.png)


## Objective 2 - ability pickup/swap system.

**What we will make:**

Map will have different abilities stored in pickups that are placed around the map. Hovering mouse over pickup will display information about ability it grants. Player will right-click on them with hero causing hero to approach the pickup and interact with it - gaining ability stored within and destroying pickup in the process.

Due to limitation of technology all abilities must have predefined position on command card. We will design our system to have 3 abilities occupying first three bottom left buttons of unit's command card (lets call them Q, W and E slots).

In case if hero picks up ability for a slot that is already taken by some other ability - they will remove and drop on the ground their currently equipped ability before equipping new one.

[gif of hero picking up and swapping 3 different Q slot abilities]

**How we will make it:**

To create such a system we will need to do 5 tasks:

**1) Data preparation.** Need to create a unit type that will serve as pickup. Create ability with which hero will interact with the pickup.

**2) Store trigger.** Need to create trigger to make pickup unit store ability of choice + display that info.

**3) Data ability preparation.** Need to configure abilities for use (check those flags, define position on CC + more).

**4) Equip/Dequip trigger.** Need to create a trigger to transfer ability from pickup to hero when hero interacts with the pickup.

**5) Wrap up trigger.** Need to tie everything together in the interaction trigger.



Everything data-related will be simple – just changing values.

Trigger part will be mostly about fetching information from data via catalog triggers and saving/retrieving information via data table.


### Part 1 – Preparation/Data

**Goal:**

Create a unit type that will serve as pickup. Create ability with which hero will interact with the pickup.

**Process:**

#### Step 1 – Pickup dummy unit:

Our goal is to create a pickup dummy (unit type) in which we will store ability reference via triggers.

For this lets duplicate "***New Equipment***" unit and name it "***Ability Pickup***" (also clear it's abilities field since we won't be needing that). Our plan is to display ability info in unit's tooltip and for that we need to go to unit's "**Flags+**" field and uncheck "**No Tooltip**". Additionally give the unit some unused collision flag ("**Air16**" is good) so that these pickups don't stack with each other when dropped on the ground.



#### Step 2 – Interact Ability:

Now lets make an ability for hero-pickup interaction. It will have a single set effect and a single validator that will make sure that ability can only activate on specific unit type of our choosing.

1) Create an "**Effect - Target**" ability. Call it "***Pickup Interact***". Either create a new button or add any existing one as it's "**Default Button**" for "**Execute**" command. ("**Commands+**" field). I've decided to use "***Pickup Scrap Small***" button.

2) Create a Validator of type "**Unit Type**", set it's value to "***Ability Pickup***" (the unit we just duplicated).

3) Create a "**Set**" effect, add our validator to it's validator field.

4) In "***Pickup Interact***" ability set effect to our newly created set effect, also go to flags and check "**Smart Command**". This will make unit automatically use ability when rightclicking (but validator makes it so that the ability will only execute when right-clicking on "***Ability Pickup***" unit.).

5) Add this ability to Zeratul. Since it's a smart ability we can go without adding a button to command card.



#### Step 3 – Trigger:

Create a new trigger, name it "***Pickup Interact***". Right now we will use this trigger simply to test that everything works, and later, once everything is done we will make use of it again. 

Event – "**Unit Uses Ability**". In ability choose our "***Pickup Interact***" ability. In stage choose "**Effect3 - Cast**".

Actions – "***Add Ability*** and "**Kill Unit**". In ability addition action for ability we can set "***ArtanisVoidPsiStorm***" and for unit "**Triggering Unit**". For unit killing action set unit to "**Triggering Ability Target Unit**". So this way that ability isn't granted on map initialization, but rather when unit rightclicks on a pickup unit.

Lets check that it works. Remove ability addition action from map initialization trigger, place "***Ability Pickup***" unit next to hero and launch the map. Rightclicking on pickup dummy with hero should make hero gain psi storm and destroy pickup.

![](SpellSwapAssets/2_1_PickupTest.gif)


### Part 2 – Making pickup unit store ability data.

Goal:

Create trigger to make pickup unit store ability of choice + display that info.

![](SpellSwapAssets/TooltipPreview.png)



Overview:

We want 2 things:

1) For pickup unit to display ability information (name, hotkey, description) when hovered over. We will use catalog triggers to access necessary texts from button that is linked to ability.

2) To store ability identifier in unit. We can achieve that with data tables.

Process:

### Step 1 - displaying info when hovering mouse over pickup unit:



First, create a new action definition (In trigger module right click -> New -> New Action Definition). Lets name it "***Set Pickup AbilityValue***". Give it 2 parameters – "**Unit**" (name it "***UNIT***") and "**Game Link – Ability***" (name it "***ABILITY***").


Create local variable of type "**Game Link – Button**", name it "***Button***".


#### Step 1.1 – Getting Button.

In actions, set our "***Button***" variable to "**Convert String to Game Link**".

In string's value choose function "**Catalog Field Value Get**".

In catalog choose preset -> "**Abilities**", in entry set our "***ABILITY***" parameter, in field path for scope chose "**Effect- Target**". In field choose "**CmdButtonArray**". Further, in index select "0" and in field chose "**Default Button Face**".

>        Variable -Set Button = (Game Link((Value of Abilities ABILITY CmdButtonArray[0].DefaultButtonFace for player Any Player)))

Now we have easy access to button that is used by ability. We can get it's catalog text values wit catalog triggers.


However, it's worth noting that this will only fetch button for abilities which have only 1 main execute button (abilities like "**Effect - Target**", "**Effect - Instant**", "**Behavior**", "**Augment**" and such). Abilities like "**Train**", "**Specialize**", "**Research**" and alike have an array of commands instead.

If we want to get a button info out of them, the process is the same up to when we need to set path for scope. Instead of "**Effect – Target**" put "**Train**" or some other ability type which uses array of commands instead of single command. After that instead of "**CmdButtonArray**" we'll need to choose "**InfoArray**" and then select from which array position to fetch the button link (for now lets settle on the first entry of the array - index 0).

Having done that, we now need to distinguish between abilities which have one command and array of commands. Thankfully we can find out ability type in triggers via function "**Ability Matches Filters**". Make an "**If Then Else**" statement with condition that if ability is of certain type – then use button fetching function setup 1, else do function setup 2.

![](SpellSwapAssets/2_2_SetPickupValue_ClassDetect.png)


#### Step 1.2 – Getting text from button.


Now that we have acquired a button we can fetch the text that and prepare it for tooltip display.

Lets create 4 variables of type text. Name them "***Name***", "***Description***", "***Hotkey***", "***Final Text***".

Set "***Name***" variable to function "**Convert Game Text**". In path chose function "**Catalog Field Value Get**". For catalog choose preset – "**Buttons**", for entry chose our "***Button***" variable, for field chose "**Name**".



Do the same thing for "***Description***" variable, but for catalog's field chose "**Tooltip**" instead.



"***Hotkey***" is going to be a little bit different, we will have to use "**Convert Game Hotkey**" function rather than the usual game text (for path use the same "**Catalog Field Value Get**" function again).



Now that we have all the information we need, we can display it in any way we want! I chose to combine all gathered information in a "***Final Text***" variable using expressions.

![](SpellSwapAssets/2_2_SetPickupValue_FinalFormatting.png)

To make pickup unit display all this text we use "**Set Unit Info**" action. "**Info Text**" is what's displayed on command card when you click on unit, "**Hightlight Tooltip**" is the tooltip.

Apply the formatting of choice.

![](SpellSwapAssets/2_2_SetPickupValue_InfoTextAction.png)


#### Step 2 - Storing ability.

We will store ability identifier in a data table entry called after pickup unit's unit tag. This way as long as we have the pickup unit, we can find out it's data table entry. If you're unfamiliar with data tables you can read more here: https://s2editor-guides.readthedocs.io/New_Tutorials/03_Trigger_Editor/041_Data_Tables/ (TL;DR it's variables you can create and destroy on the go).


Create new action: "**Save Data Table Value (String)**". For value use function "**Convert Game Link to String**", for game link choose "***ABILITY***" parameter. For name we can use units tag. Choose "**Convert Integer To String**" function, then pick "**Unit Tag**" function. For unit select "***UNIT***" parameter.

It is done!

![](SpellSwapAssets/2_2_SetPickupValue_FullTrigger.png)

### Part 3 – Preparing abilities.


As established earlier, for ability to be added to unit via triggers it needs:

- "**Use Default Button**" and "**Create Default Button**" flags toggled on.

- "**Default Button Layout+**" field modified to specify where exactly place those buttons.



We will also need to somehow determine to which slot (Q,W or E) ability belongs. Thankfully we have "**Categories+**" ability field, whose tooltip states:

>A method of categorizing abilities that can be useful for identifying certain abilities.

Perfect! Lets use "**User 1**" for Q, "**User 2**" for "W" and "**User 3**" for E.


Next, we need to decide which abilities to test out.


Lets check out all sort of stuff.
|Slot|Abil Type|Abil Name|
| ------------- | ------------- |------------- |
|Q slot|Effect Target|High Templar - Psi Storm|
|Q slot|Effect Target|Vulture - Use Spider Mines|
|Q slot|Effect Instant|Marine - Stimpack|
|W slot|Behavior|Ghost - Personal Cloaking|
|W slot|Specialize|Vulture - Make Spider Mines (Hidden Build)|
|W slot|Train|Swarm Queen Train|
|E slot|Arm Magazine|Karax - Servitors|
|E slot|Research|Engineering Bay - Research (Engineering Bay)|

Now, lets go to these abilities and modify them so that they could be used by our hero:
- In ability's "**Commands+**" field check "**Use Default Button**" and "**Create Default Button**" flags on.
- In "**Categories+**" field check "**User 1**" for Q slots, "**User 2**" for W slots, "**User 3**" for E slots.
- In their linked buttons, in the "**Default Button Layout+**" field set "**Card ID**" to "0001", "**Row**" to "2" and "**Column**" to "0" for Q slots, "1" for W slots, "2" for E slots.
- *[Optional]* In button also don't forget to change "**Hotkey**" to match Q/W/E.
- *[Optional]* Also add "Q", "W", or "E" to ability's "**Editor Prefix**" field as it will make it so much quicker to search for them in triggers.
- *[Note]* Some abilities (like stimpack) have research requirements, so don't forget to clear those (Requirements can be removed in "**Commands+**" field).
- For abilites that make use of multiple buttons (like ghost's cloak or any train/research/array abilities) we'll need to apply the above steps for each of buttons we want to be created when ability is added (don't forget to place those buttons in different slots so they don't overlap).


### Part 4 – Ability Equip/dequip.


The process of equipping ability consists of 3 steps:



1 – finding out which slot ability will use;

2 – discarding already equipped ability if it's the in the same slot as the one we're picking up;

3 – saving information that ability is stored in our hero's ability slot.


To figure out slot (#1) we can use simple loop which checks ability's catalog.

To save information about equipped ability (#3) we will use data tables again. Going to convert game link to string and save that string under appropriate path. For datatable's path we will use both unit's tag and slot number. Saving this way will also allow us to check requirements for dequipping.

#### Ability dequip.

Overview:

Lets start with creating dequip action as it's something that we'll need to use in equip process. We will create an action definition which will discard ability from target unit's target ability slot.

This process will consist of:

- finding out the ability that unit has in targeted ability slot

- removing ability for the hero

- erasing data table record that stores information abut which ability is stored in unit's targeted ability slot.

- creating a pickup unit

- implanting ability into pickup



Process:



Make a new action definition, call it "***Ability Dequip***", give it 2 parameter. A "**Unit**" type (name it "***UNIT***") and an "**Integer**" type (name it "***SLOT***").



Create local variable of type "**Game Link – Ability**", name it "***Ability***".

Create local variable of type "**String**", name it "***DataTable Path***".



We will create data table's path name out of two variables known to us – our hero's unique unit tag and ability slot's id. And a "." character to separate them (for easy readability).


So, set "***DataTable Path***" variable to expression that converts "**Unit Tag**" of "***UNIT***" parameter and "***SLOT***" parameter into string and then combines them, like in example below.

>Variable -Set DataTable Path = {(String(SLOT)).(String((Unit tag of UNIT)))}.
![](SpellSwapAssets/2_4_DataTablePath.png)

We create this shortcut so that it would be easier to change and reuse it later in code when we work with data table.


Next we retrieve ability value from data table.

Set "***Ability***" variable to function - "**Convert String to Game Link**". For string choose "**Value From Data Table (String)**", and use the "***DataTable Path***" variable for the path.

Use "**Remove Ability**" to remove ability we just retrieved from our hero.

Use "**Remove Data Table Value**" to clear data table record to avoid leaks.

>Theoretically we don't need to do it for this setup, because we'll always replace ability value stored in this data table path. But if we were using this trigger to remove ability without replacing it right away, then we should absolutely clear after ourselves.



Next we create a pickup unit at position of hero.

And finally we inject ability into created shell unit by using action we've made earlier ("***Set Pickup AbilityValue***").

![](SpellSwapAssets/2_4_AbilDequipFullTrigger.png)


#### Ability Equip.

Overview:

Equip will be similar to dequip, the actions that we will do are:

- detecting to which slot ability we're equipping belongs to

- if hero already has ability in needed ability slot – dequip currently equipped ability

- add ability to hero

- save information that hero has specified ability in ability slot to a data table record

Process:

Make a new action definition, call it "***Ability Equip***", give it 2 parameter. A "**Unit**" type (name it "***UNIT***") and a "**Game Link - Ability**" type (name it "***ABILITY***").

Create local variable of type "**Integer**", name it "***Hotkey Slot***".

Create local variable of type "**String**", name it "***DataTable Path***".



First thing – we need to understand which category flags are checked for ability we're equipping.

In data editor if we toggle "**View**"->"**View Raw Data**" (Ctrl-D shortcut) and look at category flag in ability we'll notice that all those flags are just "0" and "1", "0" for unchecked and "1" for checked. So we can use catalog trigger ("**Catalog Field Value Get As Integer**") to fetch value of each flag as integer.


![](SpellSwapAssets/2_4_CategoriesRawView.png)


So let's loop through each flag, and if that flag returns "1" – save it's numeric id to "***Hotkey Slot***" variable.

Create "**Pick Each Integer**" loop, set starting value to "0" (which will correspond with "**User 1**" flag) and finishing value to "2" (which will correspond with "**User 3**" flag).

Then inside pf the loop create an "**If Then Else**" statement. In condition use "**Catalog Field Value Get As Integer**" to see if ability category's flag (corresponding with picked integer) is 1. If it is indeed 1 – then set our "**Hotkey Slot**" variable "**Picked Integer**" (so that we remember that category number  "**Picked Integer**" is checked).

![](SpellSwapAssets/2_4_Equip_FlagDetectionSetup.png)

![](SpellSwapAssets/2_4_Equip_FlagDetectionLoopComplete.png)


One we've found our hotkey slot id, we're ready set "***DataTable Path***" variable and access data table to check if hero already has something in that slot.

>Variable -Set DataTable Path = {(String(Hotkey Slot)).(String((Unit tag of UNIT)))}

Use "**If Then Else**" statement with "**Data Table Value Exists**" function to find out if "***DataTable Path***" data table record exists – then use "***Ability Dequip***" action to unequip and drop that ability to the ground.

![](SpellSwapAssets/2_4_Equip_DequipCondition.png)

Once all that is done we add ability using "**Add Ability**" action.

Finally we save ability identifier in data table so that we can know in future that we have stuff equipped. (Use "**Save Data Table Value (String)**". For value pick "**Convert Game Link to String**" function, and for path we have our "***DataTable Path***" variable.)

![](SpellSwapAssets/2_4_Equip_FullTrigger.png)


### Part 5 - Wrap up

Now we go back, change our "***Pickup Interact***" trigger to make use of "***Ability Equip***" action.

We can remove any actions we had in there.

After clearing it up, let's create local variable of type "**String**", name it "***DataTable Path***", set it to reference pickup's unit tag.

>DataTable Path = (String((Unit tag of (Triggering ability target unit))))

Next make an "**If Then Else**" statement. If data table value exists then equip ability stored in pickup and kill pickup unit.

>Ability Equip((Triggering unit),(Game Link((DataTable Path from the Global data table))))

![](SpellSwapAssets/2_5_PickupInteractFinalTrigger.png)


After that, place a bunch of empty pickup units on the map. Add abilities to them in map initialization. Remove default ability buttons on 3rd row on Zeratul (so that nothing overlaps with our pickup acquired abilities) and also give him 10000 energy so that he doesn't have issue casting them. Run the map and see how it all works!

We now have a functional quick and simple spell equip/swap system. Well done!

* [SpellSwapTutorial.SC2Map](SpellSwapAssets/SpellSwapTutorial.SC2Map)


NOTES:

1)In my testing I've noticed that giving unit a "**Brood Lord - Brood Lord Hangar**" ability will occasionally cause starcraft to crash, while other "**Arm Magazine**" ability "**Karax - Servitors**" didn't cause any issue.

2)There exists a 32 ability limit on unit. Remove old abilities to keep currently equipped ability count within the limit. Going over this limit will cause starcraft to crash.
