function ClearRegisteredNodes()
{
    LiteGraph.registered_node_types = {};
    LiteGraph.node_types_by_file_extension = {};
    LiteGraph.Nodes = {};
}

ClearRegisteredNodes();

function BlueprintNode() {
    LGraphNode.call(this);
    this.size = [220, 120];
    this.boxcolor = null;
}

BlueprintNode.prototype = Object.create(LGraphNode.prototype);
BlueprintNode.prototype.constructor = BlueprintNode;

// Header + body drawing
BlueprintNode.prototype.onDrawBackground = function(ctx) {

    const w = this.size[0];
    const h = this.size[1];

    const margin = 10;
    const slot_height = 20;
    const title_height = 30;

    // Body
    ctx.fillStyle = "#2c2f33";
    ctx.beginPath();
    ctx.roundRect(0, 0, w, h, 8);
    ctx.fill();
};

// Blueprint-style pin layout
BlueprintNode.prototype.getSlotPosition = function(slot, isInput) {

    const x = isInput ? 0 : this.size[0];
    const slots = isInput ? this.inputs : this.outputs;
    const slotInfo = slots[slot];

    let execIndex = 0;
    let dataIndex = 0;

    for (let i = 0; i < slot; i++) {
        if (slots[i].type === LiteGraph.EVENT)
            execIndex++;
        else
            dataIndex++;
    }

    let y;

    if (slotInfo.type === LiteGraph.EVENT) {
        y = 38 + execIndex * 20;   // exec near top
    } else {
        y = 70 + dataIndex * 22;   // data lower
    }

    return [x, y];
};

BlueprintNode.prototype.onResize = function() {
    const total = (this.inputs?.length || 0) +
                    (this.outputs?.length || 0);
    this.size[1] = 100 + total * 22;
};