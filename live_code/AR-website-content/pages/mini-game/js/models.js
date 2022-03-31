var characters = [],
    tools = [];

function ARModel(name, dialogue) {
    this.name = name;
    this.dialogue = dialogue;
}

ARModel.prototype.speak = function() {
    return this.dialogue;
}


//Character model
function Character(name, dialogue, tool, successDialogue) {
    ARModel.call(this, name, dialogue);
    this.tool = tool;
    this.successDialogue = successDialogue;
}
Character.prototype = Object.create(ARModel.prototype);


//Tool model
function Tool(name, dialogue) {
    ARModel.call(this, name, dialogue);
}
Tool.prototype = Object.create(ARModel.prototype);

// we would repeat an intialization step for each character we have
// so the parts between { }, in the charactersArray = []
// for example if I had a second character, `chocobo` I would add like so:
function initiateModels() {
    var charactersArray = [
      {
        name: 'bowser',
        dialogue: 'Hi there, I\'m Bowser! I\'ve lost my skull. Let me know if you see it!',
        tool: new Tool('skull', 'You have found Bowser\'s skull!'),
        successDialogue: 'Thanks for my skull!'
      },
      {
        name: 'chocobo',
        dialogue: 'sqauak squaaak SQUAKKKKK',
        tool: new Tool('seeds', 'You have found Chocobo\'s bird seed!'),
        successDialogue: 'Squeek! Yum!'
      },
      {
        name: 'demo',
        dialogue: 'Building Interactive Systems!',
      }
    ];

    charactersArray.forEach(function(character){
        characters.push(new Character(character.name, character.dialogue, character.tool, character.successDialogue));
        if (character.tool) tools.push(character.tool);
    });

    console.log('characters', characters);
    console.log('tools', tools)
}

initiateModels();
