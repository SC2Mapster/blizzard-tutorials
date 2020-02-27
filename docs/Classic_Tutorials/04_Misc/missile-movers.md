# Missile Movers

The missile mover system uses a video editor metaphor. The map maker can chain up to 5 motion phases one after the other, transitioning between them via blends, as necessary. It is also possible to add extra motion overlays on top of the phases to further customize their look, similar to how one can overlay video processing effects on a video stream.

Missiles are typically used to configure missile-based attacks, but the underlying motion can also be used to drive a reaper's body when it jumps or a spine crawler's tentacle when it attacks.



## Motion Drivers

At the core of each motion phase is a driver. There are four types:

1. **Guidance** - The missile moves after the target in 3D space, like a standard guided missile.
2. **Ballistic** - The missile flies through the air with a parabolic trajectory.

3. **Parabola** - Causes the missile to take a fixed parabolic arc, regardless of its acceleration and deceleration.
4. **Throw** - The missile travels along an arbitrary linear path in a specified direction.



## Motion Overlays

Overlays cause a missile to move around the core driver path in some spiffy way. The user can stack up to two different overlays on top of the same driver, for instance by using sine waves to vary motion on both horizontal and vertical axes simultaneously.

While they alter the real in-game position of the missile, they do not actually alter the path of the motion driver underlying them. In other words, a guided missile moving with a sinusoidal motion overlay actually has an invisible guided path governing its arrival at the target, even though it appears to be moving in a sinusoidal fashion.

There are three types:

1. **Wave** - Enables missiles to wave back and forth as they move, in a sinusoidal fashion.
2. **Orbit** - Enables missiles to have corkscrew, spiraling motion.

3. **Revolver** - Similar to an orbit overlay, except the orbiting motion does not always travel the same direction -- it chases an arbitrary rotation on the movement axis that is generated at launch time. Depending on the speeds involved, this can send the missile revolving past the target, in which case, it slows down and revolves back in the other direction.



## PHASE TRANSITIONS AND BLENDING

The user configures the end of a phase by specifying its outro. An outro ends a phase by passing a "distance traveled" threshold relative to the source or "distance remaining" threshold relative to the target. Source-relative outros are positive and target-relative outros are negative.

When you specify an outro in data, you have to specify a Blend At value and a Stop At value. If these two values are the same, then the missile will instantly switch over to the next phase once the specified outro distance is reached. If the two values are different, then the motion phases will blend between the two values. While a blend is active, two phases (the current and the next) run in parallel and their results are blended together. Generally speaking, blends result in smoother movement, particularly when the motion drivers on the blending phases are different. Blends are almost always necessary to avoid glitches.



## How it Works

As with many other objects in StarCraft II, missiles have both a synchronous game part and an asynchronous actor part. Missiles simulate their game state 32 times per second, which is double the rate of a normal unit. As with everything else, they draw when there is enough time to do so, which means they can draw anywhere from many times between each game loop (if the game is running smoothly) to not at all for long periods (in dire frame rate situations). The game part of the missile simulates twice per game loop and then pushes the data over to the actor side of the missile, which interpolates between the data it has on hand. In dire frame rate situations, it is possible for the actor side to fall behind, in which case the user sees missiles jump.

Because of the game/actor split, missiles actually have two flight paths: a game path and an actor path. The game path travels from the origin point of the attacker to the origin point of the target. The actor path travels from the launch attach point to the impact attach point. A process called adaption occurs internally to ensure that missile the user sees on the screen tracks the basic game path, while still moving directly between launch and impact attach points.

Also of note is the fact that motion overlays are synchronous. This enables them to be much more dramatic, without causing jerky movement. They actually scale down the underlying driver movement such that the real missile velocity (with overlays included) matches the speed specified by the user.



## Data Configuration

### Relevant Catalogs

- *MoverData.xml* to determine the path the missile takes to its target.
- *EffectData.xml* to configure the missile's Launch Missile effect, which will determine the source and target for the missile, and can pick the mover to use for the missile.

