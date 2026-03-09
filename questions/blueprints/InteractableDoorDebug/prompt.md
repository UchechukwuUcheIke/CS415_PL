# Interactable Door Bug Fix

## Context
You are working on a **door actor** Blueprint in Unreal Engine 5.
The door should **toggle between open and closed** each time the player
presses the **Interact** button (`IA_Interact`).
A `Flip Flop` node is used to alternate between two `Set Actor Rotation` calls —
one for the open angle and one for the closed angle.

## The Bug
The door is currently connected to **Event Tick**, which means it tries to
toggle its rotation **every frame**, causing it to flicker uncontrollably
instead of responding to player input.

## Your Task
You have been given the following nodes:
- `Event Tick` ← **this is the buggy node**
- `Flip Flop`
- `Set Actor Rotation (Open)`
- `Set Actor Rotation (Closed)`

**Replace** the offending node with the correct input event so the door only
toggles when the player presses the Interact key.