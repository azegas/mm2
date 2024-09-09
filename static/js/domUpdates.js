export function updateStockData(data) {
    const stockDiv = document.getElementById('stock_data');
    if (stockDiv) {
        stockDiv.innerHTML = ''; // Clear previous content
        
        const stockCards = document.createElement('div');
        stockCards.className = 'stock-cards';
        
        Object.entries(data.stocks).forEach(([symbol, details]) => {
            const stockCard = document.createElement('div');
            stockCard.className = 'stock-card';
            stockCard.innerHTML = `
                <div class="stock-info">
                    <div class="row">
                        <span class="symbol">${symbol}</span>
                        <span class="data">
                            <span class="price-container">
                                <span class="price">$${details.price}</span>
                                <span class="change">${details.change}</span>
                                <span class="change-percent">${details.change_percent}</span>
                            </span>
                            <span class="volume">Volume - ${details.volume}</span>
                            <span class="one-year-estimate">1y Target Est - $${details.one_year_estimate}</span>
                        </span>
                    </div>
                </div>
            `;
            stockCards.appendChild(stockCard);
        });
        
        stockDiv.appendChild(stockCards);

        // Add timestamp for all stock data
        const timestampElement = document.createElement('p');
        timestampElement.className = 'stock-timestamp timestamp';
        timestampElement.textContent = `Stocks updated at: ${data.timestamp}`;
        stockDiv.appendChild(timestampElement);
    }
}

export function updateSensorData(data) {
    const temperatureElement = document.getElementById('temperature');
    const humidityElement = document.getElementById('humidity');
    const timestampElement = document.getElementById('timestamp');

    if (temperatureElement && humidityElement && timestampElement) {
        temperatureElement.textContent = `${data.temperature} °C`;
        humidityElement.textContent = `${data.humidity} %`;
        timestampElement.textContent = data.timestamp;
    }
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

export function updateCvbankasData(data) {
    const jobsContainer = document.getElementById('cvbankas_jobs');
    jobsContainer.innerHTML = ''; // Clear previous content
    
    const jobCards = document.createElement('div');
    jobCards.className = 'job-cards';
    
    data.jobs.forEach(job => {
        const card = document.createElement('div');
        card.className = 'job-card';
        card.innerHTML = `
            <div class="job-info">
                <div class="row">
                    <img src="${job.image_link}" alt="${job.company} logo" class="job-image">
                    <span class="job-title">${job.title}</span>
                    <span class="data">
                        <span class="job-company">${job.company}</span>
                        <span class="job-salary">${job.salary}</span>
                    </span>
                </div>
            </div>
        `;
        jobCards.appendChild(card);
    });
    
    jobsContainer.appendChild(jobCards);

    // Add timestamp at the bottom of all jobs
    const timestampElement = document.createElement('p');
    timestampElement.className = 'cvbankas-timestamp timestamp';
    timestampElement.textContent = `Jobs updated at: ${data.fetch_date}`;
    jobsContainer.appendChild(timestampElement);
}


export function updateCurrentTime() {
    const currentTimeElement = document.getElementById('current-time');
    if (currentTimeElement) {
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        currentTimeElement.textContent = `${hours}:${minutes}:${seconds}`;
    }
}
