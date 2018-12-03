$(function(){
    var isWeixin = function () { //判断是否是微信
        var ua = navigator.userAgent.toLowerCase();
        return ua.match(/MicroMessenger/i) == "micromessenger";
    };
    console.log(isWeixin())

    var isMobile = function () {
        return /Android|webOS|iPhone|BlackBerry/i.test(navigator.userAgent);
    }
    console.log(isMobile())

    if(isWeixin()){
        $("#cake_content").parent().find(".coupon_get").text("复制链接");
    }else{
    }

    $("#moreCoupon").click(function(){
        $(".am-icon-spinner").addClass("am-icon-spin");
    })




})



