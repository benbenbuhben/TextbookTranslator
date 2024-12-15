"use strict";
const serverUrl = "http://127.0.0.1:8000"; // Use local API for testing

let extractedText = "";

// Function to handle image upload and extract text
async function uploadAndExtract() {
    let file = document.getElementById("file").files[0];

    if (!file) {
        alert("Please select a file.");
        return;
    }

    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = async function () {
        const encodedString = reader.result.split(",")[1]; // Remove metadata prefix
        const response = await fetch(`${serverUrl}/images`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ filename: file.name, filebytes: encodedString })
        });

        if (!response.ok) {
            alert("Failed to upload image.");
            return;
        }

        const result = await response.json();
        document.getElementById("image").src = result.fileUrl;
        document.getElementById("image").alt = result.fileId;

        // Extract text from the image
        const extractResponse = await fetch(`${serverUrl}/images/${result.fileId}/text`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!extractResponse.ok) {
            alert("Failed to extract text.");
            return;
        }

        const extracted = await extractResponse.json();
        extractedText = extracted.map(line => line.text).join("\n");
        document.getElementById("extracted-text").textContent = extractedText;
        document.getElementById("view").style.display = "block";
    };
}

// Function to translate text
async function translateText() {
    const language = document.getElementById("language").value;

    if (!extractedText) {
        alert("No text to translate.");
        return;
    }

    const response = await fetch(`${serverUrl}/translate`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: extractedText,
            toLang: language
        })
    });

    if (!response.ok) {
        alert("Failed to translate text.");
        return;
    }

    const result = await response.json();
    document.getElementById("translated-text").textContent = result.translatedText;
}
