//
// 
//  Я постарался сделать +- читабельный код здесь, и стили в цсс
// Если нужны будут объяснения насчет работы кода - спрашивай!
// ипец стыдно, но надеюсь, что понятно)))
//
//


const PriceList = ["0.00", "1000.00", "1500.00", "350.00", "200.00",  
    "80.00", "60.00", "140.00"]
    const NumberPhotos = [0, 5, 1, 7, 2, 5, 5, 5]
    const DeteiledDescriptions = ["", 
    "Electric bike. 7 rear gears, cruise assistance. Battery: 30V*10Ah. Without front light. Excellent condition",
    "Electric bike. 4 gears in front, 7 in back wheel. Battery 36V*10Ah. Wonderful condition",
    "FOX bicycle. Great and legendary bike with 3*10 gears. Hydraulic brakes, Shock absorber on the front wheel",
    "Excelent choiсe in brilliant condition. Fast, efficient, and handome! Also with bottle holder",
    "Electro, motor doesn't work. Battery 25V*10Ah",
    "Excellent bike for city and off-road. 3*7 gears, excellent condition",
    "Excellent conditioned bike, but without grips((( 1:9 gears"]
    const modal = document.getElementById("modal");
    const modalTitle = document.getElementById("modal-title");
    const modalImage = document.getElementById("modal-image");
    const modalDescription = document.getElementById("modal-description");
    const modalPrice = document.getElementById("modal-price");
    let currentCard = 1;
    let currentImageIndex = 1;

    function openModal(cardNumber) {
        currentCard = cardNumber;
        currentImageIndex = 1;
        updateModalContent();
        modal.style.display = "flex";
    }

    function closeModal() {
        modal.style.display = "none";
    }

    function changeImage(direction) {
        currentImageIndex += direction;
        if (currentImageIndex < 1) {
            currentImageIndex = NumberPhotos[currentCard];
        } else if (currentImageIndex > NumberPhotos[currentCard]) {
            currentImageIndex = 1;
        }
        updateModalContent();
    }

    function updateModalContent() {
        modalTitle.textContent = `Bike ${currentCard}`;
        modalImage.src = `./img/bike${currentCard}/img_${currentImageIndex}.png`;
        modalDescription.textContent = DeteiledDescriptions[currentCard];
        modalPrice.textContent = `Price: CHF ${PriceList[currentCard]}`;
    }
    window.onload = changeLogo;
    window.onresize = changeLogo;
    function changeLogo(){
        const logo_img = document.getElementById("logo");
        const frb = document.getElementById("frb")
        const opm = document.getElementById("openbtn");
        if (window.innerWidth <=630){ //mobile
            frb.textContent = "Fribourg bicycles";
            logo_img.src = "img/aaa/logo600_340.png";
            opm.style.width = "23px";
            opm.style.top = "30px";
            opm.style.left = "30px";
            logo_img.style.left = ((window.innerWidth - logo_img.offsetWidth)/2) + "px";
        }
        else{
        opm.style.width = "75px";
        opm.style.top = "10px";
        opm.style.left = "45px";
        frb.textContent = "Fribourg       bicycles";
        logo_img.src = "img/aaa/logo700_700.png"; 
        logo_img.style.left = ((window.innerWidth - logo_img.offsetWidth)/2) + "px";
        }    
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            closeModal();
        }
    }
    function openNav() {
        document.getElementById("mySidebar").style.width = "250px";
    }

    function closeNav() {
        document.getElementById("mySidebar").style.width = "0";
    }