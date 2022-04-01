exports.esrever = function (list) {
  let ret = [];
  let right = list.length - 1;
  while (right >= 0) {
    ret.push (list[right]);
    right--;
  }
  return ret;
};
