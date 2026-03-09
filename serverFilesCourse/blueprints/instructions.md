
# Blueprint Editor — Student Guide

## Overview

The Blueprint Editor works just like the **node graph editor in Unreal Engine 5**. You build logic visually by placing nodes on a canvas and connecting them together with wires. No typing code required — just drag, drop, and connect.

---

## Creating Nodes

Double left click on any **empty area** of the canvas to open the node search menu.

1. Double-click on the canvas
2. A search box appears where you clicked
3. Type the name of the node you want (e.g. "Begin Play")
4. Click the node name from the dropdown list
5. The node is placed on the canvas at that position

> **Tip:** The search filters as you type, so you don't need to type the full name.

---

## Moving Nodes

Click and drag any node to move it around the canvas. Nodes can be freely repositioned at any time — your connections (wires) will follow along automatically.

---

## Connecting Nodes

This works exactly like UE5 Blueprints:

1. **Hover** over an output pin (right side of a node) — your cursor will change
2. **Click and drag** from the output pin
3. **Drop** the wire onto a compatible input pin (left side of another node)
4. A wire will appear connecting the two pins

> **Note:** Pins will only connect if their types are compatible. Incompatible pin types cannot be wired together.

### Disconnecting a wire

Left-click on a pin and drag it away to remove a connection.

---

## Deleting Nodes

There are two ways to delete a node:

- **Select** the node by clicking on it, then press the **Delete** or **Backspace** key on your keyboard

---

## Node Widgets (Input Fields)

Some nodes have **input fields** directly on them, similar to UE5's default pin values. If a pin is not connected to another node, you can type a value directly into the field on the node itself.

- Click the field to edit it
- Once you connect a wire to that pin, the field will hide automatically
- Disconnect the wire to bring the field back

---

## Submitting Your Work

When you are finished building your map, use the **Submit** button on the page. Your graph will be saved and submitted automatically — you do not need to do anything special to export it.

---

## Resetting The Graph

If you make a mistake when editing the graph, pressing the grey "Reset Graph" button will recreate the original graph.

---

## Quick Reference

| Action | How To |
|---|---|
| Create a node | Double-left click empty canvas → search → click |
| Move a node | Click + drag the node |
| Connect pins | Drag from output pin → drop on input pin |
| Disconnect pins | Drag from output pin |
| Delete a node | Select it → Delete key |
| Edit a pin value | Click the input field on the node |