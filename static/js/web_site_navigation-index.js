

    // 点击切换导航菜单网址,将当前website的ul id传入函数
    function Display(id) {
        var content = document.getElementsByClassName("website")
        for (var i = 0; i < content.length; i++) {
            content[i].classList.add('hide')
        }

        var curr_content = document.getElementById(id)
        curr_content.parentElement.classList.remove('hide')
    }

    //jquery做乘法
    function accMul(arg1, arg2) {
        var m = 0, s1 = arg1.toString(), s2 = arg2.toString();
        try {
            m += s1.split(".")[1].length
        } catch (e) {
        }
        try {
            m += s2.split(".")[1].length
        } catch (e) {
        }
        return Number(s1.replace(".", "")) * Number(s2.replace(".", "")) / Math.pow(10, m)
    }

    //根据当前web_class_obj个数定义下拉框高度
    $('#menu-content a:first-child').hover(function () {
        var id = '#' + $(this).attr('id')
        var count = $(id).children('div').children('ul').children('object').length

        var now_height = accMul(40, count)
        $(this).find('.xs').css("height", now_height)

    }, function () {
        $(this).find('.xs').css("height", 0)

    })

    function Point(id) {

        var new_id = '#co'+id
        console.log(new_id)
        $(new_id).siblings().css('color','#3299CC')
        $(new_id).css('color','#FF69B4')
    }