- *UnitData.xml* to give the missile its unit, so it can be treated as an interactable object in the game world.

- *WeaponData.xml* or *AbilData.xml* to configure the weapon or ability that triggers the Launch Missile effect.
- *ActorData.xml* to declare the actor part of the missile and to configure the visuals and audio for the attack, via Actor Action. This includes choosing the launch and target attach points that the missile travels between.

### Mover Data Editing Details

To minimize Mover data entry, data from one motion phase automatically carries over to the next phase, unless it is irrelevant or overridden there.

The user enters time data in seconds, and angle data in degrees.



## Motion Phases in Detail

Every motion phase has a number of generic fields that apply to two or more phase driver types, along with an array of fields that customize specific drivers. It also has a small array for varying the scale of the motion overlays present during that phase.

**Driver** - The type of motion that drives the entire phase: adaptable parabola, ballistic, guidance, or throw.

**Acceleration** - Controls how quickly the missile accelerates. Can be negative to decelerate the missile.

**Acceleration Range** - The range for a random extra amount to add to the base Acceleration value.

**Speed**

The speed the missile starts the phase with. The user typically configures this value on the first phase, since the missile's actual speed, in most cases, automatically carries over to the next phase while it is flight. (Speed does not currently transfer into ballistic phases, nor does it transfer out of throw phases where the rotation of the missile is not pointing in the direction of the throw.)

This field is uniquely interpreted as constant horizontal speed by the ballistic driver.

**Speed Range** - The range for a random extra amount to add to the base Speed value.

**Min Speed** - The minimum speed the missile can possibly travel during the phase. Useful for ensuring deceleration doesn't stop a missile altogether.

**Max Speed** - The maximum speed the missile can possibly travel during the phase.

**Gravity** - The gravity experienced by the missile. By tuning this value, it is possible to make certain kinds of missiles appear "floaty" (low gravity) or extra aggressive in their motion (high gravity).

**Clearance** - This is the closest the missile can come to the ground. It is useful for missile types that might collide with cliff edges when attacking targets from above or below. It is best avoided with ballistic drivers.

**Clearance Look Ahead** - This value governs how far ahead to look for a possible collision with the ground. The farther ahead a unit looks, the earlier it can start adjusting its path, but the more performance cost it has.

**Ignore Terrain** - This flag determines whether the missile uses the Clearance and Clearance Look Ahead fields or just clips through terrain.

**Turn Type**

Governs how a missile turns towards the target and whether it cares about the notion of up maintained by human fighter pilots. Can be three values:

- *Default.* The missile turns like a fighter pilot, by preferring to use whichever turn arc gets it to the target faster, yaw or pitch. This varies based on the yaw and pitch rate of the missile, along with the relative position of the target. Unlike a fighter pilot, the missile does not right itself, and happily remains upside down.
- *Revert To Up.* The missile turns like a real fighter pilot, rotating back so that its up axis points towards the sky when not turning. This turn type can cause missiles to pull the famous "Immelman Turn" devised by the noted German WWI ace.

- *Optimal.* The missile uses quaternions to arrive at the optimal 3D rotation to use to reach the target as quickly as possible. This can result in non-intuitive rotations that appear to have no regard for the laws of physics.

**Tracking**

Tunes how a missile reacts when its target moves in ways that might cause the missile to appear to behave oddly:

- *No Hook.* The default. Causes the missile actor to track the synchronous motion, except for the asynchronous steps across the final synchronous step, where the actor continues on the course from the prior synchronous step. This prevents hooks when the missile is slightly off the destination, such that facing towards it would cause the missile to rotate radically during the final subseconds of its flight. Not using this setting can cause a missile to turn wildly just before hitting its target, while setting it in the wrong situation can cause a missile to appear to shoot past its target.
- *Linear.* The missile always points in the direction established when it is first fired. Used by lasers, which should never appear to rotate. Causes them to slide sideways instead, as in the first StarCraft.

- *Actual.* The missile stays facing the same direction across the final sync step, just like No Hook, but can still guide towards the precise impact point.

**Arrival Test Type**

