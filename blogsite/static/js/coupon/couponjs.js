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
        if(exports.isMobile()){
        $("#coupon_content").parent().find(".coupon_get").text("复制链接");
        $(".coupon_url").attr("data-am-modal","{target: '#doc-modal-1', closeViaDimmer: 0, width: 300, height: 225}");
        var clipboard = new ClipboardJS('.coupon_get_div', {
                                            text: function(trigger) {
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

    exports.judge = function() {
        if (ClipboardJS.isSupported() && Util.isMobile()) {
            $("#coupon_content").parent().find(".coupon_get").text("复制链接");
            var clipboard = new ClipboardJS('.coupon_get_div', {
                text: function (trigger) {
                    var url = trigger.getAttribute('value');
                    var text = trigger.getAttribute('txt');
                    var logo = trigger.getAttribute('logo');
                    var model;
                    var msg;
                    $.ajax({
                        type: "GET",
                        url: '/youhui/create_key?text='+text + '&url=' + url + '&logo=' + logo,
                        dataType: 'json',
                        async: false,
                        success: function (response, status) {
                            model = response.tbk_tpwd_create_response.data.model;
                            console.log(response.tbk_tpwd_create_response.data.model)
                            msg = model + "复制成功，打开「手机淘宝」即可领取！"
                            $("#am-modal-bd").text(msg)
                            $(".coupon_url").attr("data-am-modal", "{target: '#doc-modal-1', closeViaDimmer: 0, width: 300, height: 125}");
                        }
                    })

                    return msg;
                }
            });
            clipboard.on('success', function (e) {
            });
            clipboard.on('error', function (e) {
            });
        } else {
            $(".coupon_get_div").attr("onclick", "cc(this)");
        }
    }

    return exports
})()


