function GamerState() {
    this.tools = [];
}

GamerState.prototype.addTool = function(tool) {
    this.tools.push(tool);
}

GamerState.prototype.hasCharacterTool = function(character) {
    return character.tool && this.tools.includes(character.tool.name);
}

var gamerState = new GamerState();
