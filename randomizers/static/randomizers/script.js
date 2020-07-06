var randomize = document.querySelector('#randomize');
var sheet = document.querySelector('.sheet');

randomize.addEventListener('click',function(){
  sheet.textContent = Math.random(0, 10);
})
