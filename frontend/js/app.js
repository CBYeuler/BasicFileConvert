const form = document.getElementById("convertForm");
const downloadLink = document.getElementById("downloadLink");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById("fileInput");
    const fromType = document.getElementById("fromType").value;
    const toType = document.getElementById("toType").value;

    if (!fileInput.files.length) {
        alert("Please select a file");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);
    formData.append("from_type", fromType);
    formData.append("to_type", toType);

    const response = await fetch("/convert", {
        method: "POST",
        body: formData
    });

    const result = await response.json();

    if (result.download_url) {
        downloadLink.href = result.download_url;
        downloadLink.style.display = "block";
        downloadLink.textContent = "Download converted file";
    } else {
        alert("Conversion failed");
    }
});
