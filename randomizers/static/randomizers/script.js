const randomize = document.querySelector('#randomize');
const colsLeft = document.querySelectorAll('.col-left');
const colsRight = document.querySelectorAll('.col-right');


function populate() {
  numsLeft = [];
  numsRight = [];
  colsLeft.forEach(function(col, index) {
    while (true) {
      num1 = Math.floor(Math.random() * Math.floor(11));
      num2 = Math.floor(Math.random() * Math.floor(11));
      nums = "" + num1 + num2;
      if (!numsLeft.includes(nums)) {
        numsLeft.push(nums);
        col.innerHTML = num1 + " + " + num2 + " = _";
        break;
      }
    }
  });
  colsRight.forEach(function(col, index) {
    while (true) {
      num1 = Math.floor(Math.random() * Math.floor(11));
      num2 = Math.floor(Math.random() * Math.floor(11));
      nums = "" + Math.max(num1, num2) + Math.min(num1, num2);
      if (!numsRight.includes(nums)) {
        numsRight.push(nums);
        col.innerHTML = Math.max(num1, num2) + " - " + Math.min(num1, num2) + " = _";
        break;
      }
    }
  });
}


window.addEventListener('load', populate);
randomize.addEventListener('click', populate);