Controls how a missile tests whether it is close enough to its target to be considered "arrived". Can be three values:

- *Adaptive.* The default. The test automatically switches between 2D for target points and 3D for target units.
- *2D.* The missile uses a 2D test, which means an EMP missile could detonate far above a target, while still being considered to have hit it.

- *3D.* Means the missile looks at real 3D distance to determine arrival. Ballistic missiles typically perform 2D tests on point targets, but sometimes need 3D tests if they have very steep arcs. Without a 3D test, the ballistic missile explodes far above the target, since it is almost directly on top of it in the XY plane even though it is still far away in 3D space.

- *Never.* The missile will never impact. This is useful for cases where you want to throw a missile in a direction without a specific target, and have a behavior on that missile scan for targets around it.

**Blend Type**

Controls how blending occurs between overlapping phases. Can be three values:

- *Linear.* Straight linear blend.
- *Logarithmic.* Causes the blend to start rapidly but taper off. Results in very smooth looking curves.

- *Exponential.* Causes the blend to start slowly but increase exponentially.

**Outro**

A critical field that controls when and how the phase ends. It has 4 different values associated with it:

- *Blend At.* Governs when a given phase starts to blend into the following phase. If the number is equal to Stop At, it means that the phase has a hard transition, and there is no blending.
  If the number is positive, it means the blend starts when the missile has traveled that distance from the unit that fired the missile. If it is negative, it means the blend starts when the missile is that distance from the target. It can be zero on the first phase, meaning a blend starts immediately, or it can be zero if it is the only entry on the last phase. In the latter case, it means the phase ends when the missile strikes the target. Regardless, this is distance along the core motion driver (for instance, the core guidance path of the guidance driver), and does not account for the extra distance the missile traverses due to overlays.
- *Stop At.* Controls when the phase actually ends if there is a blend.

- *Blend At Range.* The upper bound of a random value that gets added to the Blend At value. It causes missile flight paths to vary with each subsequent launch. It cannot cause the Blend At position to go past the Stop At position. Always positive.

- *Stop At Range.* The upper bound of a random value added to Stop At. Always positive.

**Rotation Launch Actor Type**

Configures the rotation of the visual part of the missile when it launches, so that its apparent rotation doesn't need to match the game launch rotation.

- *None.* The default. The missile actor's launch rotation matches the missile's game rotation.
- *Launch To Target.* Causes the missile to face directly at its impact point at launch time. This may not be a good choice if the missile launches out the side of a vehicle.

- *Launch To Target 2D.* Like Launch To Target, but the missile stays parallel to the ground.

- *Supplied.* Indicates that the missile actor's launch rotation is being supplied to the actor internally via game code. It is used by tentacles.

**Rotation Actor Type**

Configures the rotation of the missile while it travels, so that its apparent rotation doesn't necessarily relate to its actual travel path.

- *None.* The default. The missile actor's rotation matches the missile's game rotation.
- *Docking.* Causes the missile to arrive at the position and reversed rotation of the actor determining its impact point. This type of actor rotation is used when a tentacle returns, to ensure that the tentacle's "head" precisely matches its recoil animation. If the impact point of a missile has a forward vector of 0, -1, 0, the missile will have a forward vector of 0, 1, 0 as it moves towards its target. This is because the missile is pointing towards the tentacle's owner, even though the tentacle appears to still be pointing at its target.

- *Look At Target.* Causes the missile to face directly at its impact point, no matter how it moves. Useful for having air-to-ground missiles appear to drop from the fuselage of a fighter plane before ignition, while still facing towards the impact point.

- *Look At Target 2D.* Like Look At Target, but the missile always stays parallel to the ground. Could be used for a UFO-type projectile, that always appears to move laterally across the ground, regardless of direction.
- *Upright.* The missile always appears upright (like a humanoid walking), regardless of its current direction. In other words, it has neither a pitch nor a roll.

- *Zero Roll.* The missile never has any roll, though it may have a varying pitch.

**Timeout**

