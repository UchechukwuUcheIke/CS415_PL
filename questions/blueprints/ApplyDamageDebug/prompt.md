# Apply Damage Blueprint

## Context
You are designing a **trigger volume** that damages the player when they walk into it.
The blueprint detects when an actor enters the volume and applies damage to them.

## The Bug
The current blueprint applies damage to **any** actor that enters the trigger volume —
including AI characters and physics objects. It should only damage the **player character**.

## Your Task
You have been given the following nodes:
- `On Component Begin Overlap`
- `Apply Damage`

Add the **missing node** and fix the connections so that damage is only applied when
the overlapping actor is the **player**.