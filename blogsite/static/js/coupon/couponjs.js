var Util = (function(){
     var exports = {}
     exports.isWeixin = function () { //判断是否是微信
        var ua = navigator.userAgent.toLowerCase();
        return ua.match(/MicroMessenger/i) == "micromessenger";
    };

    exports.isMobile = function () {
        return /Android|webOS|iPhone|BlackBerry/i.test(navigator.userAgent);
    }

    exports.diff = function(){
        if(exports.isWeixin()){
        $("#coupon_content").parent().find(".coupon_get").text("复制链接");
        $(".coupon_url").attr("data-am-modal","{target: '#doc-modal-1', closeViaDimmer: 0, width: 300, height: 225}");
        var clipboard = new ClipboardJS('.coupon_get_div', {
                                            text: function(trigger) {
                                            console.log(trigger)
                                            console.log(trigger.getAttribute('value'))
                                                return trigger.getAttribute('value');
                                            }
                                        });

            clipboard.on('success', function(e) {
                });

            clipboard.on('error', function(e) {
                });
        }else{
            $(".coupon_get_div").attr("onclick","cc(this)");
        }
    }

    return exports
})()


