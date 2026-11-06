// Signs2Go Portal steps: checkboxes save on this device, counter + bar update.
// Same simple pattern as SDUSA Portal, keyed per page.
(function () {
  var allBoxes = document.querySelectorAll('.stepcheck');
  if (!allBoxes.length) return;
  var key = 's2g-steps:' + location.pathname;
  var saved = {};
  try { saved = JSON.parse(localStorage.getItem(key) || '{}'); } catch (e) {}
  var groups = [];
  document.querySelectorAll('.steps').forEach(function (stepsEl) {
    var boxes = Array.prototype.slice.call(stepsEl.querySelectorAll('.stepcheck'));
    if (!boxes.length) return;
    var wrap = null, n = stepsEl.previousElementSibling;
    while (n) { if (n.classList && n.classList.contains('progresswrap')) { wrap = n; break; } n = n.previousElementSibling; }
    var doneEl = null; n = stepsEl.nextElementSibling;
    while (n) { if (n.classList && n.classList.contains('alldone')) { doneEl = n; break; } n = n.nextElementSibling; }
    groups.push({ boxes: boxes, wrap: wrap, doneEl: doneEl });
  });
  function update() {
    allBoxes.forEach(function (b, i) { saved[i] = b.checked; });
    try { localStorage.setItem(key, JSON.stringify(saved)); } catch (e) {}
    groups.forEach(function (g) {
      var done = 0;
      g.boxes.forEach(function (b) {
        var card = b.closest('.step');
        if (b.checked) { done++; if (card) card.classList.add('done'); }
        else if (card) card.classList.remove('done');
      });
      if (g.wrap) {
        var t = g.wrap.querySelector('.progresstext');
        if (t) t.textContent = done + ' of ' + g.boxes.length + ' steps done';
        var bar = g.wrap.querySelector('.progress .bar');
        if (bar) bar.style.width = (g.boxes.length ? Math.round(done / g.boxes.length * 100) : 0) + '%';
      }
      if (g.doneEl) g.doneEl.hidden = done !== g.boxes.length;
    });
  }
  allBoxes.forEach(function (b, i) { b.checked = !!saved[i]; b.addEventListener('change', update); });
  update();
})();
