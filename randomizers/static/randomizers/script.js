const randomize = document.querySelector('#randomize');
const cols = document.querySelectorAll('.col-body');
var flag = true;

function populate() {
  cols.forEach(function(col) {
    num1 = Math.floor(Math.random() * Math.floor(11));
    num2 = Math.floor(Math.random() * Math.floor(11));
    if (flag) {
      col.innerHTML = num1 + " + " + num2 + " = _";
    } else {
      col.innerHTML = Math.max(num1, num2) + " - " + Math.min(num1, num2) + " = _";
    }
    flag = !flag;
  });
};

window.addEventListener('load', populate);
randomize.addEventListener('click', populate);
