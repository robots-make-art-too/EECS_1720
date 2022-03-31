AFRAME.registerComponent('accepts-clicks', {
  init: function() {
    this.el.addEventListener('touchend', handleClickEvent);
    this.el.addEventListener('click', handleClickEvent);
  },
  tick: function() {
    hideConvoBubbleIfNoMarker();
  }
});

function hideConvoBubbleIfNoMarker() {
  var convoBubble = document.querySelector(".convo-bubble");
  if (convoBubble.style.display === 'none' || !convoBubble.style.display) return;

  var shouldHide = true;
  characters.forEach(function(character){
    var characterMarker = document.querySelector("#" + character.name + "-marker");
    if (characterMarker && characterMarker.object3D.visible) shouldHide = false;
  });

  tools.forEach(function(tool){
    var toolMarker = document.querySelector("#" + tool.name + "-marker");
    if (toolMarker && toolMarker.object3D.visible) shouldHide = false;
  });

  if (shouldHide) convoBubble.style.display = 'none';
};

function handleClickEvent() {
  characters.forEach(function(character) {
    var characterMarker = document.querySelector("#" + character.name + "-marker");
    if (characterMarker && characterMarker.object3D.visible) {
      if (searchForCharacterTool(character)){
        toggleConvoBubble(character.successDialogue);
      } else {
        toggleConvoBubble(character.dialogue);
      }
    }
  });

  tools.forEach(function(tool){
    var toolMarker = document.querySelector("#" + tool.name + "-marker");
    if (toolMarker && toolMarker.object3D.visible) {
      toggleConvoBubble(tool.dialogue);
      if (!gamerState.hasCharacterTool(tool)) gamerState.addTool(tool);
    }
  });
}

function toggleConvoBubble(dialogue) {
  var convoBubble = document.querySelector(".convo-bubble");
  if (convoBubble.style.display === 'none' || !convoBubble.style.display) {
    convoBubble.innerHTML = dialogue;
    convoBubble.style.display = 'block';
  } else {
    convoBubble.style.display = 'none';
  }
};

function searchForCharacterTool(character) {
  return gamerState.tools.some(function(tool) {
    return tool.name === character.tool.name;
  });
};
