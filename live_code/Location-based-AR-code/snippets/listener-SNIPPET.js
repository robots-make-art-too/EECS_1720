document.querySelector('button[data-action="change"]').addEventListener('click', function () {
  const entity = document.querySelector('[gps-entity-place]');
  modelIndex++;
  const newIndex = modelIndex % models.length;
  setModel(models[newIndex], entity);
});