Causes a phase to terminate after a certain amount of time has elapsed. If the phase has a blend, it starts the blend and causes the end of the blend to be as far away from the blend start as it would normally be (i.e. if a blend and stop are set at 5 and 7, then a timeout that causes the blend to start at 2 will also cause the stop to occur at 4).

**Overlays**

An array of up to two scale values. (The system does not support more, because the effect of individual overlays become hard to discern if there are too many.) Scale controls how big an overlay appears. For a wave overlay, scale control the wave's amplitude, while for orbit and revolver overlays, it controls the revolution radius.



## The Guidance Driver in Detail

The guidance driver supports the canonical guided missile. It causes the missile to chase the target, regardless of where it moves. Most missiles that are not simple ballistic projectiles have a guided driver phase somewhere.

**Orientation**

Individually limit how fast the missile can turn in the three traditional rotational axes used by pilots (yaw, pitch, and roll). This enables the user to configure a missile like a fighter plane, which rolls faster than it can pitch and pitches faster than it can yaw.

Yaw, pitch, and roll are represented as degrees per second. This field also supports the special "MAX" value, which means that the missile can turn at the maximum possible rate per missile simulation on that axis. This value is critical for enabling missiles to always hit their targets when they get close enough.

**Orientation Range** - Like Orientation, but each value is the upper bound on a rotational rate variance added to the base yaw, pitch, and roll values.

**Orientation Acceleration** - Enables the user to accelerate the various turn rates.

**Orientation Acceleration Range** - Like Orientation Range, but for turn acceleration.

**Powerslide Angle**

