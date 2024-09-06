export function updateStockData(data) {
    Object.entries(data).forEach(([symbol, details]) => {
        const stockDiv = document.getElementById(symbol);
        if (stockDiv) {
            stockDiv.innerHTML = `
                <div class="stock-info">
                    <span class="symbol">${symbol}</span>
                    <hr>
                    <span class="data">
                        <span class="price-container">
                            <span class="price">$${details.price}</span>
                            <span class="change">${details.change}</span>
                            <span class="change-percent">${details.change_percent}</span>
                        </span>
                        <span class="timestamp">As of ${details.timestamp}</span>
                    </span>
                    <img src="/static/images/${symbol}_high_prices_with_volume.png" alt="${symbol} High Prices Chart" class="stock-chart">
                </div>
            `;
        }
    });
}

export function updateTextColors(data) {
    document.querySelectorAll('.change, .change-percent').forEach(element => {
        const text = element.textContent.trim();
        if (text.includes('-')) {
            element.classList.add("red-text");
        } else if (text.includes('+')) {
            element.classList.add("green-text");
        }
    });
}
