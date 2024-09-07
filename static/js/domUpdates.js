export function updateUpdateIntervals(intervalStock, intervalSensor, intervalCvbankas) {
    const updateIntervals = document.getElementById('update-intervals');
    if (updateIntervals) {
        const stockInterval = intervalStock / 1000 >= 60 ? `${intervalStock / 60000} minutes` : `${intervalStock / 1000} seconds`;
        const sensorInterval = intervalSensor / 1000 >= 60 ? `${intervalSensor / 60000} minutes` : `${intervalSensor / 1000} seconds`;
        const cvbankasInterval = intervalCvbankas / 1000 >= 60 ? `${intervalCvbankas / 60000} minutes` : `${intervalCvbankas / 1000} seconds`;
        updateIntervals.innerHTML = `
            <span>Sensor - ${sensorInterval}&nbsp;|&nbsp;</span>
            <span>Stock - ${stockInterval}&nbsp;|&nbsp;</span>
            <span>Cvbankas - ${cvbankasInterval}</span>
        `;
    }
}

export function updateStockData(data) {
    const stockDiv = document.getElementById('stock_data');
    if (stockDiv) {
        stockDiv.innerHTML = ''; // Clear previous content
        
        Object.entries(data).forEach(([symbol, details]) => {
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
                            <span class="timestamp">As of ${details.timestamp}</span>
                            <img src="/static/images/${symbol}_high_prices_with_volume.png" alt="${symbol} High Prices Chart" class="stock-chart">
                        </span>
                    </div>
                </div>
            `;
            stockDiv.appendChild(stockCard);
        });
    }
}

export function updateSensorData(data) {
    document.getElementById('temperature').textContent = data.temperature;
    document.getElementById('humidity').textContent = data.humidity;
    document.getElementById('last_update').textContent = data.last_update;
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
            <img src="${job.image_link}" alt="${job.company} logo" class="job-image">
            <div class="job-details">
                <p class="job-title">${job.title}</p>
                <p class="job-company"><strong>Company:</strong> ${job.company}</p>
                <p class="job-salary"><strong>Salary:</strong> ${job.salary}</p>
            </div>
        `;
        jobCards.appendChild(card);
    });
    
    jobsContainer.appendChild(jobCards);
}

