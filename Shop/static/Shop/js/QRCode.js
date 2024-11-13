let videoStream;
let qrScannerElement = document.getElementById("qrcode-scanner");

function startQRCodeScanner() {
    console.log("Inicio escaner")
    const video = document.createElement("video");

    navigator.mediaDevices.getUserMedia({
        width: 500,
        height: 600,
        video: { facingMode: "environment" }
    })
    .then(stream => {
        videoStream = stream;
        video.srcObject = stream;
        video.addEventListener("loadedmetadata", () => {
            video.play();
            requestAnimationFrame(() => scanQRCode(video));
        });
    })
    .catch(error => {
        console.error("Error al acceder a la cámara:", error);
    });
}

function scanQRCode(video) {
    console.log("Escaneo")
    const canvas = document.createElement("canvas");
    const context = canvas.getContext("2d");

    // Configurar el tamaño del canvas igual al video
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    // Dibujar el video en el canvas y obtener la imagen en cada cuadro
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageData = context.getImageData(0, 0, canvas.width, canvas.height);

    // Decodificar la imagen con jsQR
    const qrCode = jsQR(imageData.data, imageData.width, imageData.height);
    if (qrCode) {
        alert(`Código QR detectado: ${qrCode.data}`);
        stopScanner(); // Detener el escáner una vez detectado el código
    } else {
        requestAnimationFrame(() => scanQRCode(video)); // Seguir escaneando
    }
}

function stopScanner() {
    if (videoStream) {
        videoStream.getTracks().forEach(track => track.stop());
        videoStream = null;
    }
    // Oculta el contenedor del escáner QR
    qrScannerElement.style.display = "none";
    // Limpia el contenido del contenedor
    qrScannerElement.innerHTML = '';
}

// Función para abrir el escáner
function openScanner() {    
    // Asegúrate de que el escáner QR esté visible
    console.log("Abriendo Escaner")
    qrScannerElement.style.display = "block";
    // Inicia el escáner cuando se muestra el elemento
    startQRCodeScanner();
}

// Opcional: función para cerrar el escáner manualmente
function closeScanner() {
    stopScanner();
}

// Asocia el botón de abrir escáner (ejemplo de HTML)
document.getElementById("scanner-btn").addEventListener("click", openScanner);
// document.getElementById("close-scanner-btn").addEventListener("click", closeScanner);
