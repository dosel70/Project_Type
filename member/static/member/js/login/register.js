
document.getElementById("registerForm").addEventListener("submit", function (event) {
    // 1차 비밀번호와 2차 비밀번호 가져오기
    const password1 = document.getElementById("pw1").value;
    const password2 = document.getElementById("pw2").value;

    // 비밀번호가 다르면 경고창 표시
    if (password1 !== password2) {
        alert("비밀번호가 일치하지 않습니다.");
        event.preventDefault(); // 폼 제출 방지
    }
});
