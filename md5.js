const CryptoJS = require('crypto-js');
function ransg(t) {
    var e = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ];
    null == t && (t = 8);
    for (var n = "", a = 0; a < t; a++) {
        var o = Math.ceil(Math.random() * e.length - 1);
        n += e[o];
    }
    return n;
}


bitOperation = function(t, e) {
    for (var n = t.charAt(11).charCodeAt(), a = "", o = 0; o < e.length; o++) {
        var r = e[o].charCodeAt(), i = (r << 2 | 2) % n % 96;
        i = i < 32 ? 32 + i : i, a += String.fromCharCode(i);
    }
    return a;
}

function get_app_key(key){
    // tt = '5ef0e501e295489996b46f1ddf65a8b2' || ''
    tt = key || ''
    e = ransg()
    n = ransg()
    a = bitOperation(tt, e)
    o = bitOperation(tt, n)
    r = new Date().getTime()
    console.log(r)
    return "".concat(CryptoJS.MD5(a + tt + r + o), ",").concat(e, ",").concat(n, ",").concat(r).toString()

}


console.log(get_app_key());

// "6a05dea848276a13cd2202562203cf03,3PWGBWF1,Z3ZFE0OV,1743620821679"