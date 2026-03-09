window.BlueprintNode = {}

BlueprintNode.initializeBlueprintNode = function()
{
    function BlueprintNode() {
        LGraphNode.call(this);
        this.size = [220, 120];
        this.boxcolor = null;
    }

    BlueprintNode.prototype = Object.create(LGraphNode.prototype);
    BlueprintNode.prototype.constructor = BlueprintNode;
    BlueprintNode.title_color = "#FFFFFF";
    BlueprintNode.title_text_color = "#FFFFFF";


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
            y = 19 + execIndex * 10;   // exec near top
        } else {
            y = 35 + dataIndex * 11;   // data lower
        }

        return [x, y];
    };

    BlueprintNode.prototype.onResize = function() {
        const slots = Math.max(this.inputs?.length || 0, this.outputs?.length || 0);
        this.size[1] = 20 + slots * 22;
    };

    return BlueprintNode;
}
