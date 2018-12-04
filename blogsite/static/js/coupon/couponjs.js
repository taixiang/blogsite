var Util = (function(){
     var exports = {}
     exports.isWeixin = function () { //判断是否是微信
        var ua = navigator.userAgent.toLowerCase();
        return ua.match(/MicroMessenger/i) == "micromessenger";
    };

    exports.isMobile = function () {
        return /Android|webOS|iPhone|BlackBerry/i.test(navigator.userAgent);
    }

    return exports
})()


