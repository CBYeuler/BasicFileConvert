document.getElementById("convertBtn").onclick = async () => {
    const fileInput = document.getElementById("fileInput");
    const formData = new FormData();

    formData.append("file", fileInput.files[0]);

    const response = await fetch("http://localhost:5000/convert", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    alert("Converted file URL: " + data.convertedFileUrl);
}