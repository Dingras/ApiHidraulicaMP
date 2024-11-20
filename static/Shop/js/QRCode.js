let videoStream;
let qrScannerElement = document.getElementById("qrcode-scanner");

function startQRCodeScanner() {
    const video = document.createElement("video");

    navigator.mediaDevices.getUserMedia({
        video: {
            facingMode: "environment", 
            width: { ideal: 200 },   // Resolución ideal
            height: { ideal: 300 },  // Resolución ideal
        }
    })
    .then(stream => {
        videoStream = stream;
        video.srcObject = stream;

        // Esperamos a que los metadatos del video se carguen (tamaño y demás)
        video.addEventListener("loadedmetadata", () => {
            video.play();
            qrScannerElement.appendChild(video);
            // Iniciamos la detección de QR usando el video
            requestAnimationFrame(() => scanQRCode(video));
        });
        
    })
    .catch(error => {
        console.error("Error al acceder a la cámara:", error);
        alert("No se pudo acceder a la cámara. Verifica los permisos.");
    });
}

function scanQRCode(video) {
    const canvas = document.createElement("canvas");
    const context = canvas.getContext("2d");

    // Asegúrate de que las dimensiones del canvas coincidan con las del video
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    // Dibujamos el video en el canvas
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageData = context.getImageData(0, 0, canvas.width, canvas.height);

    // Usamos jsQR para intentar leer el QR
    const qrCode = jsQR(imageData.data, imageData.width, imageData.height);
    if (qrCode) {
        alert(`Código QR detectado: ${qrCode.data}`);

        
        // HACER UNA LOGICA PARA VER EL PRODUCTO O AÑADIR AL CARRITO.


        stopScanner(); // Detenemos el escáner una vez detectado el código
    } else {
        // Continuamos el escaneo de manera recursiva
        requestAnimationFrame(() => scanQRCode(video));
    }
}

function stopScanner() {
    if (videoStream) {
        videoStream.getTracks().forEach(track => track.stop());
        videoStream = null;
    }
    // Ocultamos el contenedor del escáner
    
    qrScannerElement.style.display = "none";
    // Limpiamos el contenido del contenedor
    qrScannerElement.innerHTML = '';
}

// Función para abrir el escáner
function openScanner() {    
    // Hacemos visible el contenedor del escáner
    console.log("Abriendo Escáner QR");
    qrScannerElement.style.display = "block";
    // Iniciamos el escáner cuando se muestra el contenedor
    startQRCodeScanner();
}

// Función para cerrar el escáner manualmente
function closeScanner() {
    stopScanner();
}

// Asociamos el evento de apertura del escáner con un botón
document.getElementById("scanner-btn").addEventListener("click", openScanner);
