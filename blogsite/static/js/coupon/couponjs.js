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

    // 首页判断
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
            $("#red_packet").hide();
            $("#pc_pocket").hide()
        }else {
            $("#pc_pocket").hide();
            $("#red_packet").hide()
        }
    }

    //选择
    exports.choose = function (keyword) {
        $("#select").click(function () {
            if (!$(this).hasClass("banner_hover")) {
                $("#select").addClass("banner_hover");
                $("#goods").removeClass("banner_hover");
                $("#like").removeClass("banner_hover");
                $("#div_select").show();
                $("#div_goods").hide();
                $("#div_like").hide();
                $("#moreCoupon").show();
                $("#moreGoods").hide();
                $("#moreLike").hide();
            }
        })

        $("#goods").click(function () {
            if (!$(this).hasClass("banner_hover")) {
                $("#select").removeClass("banner_hover");
                $("#goods").addClass("banner_hover");
                $("#like").removeClass("banner_hover");
                $("#div_select").hide();
                $("#div_goods").show();
                $("#div_like").hide();
                $("#moreCoupon").hide();
                $("#moreGoods").show();
                $("#moreLike").hide();

                if($("#good_list").find("li").length <= 0){
                    exports.good_list(keyword);
                }
            }
        })

        $("#like").click(function () {
            if (!$(this).hasClass("banner_hover")) {
                $("#select").removeClass("banner_hover");
                $("#goods").removeClass("banner_hover");
                $("#like").addClass("banner_hover");
                $("#div_select").hide();
                $("#div_goods").hide();
                $("#div_like").show();
                $("#moreCoupon").hide();
                $("#moreGoods").hide();
                $("#moreLike").show();

                if($("#like_list").find("li").length <= 0){
                    exports.like(keyword);
                }
            }
        })

    }

    //更多请求 精选优质
    exports.moreSelect = function(type, keyword){
        var page = 2;
        var isloading = false;

        $("#moreCoupon").click(function() {

            $(".am-icon-spinner").addClass("am-icon-spin");
            if (isloading) {
                return
            }
            isloading = true;
            $.ajax({
                type: "GET",
                url: '/youhui/more?page=' + page + '&type=' + type + '&search=' + keyword,
                dataType: 'json',
                complete: function () {
                    isloading = false;
                    $(".am-icon-spinner").removeClass("am-icon-spin");
                },
                success: function (response, status) {
                    isloading = false;
                    var data = JSON.parse(response);
                    $(".am-icon-spinner").removeClass("am-icon-spin");
                    if (!data.next) {
                        $("#moreCoupon").css("display", "none");
                    }
                    page = data.page + 1;
                    $.each(data.data, function (i, item) {
                        var baseurl = "/youhui/detail/" + item.fields.uuid;

                        $("#coupon_content").append("<li>"
                            + "<div class='am-gallery-item am_list_block'> "
                            + " <a> "
                            + "<a class='am_img_bg' href= " + baseurl + " target='_blank' > "
                            + "<img class='am_img animated' src='/static/img/loading.gif'"
                            + "data-original='" + item.fields.img + " ' "
                            + " alt='优惠券'/> "
                            + "</a>"
                            + "<span class='coupon_name'>" + item.fields.name + "</span>"
                            + "<div>"
                            + "<img class='img_juan' src='/static/img/coupon/juan.png'>"
                            + "<span class='coupon_rule'>" + item.fields.rule + "</span>"
                            + "</div>"
                            + "<div class='am_listimg_info'>"
                            + "<span class='ori_price'>原价："
                            + "<span class='ori_font'>￥</span>"
                            + "<span class='coupon_price'>" + item.fields.price + "</span>"
                            + "</span>"
                            + "</div>"
                            + "<div>"
                            + "<div class='coupon_shop'>" + item.fields.shop + "</div>"
                            + "</div>"
                            + "<div id='" + item.fields.id + "' class='coupon_get_div' data-clipboard-action='copy' value='" + item.fields.phone_url + "'" + "txt='" + item.fields.name + "'" + "logo='" + item.fields.img + "'"
                            + "data-clipboard-target='div'>"
                            + "<a class='coupon_url'>"
                            + "<span id='coupon_get' class='coupon_get'>立即领取</span>"
                            + "</a>"
                            + "</div>"
                            + "</a>"
                            + "</div>"
                            + "</li>"
                        )

                    });

                    if (ClipboardJS.isSupported() && Util.isMobile()) {
                        $("#coupon_content").parent().find(".coupon_get").text("复制优惠券");
                    } else {
                        $(".coupon_get_div").attr("onclick", "cc(this)");
                    }

                    $('.am_img_bg').removeClass('am_img_bg');
                    $(this).find('.am_img').addClass('bounceIn');

                    $(".am_list_block").on('mouseover', function () {
                        $('.am_img_bg').removeClass('am_img_bg');
                        $(this).find('.am_img').addClass('bounceIn');
                    });
                    $("img.am_img").lazyload();
                    $("a.am_img_bg").lazyload({
                        effect: 'fadeIn'
                    });

                }
            })
        })
    }

    //好劵清单
    exports.good_list = function (keyword) {

        var page = 1;
        var isloading = false;

        function more_good() {
            $(".am-icon-spinner").addClass("am-icon-spin");
            if (isloading) {
                return
            }
            isloading = true;
            $.ajax({
                type: "GET",
                url: '/youhui/good_list?page=' + page + '&search=' + keyword,
                dataType: 'json',
                complete: function () {
                    isloading = false;
                    $(".am-icon-spinner").removeClass("am-icon-spin");
                },
                success: function (response, status) {
                    isloading = false;
                    $(".am-icon-spinner").removeClass("am-icon-spin");
                    page = page + 1;
                    if (page*12 > 10000) {
                        $("#moreGoods").css("display", "none");
                    }
                    $.each(response.tbk_dg_item_coupon_get_response.results.tbk_coupon, function (i, item) {
                        var baseurl = "###" ;

                        $("#good_list").append("<li>"
                            + "<div class='am-gallery-item am_list_block'> "
                            + " <a> "
                            + "<a class='am_img_bg' href= " + baseurl + " onclick='to_detail("+JSON.stringify(item)+")' > "
                            + "<img class='am_img animated' src='/static/img/loading.gif'"
                            + "data-original='" + item.pict_url + " ' "
                            + " alt='优惠券'/> "
                            + "</a>"
                            + "<span class='coupon_name'>" + item.title + "</span>"
                            + "<div>"
                            + "<img class='img_juan' src='/static/img/coupon/juan.png'>"
                            + "<span class='coupon_rule'>" + item.coupon_info + "</span>"
                            + "</div>"
                            + "<div class='am_listimg_info'>"
                            + "<span class='ori_price'>原价："
                            + "<span class='ori_font'>￥</span>"
                            + "<span class='coupon_price'>" + item.zk_final_price + "</span>"
                            + "</span>"
                            + "</div>"
                            + "<div>"
                            + "<div class='coupon_shop'>" + item.shop_title + "</div>"
                            + "</div>"
                            + "<div class='coupon_get_div' data-clipboard-action='copy' value='" + item.coupon_click_url + "'" + "txt='" + item.title + "'" + "logo='" + item.pict_url + "'"
                            + "data-clipboard-target='div'>"
                            + "<a class='coupon_url'>"
                            + "<span id='coupon_get' class='coupon_get'>立即领取</span>"
                            + "</a>"
                            + "</div>"
                            + "</a>"
                            + "</div>"
                            + "</li>"
                        )

                    });

                    if (ClipboardJS.isSupported() && Util.isMobile()) {
                        $("#good_list").parent().find(".coupon_get").text("复制优惠券");
                    } else {
                        $(".coupon_get_div").attr("onclick", "cc(this)");
                    }

                    $('.am_img_bg').removeClass('am_img_bg');
                    $(this).find('.am_img').addClass('bounceIn');

                    $(".am_list_block").on('mouseover', function () {
                        $('.am_img_bg').removeClass('am_img_bg');
                        $(this).find('.am_img').addClass('bounceIn');
                    });
                    $("img.am_img").lazyload();
                    $("a.am_img_bg").lazyload({
                        effect: 'fadeIn'
                    });

                }
            })
        }

        more_good();

        $("#moreGoods").click(function () {
            more_good();
        });


    }

    //好劵详情
    exports.goods_detail = function () {
        var json = sessionStorage.getItem("allJson");
        console.log(json);
        var data = JSON.parse(json);
        console.log(data);
        $("#coupon_rule").text(data.coupon_info);
        $("#tbk_title").text(data.title);
        $("#tbk_shop").text(data.shop_title);
        $("#tbk_price").text("原价：￥"+data.zk_final_price);
        $("#tbk_url").attr("href",data.item_url);
        $("#tbk_img").attr("src",data.pict_url);

        if (ClipboardJS.isSupported() && Util.isMobile()) {
            $("#coupon_get").text("复制优惠券");
            var clipboard = new ClipboardJS('.coupon_get_div', {
                text: function (trigger) {
                    var url = data.coupon_click_url;
                    var text = data.title;
                    var logo = data.pict_url;
                    var model;
                    var msg;
                    $.ajax({
                        type: "GET",
                        url: '/youhui/create_key?text='+text + '&url=' + url + '&logo=' + logo,
                        dataType: 'json',
                        async: false,
                        success: function (response, status) {
                            model = response.tbk_tpwd_create_response.data.model;
                            msg = model + "复制成功，打开「手机淘宝」即可领取！";
                            $("#am-modal-bd").text(msg);
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
            $(".coupon_url").attr("href",data.coupon_click_url);
            $(".coupon_url").attr("target","_blank");
        }
    };

    //猜你喜欢
    exports.like = function (keyword) {
        var page = 1;
        var isloading = false;
        var u = navigator.userAgent;
        var net =navigator.connection.effectiveType;
        var isAndroid = u.indexOf('Android') > -1 || u.indexOf('Adr') > -1;
        var isiOS = !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/);
        var os = isAndroid ? "android" : isiOS ? "ios" :"other";

        function more_like() {
            $(".am-icon-spinner").addClass("am-icon-spin");
            if (isloading) {
                return
            }
            isloading = true;
            $.ajax({
                type: "GET",
                url: '/youhui/like?page=' + page + '&search=' + keyword + '&ua='+ u + '&net='+net+'&os='+os,
                dataType: 'json',
                complete: function () {
                    isloading = false;
                    $(".am-icon-spinner").removeClass("am-icon-spin");
                },
                success: function (response, status) {
                    isloading = false;
                    $(".am-icon-spinner").removeClass("am-icon-spin");
                    page = page + 1;
                    if (page*12 > 10000) {
                        $("#moreLike").css("display", "none");
                    }
                    $.each(response.tbk_dg_item_coupon_get_response.results.tbk_coupon, function (i, item) {
                        var baseurl = "###" ;

                        $("#like_list").append("<li>"
                            + "<div class='am-gallery-item am_list_block'> "
                            + " <a> "
                            + "<a class='am_img_bg' href= " + baseurl + " onclick='to_detail("+JSON.stringify(item)+")' > "
                            + "<img class='am_img animated' src='/static/img/loading.gif'"
                            + "data-original='" + item.pict_url + " ' "
                            + " alt='优惠券'/> "
                            + "</a>"
                            + "<span class='coupon_name'>" + item.title + "</span>"
                            + "<div>"
                            + "<img class='img_juan' src='/static/img/coupon/juan.png'>"
                            + "<span class='coupon_rule'>" + item.coupon_info + "</span>"
                            + "</div>"
                            + "<div class='am_listimg_info'>"
                            + "<span class='ori_price'>原价："
                            + "<span class='ori_font'>￥</span>"
                            + "<span class='coupon_price'>" + item.zk_final_price + "</span>"
                            + "</span>"
                            + "</div>"
                            + "<div>"
                            + "<div class='coupon_shop'>" + item.shop_title + "</div>"
                            + "</div>"
                            + "<div class='coupon_get_div' data-clipboard-action='copy' value='" + item.coupon_click_url + "'" + "txt='" + item.title + "'" + "logo='" + item.pict_url + "'"
                            + "data-clipboard-target='div'>"
                            + "<a class='coupon_url'>"
                            + "<span id='coupon_get' class='coupon_get'>立即领取</span>"
                            + "</a>"
                            + "</div>"
                            + "</a>"
                            + "</div>"
                            + "</li>"
                        )

                    });

                    if (ClipboardJS.isSupported() && Util.isMobile()) {
                        $("#like_list").parent().find(".coupon_get").text("复制优惠券");
                    } else {
                        $(".coupon_get_div").attr("onclick", "cc(this)");
                    }

                    $('.am_img_bg').removeClass('am_img_bg');
                    $(this).find('.am_img').addClass('bounceIn');

                    $(".am_list_block").on('mouseover', function () {
                        $('.am_img_bg').removeClass('am_img_bg');
                        $(this).find('.am_img').addClass('bounceIn');
                    });
                    $("img.am_img").lazyload();
                    $("a.am_img_bg").lazyload({
                        effect: 'fadeIn'
                    });

                }
            })
        }

        more_like();

        $("#moreLike").click(function () {
            more_like();
        });

    }

    // 选品库
    exports.favorites_list = function (id) {

        var page = 1;
        var isloading = false;

        function more_fav() {
            $(".am-icon-spinner").addClass("am-icon-spin");
            if (isloading) {
                return
            }
            isloading = true;
            $.ajax({
                type: "GET",
                url: '/youhui/favorites_list/' + id + ' ?page=' + page,
                dataType: 'json',
                complete: function () {
                    isloading = false;
                    $(".am-icon-spinner").removeClass("am-icon-spin");
                },
                success: function (response, status) {
                    isloading = false;
                    $(".am-icon-spinner").removeClass("am-icon-spin");
                    page = page + 1;
                    if (response.error_response != null) {
                        $("#moreFav").css("display", "none");
                        console.log("=============================")
                        return
                    }
                    $.each(response.tbk_uatm_favorites_item_get_response.results.uatm_tbk_item, function (i, item) {
                        var baseurl = "###";

                        if(item.status == 0){
                            return
                        }

                        $("#favorites_list").append("<li>"
                            + "<div class='am-gallery-item am_list_block'> "
                            + " <a> "
                            + "<a class='am_img_bg' href= " + baseurl + " onclick='to_detail(" + JSON.stringify(item) + ")' > "
                            + "<img class='am_img animated' src='/static/img/loading.gif'"
                            + "data-original='" + item.pict_url + " ' "
                            + " alt='优惠券'/> "
                            + "</a>"
                            + "<span class='coupon_name'>" + item.title + "</span>"
                            + "<div>"
                            + "<img class='img_juan' src='/static/img/coupon/juan.png'>"
                            + "<span class='coupon_rule'>" + item.coupon_info + "</span>"
                            + "</div>"
                            + "<div class='am_listimg_info'>"
                            + "<span class='ori_price'>原价："
                            + "<span class='ori_font'>￥</span>"
                            + "<span class='coupon_price'>" + item.zk_final_price + "</span>"
                            + "</span>"
                            + "</div>"
                            + "<div>"
                            + "<div class='coupon_shop'>" + item.shop_title + "</div>"
                            + "</div>"
                            + "<div class='coupon_get_div' data-clipboard-action='copy' value='" + item.coupon_click_url + "'" + "txt='" + item.title + "'" + "logo='" + item.pict_url + "'"
                            + "data-clipboard-target='div'>"
                            + "<a class='coupon_url'>"
                            + "<span id='coupon_get' class='coupon_get'>立即领取</span>"
                            + "</a>"
                            + "</div>"
                            + "</a>"
                            + "</div>"
                            + "</li>"
                        )

                    });

                    if (ClipboardJS.isSupported() && Util.isMobile()) {
                        $("#favorites_list").parent().find(".coupon_get").text("复制优惠券");
                    } else {
                        $(".coupon_get_div").attr("onclick", "cc(this)");
                    }

                    $('.am_img_bg').removeClass('am_img_bg');
                    $(this).find('.am_img').addClass('bounceIn');

                    $(".am_list_block").on('mouseover', function () {
                        $('.am_img_bg').removeClass('am_img_bg');
                        $(this).find('.am_img').addClass('bounceIn');
                    });
                    $("img.am_img").lazyload();
                    $("a.am_img_bg").lazyload({
                        effect: 'fadeIn'
                    });

                }
            })
        }

        more_fav();

        $("#moreFav").click(function () {
            more_fav();
        });

    }

    exports.wx_token = function () {
        $.ajax({
            type: "GET",
            url: '/youhui/get_access_token',
            dataType: 'json',
            success: function (response, status) {
                console.log(response)
                if (response != null) {
                    wx.config(response)
                    wx.ready(function () {   //需在用户可能点击分享按钮前就先调用
                        wx.onMenuShareAppMessage({
                            title: '优惠券分享', // 分享标题
                            desc: '海量优惠券等你来领', // 分享描述
                            link: 'https://www.manjiexiang.cn/youhui/', // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
                            imgUrl: 'https://www.manjiexiang.cn/static/img/coupon/wx_share.png', // 分享图标
                            success: function () {
                                // 设置成功
                                console.log("updateAppMessageShareData success")
                            }
                        });
                    })
                    wx.error(function(res){
                        console.log("失败》》》  ",res)
                    })
                }
            }
        })
    }

    return exports
})()


