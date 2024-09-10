document.addEventListener("DOMContentLoaded", function() {
    const button1 = document.querySelector("#TNMMFVmHVXXCqJHQ");
    const button2 = document.querySelector("#DIrjEPUbL4meVbgz");
    const modal = document.querySelector("#confirm-modal-container");
    const modal2 = document.querySelector("#confirm-modal-container1");

    if (button1 && button2 && modal && modal2) {
        button1.addEventListener("click", () => {
            console.log("클릭");
            if (modal.style.display === "none") {
                modal.style.display = "block";
                console.log("들어옴");
            } else {
                modal.style.display = "none";
                console.log("안들어옴");
            }
        });

        button2.addEventListener("click", () => {
            if (modal2.style.display === "none") {
                modal2.style.display = "block";
                console.log("들어옴");
            } else {
                modal2.style.display = "none";
                console.log("안들어옴");
            }
        });

        const confirmed_btn_modal = document.querySelector("#alertify-o-ok");
        if (confirmed_btn_modal) {
            confirmed_btn_modal.addEventListener("click", () => {
                modal.style.display = "none";
            });
        }
    } else {
        console.error("Element not found: button1, button2, or modal");
    }
        const confirmed_btn_modal1 = document.querySelector("#alertify-o-ok1");
        if (confirmed_btn_modal1) {
            confirmed_btn_modal1.addEventListener("click", ()=>{
                modal2.style.display = "none";
            });
        }else {
            console.error("Element not found: button1, button2, or modal")
        }


});

    document.addEventListener('DOMContentLoaded', function() {
    const form1 = document.querySelector('#alertify-o1 form');
    const form2 = document.querySelector('#alertify-o2 form');

    form1.addEventListener('submit', function(event) {
        const temXPress = form1.querySelector('input[name="tem_x_press"]').value.trim();

        if (temXPress === '' || isNaN(temXPress)) {
            alert('Temperature x Pressure 값에 유효한 숫자를 입력해주세요.');
            event.preventDefault();  // 폼 제출 방지
        }
    });

    form2.addEventListener('submit', function(event) {
        const conversionIndex = form2.querySelector('input[name="conversion_index"]').value.trim();

        if (conversionIndex === '' || isNaN(conversionIndex)) {
            alert('Material Conversion Index 값에 유효한 숫자를 입력해주세요.');
            event.preventDefault();  // 폼 제출 방지
        }
    });
});


