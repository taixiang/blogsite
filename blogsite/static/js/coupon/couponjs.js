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
        $("#coupon_content").parent().find(".coupon_get").text("复制优惠券");
        $(".coupon_url").attr("data-am-modal","{target: '#doc-modal-1', closeViaDimmer: 0, width: 300, height: 100}");
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
            $("#coupon_content").parent().find(".coupon_get").text("复制优惠券");
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
                            msg = model + "复制成功，打开「手机淘宝」即可领取！"
                            $("#am-modal-bd").text(msg)
                            $(".coupon_url").attr("data-am-modal", "{target: '#doc-modal-1', closeViaDimmer: 0, width: 300, height: 100}");
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

    //价格切换
    exports.tab = function (type, keyword) {
        $("#price_tab").click(function () {
            if (type == "down") {
                type = "up"
            } else if (type != null) {
                type = "down";
            }
            var url = "/youhui/price/" + type + "/";
            window.location.href = url + '?search=' + keyword
        })
    }

    //帮助
    exports.help = function (type, keyword) {
        if(exports.isMobile()){
            $("#phone_help").show();
            $("#pc_help").hide()
        }else {
            $("#pc_help").show();
            $("#phone_help").hide()
        }
    }

    //双12
    exports.packet = function(){
        var clipboard1 = new ClipboardJS('.red_packet', {
            text: function (trigger) {
                var msg = "￥gE2Mbm1H95E￥复制成功，打开「手机淘宝」领取双12红包，跨店满减不封顶！"
                $("#am-modal-bd").text(msg)
                $(".red_packet").attr("data-am-modal", "{target: '#doc-modal-1', closeViaDimmer: 0, width: 300, height: 100}");
                return msg;
            }
        });
        clipboard1.on('success', function (e) {
        });
        clipboard1.on('error', function (e) {
        });
    }

    //双端显示红包
    exports.showPocket = function () {
        if(exports.isMobile()){
            $("#red_packet").show();
            $("#pc_pocket").hide()
        }else {
            $("#pc_pocket").show();
            $("#red_packet").hide()
        }
    }

    return exports
})()