Enables missiles to powerslide -- just like cars in racing games -- but in 3D. If the missile is pointed farther than this angle from the target, it starts to powerslide. This causes the missile to skid along its original course, decelerating as it goes. As the missile moves ever more slowly, its acceleration value increases (like how a race car's wheels get more traction as it skids more slowly), enabling the missile to eventually escape the powerslide.

**Powerslide Deceleration**

The rate at which a powersliding missile leaves the powerslide. If this value is high, the missile escapes the powerslide quickly.



## The Ballistic Driver in Detail

The ballistic driver enables the user to create the typical catapult-like projectiles. They are configured by horizontal speed or Flight Time, but not both.

**Speed**

This is the generic field used by all drivers, but uniquely interpreted by the ballistic driver to mean constant horizontal velocity. This enables the user to treat the ballistic driver like a standard guided missile for purpose of balance. It also makes it impossible to create degenerate combinations of target distances, launch angles and launch speeds.

**Flight Time**

Controls the time it takes for the projectile to reach the target, regardless of distance. Enables the user to schedule ballistic projectile arrival and also makes it impossible to create degenerate ballistic missile configurations.

**Outro Altitude**

Like a standard outro, except by percentage, and correlated to altitude. Positive values refer to progress up the flight parabola, whereas negative values are progress down the parabola. For instance, a value of 0.9 means 90% towards the apex on the ascent, whereas a value of -0.9 means 90% towards the apex, but on the descent.



## The Parabola Driver in Detail

The parabola driver is best used for jumping types of behavior, like with the Reaper (the unit for which it was developed). It allows precise control over movement speed throughout the parabola without causing the parabolic arc to be deformed in any way.

**Parabola Upright**

When enabled, ensures that the missile is always parallel to the ground, which enables a unit like the Reaper to always appear upright throughout its flight path. If this flag is not set, the parabola controls the forward vector of the missile to give it the expected upward and downward pitch as the missile travels up and down its flight arc (like the nose of a football points first upward then downward as it travels).

**Parabola Clearance**

Specifies how much loft (i.e. additional height) the mover creates over the higher of either the launch or destination points. This is a variator, so can be a base plus a random range, in order to provide visual variance.

**Parabola Distance**

This is an array of numbers that specify the lengths of 4 parabola "hotspots".

- *Launch.* This is the first part of the parabola and usually represents some kind of take-off.
- *Before Apex.* A distance from the vertex on the leading edge of the parabola. It is used to start decelerating to give the path some loft.

- *After Apex.* A distance from the vertex on the trail edge of the parabola. It is used to reduce loft deceleration or even start accelerating out of the loft.

- *Land.* A distance before the final landing point. Usually represent some kind of touch down.


**Parabola Acceleration**

This is an array of numbers that specify the acceleration in different parts of the parabola. The different parts are:

- *Launch.* The first part of the parabola.
- *Ascent.* Between launch and apex.

- *Apex.* The "hump" of the parabola.

- *Descent.* Between launch and land.

- *Land.* The distance before the final landing point.

It is often best to have a Before Apex value that is longer than the After Apex value, if one wants to use deceleration to make the missile appear to "loft" realistically.



## The Throw Driver in Detail

Causes the missile to move along an arbitrary linear path. While seemingly of limited use, this is actually the most flexible and powerful driver from a visual punch perspective. When strung together with blends and varied across groups of simultaneously fired missiles, throw drivers can create stunningly unique visual patterns.

**Throw Rotation Type**

*None.* The default. The missile travels in the direction of the throw if it is the first phase, but will otherwise continue in its current direction, since throws can deflect the direction of a missile without affecting its rotation.

- *Launcher Forward.* Causes the missile to face in the direction of the firing unit or the firing unit's turret (if it has one) at the beginning of the phase. Only useful on the first phase.
- *Look At Target.* Causes the missile to face directly at its impact point, throughout its throw.

- *Look At Target 2D.* Like Look At Target, but the missile always stays parallel to the ground.

- *Throw Forward.* Causes the missile to face in the direction of the throw.

- *Vectored.* Enables the user to configure an arbitrary facing direction in local coordinates. Useful for causing missiles to throw from the firing unit in some exaggerated "dormant" pose before they activate (the fact that the missiles point elsewhere is what drives the visual message in this case). For instance, a throw can be used to drop a missile like a bomb, and the vectored value can be used to keep the missile pointing straight ahead while it drops to ignition level.

**Throw Vector**

The local coordinates of the throw. They do not need to be normalized.

**Throw Band Yaw**

Enables the user to configure throw variance along the yaw plane, as a deflection with respect to the core throw axis.

- *Positive Max.* Controls the outer yaw limit of the throw variance in the positive (clockwise) direction. Can actually be negative, for non-symmetric variances.
- *Negative Max.* Optional. Controls the outer yaw limit of the throw variance in the negative (counter-clockwise) direction. Can actually be positive, for non-symmetric variances.

- *Positive Min.* Optional, but must have a Negative Max and Negative Min configured if used. Can be used to open up a gap in the yaw band, so that missiles either come out far to the left or far to the right, but not in the middle.

- *Negative Min.* Optional, but must have a Negative Max and Positive Min configured if used. Like Positive Min, but in the negative direction.

In other words, the user can specify a throw arc with or without biases towards the right or left side, and he can prevent missiles from firing out in a gap within that arc, so that they do not appear to fly through the fuselage of the attacking craft. These numbers also make it easier to create: A) starfish-type burst patterns and B) exaggerated "whip-strike" attacks that cause the missile to flare out in a particular direction before striking the target.

**Throw Band Pitch**

Like Throw Band Yaw, but for pitch. When all four yaw and pitch min values are used, it means that missiles come out in a square ring, rather than a across the entire area of the square. As mentioned above, this is useful for creating certain kinds of flare-out missile patterns.

**Throw Forward**

A vector in local coordinate space that configures an arbitrary facing when using the Vectored rotation type.



## Overlays in Detail

Unlike phases, overlays apply to the entire flight path of the missile. The user can have up to two simultaneous overlays on a given missile, and each overlay contributes equally to the final missile position.

Overlays have a concept of scale which is how far they deflect motion from the core driver's flight path. Scale is zero at both endpoints of the flight path, but can be varied on a per-phase basis during the middle of the flight. The overlay system automatically uses cubic splines to blend smoothly between the scale values as the missile moves. The missile achieves the scale for a given phase at its midpoint.

