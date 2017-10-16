; $(document).ready(function (e) {
    $carousels = $(".view-frame").children();
    $carousel_dots = $(".carousel-dot");
    $carousel_dot_children = $carousel_dots.children();

    $img_list = $('.view-frame').find('img');

    $ele_panel = $('#wrapper');
    $ele_list = $ele_panel.find("div.ele");

    $color_panel = $('.title-out').hide();
    $color_title = $color_panel.find('.title');
    $color_list = $color_panel.find('.color');

    $button = $('button');



    $pallete_control = $('#pallete-control button');




    $carousel_dots.click(function (e) {
        view = $carousel_dot_children.index(e.target);
        $(".carousel-show").removeClass().addClass("carousel-hide");
        $($carousels[view]).removeClass().addClass('carousel-show');

    });

    $ele_list.click(function (e) {
        config_position = $(this).index();
        $ele_panel.hide();
        $color_panel.show();
        $color_title.text($(this).attr('data-name'));
        config_backup = config;
    });

    $color_list.click(function (e) {
        color_code = $(this).attr('data-color-id');
        $('.checked').removeClass('checked');
        $(this).addClass('checked');

        config[config_position]=color_code

        change_img(config);
    });

    $('#confirm').click(function (e) {
        if (color_code) {

            color_code = undefined;

            $color_panel.hide();
            $ele_panel.show();
        }

        else {
            alert("choose a color please...");
        }
    })

    $('#cancel').click(function(e){
        $color_panel.hide();
        $ele_panel.show();
        color_code = undefined;
        config = config_backup;
    });

    

    function change_img(config) {
        para1 = config.join(',')
        for (i = 0; i < 6; i++) {
            para2 = (i+1).toString() + ',' + para1;
            $img_list[i].src = './' + para2;
            console.log($img_list[i].src);
        }

        console.log(config);
    }


})
