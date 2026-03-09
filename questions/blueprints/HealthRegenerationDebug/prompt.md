# Health Regeneration Bug Fix

## Context
You are implementing a **passive health regeneration** system in Unreal Engine 5.
Every frame, the player's health should tick upward by a small amount — but
only while their health is **below the maximum value**.

## The Bug
The current blueprint increments health on **every tick with no condition check**.
This means health grows **past the maximum** indefinitely and never stops.

## Your Task
You have been given the following nodes:
- `Event Tick`
- `Float + Float` *(adds the regen amount to current health)*
- `Set Health`

Add the **two missing nodes** and wire everything correctly so that
`Set Health` is only called when **current health < max health**.