The extra distance a missile travels because of its overlays does not affect phase outros; those are governed entirely by core driver motion (this extra distance would be very hard to predict with any accuracy, and actually significantly alters missile phase changes in ways that are too variable).

**Type**

The type of overlay, whether Wave, Orbit, or Revolver.

**Polarity**

Enables the user to govern which direction an overlay travels in. For Wave overlays, this controls the direction of the first "hump", whether positive or negative. For Orbit overlays, it controls whether the orbit travels clockwise (positive) or counter-clockwise (negative). It can be useful to control these when trying to coordinate the combined look of pairs of missiles. Polarity supports several values:

- *Positive.* The overlay travels in the positive direction.
- *Negative.* The overlay travels in the negative direction.

- Random. The overlay has a 50% chance of traveling in either the positive or negative direction.

- *Alternating.* The overlay travels in a direction determined by an ongoing rolling index. This index increments for each attack or operation performed by the attacking unit, and as such, can be used to regularly vary polarity in a striping-type pattern.

**Polarity Driver**

A key that specifies the rolling index or execution index to use to drive the Alternating type of polarity. The string "::RollingIndex" specifies that the overlay's polarity is alternated by rolling index whereas a relevant effect ID specifies that it is alternated by each subsequent execution of that effect within a given effect tree. ::RollingIndex alternates the polarity across attacks, whereas specifying an effect alternates the polarity within a given attack.

**Axis**

A vector in local coordinates that controls the axis around which the overlay motion is applied. For Wave overlays, this controls the direction of the sine wave. For Orbit and Revolver overlays, it controls the axis of revolution. In most cases, this will either be 0,-1,0 (forward) or 0,1,0 (backwards). However, it is possible to create unusual and skewed overlays by varying it. (For instance, creating a lateral revolution axis for an orbit creates a vertical cycloid flight pattern.)

**Wavelength**

Specifies the distance it takes to complete an entire 360 degree sine wave for Wave overlays, or the distance it takes to complete an entire revolution for Orbit overlays.

Base. This controls the minimum wavelength distance.

Range. The outer bound of a random value that gets added to the base distance. This causes sine waves and orbits to vary noticeably, which frequently results in a more real world look.

**Wavelength Change Probability**

A percentage chance that the wavelength will be recalculated on each half-wave (i.e. after each wave "hump") or half-orbit.



## Revolver Overlays in Detail

Revolvers are like Orbits that do not always move in the same direction. They are meant to simulate Robotech-style "drunken missiles� which have missiles moving in lazy, rolling orbits that vary slowly direction and speed.

- **Revolver Speed** - Specifies the rotational velocity of the revolution.
- **Revolver Speed Range** - The range for a random extra amount to add to the base Revolver Speed value.

- **Revolver Max Speed** - Specifies the maximum rotational velocity of the revolution.

- **Revolver Max Speed Range** - The range for a random extra amount to add to the base Revolver Max Speed value.

- **Revolver Acceleration** - Specifies the rotational acceleration of the revolution.

- **Revolver Acceleration Range** - The range for a random extra amount to add to the base Revolver Acceleration value.



## Supporting Systems

**The Previewer**

Necessary for easily and clearly observing the location of model attach points that missiles launch from and impact upon.

**Effects**

Several Effects are necessary for actually launching the missiles:

*Launch Missile Effect.* The effect that launches missiles and therefore mandatory for all missile creation. Useful fields include:

- Impact Range. The distance from the missile's target that will trigger impact. Enables proximity-based detonation.

- Retarget Filters. Determines what kind of targets a missile considers for attack should its target die before it arrives.

- Retarget Range. Units within this range are viable candidates for retargeting.

- Retarget flag. Located in the Flags field. Indicates that this missile can retarget.


The Launch Missile Effect also allows the user to configure a dynamic set of movers for the missile to use based on various conditions:

- Movers - Link. A list of movers that from which the missile can choose at launch time.

- Movers - Range Less Than or Equal. A list that corresponds to the list of movers. The distance between the launcher and the target must be less than or equal to this value in order for the corresponding mover to be a candidate for selection.

