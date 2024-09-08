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
    document.getElementById('timestamp').textContent = data.timestamp;
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
    
    // Add timestamp at the top of all jobs
    const timestampElement = document.createElement('p');
    timestampElement.className = 'cvbankas-timestamp timestamp';
    timestampElement.innerHTML = `<strong>Jobs updated at:</strong> ${data.fetch_date}`;
    jobsContainer.appendChild(timestampElement);

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
