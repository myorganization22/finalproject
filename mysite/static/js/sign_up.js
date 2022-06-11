function example1() {
    //
    alert("Привет, JavaScript!")
}

function example2() {
    let name = prompt('Как вас зовут?');
    alert('Будем знакомы, ' + name);
}

function example3() {
    let choice = confirm('Вы хотите посетить сайт [bing.com]')
    if (choice === true) {
        window.location = 'https://www.bing.com';
    } else {
        alert('Ну не хотите не надо!');
    }
}

$(document).ready(() => {

    let flag1 = false;
    let flag2 = false;
    let flag3 = false;
    let flag4 = false;

    let regExpr1 = /^[a-zA-Z][a-zA-Z0-9\_\.\-\!]{5,15}$/;
    let regExpr2 = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\_\-\.\!])[a-zA-Z0-9\_\.\-\!]{8,}$/;
    let regExpr3 = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;

    //проверка логина
    $('#login').blur(() => {
        let login = $("#login").val();
        console.log(login);
        if (regExpr1.test(login)) {
            // + Проверка занятости логина
            $.ajax({
                url: '/account/ajax_reg1',
                data: 'loginX=' + login,
                success: function (result) {
                    if (result.mess === 'занят') {
                        $('#login_mess').html('Данный логин занят! попробуйте другой');
                        flag1 = false
                    } else {
                        console.log('OK');
                        $('#login_mess').html('');
                        flag1 = true;
                    }

                    console.log(result.mess);
                }
            });
        } else {
            console.log('Failed');
            $('#login_mess').html('Логин не соотвествует шаблону');
            flag1 = false;
        }
    });

    //проверка пороля
    $('#pass1').blur(() => {
        let pass1 = $("#pass1").val();
        console.log(pass1);
        if (regExpr2.test(pass1)) {
            console.log('OK');
            $('#pass1_mess').html('');
            flag2 = true;
        } else {
            console.log('Failed');
            $('#pass1_mess').html('Пароль не соотвествует шаблону');
            flag2 = false;
        }
    });

    //проверка подтверждения пороля
    $('#pass2').blur(() => {
        let pass1 = $("#pass1").val();
        let pass2 = $("#pass2").val();
        console.log(pass1);
        console.log(pass2);
        if (pass1 === pass2) {
            console.log('OK');
            $('#pass1_mess').html('');
            flag3 = true;
        } else {
            console.log('Failed');
            $('#pass2_mess').html('Пароли не совпадают');
            flag3 = false;
        }
    });

    //проверка email
    $('#email').blur(() => {
        let email = $("#email").val();
        console.log(email);
        if (regExpr3.test(email)) {
            console.log('OK');
            $('#email_mess').html('');
            flag4 = true;
        } else {
            console.log('Failed');
            $('#email_mess').html('E-Mail не соотвествует шаблону');
            flag1 = false;
        }
    });

    // Финальная проверка
    $('#submit').click(() => {
        if (flag1 == true && flag2 == true && flag3 == true && flag4 == true){
            $('#form1').attr('onsubmit', 'return true');
        } else {
            $('#form1').attr('onsubmit', 'return false');
            alert('Форма содержит не коректные данные! \nОтправка данных заблокирована');
        }
    });
});

//window.onload = () => {
//    example1();
//    example2();
//    example3();
//}