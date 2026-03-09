# Pickup Item Bug Fix

## Context
You are working on a **collectible item** Blueprint in Unreal Engine 5.
When the player walks over the item, two things should happen:
- A **pickup sound** plays at the item's location
- The **item is destroyed**

## The Bug
The current blueprint triggers the sound and destruction for **any** actor that overlaps
the collision sphere — including AI characters and physics objects. It should only
respond to the **player character**. The sound also **doesn't** play.

## Your Task
You have been given the following nodes:
- `On Component Begin Overlap`
- `Play Sound at Location`
- `Destroy Actor`

Add the **missing node** and fix the connections so that the pickup logic only
executes when the **player** is the overlapping actor.