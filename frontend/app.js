async function fetchData(endpoint) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/${endpoint}`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

async function renderInventory() {
    const inventoryTableBody = document.querySelector("#inventory-table tbody");
    const inventoryData = await fetchData("sync");

    inventoryTableBody.innerHTML = inventoryData.inventory
        .map(item => `
            <tr>
                <td>${item.product}</td>
                <td>${item.quantity}</td>
            </tr>
        `)
        .join("");
}

async function renderPredictions() {
    const predictionTableBody = document.querySelector("#prediction-table tbody");
    const predictionData = await fetchData("predict");

    predictionTableBody.innerHTML = predictionData
        .map(item => `
            <tr>
                <td>${item.product}</td>
                <td>${item.forecast}</td>
            </tr>
        `)
        .join("");
}

async function initDashboard() {
    await renderInventory();
    await renderPredictions();
}

initDashboard();