- Mover Rolling Pattern. Can be Stripe or Bounce. Stripe chooses movers in a pattern like 12341234, whereas bounce chooses them in a pattern like 1234321234.

- Mover Rolling Jump. Indicates how many mover array items to jump each time a new attack occurs.

- Mover Execute Pattern. Like Mover Rolling Pattern but for executions of the parent Launch Missile effect.

- Mover Execute Jump. Like Mover Rolling Jump, but for parent Launch Missile effect execution.

- Mover Execute Range. Controls the number of stripes or bounces in a single execution burst.


For instance a Rolling Jump of 4, an Execute Jump of 1, an Execute Range of 4, and a Mover Execute Pattern of bounce with a burst of 7 attacks would produce this pattern:

0.1.2.3.2.1.0 4.5.6.7.6.5.4 8.9.10.11.10.9.8

Also relevant is the Return Movers field which is used for tentacles. The return mover is chosen by how far the tentacle is from its source at the time it needs to return.

- *Create Persistent effect.* This is necessary for causing bursts of missiles to spread to specific points on a user-controlled schedule.

**Attach Methods** - These control how the game chooses which attach points to launch from and impact upon. Specify an attach method to use in the Action actor that controls the attack.

**Missile actors** - This component of the actor system enables data to correlate animations to the beginning and end of phases. It is also possible to trigger animations based on time elapsed from any of these points.



## TIPS AND TECHNIQUES

This section contains useful advice for achieving certain visuals or avoiding known pitfalls.

**Giving missiles short "charge up" animations**

For instance, the Yamato Cannon appears to draw energy together before firing. The best way to do something like this is to give a guided missile phase 0 speed and acceleration, but a timeout of the desired animation duration.

**Preventing perpetually looping missiles**

This happens when a missile does not have a sufficient turn rate to ever arrive at a static target. It can occur when a target moves at the last moment and then either dies or becomes stationary, such that it is just inside the missile's ability to turn towards it. The way around this is to give a missile a "terminator phase", which is a guidance phase with a MAX Orientation. This enables the missile to turn on a dime, which makes it impossible to escape.

**Forcing powersliding missiles to reach the target**

Without using these techniques, enterprising players can forever kite powersliding missiles by "juking" their units just before they are hit. The most direct technique for handling the problem is to give the powersliding motion phase a timeout. When doing this, it is important to remember to that the next phase needs a steep powerslide deceleration, but 0 powerslide angle. This enables the missile to move out of the slide quickly, but without being abrupt. Another technique for this is to give powerslide missiles a positive outro. This causes them to transition out of the powerslide after they have traveled a specific distance.

**Avoiding missiles that hang in space if the launching unit is killed**

If a unit is configured to use a Create Persistent effect to launch a burst or barrage of missiles, then that Create Persistent effect must be marked as channeled. This ensures that the unit does not accidentally try to create missiles while it is playing its death model, since this can cause the missiles to get empty configuration data.

**Eliminating backwards-looking loops with revolvers**

If a missile turns sharply enough and it attempts to revolve slowly through the inside of the turn, it can cause kinking. Revolvers always try to rotate around the flight path, so hairpin turns can actually cause the missile's position to appear to move backwards as the rapidly rotating driver causes the final overlay position of the missile to rotate around the focus point of the hairpin turn. The solution to this is to increase the rotational speed of the revolver so that it rapidly jumps past the point where it is on the inside of the turn. Alternatively, one can avoid hairpin turns or reduce the scale of the overlay to minimize how noticeable this side effect is. It is often possible to simply reduce the overlay scale only at the hairpin turn itself with very little overall visual impact.

**Preventing overlay missiles from skipping past the target**

This happens when an overlay missile is configured to use No Hook actor tracking (the default, no less), which causes the missile to lock onto a final course as it nears the target. The problem is that overlays can cause the missile to be pointing in the wrong direction when this happens, which causes the missile's visual representation to go careening off into the wild blue yonder. The solution is to simply set the missile to use actual actor tracking, since it exists to handle this case.
