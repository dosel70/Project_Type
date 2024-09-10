const button = document.querySelector("#zAe48RRRnK70L4yH");
const image = document.querySelector(".bottom-modal-profile-portal");

button.addEventListener("click", () => {
    image.style.display = image.style.display === "none" ? "block" : "none";
});

button4.addEventListener("click", () => {
    if (modal.style.display === "none") {
        modal.style.display = "block";
    } else {
        modal.style.display = "none";
    }
});

// 모달 열기 함수
function openModal() {
    const saveImage = document.querySelector("#confirm-modal-container");
    saveImage.style.display = "block";
}

// 모달 닫기 함수
function closeModal() {
    const saveImage = document.querySelector("#confirm-modal-container");
    saveImage.style.display = "none";
}

function closeImage() {
    const image = document.querySelector(".bottom-modal-profile-portal");
    image.style.display = "none";
}

const profileButton = document.querySelector("#attach");

profileButton.addEventListener("click", () => {
    console.log("출력");
});
